from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from django.urls import reverse_lazy

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

def ListarProductos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def ListarCategorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

class CreditosView(TemplateView):
    template_name = 'creditos.html'

class CrearProducto(CreateView):
    template_name = 'crear_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('home:productosapp')

class CrearCategoria(CreateView):
    template_name = 'crear_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('home:categoriasapp')

class EditarProducto(UpdateView):
    template_name = 'editar_producto.html'
    form_class = ProductoForm
    model = Producto
    success_url = reverse_lazy('home:productosapp') 

class EditarCategoria(UpdateView):
    template_name = 'editar_categoria.html'
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('home:categoriasapp')