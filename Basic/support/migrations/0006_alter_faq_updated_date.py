# Generated by Django 4.0.3 on 2022-05-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_faq_last_modi_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='최종 수정일시'),
        ),
    ]
