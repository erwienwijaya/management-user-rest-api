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
    path('', UsersListApi.as_view(), name='user-list'),
    path('create/', UsersCreateApi.as_view(), name='user-create'),
    path('<email>/', UsersListApiById.as_view(), name='user-list-by-id'),
    path('update/<email>/', UsersUpdateApi.as_view(), name='user-update'),
    path('delete/<email>/', UsersDeleteApi.as_view(), name='user-delete'),
]