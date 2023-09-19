# Generated by Django 3.2.12 on 2023-09-19 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDeveloper',
            fields=[
                ('intern_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_model.intern')),
                ('college', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('base_model.intern',),
        ),
    ]