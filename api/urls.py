from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('encargado', views.EncargadoView)
router.register('recurso', views.RecursoView)
router.register('tiporecurso', views.TipoRecursoView)
router.register('tipoencargado', views.TipoEncargadoView)
router.register('proveedor', views.ProveedorView)

urlpatterns = [
    path('', include(router.urls)),
    # path('encargado/', views.EncargadoList.as_view(), name='encargado'),
    # path('recurso/', views.RecursoView.as_view(), name='recurso'),
    # path('tiporecurso/', views.TipoRecursoList.as_view(), name='recurso'),
    # path('tipoencargado/', views.TipoEncargadoList.as_view(), name='recurso'),
    # path('proveedor/', views.ProveedorList.as_view(), name='recurso')
]
