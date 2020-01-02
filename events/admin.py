from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'url_image', 'created_date')
    list_display_links = ('title', 'created_date')
    search_fields = ('title',  'created_date')


admin.site.register(Post, PostAdmin)
