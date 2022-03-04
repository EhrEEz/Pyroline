from rest_framework import viewsets
from .models import Question, QuestionPaper, QuestionSetter, Answer
from .serializers import (
    QuestionPaperSerializer,
    QuestionSetSerializer,
    QuestionSerializer,
    AnswerSerializer,
)
from rest_framework.permissions import (
    IsAdminUser,
)
from apps.authentication.permissions import ReadOnly


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]


class QuestionSetterViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSetSerializer
    queryset = QuestionSetter.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]


class QuestionPaperViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionPaperSerializer
    queryset = QuestionPaper.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAdminUser | ReadOnly]
