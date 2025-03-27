from rest_framework_simplejwt.views import(
     TokenObtainPairView, TokenRefreshView
)
from django.urls import path
from .views import (
    RegisterUser, LoginUser, GetAllUsers,
    ForgotPassword, ResetPassword, UpdateUser,
    DeleteUser, AddUser
)

urlpatterns = [
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(), 
         name='token_refresh'
         ),
    path('register/',
         RegisterUser.as_view(),
         name='register'
         ),
    path('login/',
         LoginUser.as_view(),
         name='login'
         ),
    path('forgot-password/',
         ForgotPassword.as_view(),
         name='forgot-password'
         ),
    path('reset-password/',
          ResetPassword.as_view(),
          name='reset-password'
          ),
    path('users/list/',
         GetAllUsers.as_view(),
         name='get-all-users'
         ),
    path('users/add/',
         AddUser.as_view(),
         name='add_user'
         ),
    path('users/update/<int:id>/', 
         UpdateUser.as_view(),
         name='update-user'
         ),
    path('users/<int:id>/delete/', 
         DeleteUser.as_view(), 
         name='delete-user'
         ),
]