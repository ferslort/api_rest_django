from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializer import UserRegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated



class RegisterView(APIView):
    def post(self, request):
      user = UserRegisterSerializer(data=request.data)

      if user.is_valid(raise_exception=True):
          user.save()
          return Response(user.data, status=status.HTTP_201_CREATED)

      return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
