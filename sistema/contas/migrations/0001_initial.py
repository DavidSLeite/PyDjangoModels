# Generated by Django 2.0.4 on 2018-05-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField(verbose_name='Ra')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('email', models.CharField(max_length=60, verbose_name='Emai')),
            ],
        ),
    ]
