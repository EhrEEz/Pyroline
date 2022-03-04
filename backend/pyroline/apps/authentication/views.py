# rest_framework classes
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView
)

# JWT classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# App defined Classes
from .models import User
from .serializers import (
    UserSerializer,
    MyTokenObtainPairSerializer,
    UserActivityLogSerializer,
)

# Permissions
from rest_framework.permissions import AllowAny
from .permissions import IsAdminUser, IsLoggedInUserOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.admin.models import LogEntry


class UserActivityView(ListAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        user = self.kwargs["usr"]
        queryset = LogEntry.objects.all()
        queryset = queryset.filter(user=user)
        return queryset


class GetTokenWithRoleView(TokenObtainPairView):
    authentication_class = ()
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegistrationView(APIView):
    authentication_class = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format="json"):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsLoggedInUserOrAdmin]
