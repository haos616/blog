from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title', 'author')
    list_filter = ('title',)
    date_hierarchy = 'created_date'


admin.site.register(Post, PostAdmin)
