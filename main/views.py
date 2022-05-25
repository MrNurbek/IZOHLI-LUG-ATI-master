from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Word


class HomePageView(TemplateView):
    extra_context = {'title': 'Bosh sahifa', 'countWords': Word.objects.all().count()}
    template_name = 'main/index.html'


class SearchResultsView(ListView):
    model = Word
    template_name = 'main/index.html'
    extra_context = {'title':'Bosh sahifa', 'countWords': Word.objects.all().count()}

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Word.objects.filter(Q(name=query))
        return object_list
