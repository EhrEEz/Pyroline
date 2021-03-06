# Generated by Django 4.0.1 on 2022-02-05 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0002_historicaltopic_historicalsubject_historicalprogram_and_more'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalQuestionSetter',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('question_set_id', models.BigIntegerField(blank=True, db_index=True)),
                ('question_no', models.PositiveIntegerField(verbose_name='Question No')),
                ('group', models.CharField(max_length=2, verbose_name='Group')),
                ('marks', models.PositiveIntegerField(verbose_name='Mark Weight')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='question.question', verbose_name='Question')),
                ('question_paper', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='question.questionpaper', verbose_name='Question Paper')),
            ],
            options={
                'verbose_name': 'historical question setter',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalQuestionPaper',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('question_paper_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Question Paper ID')),
                ('grade', models.CharField(choices=[('Y1', 'First Year'), ('Y2', 'Second Year'), ('Y3', 'Third Year'), ('Y4', 'Fourth Year'), ('S1', 'First Semeseter'), ('S2', 'Second Semeseter'), ('S3', 'Third Semeseter'), ('S4', 'Fourth Semeseter'), ('S5', 'Fifth Semeseter'), ('S6', 'Sixth Semeseter'), ('S7', 'Seventh Semeseter'), ('S8', 'Eighth Semeseter')], max_length=50, verbose_name='Semester/Year')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('full_marks', models.PositiveIntegerField(verbose_name='Full Marks')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('program', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.program', verbose_name='Program')),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'historical question paper',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalQuestion',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('question_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Question ID')),
                ('question', models.CharField(max_length=1000, verbose_name='Question Name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('chapter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.chapter', verbose_name='Question Chapter')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.subject', verbose_name='Question Subject')),
                ('topic', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.topic', verbose_name='Question Topic')),
            ],
            options={
                'verbose_name': 'historical question',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalAnswer',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('answer_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='answer no')),
                ('answer', django_quill.fields.QuillField(verbose_name='answer')),
                ('answer_credit', models.CharField(max_length=64, verbose_name='Answer By')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='question.question', verbose_name='question')),
            ],
            options={
                'verbose_name': 'historical answer',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
