from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from .serializers import QuestionPaperSerializer, QuestionSetSerializer
from .models import QuestionPaper, QuestionSetter


class FilteredQuestionPaperListView(generics.ListAPIView):
    serializer_class = QuestionPaperSerializer

    def get_queryset(self):
        queryset = QuestionPaper.objects.all()
        subject = self.kwargs["subject"]
        queryset = queryset.filter(subject__subject_name=subject)
        return queryset


class FilteredQuestionSetListView(generics.ListAPIView):
    serializer_class = QuestionSetSerializer

    def get_queryset(self):
        queryset = QuestionSetter.objects.all()
        subject = self.kwargs["subject"]
        year = self.kwargs["year"]
        queryset = queryset.filter(
            question_paper__subject__subject_name=subject, question_paper__year=year
        )
        return queryset


class ChapterWiseQuestionView(generics.ListAPIView):
    serializer_class = QuestionSetSerializer

    def get_queryset(self):
        queryset = QuestionSetter.objects.all()
        subject = self.kwargs["subject"]
        chapter = self.kwargs["chapter"]
        queryset = queryset.filter(
            question__subject__subject_name=subject,
            question__chapter__chapter_name=chapter,
        )
        return queryset


class TopicWiseQuestionView(generics.ListAPIView):
    serializer_class = QuestionSetSerializer

    def get_queryset(self):
        queryset = QuestionSetter.objects.all()
        subject = self.kwargs["subject"]
        chapter = self.kwargs["chapter"]
        topic = self.kwargs["topic"]
        queryset = queryset.filter(
            question__subject__subject_name=subject,
            question__chapter__chapter_name=chapter,
            question__topic__topic_name=topic,
        )
        return queryset
