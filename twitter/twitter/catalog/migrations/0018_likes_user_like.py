# Generated by Django 4.1.7 on 2023-05-24 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='user_like',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_of_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
