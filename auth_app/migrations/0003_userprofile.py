# Generated by Django 4.2.5 on 2024-09-10 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
