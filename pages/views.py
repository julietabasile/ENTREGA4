from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from pages.models import Blog, UserProfile
from pages.forms import SignUpForm

# Vista para la lista de blogs
def blog_list(request):
    blogs = Blog.objects.all()  # Obtén todos los blogs, 
    context = {'blogs': blogs}
    return render(request, 'pages/blog_list.html', context)

# Definimos el atributo blog_list en views
blog_list = blog_list

# Vista para los detalles de un blog
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # Obtén un blog específico o devuelve un 404 si no existe
    context = {'blog': blog}
    return render(request, 'pages/blog_detail.html', context)

# Vista para la página "Acerca de Mí"
def about(request):
    return render(request, 'pages/about.html')

# Vista para el registro de usuario
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Realizar acciones adicionales después del registro
    else:
        form = SignUpForm()

    return render(request, 'pages/signup.html', {'form': form})


