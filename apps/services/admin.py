from django.contrib import admin
from .models import Service, Server, Deployment, Product

admin.site.register(Service)
admin.site.register(Server)
admin.site.register(Deployment)
admin.site.register(Product)
