from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    starred_by = models.ManyToManyField(User, related_name="starred_projects", blank=True)
    def __str__(self):
        return self.name