
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home, name= "home"),
    path('contacto',views.contacto, name= "contacto"),
    path('gonzalo',views.gonzalo, name= "gonzalo"),
    path('guido',views.guido, name= "guido"),
    path('francisco',views.francisco, name= "francisco"),
    path('usuario',views.usuario, name= "usuario"),
    path('admin_login',views.admin_login, name= "admin_login"),
    path('logeado',views.logeado, name= "logeado"),
    path('cliente',views.cliente, name= "cliente"),
    path('registro',views.registro, name= "registro"),
    path('administrador',views.administrador, name= "administrador"),
    path('ing_producto',views.ing_producto, name= "ing_producto"),
    path('pendiente',views.pendiente, name= "pendiente"),
    path('cajacambio',views.cajacambio, name= "cajacambio"),
    path('pantalladireccion',views.pantalladireccion, name= "pantalladireccion"),
    path('pantallaelectronica',views.pantallaelectronica, name= "pantallaelectronica"),
    path('registro_usuario',views.registro_usuario, name= "registro_usuario"),
    path('employ',views.employ, name= "employ"),
    path('reg_factura_boleta',views.reg_factura_boleta, name= "reg_factura_boleta"),
    path('reg_orden_pedido',views.reg_orden_pedido, name= "reg_orden_pedido"),
    path('reg_recep_producto',views.reg_recep_producto, name= "reg_recep_producto"),
    path('adminis',views.adminis, name= "adminis"),
    path('reg_proveedores',views.reg_proveedores, name= "reg_proveedores"),
    path('reg_servicios',views.reg_servicios, name= "reg_servicios"),
    path('reserva_hra',views.reserva_hra, name= "reserva_hra"),
    path('catalogo',views.catalogo, name= "catalogo"),




]