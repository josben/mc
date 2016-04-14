from django.db import models
from socialnetworks.models import SocialNetwork

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to="media/contacts/avatar/",
                               blank=True,
                               null=True)
    created_profile = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

class ContactNumber(models.Model):
    contact = models.ForeignKey(Contact)
    country_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    username = models.CharField(max_length=50, blank=True, null=True)
    via = models.ForeignKey(SocialNetwork, blank=True, null=True)

