from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'updated']
    list_display_links = ['timestamp']
    list_filter = ['title', 'timestamp']

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
