import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_exam_user_profile(sender, instance, created, **kwargs):
    if created:

        new_id = f"STU{random.randint(100, 999)}"
        Profile.objects.create(
            user=instance,
            student_id=new_id,
            full_name=instance.get_full_name()
        )