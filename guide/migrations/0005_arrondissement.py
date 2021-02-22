# Generated by Django 3.1.4 on 2020-12-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0004_department_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrondissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_arr', models.CharField(max_length=17)),
                ('code_arr', models.CharField(max_length=4)),
                ('desc_arr', models.TextField()),
                ('img_arr', models.ImageField(upload_to='images/arrondissements')),
                ('last_modify_arr', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]