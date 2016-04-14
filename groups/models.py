from django.db import models
from contacts.models import Contact

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

class GroupContact(models.Model):
    group = models.ForeignKey(Group)
    contact = models.ForeignKey(Contact)

