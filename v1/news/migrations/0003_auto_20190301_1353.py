# Generated by Django 2.1.7 on 2019-03-01 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161125_0846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('pub_date',), 'verbose_name_plural': 'news'},
        ),
    ]
