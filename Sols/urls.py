from django.urls import path
from .views import(ServiceDetail, index, about, PortFolioFormView,
                   ContactFormView, TestimonialDetail, PortFolioDetail,
                   resume, success, PortFolioList, ServiceList,
                   contact)


urlpatterns = [
    path('', index, name='index'),
    path('resume/', resume, name='resume'),
    path('success/', success, name='success'),
    path('contact', contact, name='contact'),
    path('about/', about, name='about'),
    path('portfolio-form/', PortFolioFormView.as_view(), name='portfolio-form'),
    path('contact-form/', ContactFormView.as_view(), name='contact-form'),
    path('service/<slug:slug>', ServiceDetail.as_view(), name='service-detail'),
    path('testimonial/<int:pk>', TestimonialDetail.as_view(),
         name='testimonial-detail'),
    path('portfolio/<int:pk>/<slug:slug>/',
         PortFolioDetail.as_view(), name='portfolio-detail'),
    path('portfolio/', PortFolioList.as_view(), name='portfolio-list'),
    path('service/', ServiceList.as_view(), name='service-list')
]
