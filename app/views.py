from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import App

class AppDetailView(DetailView):
    # template_name = "app/detail_view.html"
    queryset = App.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(App, pk=pk)
        return App.objects.get(id=pk)

class AppListView(ListView):
    # template_name = "app/list_view.html"
    queryset = App.objects.all()


def app_detail_view(request, id=1):
    obj = App.objects.get(id=id)
    print(obj)
    context = {
        "object" : obj
    }
    return render(request, "app/app_detail.html", context)

def app_list_view(request, id=1):
    queryset = App.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list" : queryset
    }
    return render(request, "app/app_list.html", context)