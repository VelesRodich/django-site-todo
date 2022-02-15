# Generated by Django 4.0.2 on 2022-02-15 13:44

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
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Задача')),
                ('memo', models.TextField(blank=True, verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Задача создана')),
                ('datecompleted', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время завершения')),
                ('important', models.BooleanField(default=False, verbose_name='Важно!')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Дело',
                'verbose_name_plural': 'Дела',
            },
        ),
        migrations.CreateModel(
            name='FrontendConfig',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='todo.todo')),
            ],
            bases=('todo.todo',),
        ),
    ]
