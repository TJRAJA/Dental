# Generated by Django 4.1.4 on 2023-02-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='denal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=64)),
                ('p_email', models.EmailField(max_length=50)),
                ('p_date', models.DateField()),
                ('p_time', models.TimeField()),
            ],
        ),
    ]
