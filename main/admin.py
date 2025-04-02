from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted')  # Отображаем заголовок, автора и дату публикации
    search_fields = ('title', 'author__username')  # Добавляем поиск по названию и имени автора

admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'date')  # Отображаем автора, статью и дату комментария
    search_fields = ('author__username', 'post__title')  # Добавляем поиск по имени автора и названию статьи
admin.site.register(Comment, CommentAdmin)
