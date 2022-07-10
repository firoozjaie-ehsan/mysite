from django.contrib import admin

from blog.models import Post

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy= 'create_date'
    empty_value_display= '-empty-'
    # fields=("title",)
    list_display=("title","counted_view","status",'published_date','create_date')
    list_filter=("status",)
    # ordering=("-create_date",)
    search_fields=("title","content")
# Register your models here.
admin.site.register(Post,PostAdmin)
