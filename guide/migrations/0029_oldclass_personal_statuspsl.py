# Generated by Django 3.1.4 on 2020-12-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0028_detail_ss_acte'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odl_class', models.CharField(max_length=8)),
                ('number_class', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_psl', models.CharField(max_length=15)),
                ('sec_name_psl', models.CharField(max_length=15)),
                ('genre', models.CharField(max_length=7)),
                ('password_psl', models.CharField(max_length=8)),
                ('email_psl', models.CharField(max_length=76)),
                ('date_naiss', models.CharField(max_length=10)),
                ('mat_number_psl', models.CharField(max_length=10)),
                ('cat_psl', models.CharField(max_length=2)),
                ('fonc_grd_psl', models.CharField(max_length=2)),
                ('pl_h_dip_pro', models.CharField(max_length=13)),
                ('pl_h_dip_aca', models.CharField(max_length=13)),
                ('anciennete_svr', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='StatusPsl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_stp', models.CharField(max_length=13)),
                ('abbrev_stp', models.CharField(max_length=6)),
            ],
        ),
    ]