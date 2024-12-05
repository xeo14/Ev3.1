from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from X import views

urlpatterns = [
path('admin/', admin.site.urls),  
    path('', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),  
    path('register/', views.register_view, name='register'),  
    
    path('animales/', views.listadoAnimales, name='listadoAnimales'), 
    path('agregarAnimales/', views.agregarAnimales, name='agregarAnimales'),  
    path('eliminarAnimales/<int:id>/', views.eliminarAnimales, name='eliminarAnimales'),  
    path('actualizarAnimales/<int:id>/', views.actualizarAnimales, name='actualizarAnimales'), 
    
    path('personas/', views.listadoPersonas, name='listadoPersonas'), 
    path('agregarPersona/', views.agregarPersonas, name='agregarPersona'),  
    path('eliminarPersona/<int:id>/', views.eliminarPersona, name='eliminarPersona'),  
    path('actualizarPersona/<int:id>/', views.actualizarPersona, name='actualizarPersona'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
