from django.urls import path
from pages import views

urlpatterns = [
    # URL para la lista de blogs
    path('blogs/', views.blog_list, name='blog_list'),

    # URL para los detalles de un blog
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),

    # URL para la página "Acerca de Mí"
    path('about/', views.about, name='about'),

    # URL para el registro de usuario
    path('signup/', views.signup_view, name='signup'),
]


