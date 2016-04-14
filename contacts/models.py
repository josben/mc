from django.db import models
from socialnetwork.models import Social_Network

class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    nik_name = models.CharField(max_length=50)
    photo = models.ImaageField(upload_to="media/contacts/avatar/",
                               blank=True,
                               null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Contact_Number(models.Model):
    country_code = models.IntegerField()
    number = models.IntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    via = models.ForeignKey(Social_Network, blank=True, null=True)

