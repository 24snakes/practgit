# Generated by Django 2.0.6 on 2018-11-27 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrumChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrumChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('hash', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumDemoProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrumGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('moveable', models.BooleanField(default=True)),
                ('name', models.TextField()),
                ('status', models.IntegerField(default=-1)),
                ('goal_project_id', models.IntegerField(default=0)),
                ('hours', models.IntegerField(default=-1)),
                ('time_created', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ScrumProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('project_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ScrumProjectRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumProject')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumSprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField()),
                ('ends_on', models.DateTimeField()),
                ('goal_project_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nickname'],
            },
        ),
        migrations.AddField(
            model_name='scrumprojectrole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumUser'),
        ),
        migrations.AddField(
            model_name='scrumgoal',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumProject'),
        ),
        migrations.AddField(
            model_name='scrumgoal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumProjectRole'),
        ),
        migrations.AddField(
            model_name='scrumdemoproject',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumProject'),
        ),
        migrations.AddField(
            model_name='scrumchatmessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Scrum.ScrumChatRoom'),
        ),
    ]
