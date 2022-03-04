from django.db import models
from django_quill.fields import QuillField
# from simple_history.models import HistoricalRecords
from apps.authentication.models import User
# Create your models here.
PROGRAM_TYPE_CHOICES = [
    ("Y", "Year"),
    ("S", "Semester"),
]

PROGRAM_LEVEL_CHOICES = [
    ("I", "Intermediate"),
    ("B", "Bachelors"),
    ("M", "Masters"),
]

GRADES = [
    ("Y1", "First Year"),
    ("Y2", "Second Year"),
    ("Y3", "Third Year"),
    ("Y4", "Fourth Year"),
    ("S1", "First Semeseter"),
    ("S2", "Second Semeseter"),
    ("S3", "Third Semeseter"),
    ("S4", "Fourth Semeseter"),
    ("S5", "Fifth Semeseter"),
    ("S6", "Sixth Semeseter"),
    ("S7", "Seventh Semeseter"),
    ("S8", "Eighth Semeseter"),
]


def GET_DELETED_USER():
    return User.objects.get(username="deleted")


class BaseModel(models.Model):
    created_date = models.DateTimeField(
        verbose_name="Added On", auto_now_add=True)
    modified_date = models.DateTimeField(
        verbose_name="Modified On", auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.SET(GET_DELETED_USER), verbose_name="user")

    class Meta:
        abstract = True


class Program(BaseModel):
    program_id = models.BigAutoField("Program ID", primary_key=True)
    program_name = models.CharField("Program", unique=True, max_length=64)
    program_type = models.CharField(
        "Program Type", choices=PROGRAM_TYPE_CHOICES, max_length=50
    )
    program_level = models.CharField(
        "Level Program", choices=PROGRAM_LEVEL_CHOICES, max_length=50
    )

    def __str__(self):
        return self.program_name


class Subject(BaseModel):
    subject_id = models.BigAutoField("Subject ID", primary_key=True)
    subject_name = models.CharField("Subject Name", max_length=50)
    program = models.ManyToManyField(Program, verbose_name="Program")
    subject_code = models.CharField("Subject Code", max_length=10, unique=True)
    grade = models.CharField("Year/Semester", choices=GRADES, max_length=50)

    def __str__(self):
        return "%s - %s" % (self.subject_code, self.subject_name)


class Chapter(BaseModel):
    chapter_id = models.BigAutoField("Chapter ID", primary_key=True)
    chapter_name = models.CharField("Chapter Name", max_length=64)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="subject"
    )

    def __str__(self):
        return self.chapter_name


class ChapterSet(BaseModel):
    chapter_set_id = models.BigAutoField("Chapter Set id", primary_key=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="subject"
    )
    chap_pos = models.PositiveIntegerField("Chapter Number")
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, verbose_name="Chapter"
    )
    chapter_credit = models.PositiveSmallIntegerField("Credit Hours")

    def __str__(self):
        return "%s. %s" % (self.chap_pos, self.chapter)

    class Meta:
        ordering = [
            "chap_pos",
        ]


class Topic(BaseModel):
    topic_id = models.BigAutoField("Topic ID", primary_key=True)
    topic_name = models.CharField("Topic Title", max_length=200)
    chapter = models.ForeignKey(
        Chapter, on_delete=models.CASCADE, verbose_name="Chapter"
    )

    def __str__(self):
        return self.topic_name


class Description(BaseModel):
    description_id = models.BigAutoField("Description ID", primary_key=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, verbose_name="Topic")
    description = QuillField(verbose_name="description")

    def __str__(self):
        return "%s -- %s" % (self.topic, self.description_id)
