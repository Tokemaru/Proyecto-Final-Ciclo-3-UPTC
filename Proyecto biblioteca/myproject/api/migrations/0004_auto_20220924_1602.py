# Generated by Django 3.0.6 on 2022-09-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220924_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='ID_User',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='ID_User',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
