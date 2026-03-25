from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.full_name} ({self.student_id})"