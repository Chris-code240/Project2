from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User


class PersonSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Person
        fields = "__all__"