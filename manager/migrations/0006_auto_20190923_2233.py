# Generated by Django 2.2.5 on 2019-09-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_meetings_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetings',
            old_name='regist_date',
            new_name='due_date',
        ),
    ]
