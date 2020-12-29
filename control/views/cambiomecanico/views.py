from control.models import CambioMecanico
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from control.forms import CambioMecanicoForm
from django.urls import reverse_lazy

class CambioMecanicoListView(ListView):
    model = CambioMecanico
    template_name = 'cambiomecanico/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = CambioMecanico.objects.get(pk = request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de cambio mecánicos asignados a un parte de impresión'
        context['create_url'] = reverse_lazy('cambiomecanico_create')
        context["entidad"] = 'Cambio Mecánico'
        return context

class CambioMecanicoCreateView(CreateView):
    model = CambioMecanico
    template_name = "cambiomecanico/create.html"
    form_class = CambioMecanicoForm
    success_url = reverse_lazy('cambiomecanico_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_url'] = self.success_url
        context["title"] = 'Cambio Mecánico'
        context['entidad'] = 'Cambio Mecánico'
        return context