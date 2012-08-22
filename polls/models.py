from django.db import models
from django.utils import timezone
import datetime

AUDIENCE_CHOICES=[
          ('corp','Corporate Users'),
          ('pub','Public Users'),
    ]

class Poll(models.Model):
    question = models.CharField(max_length=128)
    pub_date = models.DateTimeField(verbose_name='Date Published',
                                    auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name='Date Updated',
                                    auto_now=True)
    audience = models.CharField(max_length=8, choices=AUDIENCE_CHOICES)
    frequency = models.FloatField(verbose_name='Display Frequency',
                    help_text='Controls how frequently the poll is displayed?')
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()    