from tortoise import fields
from tortoise.models import Model


class Note(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    filename = fields.CharField(max_length=256)
    title = fields.CharField(max_length=1000)
    content = fields.TextField(default="")
