from django.db import models

# Create your models here.

class JsonTest(models.Model):
    test = models.TextField(blank=True, null=True, default='{"t1":""}')
    test2 = models.TextField(blank=True, null=True, default='{"t2":""}')

