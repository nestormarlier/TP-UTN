from apps.control.models import ParteImpresion
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from apps.control.forms import ParteImpresionForm
from django.urls import reverse_lazy

class ParteImpresionListView(ListView):
    model = ParteImpresion
    template_name = 'parteimpresion/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = ParteImpresion.objects.get(pk = request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de partes de impresión'
        return context

class ParteImpresionCreateView(CreateView):
    model = ParteImpresion
    template_name = "parteimpresion/create.html"
    form_class = ParteImpresionForm
    success_url = reverse_lazy('parteimpresion_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación parte de impresión'
        context['entidad'] = 'Parte de impresión'
        context['list_url'] = self.success_url
        context['accion'] = 'add'
        return context
    