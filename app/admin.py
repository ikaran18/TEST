from django.contrib import admin
from app.models import Blog,Comment

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','author','created_at']
    
    class Media:
        js = ('https://cdn.tiny.cloud/1/4joqhh2ob716xc9ys18t112yysx6yfk6l1k050zlpda9u4ok/tinymce/6/tinymce.min.js','js/script.js')
    
admin.site.register(Comment)


