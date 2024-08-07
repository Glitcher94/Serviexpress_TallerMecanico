
from django.contrib.messages.api import error
from django.core import validators
from django.http import response
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from core.validators import validar


from . models import Articulo, RegistroAdministrador, RegistroCliente, RegistroEmpleado
from .forms import ArticuloForm, LoginAdministradorForms, LoginClienteForms, LoginEmpleadoForms, RegistroAdministradorForm, RegistroClienteForms, RegistroEmpleadoForm, RegistroHoraForm, RegistroProveedorForm, RegistroServicioForm

# Create your views here.


def home(request):
    articulo = Articulo.objects.all()
    return render (request, 'core/home.html',{'articulo': articulo})

def contacto(request):
    return render (request, 'core/contacto.html')

def gonzalo(request):
    datos = {'form':RegistroHoraForm()}

    if request.method == 'POST':

        formulario = RegistroHoraForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Hora agendada"

            datos['form'] = formulario
        else:
            datos['mensaje'] = "Error hora no agendada"

            datos['form'] = formulario
    return render (request, 'core/gonzalo.html', datos)

def guido(request):
    return render (request, 'core/guido.html')

def francisco(request):
    return render (request, 'core/francisco.html')

def usuario(request):
    datos = {'form':LoginEmpleadoForms()}
    
    if request.method == 'POST':

        formulario = RegistroEmpleadoForm(request.POST)
        if formulario.is_valid:
            correo = request.POST['correo']
            contrasena = request.POST['contrasena']
        
        verificacion = RegistroEmpleado.objects.filter(correo=correo, contrasena=contrasena).exists()
        print(verificacion)

        if verificacion == True:
            return HttpResponseRedirect('/employ')
        else:   
            datos['mensaje'] = "Usuario o contraseña incorrecta, Ingrese nuevamente!."
             
    else:
        formulario = RegistroClienteForms()
    return render(request, "core/usuario.html", datos)

def admin_login(request):
    datos = {'form':LoginAdministradorForms()}
    
    if request.method == 'POST':

        formulario = RegistroAdministradorForm(request.POST)
        if formulario.is_valid:
            correo = request.POST['correo']
            contrasena = request.POST['contrasena']
        
        verificacion = RegistroAdministrador.objects.filter(correo=correo, contrasena=contrasena).exists()
        print(verificacion)

        if verificacion == True:
            return HttpResponseRedirect('/adminis')
        else:   
            datos['mensaje'] = "Usuario o contraseña incorrecta, Ingrese nuevamente!."
             
    else:
        formulario = RegistroAdministradorForm()
    return render(request, "core/admin_login.html", datos)

def logeado(request):
    return render (request, 'core/logeado.html')

def cliente(request):
    datos = {'form':LoginClienteForms()}
    
    if request.method == 'POST':

        formulario = RegistroClienteForms(request.POST)
        if formulario.is_valid:
            correo = request.POST['correo']
            contrasena = request.POST['contrasena']
        
        verificacion = RegistroCliente.objects.filter(correo=correo, contrasena=contrasena).exists()
        print(verificacion)

        if verificacion == True:
            return HttpResponseRedirect('/logeado')
        else:   
            datos['mensaje'] = "Usuario o contraseña incorrecta, Ingrese nuevamente!."
             
    else:
        formulario = RegistroClienteForms()
    return render(request, "core/cliente.html", datos)
   
def registro(request):
    datos = {'form':RegistroClienteForms()}

    if request.method == 'POST':

        formulario = RegistroClienteForms(request.POST)
        if formulario.is_valid:
            contrasena = request.POST['contrasena']
            confirmar_contrasena = request.POST['confirmar_contrasena']
            if contrasena == confirmar_contrasena:
                formulario.save()
                datos['mensaje'] = "Usuario creado con exito!."

                datos['form'] = formulario
            else:
                datos['mensaje'] = "Contraseñas no coinciden!. Ingrese nuevamente"

                datos['form'] = formulario
    return render(request, "core/registro.html", datos)

def administrador(request):
    return render (request, 'core/administrador.html')

def pendiente(request):
    return render (request, 'core/pendiente.html')

def cajacambio(request):
    return render (request, 'core/cajacambio.html')

def pantalladireccion(request):
    return render (request, 'core/pantalladireccion.html')

def pantallaelectronica(request):
    return render (request, 'core/pantallaelectronica.html')   

def ing_producto(request):
    datos = {'form':ArticuloForm()}

    if request.method == 'POST':

        formulario = ArticuloForm(request.POST)

        if formulario.is_valid:

            formulario.save()

            datos['mensaje'] = "Productos guardados con exito!."

            datos['form'] = formulario

    return render(request, "core/ing_producto.html", datos)

def registro_usuario(request):
    datos = {'form':RegistroEmpleadoForm()}

    if request.method == 'POST':

        formulario = RegistroEmpleadoForm(request.POST)

        if formulario.is_valid:

            contrasena = request.POST['contrasena']
            confirmar_contrasena = request.POST['confirmar_contrasena']
            if contrasena == confirmar_contrasena:
                formulario.save()

                datos['mensaje'] = "Usuario creado con exito!."

                datos['form'] = formulario
            else:
                datos['mensaje'] = "Contraseñas no coinciden!. Ingrese nuevamente"

                datos['form'] = formulario

    return render(request, "core/registro_usuario.html", datos)

def employ(request):
    return render (request, 'core/employ.html')

def reg_factura_boleta(request):
    return render (request, 'core/reg_factura_boleta.html')

def reg_orden_pedido(request):
    return render (request, 'core/reg_orden_pedido.html')

def reg_recep_producto(request):
    return render (request, 'core/reg_recep_producto.html')

def adminis(request):
    return render (request, 'core/adminis.html')

def reg_proveedores(request):
    datos = {'form':RegistroProveedorForm()}

    if request.method == 'POST':

        formulario = RegistroProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Proveedor registrado con exito!'

            datos['form'] = formulario
        else:
            datos['mensaje'] = "Error proveedor no registrado"

            datos['form'] = formulario
    return render (request, 'core/reg_proveedores.html', datos)  

def reg_servicios(request):
    datos = {'form':RegistroServicioForm()}

    if request.method == 'POST':

        formulario = RegistroServicioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Servicio registrado con exito!'

            datos['form'] = formulario
        else:
            datos['mensaje'] = "Error al registrar servicio"

            datos['form'] = formulario
    return render (request, 'core/reg_servicios.html', datos)  


def reserva_hra(request):
    datos = {'form':RegistroHoraForm()}

    if request.method == 'POST':

        formulario = RegistroHoraForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Reserva registrada exitosamente, se enviara un email con los datos de reserva'

            datos['form'] = formulario
        else:
            datos['mensaje'] = "Error hora no agendada"

            datos['form'] = formulario
    return render (request, 'core/reserva_hra.html', datos)

def catalogo(request):
    articulo = Articulo.objects.all()
    return render (request, 'core/catalogo.html',{'articulo': articulo})
