# Generated by Django 2.1.5 on 2019-01-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatterApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatteruser',
            name='username',
            field=models.CharField(default='biggeCheese', max_length=30),
            preserve_default=False,
        ),
    ]
