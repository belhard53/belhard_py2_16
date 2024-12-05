import os
from celery import Celery

os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

app = Celery(__name__, broker="redis://localhost:6379/0")

#celery --app=app.app worker --pool=solo
#celery --app=app.app worker --pool=threads --concurrency=8
#celery --app=app.app worker --pool=gevent --concurrency=8