# Generated by Django 3.1 on 2020-08-21 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200820_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='language',
            name='language',
        ),
        migrations.AddField(
            model_name='language',
            name='name',
            field=models.CharField(blank=True, help_text='Enter a language (e.g. English)', max_length=200),
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Select a language', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
