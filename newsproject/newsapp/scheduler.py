
from apscheduler.schedulers.blocking import BlockingScheduler
from django import setup

from .models import Vote


setup()
schedule = BlockingScheduler()


@schedule.scheduled_job('interval', days=1)
def remove_votes():

"""
Fuction running everyday task:
clearing table newsapp_vote
"""

    Vote.objects.all().delete() 
