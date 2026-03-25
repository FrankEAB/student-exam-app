from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    exam_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_code