import uuid
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="created_%(class)s_set", null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="updated_%(class)s_set", null=True, blank=True)

    class Meta:
        abstract = True
