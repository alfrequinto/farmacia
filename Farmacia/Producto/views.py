from django.shortcuts import render, get_object_or_404, redirect
from .models import Administrador, Empleado, Medicamento, Proveedor
from .forms import FormAdministrador, FormEmpleado, FormProveedor, FormMedicamento
from django.db.models import Q
from datetime import datetime

def home(request):
    return render(request, "paginas/g_principal.html")

def pag_principal(request):
    return render(request, "paginas/g_principal.html")

def empleado(request):
    query = request.GET.get('q')

    if query:
        empleados = Empleado.objects.filter(
            Q(id__icontains=query) | Q(nombres__icontains=query)
        )
    else:
        empleados = Empleado.objects.all()

    return render(request, 'ediciones/g_empleados.html', {'empleado': empleados})

def registroempleado(request):
    if request.method == 'POST':
        nombres = request.POST['txtNombres']
        apellidos = request.POST['txtApellidos']
        telefono = request.POST['numTelefono']
        cargo = request.POST['txtCargo']

        Empleado.objects.create(nombres=nombres, apellidos=apellidos, telefono=telefono, cargo=cargo)
        return redirect('empleado')
    
    return render(request, 'ediciones/g_empleados.html')

def edicion_empleado(request, id):
    empleado= Empleado.objects.get(id=id)
    return render(request, "ediciones/edicionEmpleados.html", {"empleado": empleado})

def editar_empleado(request, id):
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    telefono = request.POST['numTelefono']
    cargo = request.POST['txtCargo']
    
    empleado = Empleado.objects.get(id=id)
    empleado.nombres=nombres
    empleado.apellidos=apellidos
    empleado.telefono=telefono
    empleado.cargo = cargo
    empleado.save()

    return redirect('empleado')

def eliminarempleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('empleado')


def administrador(request):
    query = request.GET.get('q')

    if query:
        administrador = Administrador.objects.filter(
            Q(id__icontains=query) | Q(nombres__icontains=query)
        )
    else:
        administrador = Administrador.objects.all()

    return render(request, 'ediciones/g_administrador.html', {'admin': administrador})

def registrar_administrador(request):
    if request.method == 'POST':
        nombres = request.POST['txtNombres']
        apellidos = request.POST['txtApellidos']
        codigo = request.POST['numCodigo']
        telefono = request.POST['numTelefono']

        Administrador.objects.create(nombres=nombres, apellidos=apellidos, codigo=codigo, telefono=telefono)
        return redirect('administrador')
    
    return render(request, 'ediciones/g_administrador.html')


def edicion_administrador(request, id):
    administrador= Administrador.objects.get(id=id)
    return render(request, "ediciones/edicionAdministrador.html", {"administrador": administrador})

def editar_administrador(request, id):
    nombres = request.POST['txtNombres']
    apellidos = request.POST['txtApellidos']
    codigo = request.POST['numCodigo']
    telefono = request.POST['numTelefono']
    
    administrador = Administrador.objects.get(id=id)
    administrador.nombres=nombres
    administrador.apellidos=apellidos
    administrador.codigo=codigo
    administrador.telefono=telefono
    administrador.save()

    return redirect('administrador')

def eliminarAdministrador(request,id):
    administrador = Administrador.objects.get(id=id)
    administrador.delete()
    return redirect('administrador')

def proveedor(request):
    query = request.GET.get('q')

    if query:
        proveedor = Proveedor.objects.filter(
            Q(id__icontains=query) | Q(nombre_proveedor__icontains=query)
        )
    else:
        proveedor = Proveedor.objects.all()

    return render(request, 'ediciones/g_proveedor.html', {'Proveedores': proveedor})

def registro_proveedor(request):
    if request.method == 'POST':
        nombre_proveedor=request.POST['txtNombre']
        ruc = request.POST['numRuc']
        telefono = request.POST['numTelefono']
        direccion = request.POST['txtDireccion']

        Proveedor.objects.create(nombre_proveedor=nombre_proveedor, ruc=ruc, telefono=telefono, direccion=direccion)
        return redirect('proveedor')
    
    return render(request, 'ediciones/g_proveedor.html')


def edicion_proveedor(request, id):
    proveedor= Proveedor.objects.get(id=id)
    return render(request, "ediciones/edicionProveedor.html", {"Proveedores": proveedor})

def editar_proveedor(request, id):
    nombre_proveedor=request.POST['txtNombre']
    ruc = request.POST['numRuc']
    telefono = request.POST['numTelefono']
    direccion = request.POST['txtDireccion']
    
    proveedor= Proveedor.objects.get(id=id)
    proveedor.nombre_proveedor= nombre_proveedor
    proveedor.ruc=ruc
    proveedor.telefono=telefono
    proveedor.direccion=direccion
    proveedor.save()

    return redirect('proveedor')

def eliminarProveedor(request,id):
    proveedor = Proveedor.objects.get(id=id)
    proveedor.delete()
    return redirect('proveedor')


def medicamento(request):
    query = request.GET.get('q')

    if query:
        medicamento = Medicamento.objects.filter(
            Q(id__icontains=query) | Q(nombre__icontains=query)
        )
    else:
        medicamento = Medicamento.objects.all()

    return render(request, 'ediciones/g_medicamento.html', {'medicamento': medicamento})

def registro_medicamento(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        fecha_expiracion = datetime.strptime(request.POST['numFechaexpiracion'], '%d/%m/%Y').date()
        fecha_produccion = datetime.strptime(request.POST['numFechaproduccion'], '%d/%m/%Y').date()
        precio_Compra = request.POST['numCompra']
        precio_venta = request.POST['numVenta']

        Medicamento.objects.create(nombre=nombre, fecha_expiracion=fecha_expiracion, fecha_produccion=fecha_produccion, precio_Compra=precio_Compra, precio_venta=precio_venta)
        return redirect('medicamento')
    
    return render(request, 'ediciones/g_medicamento.html')

def edicion_medicamento(request, id):
    medicamento= Medicamento.objects.get(id=id)
    return render(request, "ediciones/edicionMedicamentos.html", {"medicamento": medicamento})
    
def editar_medicamento(request, id):
    nombre = request.POST['txtNombre']
    fecha_expiracion = datetime.strptime(request.POST['numFechaexpiracion'], '%d/%m/%Y').date()
    fecha_produccion = datetime.strptime(request.POST['numFechaproduccion'], '%d/%m/%Y').date()
    precio_Compra = request.POST['numCompra']
    precio_venta = request.POST['numVenta']
    
    medicamento =  Medicamento.objects.get(id=id)
    medicamento.nombre = nombre 
    medicamento.fecha_expiracion=fecha_expiracion
    medicamento.fecha_produccion=fecha_produccion
    medicamento.precio_Compra=precio_Compra
    medicamento.precio_venta=precio_venta
    medicamento.save()
    
    return redirect('medicamento')

def eliminarMedicamento(request,id):
    medicamento = Medicamento.objects.get(id=id)
    medicamento.delete()
    return redirect('medicamento')  