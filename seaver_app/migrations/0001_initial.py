# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 16:53
from __future__ import unicode_literals

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
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(db_index=True, default=False)),
                ('offset', models.FloatField(default=0)),
                ('stretching', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=20)),
                ('field_index', models.IntegerField()),
                ('field_value', models.FloatField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_data', to='seaver_app.File')),
            ],
        ),
        migrations.CreateModel(
            name='IntervalAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IntervalAnnotationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('start', models.FloatField()),
                ('stop', models.FloatField()),
                ('interval_annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='seaver_app.IntervalAnnotation')),
            ],
        ),
        migrations.CreateModel(
            name='PunctualAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PunctualAnnotationEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('offset', models.FloatField(default=0)),
                ('punctual_annotation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='seaver_app.PunctualAnnotation')),
            ],
        ),
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspaces', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='workspace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='seaver_app.Workspace'),
        ),
        migrations.AlterUniqueTogether(
            name='workspace',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='punctualannotationevent',
            unique_together=set([('punctual_annotation', 'index')]),
        ),
        migrations.AlterUniqueTogether(
            name='intervalannotationevent',
            unique_together=set([('interval_annotation', 'index')]),
        ),
        migrations.AlterUniqueTogether(
            name='filedata',
            unique_together=set([('file', 'field_name', 'field_index')]),
        ),
        migrations.AlterUniqueTogether(
            name='file',
            unique_together=set([('workspace', 'name')]),
        ),
    ]
