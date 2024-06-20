# Generated by Django 5.0.6 on 2024-06-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_alter_article_known_for'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='designed_by_developer',
            new_name='designed_by',
        ),
        migrations.AddField(
            model_name='article',
            name='developer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='notable_work',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
