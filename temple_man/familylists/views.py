from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Family


def home(request):
    all_posts = Family.objects.all()
    return render(request, 'index.html', {'posts': all_posts})

