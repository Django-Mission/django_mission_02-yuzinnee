# Generated by Django 4.0.4 on 2022-04-17 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0003_answer_last_modi_writer_alter_inquiry_category_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='user_email',
        ),
    ]
