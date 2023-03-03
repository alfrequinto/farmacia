from django.contrib import admin
from .models import Empleado
from .models import Administrador
from .models import Proveedor
from .models import Medicamento

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Administrador)
admin.site.register(Proveedor)
admin.site.register(Medicamento)

