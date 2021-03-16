from django.urls import path
from apps.control.views.fichatecnica.views import *
from apps.control.views.impresora.views import *
from apps.control.views.parteimpresion.views import *
from apps.control.views.parada.views import *
from apps.control.views.cambiomecanico.views import *
from apps.control.views.setup.views import *
from apps.control.views.produccion.views import *


urlpatterns = [
    path('impresora/list/', ImpresoraListView.as_view(), name="impresora_list"),
    path('parada/list/', ParadaListView.as_view(), name='parada_list'),
    path('cambiomecanico/list/', CambioMecanicoListView.as_view(), name='cambiomecanico_list'),
    path('setup/list/', SetupListView.as_view(), name='setup_list'),
    path('produccion/list/', ProduccionListView.as_view(), name='produccion_list'),
    path('parteimpresion/list/', ParteImpresionListView.as_view(), name="parteimpresion_list"),
    ### ALTAS ###
    path('fichatecnica/alta/', FichaTecnicaCreateView.as_view(), name="fichatecnica_create"),
    path('impresora/alta/', ImpresoraCreateView.as_view(), name='impresora_create'),
    path('parada/alta/', ParadaCreateView.as_view(), name='parada_create'),
    path('cambiomecanico/alta/', CambioMecanicoCreateView.as_view(), name='cambiomecanico_create'),
    ### MODIFICACIONES ###
    path('impresora/modif/<int:pk>/', ImpresoraUpdateView.as_view(), name='impresora_edit'),
    ### BAJAS ###
    path('impresora/baja/<int:pk>/', ImpresoraDeleteView.as_view(), name='impresora_delete'),
]