from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='service/')
    detail = models.TextField()
    show = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    iden = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=255, default='web')

    def get_absolute_url(self):
        return reverse("service-detail", args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Services'


class Testimonial(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    review = models.TextField()
    ratings = models.IntegerField()
    role = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    show = models.BooleanField(default=False)
    portfolio = models.OneToOneField(
        'PortFolio', on_delete=models.CASCADE, null=True, related_name='portfolio')
    picture = models.ImageField(upload_to='testimonial/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("testimonial-detail", args=[self.pk])

    def __str__(self):
        return self.first_name

    @property
    def client_name(self):
        client_name = (self.first_name, self.last_name)
        return ' '.join(client_name)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Testimonials'


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='team/')
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Team Members'


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    subject = models.CharField(max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def get_absolute_url(self):
        return reverse("")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Contacts'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile/', null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("")

    def __str__(self):
        return self.user.name

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Profiles'


class PortFolio(models.Model):
    categories = (
        ('web', 'Web'),
        ('data', 'Data'),
        ('api', 'API'),
        ('scraping', 'Web Scraping')
    )

    category = models.CharField(max_length=255, choices=categories)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client_full_name = models.CharField(max_length=255)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField(null=True)

    project_picture = models.ImageField(upload_to='portfolio/')
    project_detail = models.TextField()
    pic2 = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    pic3 = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    pic4 = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    description = models.CharField(max_length=255, null=True)
    tags = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse("portfolio-detail", args=[self.pk, self.slug])

    def __str__(self):
        return self.client_full_name

    class Meta:
        ordering = ['-project_date']
        verbose_name_plural = 'Portfolios'
