from django.contrib import admin
from .models import *


class ResponseInline(admin.TabularInline):
    model = Response
    extra = 1  

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date', 'location', 'get_responses_count', 'created_at')
    list_filter = ('author', 'date', 'category')
    search_fields = ('title', 'description', 'location')
    list_display_links = ('title',)
    inlines = [ResponseInline, CommentInline]
    
    @admin.display(ordering='get_responses_count', description='Responses Count')
    def get_responses_count(self, obj):
        return obj.get_responses_count()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')  
    raw_id_fields = ('user', 'event')  
    search_fields = ('user__username', 'event__title')  


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'event', 'created_at', 'text_snippet')  
    readonly_fields = ('created_at',)  
    search_fields = ('author__username', 'event__title', 'text')  

    
    @admin.display(description="Text Snippet")
    def text_snippet(self, obj):
        return obj.text[:50]  
