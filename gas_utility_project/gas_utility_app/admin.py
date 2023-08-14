from django.contrib import admin
from .models import ServiceRequest

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'service_type', 'request_details', 'submission_date', 'resolved_date', 'status']
    list_editable = ('status',) 

admin.site.register(ServiceRequest, ServiceRequestAdmin)
