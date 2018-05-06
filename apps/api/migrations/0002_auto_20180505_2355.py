# Generated by Django 2.0.5 on 2018-05-05 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentevent',
            name='performance',
        ),
        migrations.AddField(
            model_name='contentevent',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='api.Stage'),
            preserve_default=False,
        ),
    ]