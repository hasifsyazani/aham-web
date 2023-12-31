from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from apps.home.models import CustomerInfo
from django.views.generic import ListView, UpdateView, FormView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from apps.home.forms import CustomerEditForm, CustomerAddForm
import datetime as dt
from django.db.models import F
from django.contrib import messages


@login_required(login_url="/login/")
def index(request):
    """_summary_
    Render mock dashboards from existing template

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    context = {}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request,))

@method_decorator(login_required, name='dispatch')
class CustomerList(ListView):
    """_summary_
    Render list of customers to table

    Args:
        ListView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = CustomerInfo
    template_name = 'home/table.html'
    paginate_by = 10
    
    def get_queryset(self):
        return self.model.objects.all().order_by(
            F('date_modified').desc(nulls_last=True)
            )

@method_decorator(login_required, name='dispatch')
class EditCustomer(SuccessMessageMixin, UpdateView):
    """_summary_
    Edit form for customer information 

    Args:
        SuccessMessageMixin (_type_): _description_
        UpdateView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = CustomerInfo
    form_class = CustomerEditForm
    template_name = 'home/edit_customer.html'
    success_message = "Customer info has been updated"
    success_url = reverse_lazy('listcust')
    
    def form_valid(self, form):
        self.object.date_modified = dt.datetime.now()
        return super().form_valid(form)
    
@method_decorator(login_required, name='dispatch')
class AddCustomer(SuccessMessageMixin, FormView):
    """_summary_
    Add form for new customer    

    Args:
        SuccessMessageMixin (_type_): _description_
        FormView (_type_): _description_

    Returns:
        _type_: _description_
    """
    form_class = CustomerAddForm
    template_name = 'home/add_customer.html'
    success_message = "New customer has been added"
    success_url = reverse_lazy('listcust')
    
    def form_valid(self, form):
        obj = CustomerInfo()
        obj.first_name = form.cleaned_data['first_name']
        obj.last_name = form.cleaned_data['last_name']
        obj.email_address = form.cleaned_data['email_address']
        obj.address = form.cleaned_data['address']
        obj.phone_no = form.cleaned_data['phone_no']
        obj.date_modified = dt.datetime.now()
        obj.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')   
class DeleteCustomer(DeleteView):
    """_summary_
    Delete form for customer

    Args:
        DeleteView (_type_): _description_

    Returns:
        _type_: _description_
    """
    model = CustomerInfo
    success_message = "Customer has been removed"
    success_url = reverse_lazy('listcust')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteCustomer, self).delete(request, *args, **kwargs)


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
