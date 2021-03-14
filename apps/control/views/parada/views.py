from apps.control.models import Parada
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from apps.control.forms import ParadaForm
from django.urls import reverse_lazy
 
class ParadaListView(ListView):
    model = Parada
    template_name = 'parada/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        data = {}
        try:
            data = Parada.objects.get(pk = request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de paradas'
        context['entidad'] = 'Parada de máquina'
        context['create_url']= reverse_lazy('parada_create')
        return context
    
class ParadaCreateView(CreateView):    
    model = Parada
    template_name = "parada/create.html"
    form_class = ParadaForm
    success_url = reverse_lazy('parada_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación paradas de máquina'
        context['entidad'] = 'Parada de máquina'
        context['list_url'] = self.success_url
        return context
    

