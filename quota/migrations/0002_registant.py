# Generated by Django 4.1.1 on 2022-10-08 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('quotas', models.ManyToManyField(blank=True, related_name='registants', to='quota.quota')),
            ],
        ),
    ]
