# Generated by Django 5.0.6 on 2024-06-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0005_alter_article_born_alter_article_died'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
