from django.contrib import admin
from .models import Post


admin.site.site_header = 'MYAPP ADMIN'
admin.site.site_title =  'ADMIN - MYAPP'
admin.site.name = "PhoneAI"

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'title_tag' ,'author', 'body')
    list_filter = [
        "author",
    ]

    search_fields = ['title', 'title_tag']

admin.site.register(Post, PostAdmin)
