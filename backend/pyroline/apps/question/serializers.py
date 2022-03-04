from rest_framework import serializers

from .models import (
    Answer,
    Question,
    QuestionPaper,
    QuestionSetter,
)
from apps.note.models import Subject, Chapter, Topic


class QuestionSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        slug_field="subject_name",
        read_only=False,
        many=False,
        queryset=Subject.objects.all(),
    )
    chapter = serializers.SlugRelatedField(
        slug_field="chapter_name",
        read_only=False,
        many=False,
        queryset=Chapter.objects.all(),
    )
    topic = serializers.SlugRelatedField(
        slug_field="topic_name",
        read_only=False,
        many=False,
        queryset=Topic.objects.all(),
    )

    class Meta:
        model = Question
        fields = (
            "question_id",
            "subject",
            "chapter",
            "topic",
            "question",
        )

    def validate(self, data):
        chapter = data["chapter"]
        subject = data["subject"]
        topic = data["topic"]

        if chapter.subject.subject_id != subject.subject_id:
            raise serializers.ValidationError(
                "No chapter named %s in the subject %s."
                % (chapter.chapter_name, subject.subject_name)
            )
        if topic.chapter.chapter_id != chapter.chapter_id:
            raise serializers.ValidationError(
                "No topic named %s in the subject %s."
                % (topic.topic_name, chapter.chapter_name)
            )
        return data


class QuestionPaperSerializer(serializers.ModelSerializer):
    program = serializers.SlugRelatedField(
        slug_field="program_name", read_only=True, many=False
    )
    subject = serializers.SlugRelatedField(
        slug_field="subject_name", read_only=True, many=False
    )

    class Meta:
        model = QuestionPaper
        fields = (
            "question_paper_id",
            "program",
            "subject",
            "grade",
            "year",
            "full_marks",
        )


class QuestionSetSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(
        slug_field="question", read_only=True, many=False
    )

    class Meta:
        model = QuestionSetter
        fields = (
            "question_set_id",
            "question_paper",
            "question_no",
            "question",
            "group",
            "marks",
        )


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(
        slug_field="question", read_only=True, many=False
    )

    class Meta:
        model = Answer
        fields = (
            "answer_id",
            "question",
            "answer",
            "answer_credit",
        )
