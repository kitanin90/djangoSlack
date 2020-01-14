from django.contrib import admin
from .models import Post, Profile


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'created_date', 'fullname')
    list_display_links = ('title', 'created_date')
    search_fields = ('title',  'created_date')


class UserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'number_message')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, UserAdmin)
