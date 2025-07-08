from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Article,
    MaterialImage,
)
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cover_preview', 'author', 'created_at', 'updated_at')
    search_fields = ('id', 'title', 'author__username')
    list_filter = ('created_at', 'author')
    readonly_fields = ('cover_preview', 'created_at', 'updated_at')
    
    def cover_preview(self, obj):
        if obj.cover.image:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.cover.image.url)
        
        return "-"
    
    
@admin.register(MaterialImage)
class MaterialImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'preview', 'created_at')
    readonly_fields = ('preview', )
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 80px;" />', obj.image.url)
        
        return "-"
    
    preview.short_description = "預覽"