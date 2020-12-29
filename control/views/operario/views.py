from control.models import Operario
from django.views.generic import ListView, CreateView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from control.forms import OperarioForm
from django.urls import reverse_lazy


class OperarioListView(ListView):
    model = Operario
    template_name = 'operario/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Operario.objects.get(pk=request.POST['legajo']).toJSON
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de operarios'
        context['entidad'] = 'Operario'
        context['create_url'] = reverse_lazy('operario_create')
        return context


class OperarioCreateView(CreateView):
    model = Operario
    template_name = "operario/create.html"
    form_class = OperarioForm
    success_url = reverse_lazy('operario_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación operario'
        context['entidad'] = 'Operario'
        context['list_url'] = self.success_url
        return context
