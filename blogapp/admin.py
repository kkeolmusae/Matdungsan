from django.contrib import admin
from .models import Blog, Profile, Comment,FollowRelation
# Register your models here.

admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(FollowRelation)