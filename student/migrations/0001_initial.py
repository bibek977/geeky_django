# Generated by Django 4.2.4 on 2023-08-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('sname', models.CharField(max_length=100)),
                ('semail', models.CharField(max_length=100)),
                ('spass', models.CharField(max_length=100)),
            ],
        ),
    ]