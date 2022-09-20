import os
"""Example of decorators."""
from flask import Flask, render_template, redirect, url_for
from flask_apscheduler import APScheduler
from dotenv import load_dotenv


class Config:
    """App configuration."""

    SCHEDULER_API_ENABLED = True


scheduler = APScheduler()
app = Flask(__name__)
app.config['DEBUG'] = True
# app.config['SERVER_NAME'] = '78.24.223.130:5000'
app.config.from_object(Config())

# it is also possible to enable the API directly
# scheduler.api_enabled = True  # noqa: E800
scheduler.init_app(app)
scheduler.start()
load_dotenv()
n = 0


# interval examples
# @scheduler.task("interval", id="do_job_1", seconds=1, misfire_grace_time=900)
# def job1():
#     """Sample job 1."""
#     print("Job 1 executed")
#     with scheduler.app.app_context():
#         global n
#         n += 1
#         return redirect('index') if n % 2 else redirect('index')


# # cron examples
# @scheduler.task("cron", id="do_job_2", minute="*")
# def job2():
#     """Sample job 2."""
#     print("Job 2 executed")
#
#
# @scheduler.task("cron", id="do_job_3", week="*", day_of_week="sun")
# def job3():
#     """Sample job 3."""
#     print("Job 3 executed")


@app.get('/')
def index():
    d = {}
    d['host'] = os.getenv('host')
    d['port'] = os.getenv('port')
    d['CONNECTION_STRING'] = os.getenv('CONNECTION_STRING')
    d['user'] = os.getenv('user')
    d['password'] = os.getenv('password')
    print(*d.values())
    return render_template('n2.html', n=n)


@app.get('/1')
def index1():
    host = os.getenv('host')
    return render_template('n3.html', n=n)


if __name__ == "__main__":
    app.run()
