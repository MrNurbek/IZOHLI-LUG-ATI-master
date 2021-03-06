# Generated by Django 4.0.4 on 2022-05-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name="So'z")),
                ('description', models.TextField(max_length=500, verbose_name="So'z izohi")),
                ('slug', models.SlugField(max_length=200, verbose_name='slug')),
            ],
            options={
                'verbose_name': "So'z",
                'verbose_name_plural': "So'zlar",
            },
        ),
    ]
