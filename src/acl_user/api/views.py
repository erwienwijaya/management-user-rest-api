from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserListModelSerializers
from ..models import UserList
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response


class UsersListApi(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = UserList.objects.all().order_by('-created_at')
    serializer_class = UserListModelSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['email', 'first_name','last_name','phone','active']

    def get(self, request):
        qs = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(qs)

        if page is not None:
            serializers = self.get_serializer(page, many=True)
            result = self.get_paginated_response(serializers.data)
            data = result.data  # pagination data
        else:
            serializers = self.get_serializer(qs, many=True)
            data = serializers.data

        payload = {
            "data": data,
            "message": "Success",
            "res_code": '0000'
        }
        return Response(payload, status=status.HTTP_200_OK)

class UsersListApiById(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = UserListModelSerializers

    def get_queryset(self):
        queryset = UserList.objects.filter(pk=self.kwargs['email'])
        return queryset

    def get(self, request,email):
        qs = self.filter_queryset(self.get_queryset())
        serializers = self.get_serializer(qs, many=True)

        data = serializers.data

        if data:
            payload = {
                "data": data,
                "message": "Success",
                "res_code": '0000'
            }
            return Response(payload, status=status.HTTP_200_OK)

        payload_error = {
            "message": "Data Not Found, makesure the id is email!",
            "res_code": '0000'
        }
        return Response(payload_error, status=status.HTTP_404_NOT_FOUND)

class UsersCreateApi(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListModelSerializers

    def post(self, request):
        serializers = UserListModelSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()

            payload = {
                "data": serializers.data,
                "message": "new user created",
                "res_code": '0000'
            }
            return Response(payload,status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersUpdateApi(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListModelSerializers

    def patch(self, request, email):
        try:
            qs = UserList.objects.get(pk=self.kwargs['email'])

            data = request.data

            qs.first_name = data.get('first_name',qs.first_name)
            qs.last_name = data.get('last_name',qs.last_name)
            qs.phone = data.get('phone',qs.phone)
            qs.active = data.get('active',qs.active)
            qs.save()

            serializers = UserListModelSerializers(qs)

            payload = {
                "data": serializers.data,
                "message": "user updated",
                "res_code": '0000'
            }
            return Response(payload, status=status.HTTP_202_ACCEPTED)

        except ObjectDoesNotExist:
            payload_error = {
                "message": "Email not found!",
                "res_code": '0000'
            }

            return Response(payload_error, status=status.HTTP_404_NOT_FOUND)

class UsersDeleteApi(DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserListModelSerializers

    def delete(self, request, email):
        try:
            qs = UserList.objects.get(pk=self.kwargs['email'])

            qs.delete()

            payload = {
                "message": "user deleted",
                "res_code": '0000'
            }
            return Response(payload, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            payload_error = {
                "message": "Email not found!",
                "res_code": '0000'
            }

            return Response(payload_error, status=status.HTTP_404_NOT_FOUND)
