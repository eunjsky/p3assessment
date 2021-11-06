from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm


def home(request):
    if request.method == "POST":
        widget_form = WidgetForm(request.POST)
        if widget_form.is_valid():
            widget_form.save()
        else:
            print('failed')

        return redirect('home')
    widget_form = WidgetForm()
    widgets = Widget.objects.all()
    return render(request, 'home.html', {'widgets': widgets, 'widget_form': widget_form})


def delete_widget(request, pk):
    widgets = Widget.objects.get(id=pk)
    widgets.delete()
    return redirect('home')


# def add_widget(request):
#     form = WidgetForm(request.POST)
#     if form.is_valid():
#         add_widget = form.save(commit=False)
#         add_widget.save()
#         print('working')
#     return redirect('home')
# path('', views.add_widget, name='add_widget'),

# def WidgetCreate(request):
#     if request.method == 'POST':
#         form = WidgetForm(request.POST, request.FILES)
#         if form.is_valid():
#             widget = form.save()
#             widget.save()
#             print('working')
#             return redirect('home')
#         else:
#             return redirect('home')
#     else:
#         widget = WidgetForm()
#         print('checking')
#     return render(request, 'home.html', {'widget': widget})
