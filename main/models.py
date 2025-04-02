from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя
from django.urls import reverse
from datetime import datetime



# создание модели блога
class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    summary = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    posted = models.DateTimeField(default=datetime.now, db_index=True, verbose_name="Опубликована")
    
    author = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Автор"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
    

# создание комментариев в блоге
class Comment(models.Model):
    post = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments", verbose_name="Статья")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField(verbose_name="Комментарий")
    date = models.DateTimeField(default=datetime.now, verbose_name="Дата добавления")

def __str__(self):
    return f"Комментарий от {self.author} к {self.post.title}"


