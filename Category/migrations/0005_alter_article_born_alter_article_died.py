# Generated by Django 5.0.6 on 2024-06-22 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0004_rename_designed_by_developer_article_designed_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='born',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='died',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
