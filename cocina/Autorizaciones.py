from django.contrib import admin, messages
from .models import orden, productoOrden, receta, productoReceta, gastosAdicionalesReceta

@admin.action(description="Confirmar sesion")
def confirmar_orden(modeladmin, request, queryset): 

    #Validacion para que seleccione solo 1 queryset
    if len(queryset) != 1:
        messages.error(request, "Solo se puede aceptar 1 orden a la vez.")
        return
    
    orden = queryset[0]

    if orden.Estado != "Pendiente":
        messages.error(request, "El pedido ya se encuentra confirmado.")
        return
    else:
        orden.Estado = "Aceptado"
        orden.TotalOrden = orden.total_costo()
        orden.save()
        return
    
@admin.action(description="Terminar sesion")
def terminar_orden(modeladmin, request, queryset): 
    
    for orden in queryset:

        productos = productoOrden.objects.filter(Orden= orden)
        
        texto = "-"

        diagnostico = orden.diagnostico_set.first().concatenar_campos() if orden.diagnostico_set.first() is not None else '-'
        

        for prod in productos:
            productoss = productoReceta.objects.filter(Receta = prod.Producto)
            for produc in productoss:
                texto += f"{produc.Producto.Nombre} - Cantidad: {produc.Cantidad}\n"

        
        orden.detalle_final = texto
        orden.diagnostico_final = diagnostico
        orden.TotalOrden = orden.total_costo()
        orden.Estado = "Entregado"
        orden.save()
        
    messages.success(request, "Sesion terminada correctamente.")
    return
    