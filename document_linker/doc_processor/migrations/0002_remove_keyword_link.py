# Generated by Django 4.2.11 on 2024-08-13 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doc_processor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='link',
        ),
    ]
