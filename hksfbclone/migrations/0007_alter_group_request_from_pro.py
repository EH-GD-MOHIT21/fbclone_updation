# Generated by Django 3.2.5 on 2022-02-01 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hksfbclone', '0006_auto_20220201_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_request',
            name='from_pro',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_pro', to='hksfbclone.profile_details'),
        ),
    ]
