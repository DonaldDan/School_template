# Generated by Django 4.0.5 on 2022-09-11 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_result_school_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='national',
            name='topic',
            field=models.ManyToManyField(blank=True, related_name='nationals', to='base.school'),
        ),
    ]