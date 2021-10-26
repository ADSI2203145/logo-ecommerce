from django.contrib.auth import login
from django.urls import path
from  .import views

urlpatterns = [
	
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('logins/', views.logins, name='logins' ),
	path('registrar_usuario/', views.registrar_usuario, name='registrar'),
	path('producto/',views.nuevo_producto, name='producto'),
	path('lista/',views.lista_produtos, name='lista'),
	path('editar/<id>/',views.editar_produtos, name='editar'),
	path('eliminar/<id>/',views.elimanar_producto, name='eliminar'),
	
	path('categoria/',views.nueva_categoria, name='categoria'),
	path('listar/',views.lista_categoria, name='listar'),
	path('edita/<id>/',views.editar_categoria, name='edita'),
	path('elimina/<id>/',views.elimina_categoria, name='elimina'),

]