from django.contrib.auth.models import User
from django.db import models

class Table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tables")
    result = models.IntegerField(default=0)
