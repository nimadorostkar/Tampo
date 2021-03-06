from django.contrib import admin
from .models import Post, Comment, Newsletter, Contact

from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)






class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'email')
    search_fields = ('email', 'email')

admin.site.register(Newsletter, NewsletterAdmin)








class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'email', 'body')

admin.site.register(Contact, ContactAdmin)






# End
