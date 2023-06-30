from django.shortcuts import render
from django.views.generic import CreateView
from .forms import myform
from .models import Datavisualization
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

def get(request):
    data = Datavisualization.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/index.html', {"data":page_obj})

    
class data(CreateView):
    model=Datavisualization
    form_class=myform
    template_name='myapp/myform.html'
    success_url =reverse_lazy('home')
    
class ContactListView(ListView):
    paginate_by = 4
    model = Datavisualization
    
    
    
