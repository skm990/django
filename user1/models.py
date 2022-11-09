from email.policy import default
from django.db import models

class User_profile(models.Model):
    email         = models.EmailField(('email address'),max_length=60,unique=True , null=True)
    auth_id       = models.IntegerField(default=0 , null = True)
    first_name    = models.CharField(max_length=30,blank=True,null = True)
    last_name     = models.CharField(max_length=30,blank=True,null = True)
    moblie_no     = models.CharField(max_length=50,blank=True,unique=True, null = True)
    tenant_id     =  models.CharField(max_length=30,blank=True,null = True)
    is_active     = models.BooleanField(default=True,null = True)
    location_tacking = models.CharField(max_length=10,default=0)
    created_at   = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)

    def __str__(self):
        return self.email


class Teams(models.Model):
    name = models.CharField(max_length=128)
    tenant_id=models.CharField(max_length =20,default=0)
    created_at   = models.DateTimeField()
    created_by =models.ForeignKey(User_profile,on_delete =models.CASCADE)
    def __str__(self):
        return self.name

class Team_members(models.Model):
    user_id = models.OneToOneField(User_profile,on_delete =models.CASCADE,unique=False)
    team_id = models.ForeignKey(Teams,on_delete =models.CASCADE)
    
# Create your models here.
