# project/celery.py
# -----------------
# Django 프로젝트에서 Celery 앱을 초기화하는 표준 진입점 파일.
# 이 파일을 통해 Django 설정(환경변수 DJANGO_SETTINGS_MODULE)을 읽고,
# Celery 인스턴스를 생성해서 tasks 자동 발견(autodiscover_tasks)을 수행한다.
#
# 또한 여기서 beat_schedule(정기 스케줄)을 정의할 수 있으며,
# 실제 배포에서는 django-celery-beat를 사용해 DB 기반 스케줄 관리를 하는 편이 더 유연하다.

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# 1) Django settings 모듈 지정 (환경변수)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lory.settings')

# 2) Celery 앱 인스턴스 생성
app = Celery('lory')

# 3) Django settings.py의 CELERY_* 설정을 "CELERY" namespace로 로드
#    즉, settings에 CELERY_BROKER_URL, CELERY_RESULT_BACKEND 같은 키를 두면 읽어온다.
app.config_from_object('django.conf:settings', namespace='CELERY')

# 4) INSTALLED_APPS 내의 tasks 모듈을 자동으로 찾아 등록한다.
#    (각 앱의 tasks.py 에 @shared_task가 있으면 자동 등록됨)
app.autodiscover_tasks()

# 5) 예시: Celery Beat 스케줄을 여기서 정의할 수 있음.
#    아래는 매일 새벽 03:00에 만료 토큰 삭제 task를 실행하도록 설정한 예시.
#    (운영에서는 timezone / crontab 값 검토 필요)
app.conf.beat_schedule = {
    'delete-expired-tokens-daily': {
        # users.tasks.delete_expired_tokens 함수(정의한 task)의 경로
        'task': 'users.tasks.delete_expired_tokens',
        # 크론 형태로 스케줄 정의 (시: 3, 분: 0 -> 매일 03:00)
        'schedule': crontab(hour=3, minute=0),
        # 'args': ()  # 필요시 task에 전달할 인자를 정의
    },
}

# (선택) 디버그용: 간단한 디버그 태스크
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
