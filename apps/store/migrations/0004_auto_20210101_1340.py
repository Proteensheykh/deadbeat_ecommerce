# Generated by Django 3.0.7 on 2021-01-01 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20201230_0821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('ordering',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='ordering',
            field=models.IntegerField(default=0),
        ),
    ]
