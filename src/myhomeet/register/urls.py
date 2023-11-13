from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'register'
router = DefaultRouter()
router.register('user', UserViewSet, basename="user-viewset")

urlpatterns = [
    path('', index, name='register'),
    path('user/', UserAPIView.as_view(), name='user_view'),
    path(r'whatuser/', current_user, name='page1')
]
urlpatterns += [path(r'api/', include(router.urls))]
