# Generated by Django 3.1.4 on 2020-12-26 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0005_arrondissement'),
    ]

    operations = [
        migrations.AddField(
            model_name='arrondissement',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guide.department'),
            preserve_default=False,
        ),
    ]
