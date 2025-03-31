# Generated by Django 4.2.11 on 2024-10-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_processor', '0002_remove_keyword_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='alternative_names',
            field=models.CharField(default='models', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='notation',
            field=models.CharField(default='models', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='reference',
            field=models.CharField(default='models', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='keyword',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
