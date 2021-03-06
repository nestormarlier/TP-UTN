from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from django.urls import reverse_lazy
from control.models import Impresora
from control.forms import ImpresoraForm


class ImpresoraListView(ListView):
    model = Impresora
    template_name = 'impresora/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}        
        try:
            action = request.POST['accion']
            if action == 'buscar':
                data = []
                for i in Impresora.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    # def post(self, request, *args, **kwargs):
    #     data = {}
    #     try:
    #         # data = Impresora.objects.get(
    #         #     pk=request.POST['impresora_id']).toJSON()
    #         action = request.POST['accion']
    #         if action == 'buscardatos':
    #             data = []
    #             for i in Impresora.objects.all():
    #                 data.append(i.toJSON())
    #         else:
    #             data['error'] = 'Ha ocurrido un error'
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Listado de impresoras'
        context['entidad'] = 'Impresora'
        context['create_url'] = reverse_lazy('impresora_create')
        return context

class ImpresoraCreateView(CreateView):
    model = Impresora
    form_class = ImpresoraForm
    template_name = "impresora/create.html"
    success_url = reverse_lazy('impresora_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['accion']
            if action == 'add':
                #form = CategoryForm(request.POST)
                # con esta propiedad obtengo todos los datos enviado, inclusive si son imagenes
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Creación de impresoras'
        context['entidad'] = 'Impresora'
        context['list_url'] = self.success_url
        context['accion'] = 'add'
        return context

class ImpresoraUpdateView(UpdateView):
    model = Impresora
    form_class = ImpresoraForm
    template_name = "impresora/create.html"
    success_url = reverse_lazy('impresora_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object() 
        # para que el funcionamiento no se altere y para que funcione el POST como edit y no como create
        return super().dispatch(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['accion']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edición de una impresora'
        context['entidad'] = 'Impresora'
        context['list_url'] = self.success_url
        context['accion'] = 'edit'
        return context

class ImpresoraDeleteView(DeleteView):
    model = Impresora
    template_name = 'impresora/delete.html'
    success_url = reverse_lazy('impresora_list')

    #@method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Eliminación de una impresora'
        context['entidad'] = 'Impresora'
        context['list_url'] = self.success_url
        return context