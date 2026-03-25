from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class RegisterSerializer(serializers.ModelSerializer):

    student_id = serializers.CharField(source='profile.student_id', read_only=True)

    class Meta:
        model = User

        fields = ['email', 'first_name', 'last_name', 'password', 'student_id']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):

        email = validated_data.get('email')


        user = User.objects.create_user(
            username=email,
            **validated_data
        )



        return user