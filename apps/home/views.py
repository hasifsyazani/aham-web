from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from apps.home.models import CustomerInfo
from django.views.generic import ListView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from apps.home.forms import CustomerEditForm


@method_decorator(login_required, name='dispatch')
class Index(ListView):
    model = CustomerInfo
    template_name = 'home/index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


@method_decorator(login_required, name='dispatch')
class EditCustomer(SuccessMessageMixin, UpdateView):
    model = CustomerInfo
    form_class = CustomerEditForm
    template_name = 'home/edit_customer.html'
    success_message = "Customer has been updated"
    success_url = reverse_lazy('home')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def profile(request):
    """_summary_
    Render profile page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return render(request, 'home/profile.html', {})


@login_required(login_url="/login/")
def table(request):
    """_summary_
    Render profile page

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """    
    return render(request, 'home/table.html', {})
