from django.shortcuts import render
from rest_framework import generics

from .models import ChapterSet, Topic, Program
from .serializers import (
    ChapterSetSerializer,
    ChapterSerializer,
    SubjectSerializer,
    ProgramSerializer,
    TopicSerializer,
    DescriptionSerializer,
    # ProgramHistorySerializer,
)
from rest_framework.permissions import (
    IsAdminUser,
)
from apps.authentication.permissions import ReadOnly


# class ProgramHistoryView(generics.RetrieveAPIView):
#     serializer_class = ProgramHistorySerializer
#     permission_classes = [IsAdminUser | ReadOnly]

#     def get_object(self):
#         program_id = self.kwargs["program"]
#         program = Program.objects.get(program_id=program_id)
#         user = self.kwargs["user"]
#         queryset = program.history.filter(history_user=user)
#         return queryset


class TopicView(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        topics = Topic.objects.all()
        queryset = Topic.objects.all()
        chapterset = ChapterSet.objects.all()
        subject = self.kwargs["subject"]
        chapter = self.kwargs["chapter"]
        if subject is not None:
            chapterset = chapterset.filter(subject__subject_name=subject)
            queryset = Topic.objects.none()
            for chap in chapterset:
                x = chap.chapter.chapter_name
                f_topics = topics.filter(chapter__chapter_name=x)
                queryset |= f_topics

            if chapter is not None:
                queryset = queryset.filter(chapter__chapter_name=chapter)

        return queryset


class SyllabusView(generics.ListAPIView):
    serializer_class = ChapterSetSerializer

    def get_queryset(self):
        queryset = ChapterSet.objects.all()
        subject = self.kwargs["subject"]
        if subject is not None:
            queryset = queryset.filter(subject__subject_name=subject)

        return queryset
