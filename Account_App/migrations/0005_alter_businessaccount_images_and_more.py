# Generated by Django 4.2.6 on 2023-10-25 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account_App', '0004_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessaccount',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='business_account_images', to='Account_App.image'),
        ),
        migrations.AlterField(
            model_name='businessaccount',
            name='menu',
            field=models.ManyToManyField(blank=True, null=True, related_name='business_account_menu', to='Account_App.image'),
        ),
        migrations.AlterField(
            model_name='businessaccount',
            name='reviews',
            field=models.ManyToManyField(blank=True, null=True, related_name='business_accounts', to='Account_App.review'),
        ),
    ]
