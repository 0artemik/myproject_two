from django import forms
from .models import Comment

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100)
    email = forms.EmailField(label='Ваш email')

    
    # Радиокнопки для оценки сайта
    rating = forms.ChoiceField(
        label='Оценка сайта',
        choices=[(1, 'Плохо'), (2, 'Удовлетворительно'), (3, 'Хорошо'), (4, 'Очень хорошо'), (5, 'Отлично')],
        widget=forms.RadioSelect
    )
    
    # Флажки для выбора интересующих разделов
    interests = forms.MultipleChoiceField(
        label='Интересующие разделы',
        choices=[('auctions', 'Аукционы'), ('catalog', 'Каталог'), ('resources', 'Полезные ресурсы')],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    # Выпадающий список для выбора частоты посещений
    frequency = forms.ChoiceField(
        label='Как часто вы посещаете наш сайт?',
        choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'), ('monthly', 'Ежемесячно')]
    )
    
    # Текстовое поле для комментариев и пожеланий
    comments = forms.CharField(
        label='Комментарии и пожелания',
        widget=forms.Textarea,
        required=False
    )


# Форма для комментариев в блоге
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': 'Комментарий'}

