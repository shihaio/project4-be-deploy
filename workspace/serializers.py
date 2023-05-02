from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "first_name",
      "last_name",
      "email",
      "password",
      "role",
      "birthday",
      "user_created_date",
    )
    depth = 1