from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import *


app_name = 'register'
router = DefaultRouter()
router.register('user', UserViewSet, basename="user-viewset")

urlpatterns = [
    path('', index, name='register'),
    path('user/', UserAPIView.as_view(), name='user_view'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('userlist/', UserListView.as_view()),
]
urlpatterns += [path(r'api/', include(router.urls))]
