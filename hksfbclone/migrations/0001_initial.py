# Generated by Django 3.2.5 on 2022-02-01 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('time_creat', models.DateTimeField(auto_now_add=True)),
                ('about', models.TextField()),
                ('img', models.FileField(blank=True, null=True, upload_to='imgs')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('liked', models.ManyToManyField(blank=True, default=None, related_name='liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='total_likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likesss', models.IntegerField(default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesno', to='hksfbclone.item')),
            ],
        ),
        migrations.CreateModel(
            name='profile_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgp', models.FileField(blank=True, default='default.jpg', null=True, upload_to='imgs')),
                ('u_nm', models.CharField(max_length=150)),
                ('fstname', models.CharField(max_length=250)),
                ('secname', models.CharField(max_length=250)),
                ('terimail', models.EmailField(max_length=254)),
                ('fbacc', models.CharField(max_length=250)),
                ('unicode', models.CharField(max_length=100, null=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('verified', models.BooleanField(default=False)),
                ('friends', models.ManyToManyField(blank=True, related_name='Friends', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=10)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='hksfbclone.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='hksfbclone.profile_details'),
        ),
        migrations.CreateModel(
            name='friend_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='hksfbclone.profile_details')),
                ('to_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='hksfbclone.profile_details')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('pst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='hksfbclone.item')),
            ],
        ),
        migrations.CreateModel(
            name='Chat_Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgp', models.FileField(blank=True, default='default.jpg', null=True, upload_to='imgs')),
                ('name', models.CharField(max_length=50)),
                ('members', models.IntegerField()),
                ('admin', models.ManyToManyField(blank=True, related_name='admin', to='hksfbclone.profile_details')),
                ('user', models.ManyToManyField(null=True, to='hksfbclone.profile_details')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hksfbclone.chat_groups')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hksfbclone.profile_details')),
            ],
        ),
    ]