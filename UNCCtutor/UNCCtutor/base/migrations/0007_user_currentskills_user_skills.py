# Generated by Django 5.2 on 2025-04-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_user_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='currentSkills',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
