from django.contrib import admin
from .models import RegistroCliente
admin.site.register(RegistroCliente)

from .models import RegistroAdministrador
admin.site.register(RegistroAdministrador)

from .models import RegistroEmpleado
admin.site.register(RegistroEmpleado)

from .models import Articulo
admin.site.register(Articulo)

from .models import Categoria
admin.site.register(Categoria)

from .models import RegistroHora
admin.site.register(RegistroHora)



# Register your models here.

