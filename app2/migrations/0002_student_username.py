# Generated by Django 3.2.6 on 2021-09-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Username',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
