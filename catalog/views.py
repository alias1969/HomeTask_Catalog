from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Contacts


class ProductListView(ListView):
    """ Контроллер отображения списка продукции"""
    model = Product


class ProductDetailView(DetailView):
    """ Страница карточки продукта"""
    model = Product


class ProductCreateView(CreateView):
    """ Страница создания продукта"""
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    """ Страница редактирования продукта"""
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image')
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    """ Страница удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactsView(TemplateView):
    """Страница контактов"""
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context

