# Generated by Django 4.2.4 on 2023-09-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=9800000000)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]