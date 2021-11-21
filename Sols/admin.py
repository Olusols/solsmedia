from django.contrib import admin

from .models import Contact, Profile, TeamMember, Testimonial, Service, PortFolio

TEXT = 'Welcome to SolsMedia.com'


class TestimonialAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Section1', {
            'fields': ('first_name', 'last_name', 'role',  'picture', 'portfolio'),
            'description': '%s' % TEXT,
        }),
        ('Section2', {
            'fields': ('review', 'ratings', 'country', 'show',),
            'description': '%s' % TEXT,
            'classes': ('collapse')
        }),
    )


class PortFolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("client_full_name",)}
    fieldsets = (
        ('Section1', {
            'fields': ('client_full_name', 'service', 'category', 'project_url', 'project_picture', 'slug'),
            'description': '%s' % TEXT,
        }),
        ('Section2', {
            'fields': ('project_detail', 'pic2', 'pic3', 'pic4',),
            'description': '%s' % TEXT,
            'classes': ('collapse')
        }),
        ('Section3', {
            'fields': ('description', 'tags'),
            'description': '%s' % TEXT,
            'classes': ('collapse')
        }),
    )


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created']


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(PortFolio, PortFolioAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Profile)
admin.site.register(Contact, ContactAdmin)
admin.site.register(TeamMember)
