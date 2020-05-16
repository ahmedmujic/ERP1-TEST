from django.contrib import admin
from .models import Item, OrderItem, Order, FormInfoadress, Asortiman, Racun, ulazni_rac, izlazni_rac, Partner, Ugovor
# Register your models here.
admin.site.register(Asortiman)
admin.site.register(Racun)
admin.site.register(ulazni_rac)
admin.site.register(izlazni_rac)
admin.site.register(Partner)
admin.site.register(Ugovor)
