# Generated by Django 4.0.1 on 2022-02-05 12:31

from django.db import migrations, models
import django.db.models.deletion
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('chapter_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Chapter ID')),
                ('chapter_name', models.CharField(max_length=64, verbose_name='Chapter Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('program_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Program ID')),
                ('program_name', models.CharField(max_length=64, unique=True, verbose_name='Program')),
                ('program_type', models.CharField(choices=[('Y', 'Year'), ('S', 'Semester')], max_length=50, verbose_name='Program Type')),
                ('program_level', models.CharField(choices=[('I', 'Intermediate'), ('B', 'Bachelors'), ('M', 'Masters')], max_length=50, verbose_name='Level Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('topic_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Topic ID')),
                ('topic_name', models.CharField(max_length=200, verbose_name='Topic Title')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.chapter', verbose_name='Chapter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('subject_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Subject ID')),
                ('subject_name', models.CharField(max_length=50, verbose_name='Subject Name')),
                ('subject_code', models.CharField(max_length=10, unique=True, verbose_name='Subject Code')),
                ('grade', models.CharField(choices=[('Y1', 'First Year'), ('Y2', 'Second Year'), ('Y3', 'Third Year'), ('Y4', 'Fourth Year'), ('S1', 'First Semeseter'), ('S2', 'Second Semeseter'), ('S3', 'Third Semeseter'), ('S4', 'Fourth Semeseter'), ('S5', 'Fifth Semeseter'), ('S6', 'Sixth Semeseter'), ('S7', 'Seventh Semeseter'), ('S8', 'Eighth Semeseter')], max_length=50, verbose_name='Year/Semester')),
                ('program', models.ManyToManyField(to='note.Program', verbose_name='Program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('description_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Description ID')),
                ('description', django_quill.fields.QuillField(verbose_name='description')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.topic', verbose_name='Topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChapterSet',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified On')),
                ('chapter_set_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Chapter Set id')),
                ('chap_pos', models.PositiveIntegerField(verbose_name='Chapter Number')),
                ('chapter_credit', models.PositiveSmallIntegerField(verbose_name='Credit Hours')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.chapter', verbose_name='Chapter')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.subject', verbose_name='subject')),
            ],
            options={
                'ordering': ['chap_pos'],
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.subject', verbose_name='subject'),
        ),
    ]
