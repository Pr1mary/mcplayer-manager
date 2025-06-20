from django.db import models
from django.contrib.auth.models import User

class ServerList(models.Model):

    server_url = models.CharField(max_length=255)
    server_name = models.CharField(max_length=255, null=True, blank=True)
    server_secret = models.CharField(max_length=255, null=True, blank=True)
    server_is_vanilla = models.BooleanField(default=False)
    server_invite_code = models.CharField(max_length=255, null=True, blank=True)
    server_expired_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="server_list_cb")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="server_list_ub")
