from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Blog, ReviewBlog
from apps.homepage.models import SettingMain
from apps.aboutpage.models import AboutAuthor

from apps.gallery.models import Gallery
from apps.contacts.models import Contact

from .forms import ReviewForm

class BlogDetailView(DetailView):
    model = Blog
    slug_field = "slug"
    template_name = "blogs/blog-single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        return context 


class BlogListView(ListView):
    model = Blog
    queryset = model.objects.all()
    template_name = "blogs/blog-archive.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_author'] = AboutAuthor.objects.get(id=1)
        context['posts'] = Blog.objects.all()[::-1][:3]

        # settings
        context['setting'] = SettingMain.objects.get(active=True)
        context['blogs'] = Blog.objects.all()[::-1][:2]
        context['images'] = Gallery.objects.all()[2:8]
        context['contacts'] = Contact.objects.get(id=1)
        return context 


class AddReview(View):
    def get(self, request, pk):
        form = ReviewForm(request.POST)
        blog = Blog.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog = blog
            form.save()
        return redirect("/")