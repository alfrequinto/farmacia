from django import forms
from .models import Empleado, Administrador, Proveedor, Medicamento

class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombres','apellidos','telefono','cargo']
        
class FormAdministrador(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombres','apellidos','codigo','telefono']
        
class FormProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor','ruc','telefono','direccion']
        
class FormMedicamento(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre','fecha_expiracion','fecha_produccion','precio_Compra','precio_venta']