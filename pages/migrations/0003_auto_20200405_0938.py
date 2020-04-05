# Generated by Django 3.0.3 on 2020-04-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200405_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Szolgáltatás neve')),
                ('photo', models.ImageField(upload_to='media/services', verbose_name='Kép')),
                ('description', models.TextField(verbose_name='Leírás')),
            ],
            options={
                'verbose_name_plural': 'Szolgáltatások',
            },
        ),
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'Magamról'},
        ),
    ]
