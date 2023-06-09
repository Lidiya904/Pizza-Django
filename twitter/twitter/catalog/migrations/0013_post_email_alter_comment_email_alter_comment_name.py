# Generated by Django 4.1.7 on 2023-05-19 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_remove_comment_active_remove_comment_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postemail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentemail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentauthor', to=settings.AUTH_USER_MODEL),
        ),
    ]
