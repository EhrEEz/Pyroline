from django.db import models
from django.db.models.fields import CharField
from django_quill.fields import QuillField
from apps.note.models import Program, Subject, Chapter, Topic
from simple_history.models import HistoricalRecords
from apps.authentication.models import User

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


class Question(BaseModel):
    question_id = models.BigAutoField(
        verbose_name="Question ID", primary_key=True)
    question = models.CharField(verbose_name="Question Name", max_length=1000)
    subject = models.ForeignKey(
        Subject,
        verbose_name="Question Subject",
        related_name="question_subject",
        on_delete=models.CASCADE,
    )
    chapter = models.ForeignKey(
        Chapter,
        verbose_name="Question Chapter",
        related_name="question_chapter",
        on_delete=models.CASCADE,
    )
    topic = models.ForeignKey(
        Topic,
        verbose_name="Question Topic",
        related_name="question_topic",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["-modified_date", "question_id", "question"]
        verbose_name_plural = "Questions"


class Answer(BaseModel):
    question = models.ForeignKey(
        Question,
        related_name="problem",
        verbose_name="question",
        on_delete=models.CASCADE,
    )
    answer_id = models.BigAutoField("answer no", primary_key=True)
    answer = QuillField(verbose_name="answer")
    answer_credit = models.CharField("Answer By", max_length=64)

    def __str__(self):
        x = "%s -- %s" % (str(self.question), self.answer_id)
        return x


class QuestionPaper(BaseModel):
    question_paper_id = models.BigAutoField(
        "Question Paper ID", primary_key=True)
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        verbose_name="Program",
        related_name="program_question",
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="Subject"
    )
    grade = models.CharField("Semester/Year", choices=GRADES, max_length=50)
    year = models.CharField("Year", max_length=4)
    full_marks = models.PositiveIntegerField("Full Marks")

    def __str__(self):
        return "%s %s %s %s" % (
            self.program.program_name,
            self.grade,
            self.subject.subject_name,
            self.year,
        )


class QuestionSetter(BaseModel):
    question_set_id = models.BigAutoField(primary_key=True)
    question_no = models.PositiveIntegerField("Question No")
    question = models.ForeignKey(
        Question, verbose_name="Question", on_delete=models.CASCADE
    )
    group = models.CharField("Group", max_length=2)
    marks = models.PositiveIntegerField("Mark Weight")
    question_paper = models.ForeignKey(
        QuestionPaper, verbose_name="Question Paper", on_delete=models.CASCADE
    )

    def __str__(self):
        return "%s. %s" % (self.question_no, self.question.question)
