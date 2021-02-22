# Generated by Django 3.1.4 on 2020-12-26 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0010_auto_20201226_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='arrondissement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guide.arrondissement'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guide.order'),
            preserve_default=False,
        ),
    ]