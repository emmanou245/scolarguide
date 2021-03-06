# Generated by Django 3.1.4 on 2020-12-29 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0030_auto_20201229_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='img_psl',
            field=models.ImageField(default=5, upload_to='images/personals'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personal',
            name='school',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='guide.school'),
            preserve_default=False,
        ),
    ]
