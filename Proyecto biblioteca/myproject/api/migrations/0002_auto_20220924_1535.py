# Generated by Django 3.0.6 on 2022-09-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='ID_Libro',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]