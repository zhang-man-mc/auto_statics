from datetime import datetime
from sql_statement.authentication import Authentication
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print(str(datetime.now())+" Hello World")

sched = BlockingScheduler()

# 每2小时触发
sched.add_job(job_function, 'interval',seconds=3600,start_date='2023-10-18 00:05:00', end_date=None, id='测试')
print(str(datetime.now()))
sched.start()