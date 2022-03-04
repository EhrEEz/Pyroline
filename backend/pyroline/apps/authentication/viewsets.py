from rest_framework import viewsets
from rest_framework.permissions import (
    IsAdminUser,
)
from apps.authentication.permissions import ReadOnly

from .models import User
from .serializers import (
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | ReadOnly]
