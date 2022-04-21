# Generated by Django 4.0.4 on 2022-04-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekApp', '0006_alter_blogpost_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='you',
            field=models.CharField(default='Food', max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tag',
            field=models.ManyToManyField(blank=True, to='geekApp.tag'),
        ),
    ]
