from django.shortcuts import render
from .models import PortFolio, Contact, Service, Testimonial, TeamMember
from .forms import PortFolioForm, ContactForm
from django.views .generic import DeleteView, CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
import math


def index(request):

    # contact

    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form = Contact(name=name, subject=subject,
                       email=email, message=message)
        form.save()
        return HttpResponseRedirect('success')

    # requests from the database

    service = Service.objects.filter(show=True)[:6]
    testimonial = Testimonial.objects.all()
    portfolio = PortFolio.objects.all()
    team = TeamMember.objects.all().count()

    # experience
    time_now = datetime.datetime.now().year
    time_then = datetime.datetime(year=2020, month=6, day=2).year
    time_born = datetime.datetime(year=2000, month=5, day=6).year
    time_difference = time_now - time_then
    age_diff = time_now - time_born

    context = {
        # for testimonial
        'testcount': testimonial.count(),
        'testimonial': testimonial[:5],

        # for service
        'service': service,

        # for team member
        'team': team,

        # for facts
        'projects': portfolio.count(),
        'hour': portfolio.count() * 8,

        # experience & age
        'experience': time_difference,
        'age': age_diff,


        # portfolio
        'all': portfolio,


    }
    return render(request, 'index.html', context)


#>>>>>>>>>>>>> DETAIL PAGES <<<<<<<<<<<<<#
class PortFolioDetail(DetailView):
    model = PortFolio
    template_name = 'portfolio-detail.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['port'] = PortFolio.objects.all()
        return context


class PortFolioList(ListView):
    model = PortFolio
    template_name = 'portfolio-list.html'
    context_object_name = 'portfolio'


class TestimonialDetail(DetailView):
    model = Testimonial
    template_name = 'testimonial-detail.html'


class ServiceDetail(DetailView):
    model = Service
    template_name = 'service-detail.html'
    #context_object_name = 'service'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['serve'] = PortFolio.objects.all()
        context['port'] = Service.objects.all()
        return context


#>>>>>>>>>>>>>>>>>  FORMS <<<<<<<<<<<<<<<<<#


class PortFolioFormView(CreateView):
    model = PortFolio
    form_class = PortFolioForm
    template_name = 'portfolio-form.html'
    success_url = reverse_lazy('success')


class ContactFormView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact-form.html'
    success_url = reverse_lazy('success')


def success(request):
    return render(request, 'success.html')


def about(request):
    time_born = datetime.datetime(year=2000, month=5, day=6).year
    age_diff = datetime.datetime.now().year - time_born

    time_now = datetime.datetime.now().year
    time_then = datetime.datetime(year=2020, month=6, day=2).year
    time_born = datetime.datetime(year=2000, month=5, day=6).year
    time_difference = time_now - time_then
    age_diff = time_now - time_born

    context = {
        # experience & age
        'experience': time_difference,
        'age': age_diff,
    }

    return render(request, 'about.html', context)


def resume(request):
    return render(request, 'resume.html')


class ServiceList(ListView):
    model = Service
    template_name = 'service-list.html'
    context_object_name = 'service'


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        form = Contact(name=name, subject=subject,
                       email=email, message=message)
        form.save()
        return HttpResponseRedirect('success')

    return render(request, 'contact.html')
