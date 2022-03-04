from django.db.models.fields.related import ManyToManyField
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField

from .models import Program, Subject, Chapter, ChapterSet, Topic, Description


# class HistoricalRecordField(serializers.ListField):
#     child = serializers.DictField()

#     def to_representation(self, data):
#         return super().to_representation(data.values())


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = (
            "program_id",
            "program_name",
            "program_type",
            "program_level",
        )


class SubjectSerializer(serializers.ModelSerializer):
    program = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="program_name"
    )

    class Meta:
        model = Subject
        fields = (
            "subject_id",
            "subject_name",
            "program",
            "subject_code",
            "grade",
        )


class ChapterSerializer(serializers.ModelSerializer):
    subject = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="subject_name"
    )

    class Meta:
        model = Chapter
        fields = (
            "chapter_id",
            "chapter_name",
            "subject",
        )


class ChapterSetSerializer(serializers.ModelSerializer):
    chapter = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="chapter_name"
    )
    subject = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="subject_name"
    )

    class Meta:
        model = ChapterSet
        fields = (
            "chapter_set_id",
            "subject",
            "chap_pos",
            "chapter",
            "chapter_credit",
        )


class TopicSerializer(serializers.ModelSerializer):
    chapter = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="chapter_name"
    )

    class Meta:
        model = Topic
        fields = (
            "topic_id",
            "topic_name",
            "chapter",
        )


class DescriptionSerializer(serializers.ModelSerializer):
    topic = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field="topic_name")

    class Meta:
        model = Description
        fields = (
            "description_id",
            "topic",
            "description",
        )
