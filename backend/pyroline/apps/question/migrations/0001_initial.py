# Generated by Django 4.0.1 on 2022-02-05 12:31

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('question_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Question ID')),
                ('question', models.CharField(max_length=1000, verbose_name='Question Name')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_chapter', to='note.chapter', verbose_name='Question Chapter')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_subject', to='note.subject', verbose_name='Question Subject')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_topic', to='note.topic', verbose_name='Question Topic')),
            ],
            options={
                'verbose_name_plural': 'Questions',
                'ordering': ['-modified_date', 'question_id', 'question'],
            },
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('question_paper_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Question Paper ID')),
                ('grade', models.CharField(choices=[('Y1', 'First Year'), ('Y2', 'Second Year'), ('Y3', 'Third Year'), ('Y4', 'Fourth Year'), ('S1', 'First Semeseter'), ('S2', 'Second Semeseter'), ('S3', 'Third Semeseter'), ('S4', 'Fourth Semeseter'), ('S5', 'Fifth Semeseter'), ('S6', 'Sixth Semeseter'), ('S7', 'Seventh Semeseter'), ('S8', 'Eighth Semeseter')], max_length=50, verbose_name='Semester/Year')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('full_marks', models.PositiveIntegerField(verbose_name='Full Marks')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='program_question', to='note.program', verbose_name='Program')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.subject', verbose_name='Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionSetter',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('question_set_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('question_no', models.PositiveIntegerField(verbose_name='Question No')),
                ('group', models.CharField(max_length=2, verbose_name='Group')),
                ('marks', models.PositiveIntegerField(verbose_name='Mark Weight')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.question', verbose_name='Question')),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questionpaper', verbose_name='Question Paper')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('answer_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='answer no')),
                ('answer', django_quill.fields.QuillField(verbose_name='answer')),
                ('answer_credit', models.CharField(max_length=64, verbose_name='Answer By')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='question.question', verbose_name='question')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]