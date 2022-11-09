from user1.models import *
from rest_framework import serializers

class User_profileSerializer(serializers.ModelSerializer):
 class Meta:
  model = User_profile
  fields = ['email','auth_id','first_name', 'last_name', 'moblie_no','tenant_id','is_active','created_at']

  
class TeamsSerializer(serializers.ModelSerializer):
 class Meta:
  model = Teams
  fields = ['name','tenant_id','created_at', 'created_by']


class Team_membersSerializer(serializers.ModelSerializer):
 class Meta:
  model = Team_members
  fields = ['user_id','team_id']









