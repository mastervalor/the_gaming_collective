# Generated by Django 2.2.4 on 2022-09-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220921_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='dev_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Platforms',
        ),
    ]