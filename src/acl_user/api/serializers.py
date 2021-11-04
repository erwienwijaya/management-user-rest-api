from rest_framework import serializers
from ..models import UserList

class UserListModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ['id','email','first_name','last_name','phone','active','created_at','updated_at']