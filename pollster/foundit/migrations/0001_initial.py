# Generated by Django 5.1.6 on 2025-02-14 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='founditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_lost', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
