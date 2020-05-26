from core.views import UlazniRacuniView, Nabavke, PregledRacuna1, NewBill, MyLoginView, Avansi, Usluge, Partneri, Ugovori, UlazniRacuniView, Login, Konto1, Artikli, ChartData, Pocetna, Pocetna12, PregledRacunaUlazni, PregledRacunaIzlazni
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
app_name = 'core'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('NewBill', NewBill, name='NewBill'),
    path('UlazniRacuniView', UlazniRacuniView, name='UlazniRacuniView'),
    path('PregledRacuna1/<racun>', PregledRacuna1, name="PregledRacuna1"),
    url('^api/chart/data/(?P<username>.+)/$', ChartData.as_view(), name="proc"),
    path('Pocetna', Pocetna, name='Pocetna'),
    path('Ulazni', PregledRacunaUlazni, name='Ulazni_racun'),
    path('Izlazni', PregledRacunaIzlazni, name='Izlazni'),
    path('Pocetna12', Pocetna12, name='ERP1'),
    path('Login', Login, name='Login'),
    path('Artikli', Artikli, name='Artikli'),
    path('Usluge', Usluge, name='Usluge'),
    path('Ugovori', Ugovori, name='Ugovori'),
    path('Avansi', Avansi, name='Avansi'),
    path('Konto1', Konto1, name='Konto1'),
    path('Partneri', Partneri, name='Partneri'),
    path('Nabavke', Nabavke, name='Nabavke'),
    path('accounts/login1/', MyLoginView.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
