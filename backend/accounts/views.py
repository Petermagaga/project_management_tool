from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User

from .serializers import(
    UserSerializer,
    RegisterSerializer,
    ProfileUpdateSerializer,
    ChangePasswordSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]


class CurrentUserView(APIView):
    permission_classes= [IsAuthenticated]
    def  get(self,request):
        serializer=UserSerializer(request.user)
        return Response(serializer.data)


class UpdateProfileView(APIView):
    permission_classes=[IsAuthenticated]

    def put(self,request):
        serializer=ProfileUpdateSerializer(
            request.user,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )


        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class ChangePasswordView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        serializer=ChangePasswordSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user=request.user
        if not user.check_password(
            serializer.validated_data["old_password"]
        ):
            return Response(
                {"error":"Incorrect password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(
            serializer.validated_data["new_password"]
        )

        user.save()
        return Response(
            {"message":"Password Updated"}
        )