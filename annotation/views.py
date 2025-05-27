from django.shortcuts import render
# annotations/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from .models import Annotation
from django.contrib.auth.decorators import login_required
from .forms import AnnotationForm
# Create your views here.

def annotation_list(request):
    annotations = Annotation.objects.all()
    return render(request, "annotation_list.html", {"annotations": annotations})

def annotation_detail(request, pk):
    annotation = get_object_or_404(Annotation, pk=pk)
    return render(request, "annotation_detail.html", {"annotation": annotation})

@login_required
def annotation_create(request):
    if request.method == "POST":
        form = AnnotationForm(request.POST)
        if form.is_valid():
            annotation = form.save(commit=False)
            annotation.created_by = request.user
            annotation.save()
            return redirect("annotations:annotation_list")
    else:
        form = AnnotationForm()
    return render(request, "annotation_form.html", {"form": form})


@login_required
def annotation_update(request, pk):
    annotation = get_object_or_404(Annotation, pk=pk)
    form = AnnotationForm(request.POST or None, instance=annotation)
    if form.is_valid():
        form.save()
        return redirect("annotation:annotation_list")
    return render(request, "annotation_form.html", {"form": form})



@login_required
def annotation_delete(request, pk):
    annotation = get_object_or_404(Annotation, pk=pk)
    if request.method == "POST":
        annotation.delete()
        return redirect("annotation:annotation_list")
    return render(request, "annotation_confirm_delete.html", {"annotation": annotation})
