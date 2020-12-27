from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from control.models import FichaTecnica

from django.urls import reverse_lazy

from control.forms import FichaTecnicaForm


def fichatecnica_list(request):
    data = {
        'title': 'Listado de Fichas Técnicas',
        'categories': FichaTecnica.objects.all()
    }
    return render(request, 'fichatecnica/listfunction.html', data)


class FichaTecnicaListView(ListView):
    model = FichaTecnica
    template_name = 'fichatecnica/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = FichaTecnica.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Fichas Técnicas'
        context['entidad'] = 'Ficha técnica'
        context['create_url'] = reverse_lazy('erp:fichatecnica_create')
        
        return context

class FichaTecnicaCreateView(CreateView):
        model = FichaTecnica
        form_class = FichaTecnicaForm
        template_name = 'fichatecnica/create.html'
        success_url = reverse_lazy('erp:fichatecnica_list')

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["title"] = 'Creación de Ficha Técnica'
            context['entidad'] = 'Ficha técnica'
            context['list_url'] = self.success_url
            return context