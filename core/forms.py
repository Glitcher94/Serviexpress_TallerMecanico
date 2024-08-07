from django import forms
from django.forms import ModelForm
from .models import Articulo, RegistroAdministrador, RegistroCliente, RegistroEmpleado, RegistroHora, RegistroHoraEmpleado, RegistroProveedor, RegistroServicio

class RegistroClienteForms(ModelForm):

    class Meta:

        model = RegistroCliente
        fields = ['correo','nombre', 'rut','fecha_nacimiento','direccion','estado_civil','contrasena','confirmar_contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),
            'confirmar_contrasena': forms.PasswordInput(attrs={'class':'form-control'}),


        }


class LoginAdministradorForms(ModelForm):

    class Meta:

        model = RegistroAdministrador
        fields = ['correo','contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),

        }




class LoginClienteForms(ModelForm):

    class Meta:

        model = RegistroCliente
        fields = ['correo','contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),

        }




class RegistroAdministradorForm(ModelForm):

    class Meta:

        model = RegistroAdministrador

        fields = ['correo','nombre', 'rut','fecha_nacimiento','direccion','estado_civil','contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),
            

        }

        


class RegistroEmpleadoForm(ModelForm):

    class Meta:
        
        model = RegistroEmpleado
        
        fields = ['correo','nombre', 'rut','fecha_nacimiento','direccion','estado_civil','contrasena','confirmar_contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),
            'confirmar_contrasena': forms.PasswordInput(attrs={'class':'form-control'}),
        }

class LoginEmpleadoForms(ModelForm):

    class Meta:

        model = RegistroEmpleado
        fields = ['correo','contrasena']
        widgets = {

            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasena': forms.PasswordInput(attrs={'class':'form-control'}),

        }

class ArticuloForm(ModelForm):

    class Meta:

        model = Articulo

        fields = ['idArticulo','nombre','precio','cantidad','foto','categoria']
        widgets = {

            'idArticulo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.TextInput(attrs={'class': 'form-control'}),
            'foto': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            


        }

class RegistroHoraForm(ModelForm):

    class Meta:

        model = RegistroHora

        fields = ['idRegistro','hora','dia','modelo','anno','descripcion']
        widgets = {

            'idRegistro': forms.TextInput(attrs={'class': 'form-control'}),
            'hora': forms.TextInput(attrs={'class': 'form-control'}),
            'dia': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anno': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            
            


        }

class RegistroHoraEmpleadoForm(ModelForm):

    class Meta:

        model = RegistroHoraEmpleado

        fields = ['idRegistro','hora','dia','modelo','anno','descripcion','cliente']
        widgets = {

            'idRegistro': forms.TextInput(attrs={'class': 'form-control'}),
            'hora': forms.TextInput(attrs={'class': 'form-control'}),
            'dia': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anno': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            
            


        }

class RegistroProveedorForm(ModelForm):

    class Meta:

        model = RegistroProveedor

        fields = ['codigoProveedor','nombre','rut','direccion','telefono','giro','correo']
        widgets = {

            'codigoProveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'giro': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            
            


        }

class RegistroServicioForm(ModelForm):

    class Meta:

        model = RegistroServicio

        fields = ['codigo_servicio','nombre_servicio','precio','observacion']
        widgets = {

            'codigo_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),

        }

