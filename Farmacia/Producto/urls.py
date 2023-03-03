from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('g_principal.html', views.pag_principal, name="principal"),
    path('g_empleados.html', views.empleado, name='empleado'),
    path('registroempleado/', views.registroempleado, name='registro_empleado'),
    path('edicion_empleado/<int:id>/', views.edicion_empleado, name='edicion_empleado'),
    path('editar_empleado/<int:id>/', views.editar_empleado, name='editar_empleado'),
    path('eliminarempleado/<int:id>/', views.eliminarempleado, name='eliminarempleado'),
    
    path('g_administrador.html', views.administrador, name='administrador'),
    path('registrar-administrador/', views.registrar_administrador, name='registrar_administrador'),
    path('edicion_administrador/<int:id>/', views.edicion_administrador, name='edicion_administrador'),
    path('editar_administrador/<int:id>/', views.editar_administrador, name='editar_administrador'),
    path('eliminarAdministrador/<id>', views.eliminarAdministrador),
    
    path('g_proveedor.html', views.proveedor, name='proveedor'),
    path('registro_proveedor/', views.registro_proveedor, name='registro_proveedor'),
    path('edicion_proveedor/<int:id>', views.edicion_proveedor, name='edicion_proveedor'),
    path('editar_proveedor/<int:id>', views.editar_proveedor, name='editar_proveedor'),
    path('eliminarProveedor/<id>', views.eliminarProveedor),
    
    path('g_medicamento.html', views.medicamento, name='medicamento'),
    path('registro_medicamento/', views.registro_medicamento, name='registro_medicamento'),
    path('edicion_medicamento/<int:id>', views.edicion_medicamento, name='edicion_medicamento'),
    path('editar_medicamento/<int:id>', views.editar_medicamento, name='editar_medicamento'),
    path('eliminarMedicamento/<int:id>', views.eliminarMedicamento),
]