from django.contrib.admin.models import LogEntry
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAdminUser,
)
from apps.authentication.permissions import ReadOnly
from .models import Program, Subject, ChapterSet, Chapter, Topic, Description
from .serializers import (
    ProgramSerializer,
    SubjectSerializer,
    ChapterSetSerializer,
    ChapterSerializer,
    TopicSerializer,
    DescriptionSerializer,
)


class ProgramViewset(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class SubjectViewset(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class ChapterSetViewset(viewsets.ModelViewSet):
    queryset = ChapterSet.objects.all()
    serializer_class = ChapterSetSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class ChapterViewset(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class TopicViewset(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class DescriptionViewset(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer
    permission_classes = [IsAdminUser | ReadOnly]
