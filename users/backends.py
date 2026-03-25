from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q

class StudentBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None


        try:
            profile = Profile.objects.get(student_id=username)
            user = profile.user
            if user.check_password(password):
                return user
        except Profile.DoesNotExist:
            pass


        try:

            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

        return None