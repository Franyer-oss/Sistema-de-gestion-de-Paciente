from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_facturas, name='lista_facturas'),
    path('crear/', views.crear_factura, name='crear_factura'),
    path('actualizar/<int:id>/', views.actualizar_factura, name='actualizar_factura'),
    path('eliminar/<int:id>/', views.eliminar_factura, name='eliminar_factura'),
    path('detalle/<int:id>/', views.detalle_factura, name='detalle_factura'),
]
