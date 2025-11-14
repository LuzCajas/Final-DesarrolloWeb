from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ListarProductos, ListarCategorias, CreditosView, CrearProducto, CrearCategoria, EditarProducto, EditarCategoria

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('productos/', ListarProductos, name='productosapp'),
    path('categorias/', ListarCategorias, name='categoriasapp'),
    path('creditos/', CreditosView.as_view(), name='creditosapp'),
    path('crear_producto/', CrearProducto.as_view(), name='crear_producto'),
    path('crear_categoria/', CrearCategoria.as_view(), name='crear_categoria'),
    path('editar_producto/<int:pk>/', EditarProducto.as_view(), name='editar_producto'),
    path('editar_categoria/<int:pk>/', EditarCategoria.as_view(), name='editar_categoria'),
]