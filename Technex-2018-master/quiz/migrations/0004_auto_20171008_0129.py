# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-07 19:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_domain'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionResponse',
            fields=[
                ('responseId', models.AutoField(primary_key=True, serialize=False)),
                ('responseTime', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='quiz_response',
            new_name='QuizResponse',
        ),
        migrations.RemoveField(
            model_name='question_response',
            name='option',
        ),
        migrations.RemoveField(
            model_name='question_response',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question_response',
            name='quiz',
        ),
        migrations.RenameField(
            model_name='options',
            old_name='is_correct',
            new_name='isCorrect',
        ),
        migrations.RenameField(
            model_name='options',
            old_name='option_id',
            new_name='optionId',
        ),
        migrations.RenameField(
            model_name='options',
            old_name='option_quote',
            new_name='optionQuote',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_id',
            new_name='questionId',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_title',
            new_name='questionTitle',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_type',
            new_name='questionType',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='beginning_quote',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='quiz_id',
            new_name='quizId',
        ),
        migrations.RenameField(
            model_name='quizresponse',
            old_name='response_id',
            new_name='responseId',
        ),
        migrations.RenameField(
            model_name='quizresponse',
            old_name='time_of_attempt',
            new_name='timeOfAttempt',
        ),
        migrations.RemoveField(
            model_name='options',
            name='option_status',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='Incorrect_message',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='correct_message',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='end_quote',
        ),
        migrations.AddField(
            model_name='quiz',
            name='activeStatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='endTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='startTime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='options',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Questions'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Quiz'),
        ),
        migrations.DeleteModel(
            name='question_response',
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='option',
            field=models.ManyToManyField(null=True, to='quiz.Options'),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Questions'),
        ),
        migrations.AddField(
            model_name='questionresponse',
            name='quizResponse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizResponse'),
        ),
    ]
