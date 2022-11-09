from django.urls import path, include
from user1.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('z1', views.UserViewSet, basename='user1')


urlpatterns = [
    path('z/', include(router.urls)), 
]
