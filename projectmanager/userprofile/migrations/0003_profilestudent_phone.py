# Generated by Django 4.2.8 on 2024-02-25 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_profilestudent_birthday_profilestudent_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilestudent',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
