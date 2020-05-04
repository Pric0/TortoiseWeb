# Generated by Django 3.0.5 on 2020-05-04 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=129)),
                ('originaltitle', models.CharField(max_length=129)),
                ('year', models.DateTimeField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('plot', models.TextField()),
            ],
        ),
    ]