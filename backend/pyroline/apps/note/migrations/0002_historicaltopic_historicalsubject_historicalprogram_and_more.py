# Generated by Django 4.0.1 on 2022-02-05 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTopic',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('topic_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Topic ID')),
                ('topic_name', models.CharField(max_length=200, verbose_name='Topic Title')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('chapter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.chapter', verbose_name='Chapter')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical topic',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSubject',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('subject_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Subject ID')),
                ('subject_name', models.CharField(max_length=50, verbose_name='Subject Name')),
                ('subject_code', models.CharField(db_index=True, max_length=10, verbose_name='Subject Code')),
                ('grade', models.CharField(choices=[('Y1', 'First Year'), ('Y2', 'Second Year'), ('Y3', 'Third Year'), ('Y4', 'Fourth Year'), ('S1', 'First Semeseter'), ('S2', 'Second Semeseter'), ('S3', 'Third Semeseter'), ('S4', 'Fourth Semeseter'), ('S5', 'Fifth Semeseter'), ('S6', 'Sixth Semeseter'), ('S7', 'Seventh Semeseter'), ('S8', 'Eighth Semeseter')], max_length=50, verbose_name='Year/Semester')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical subject',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalProgram',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('program_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Program ID')),
                ('program_name', models.CharField(db_index=True, max_length=64, verbose_name='Program')),
                ('program_type', models.CharField(choices=[('Y', 'Year'), ('S', 'Semester')], max_length=50, verbose_name='Program Type')),
                ('program_level', models.CharField(choices=[('I', 'Intermediate'), ('B', 'Bachelors'), ('M', 'Masters')], max_length=50, verbose_name='Level Program')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical program',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDescription',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('description_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Description ID')),
                ('description', django_quill.fields.QuillField(verbose_name='description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.topic', verbose_name='Topic')),
            ],
            options={
                'verbose_name': 'historical description',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChapterSet',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('chapter_set_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Chapter Set id')),
                ('chap_pos', models.PositiveIntegerField(verbose_name='Chapter Number')),
                ('chapter_credit', models.PositiveSmallIntegerField(verbose_name='Credit Hours')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('chapter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.chapter', verbose_name='Chapter')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.subject', verbose_name='subject')),
            ],
            options={
                'verbose_name': 'historical chapter set',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChapter',
            fields=[
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Modified On')),
                ('chapter_id', models.BigIntegerField(blank=True, db_index=True, verbose_name='Chapter ID')),
                ('chapter_name', models.CharField(max_length=64, verbose_name='Chapter Name')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='note.subject', verbose_name='subject')),
            ],
            options={
                'verbose_name': 'historical chapter',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
