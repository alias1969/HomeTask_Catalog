from audioop import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from blogs.models import Blogs


class BlogsListView(ListView):
    """ Страница списка блогов """
    model = Blogs

    def get_queryset(self, *args, **kwargs):
        """ Получает все публикации блога, которые опубликованы"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogsDetailView(DetailView):
    """ Страница просмотра блога"""
    model = Blogs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['headline'] = Blogs.objects.get(pk=self.kwargs['pk'])
        return context_data

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if object.count_views is None:
            object.count_views = 1
        else:
            object.count_views += 1
        object.save()

        return object


class BlogsCreateView(CreateView):
    """ Страница создания блога """
    model = Blogs
    fields = ('headline', 'content', 'preview')
    success_url = reverse_lazy('blogs:blogs_list')

    def form_valid(self, form):
        """ Проверяет данные на валидность и генерирует slug """
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.headline)
            new_blog.save()
        return super().form_valid(form)


class BlogsUpdateView(UpdateView):
    """ Страница редактирования блога"""
    model = Blogs
    fields = ('headline', 'content', 'preview')
    success_url = reverse_lazy('blogs:blogs_list')


class BlogsDeleteView(DeleteView):
    """ Страница удаления блока """
    model = Blogs
    success_url = reverse_lazy('blogs:blogs_list')

def toggle_activity(request, pk):
    blog = get_object_or_404(Blogs, pk=pk)
    blog.is_published = not blog.is_published
    blog.save()

    return redirect(reverse('blogs: blogs_list'))


