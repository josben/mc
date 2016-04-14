from django.db import models
from socialnetwork.models import Social_Network

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImaageField(upload_to="media/contacts/avatar/",
                               blank=True,
                               null=True)
    created_profile = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

class Contact_Number(models.Model):
    contact = models.ForeignKey(Contact)
    country_code = models.IntegerField()
    phone = models.IntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    via = models.ForeignKey(Social_Network, blank=True, null=True)

