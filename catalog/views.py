from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from catalog.forms import ProductForm, VersionForms, ProductModeratorForm
from catalog.models import Product, Contacts, Version


class ProductListView(ListView):
    """Контроллер отображения списка продукции"""

    model = Product


class ProductDetailView(DetailView):
    """Страница карточки продукта"""

    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        current_version = self.object.versions.filter(is_current_version=True)
        context_data["current_version"] = current_version
        return context_data


class ProductCreateView(CreateView, LoginRequiredMixin):
    """Страница создания продукта"""

    model = Product
    form_class = ProductForm
    # fields = ("name", "description", "category", "price", "image")
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        #автор = текущий пользователь
        user = self.request.user
        product.owner = user
        #product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    """Страница редактирования продукта"""

    model = Product
    form_class = ProductForm
    # fields = ("name", "description", "category", "price", "image")
    success_url = reverse_lazy("catalog:home")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForms, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ProductFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm
        elif min(user.has_perm('can_edit_description'),
                 user.has_perm('can_edit_category'),
                 user.has_perm('can_edit_is_published')):
            return ProductModeratorForm
        else:
            return PermissionDenied


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    """Страница удаления продукта"""

    model = Product
    success_url = reverse_lazy("catalog:home")


class ContactsView(TemplateView):
    """Страница контактов"""

    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contacts.objects.all()
        return context
