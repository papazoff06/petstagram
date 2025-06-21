from django.contrib import admin

from petstagram_two.common.models import Comment, Like
from petstagram_two.pets.models import Pet


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
