from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add_image, name='addImage'),
    url(r'^registration/$', views.user_registration_view, name='registration'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfilaActializar/$', views.perfil_actualizar, name='perfilActualizar'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^perfil/password/$', views.cambiar_contrasenia, name='cambiar_contrasenia')
]
