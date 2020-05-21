from django.shortcuts import render

from .models import App

def app_detail_view(request, id=1):
    obj = App.objects.get(id=id)
    print(obj)
    context = {
        "object" : obj
    }
    return render(request, "app/detail_view.html", context)

def app_list_view(request, id=1):
    queryset = App.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.content)
    context = {
        "object_list" : queryset
    }
    return render(request, "app/list_view.html", context)