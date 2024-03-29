# Generated by Django 2.1.1 on 2019-01-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=255)),
                ('diabetes_specialist', models.BooleanField(default=False)),
                ('location', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=255)),
                ('phonenumber', models.CharField(max_length=255)),
                ('shedule', models.CharField(max_length=255)),
                ('fees', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
