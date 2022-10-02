# Generated by Django 4.1.1 on 2022-10-02 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('parentezco', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
    ]
