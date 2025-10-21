# users/utils/token_cleanup.py
# ---------------------------
# SimpleJWT의 OutstandingToken/BlacklistedToken 모델을 사용해서
# 만료된 토큰을 정리하는 비즈니스 로직을 모아둔 유틸 파일입니다.
#
# 핵심 아이디어:
# 1) OutstandingToken.expires_at 필드를 기준으로 "이미 만료된" 토큰들을 찾는다.
# 2) 그 만료된 토큰들의 JTI(jti)를 사용해 BlacklistedToken 레코드(만료 이전에 블랙리스트화 된 항목)를 먼저 삭제한다.
#    -> ForeignKey 관계로 인해 BlacklistedToken을 먼저 지우는 것이 안전하다.
# 3) 그 다음 OutstandingToken 레코드를 삭제한다.
#
# 반환값: 삭제된 outstanding 토큰 개수와 blacklisted 토큰 개수를 포함한 dict
# (Django의 QuerySet.delete()는 (deleted_count, {model_label: count, ...}) 형태의 튜플을 반환함에 주의)

from datetime import datetime, timezone  # timezone-aware 비교를 위해 사용
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

def delete_expired_tokens():
    """
    만료된 JWT 토큰을 데이터베이스에서 삭제하는 함수.

    동작 상세:
    1) 현재 시각(now)을 UTC 기준으로 구함.
    2) OutstandingToken.objects.filter(expires_at__lt=now)로 만료된 토큰들을 조회.
       - QuerySet은 삭제 시점까지 DB 쿼리를 지연시킬 수 있으므로,
         JTI 목록은 별도로 리스트로 추출해서 BlacklistedToken 필터에 사용.
    3) 해당 JTI 목록을 이용해 BlacklistedToken 레코드들을 삭제.
       - BlacklistedToken이 OutstandingToken을 참조(FK)하고 있으므로
         먼저 삭제하지 않으면 FK 제약 조건에 걸릴 수 있음.
    4) 만료된 OutstandingToken들을 삭제.
    5) 삭제된 개수를 정리해서 리턴.
    """
    # 1) 현재 시각 (UTC) — DB에 저장된 expires_at이 timezone-aware(UTC)라고 가정
    now = datetime.now(timezone.utc)

    # 2) 만료된 outstanding token들을 QuerySet으로 가져온다.
    expired_tokens_qs = OutstandingToken.objects.filter(expires_at__lt=now)

    # 2.1) JTI 목록을 가져온다. QuerySet을 바로 전달하면 나중에 delete로 인해 문제가 될 수 있으니 리스트로 평가(evaluate)한다.
    expired_jti_list = list(expired_tokens_qs.values_list('jti', flat=True))

    # 3) 관련된 BlacklistedToken을 먼저 삭제
    #    .delete()는 (num_deleted, {<model_label>: count, ...}) 를 반환
    blacklisted_delete_result = BlacklistedToken.objects.filter(token__jti__in=expired_jti_list).delete()
    # blacklisted_delete_result[0]는 전체 삭제된 행 개수
    blacklisted_deleted_count = blacklisted_delete_result[0]

    # 4) 만료된 OutstandingToken 삭제
    outstanding_delete_result = expired_tokens_qs.delete()
    outstanding_deleted_count = outstanding_delete_result[0]

    # 5) 결과 리턴 (숫자만 깔끔하게 리턴)
    return {
        "outstanding_deleted": outstanding_deleted_count,
        "blacklisted_deleted": blacklisted_deleted_count,
    }
