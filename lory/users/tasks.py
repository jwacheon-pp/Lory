# users/tasks.py
# --------------
# Celery에서 호출할 수 있는 @shared_task 래퍼를 제공.
# 실제 삭제 로직은 위 유틸(delete_expired_tokens)에 두어 비즈니스 로직과
# Celery task 레이어를 분리했습니다.
#
# 이렇게 분리하면:
# - 단위 테스트가 쉬워진다 (유틸 함수는 일반 함수로 테스트 가능)
# - Celery가 아닌 환경에서도 동일 로직을 재사용할 수 있다 (예: 관리 명령어)

from celery import shared_task
from users.utils.token_cleanup import delete_expired_tokens as _delete_expired_tokens_util

@shared_task(bind=True)
def delete_expired_tokens(self):
    """
    Celery Task: 만료된 토큰 정리 작업을 수행한다.

    bind=True로 정의하면 task 인스턴스(self)에 접근 가능하다.
    self.request 등으로 task id, 전달된 인자, retry 등 메타데이터에 접근할 수 있다.
    (여기선 로깅/모니터링 목적이나 retry 정책 적용 시 유용)

    반환값:
      delete_expired_tokens 유틸이 반환한 dict를 그대로 반환한다.
      Celery result backend를 사용 중이라면 이 반환값이 backend에 저장된다.
    """
    try:
        # 실제 정리 로직 호출 (DB 접근)
        result = _delete_expired_tokens_util()

        # 간단한 로그 출력 (운영 환경에서는 로거 사용 권장)
        # self.request.id 등을 사용해 task id를 기록하면 디버깅에 좋다.
        print(f"[Celery Task] delete_expired_tokens: success - {result} (task_id={getattr(self.request, 'id', None)})")
        return result

    except Exception as exc:
        # 예외 처리: 필요에 따라 retry 하도록 설정하거나, 에러를 기록한다.
        # 예: self.retry(exc=exc, countdown=60, max_retries=3)
        print(f"[Celery Task] delete_expired_tokens: failed - {exc} (task_id={getattr(self.request, 'id', None)})")
        # 예외를 다시 raise 하면 Celery가 실패로 처리하고 retry 정책(설정된 경우)에 따라 재시도한다.
        raise
