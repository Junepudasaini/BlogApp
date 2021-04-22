from django.contrib import admin
from .models import Post, Comment
from tinymce.widgets import TinyMCE 
from django.db import models


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/Date", {"fields":["title", "date_upload"]}),
        ("URL", {"fields":["slug"]}),
        ("Image", {"fields":["image"]}),
        ("Introduction", {"fields":["intro"]}),
        ("Content", {"fields":["body"]}),
        ("Snippets", {"fields":["snippets_content"]}),
    ]
    formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
	}

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
