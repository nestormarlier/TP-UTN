from django.shortcuts import render
from apps.control.models import CategoriasUsuario
from django.http import JsonResponse, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator

from django.urls import reverse_lazy

from apps.control.forms import CategoriasUsuarioForm


class CategoriasUsuarioListView(ListView):
    model = CategoriasUsuario
    template_name = "categoria/list.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['accion']
            if action == 'searchdata':
                data = []
                for i in Impresora.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorías'
        context["entidad"] = 'Categoría'
        context["list_url"] = reverse_lazy('categoria_list')
        context["create_url"] = reverse_lazy('categoria_create')
        return context


class CategoriasUsuarioCreateView(CreateView):
    model = CategoriasUsuario
    form_class = CategoriasUsuarioForm
    template_name = "categoria/create.html"
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de una categoría'
        context["entidad"] = 'Categoría'
        context["list_url"] = reverse_lazy('categoria_list')

        return context