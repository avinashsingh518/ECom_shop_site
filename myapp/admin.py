from django.contrib import admin
from .models import Cloth, product, Contact, Cloth

# Register your models here.

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Cloth)

