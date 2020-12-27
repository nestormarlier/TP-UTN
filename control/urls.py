from django.urls import path
from control.views.fichatecnica.views import *
from control.views.categoria.views import *
from control.views.operario.views import *
from control.views.impresora.views import *
from control.views.parteimpresion.views import *
from control.views.parada.views import *
from control.views.cambiomecanico.views import *
from control.views.setup.views import *
from control.views.produccion.views import *


urlpatterns = [
    path('fichatecnicaxfuncion/list/', fichatecnica_list, name='fichatecnica_list_x_funcion'),
    path('fichatecnica/list/', FichaTecnicaListView.as_view(), name='fichatecnica_list'),
    path('categoria/list/', CategoriaListView.as_view(), name='categoria_list'),
    path('operario/list/', OperarioListView.as_view(), name='operario_list'), 
    path('impresora/list/', ImpresoraListView.as_view(), name="impresora_list"),
    path('parada/list/', ParadaListView.as_view(), name='parada_list'),
    path('cambiomecanico/list/', CambioMecanicoListView.as_view(), name='cambiomecanico_list'),
    path('setup/list/', SetupListView.as_view(), name='setup_list'),
    path('produccion/list/', ProduccionListView.as_view(), name='produccion_list'),
    path('parteimpresion/list/', ParteImpresionListView.as_view(), name="parteimpresion_list"),
    ### ALTAS ###
    path('categoria/alta/', CategoriaCreateView.as_view(), name="categoria_create"),
    path('fichatecnica/alta/', FichaTecnicaCreateView.as_view(), name="fichatecnica_create"),
    path('operario/alta/', OperarioCreateView.as_view(), name="operario_create"),
    path('impresora/alta/', ImpresoraCreateView.as_view(), name='impresora_create'),
    path('parada/alta/', ParadaCreateView.as_view(), name='parada_create'),
    path('cambiomecanico/alta/', CambioMecanicoCreateView.as_view(), name='cambiomecanico_create'),
]