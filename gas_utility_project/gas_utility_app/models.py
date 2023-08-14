from django.db import models

class ServiceRequest(models.Model):
    class Meta:
        app_label = 'gas_utility_app'
        
    SERVICE_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('meter_issue', 'Meter Issue'),
        ('new_connection', 'New Connection'),
        ('billing_issue', 'Billing Issue'),
        ('appliance_installation', 'Appliance Installation'),
        ('maintenance_request', 'Maintenance Request'),
    ]

    customer_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=40, choices=SERVICE_TYPES)
    request_details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    resolved_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f'{self.customer_name} - {self.service_type}'
