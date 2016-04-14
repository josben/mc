from django.db import models
from contacts.models import Contact
from groups.models import Group

class Message_Center_Received(models.Model):
    contact = models.ForeignKey(Contact)
    message_received = models.CharField(max_length=140,
                                        blank=True, null=True)
    long_message_received = models.CharField(max_length=350,
                                             blank=True, null=True)
    visibility = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    date_received = models.DateTimeField(auto_now_add=True)

class Reply(models.Model):
    contact = models.ForeignKey(Contact)
    message_center = models.ForeignKey(Message_Center_Received)
    reply_message = models.CharField(max_length=140)
    long_reply_message = models.CharField(max_length=350)
    date_sent = models.DateTimeField(auto_now_add=True)

class Message_Center_Sent(models.Model):
    contact = models.ForeignKey(Contact)
    message_sent = models.CharField(max_length=140,
                                        blank=True, null=True)
    long_message_sent = models.CharField(max_length=350,
                                             blank=True, null=True)
    visibility = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

class Message_Group(models.Model):
    group = models.ForeignKey(Group)
    message_sent = models.CharField(max_length=140,
                                        blank=True, null=True)
    long_message_sent = models.CharField(max_length=350,
                                             blank=True, null=True)
    visibility = models.BooleanField(default=True)
    closed = models.BooleanField(default=False)
    date_sent = models.DateTimeField(auto_now_add=True)

