# Generated by Django 2.0.2 on 2018-02-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0017_auto_20171207_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='sent_summary_up_to',
            field=models.DateTimeField(null=True),
        ),
    ]
