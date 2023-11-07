from django.db import models

# Create your models here.

'''
In a Django app, the models.py file serves as a central place for defining 
the data models that represent the structure of your application's database.
It defines the tables, fields, and relationships that are used to store and organize data.
'''

from django.db import models

class NotificationList(models.Model):
    messages = models.JSONField

    def __str__(self) -> str:
        return self.messages
