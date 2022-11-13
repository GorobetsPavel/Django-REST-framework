# Generated by Django 4.1.2 on 2022-11-13 09:18

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
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=150, verbose_name='Title')),
                ('repository', models.URLField()),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('deleted', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
                'ordering': ('-create_date',),
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Text')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update')),
                ('active', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.project', verbose_name='Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
                'ordering': ('-create_date',),
            },
        ),
    ]