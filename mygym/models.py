from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta



class Training(models.Model):
    training_routine = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now()+timedelta(days=30))

    def __unicode__(self):
        return self.user.username + ' -> ' + self.training_routine

class Activity(models.Model):
    user_set = models.IntegerField(default=0)
    user_rep = models.IntegerField(default=0)
    training = models.ForeignKey(Training)




    


















