from django.contrib import admin
from django.urls import include, path
from main import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.about, name='home'),  # Сделали 'about' главной страницей

    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('contacts/', views.contacts, name='contacts'),
    path('pool/', views.pool, name='pool'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('registration/', views.registration, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
#    path('logout/', auth_views.LogoutView.as_view(next_page='about'), name='logout'),
#    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('blog/', views.blog, name='blog'),
    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),

]



