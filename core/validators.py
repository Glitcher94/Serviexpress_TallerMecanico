from django.core.exceptions import ValidationError

def validar(value):
    if not len(value) > 4:
        raise ValidationError('Mínimo 4 caracteres')

def validar2(contrasena):
    if validar3 != contrasena:
        raise ValidationError('Error al confirmar contraseña')

def validar3(confirmar_contrasena):
    if validar2 != confirmar_contrasena:
        raise ValidationError('Error al confirmar contraseña')