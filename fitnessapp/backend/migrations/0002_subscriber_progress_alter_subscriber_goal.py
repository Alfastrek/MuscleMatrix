# Generated by Django 5.0.4 on 2024-04-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='progress',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='goal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]