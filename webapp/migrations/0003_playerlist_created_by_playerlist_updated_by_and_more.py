# Generated by Django 5.1.7 on 2025-04-12 04:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_serverlist_server_expired_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playerlist',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_cb', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='playerlist',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_ub', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playerlist',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
