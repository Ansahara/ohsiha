# Generated by Django 2.0.1 on 2018-03-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=200)),
                ('pituus', models.CharField(max_length=200)),
                ('katselukerrat', models.IntegerField()),
                ('kanava', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('julkaistu', models.DateTimeField()),
            ],
        ),
    ]
