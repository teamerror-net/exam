# Generated by Django 4.2.6 on 2023-10-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name_plural': 'STUDENT ACCOUNT'},
        ),
        migrations.AddField(
            model_name='useraccount',
            name='profile_pic',
            field=models.ImageField(blank=True, default='faces/profile.png', null=True, upload_to='faces/'),
        ),
    ]