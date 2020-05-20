from django.contrib import admin
from .models import Item, OrderItem, Order, FormInfoadress, Artikal, Racun, Budzet, ulazni_rac, Usluga, izlazni_rac, Partner, Ugovor, Kategorija, Asortiman
# Register your models here.
admin.site.register(Artikal)
admin.site.register(Kategorija)
admin.site.register(Asortiman)
admin.site.register(Racun)
admin.site.register(ulazni_rac)
admin.site.register(izlazni_rac)
admin.site.register(Partner)
admin.site.register(Ugovor)
admin.site.register(Usluga)
admin.site.register(Budzet)
