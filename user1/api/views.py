from user1.models import *
from user1.api.serializers import *
from rest_framework import viewsets

# class UserViewSet(viewsets.ModelViewSet):
#   queryset = User_profile.objects.all()
#   serializer_class = User_profileSerializer
  
class UserViewSet(viewsets.ModelViewSet):
  queryset = Teams.objects.all()
  serializer_class = TeamsSerializer
  

# class UserViewSet(viewsets.ModelViewSet):
#   queryset = Team_members.objects.all()
#   serializer_class = Team_membersSerializer
  