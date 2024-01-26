from django.urls import path
from .views import blog_list, blog_detail, about, signup_view

urlpatterns = [
    # URL para la lista de blogs
    path('blogs/', blog_list, name='blog_list'),

    # URL para los detalles de un blog
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'),

    # URL para la página "Acerca de Mí"
    path('about/', about, name='about'),

    # URL para el registro de usuario
    path('signup/', signup_view, name='signup'),

    # Puedes agregar más URLs según sea necesario
]


   
]

