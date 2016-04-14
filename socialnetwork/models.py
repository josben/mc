from django.db import models

# This model is for Whatsapp, Twitter, Facebook and others

class Social_Network(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

