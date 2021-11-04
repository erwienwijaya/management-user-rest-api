from django.urls import path
from .views import (
    UsersListApi,
    UsersListApiById,
    UsersCreateApi,
    UsersUpdateApi,
    UsersDeleteApi,
)

app_name = 'users'
urlpatterns = [
    path('', UsersListApi.as_view(), name='userlist'),
    path('create/', UsersCreateApi.as_view(), name='usercreate'),
    path('<email>/', UsersListApiById.as_view(), name='userlistbyid'),
    path('update/<email>/', UsersUpdateApi.as_view(), name='userupdate'),
    path('delete/<email>/', UsersDeleteApi.as_view(), name='userdelete'),
]