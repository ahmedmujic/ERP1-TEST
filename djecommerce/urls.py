from core.views import *
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
    url('^api/chart/data/(?P<username>.+)/(?P<mjesec>.+)$',
        ChartData.as_view(), name="proc"),
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
    path('accounts/login1/', MyLoginView.as_view(), name='login'),
    path('User', UserView, name='User'),
    path('KreirajRacun', KreirajRacun, name='KreirajRacun'),
    path('NoviRacun', NoviRacun, name='NoviRacun'),
    path('IzlazniArtikli/<id>', Izlazni_Artikli_pregled, name="izlaz"),
    path('Obavijest', Obavijest, name='Obavijest'),
    path('Projekti', Projekt, name='Projekt'),
    path('Tenderi', Tender, name='Tenderi'),
    path('unostendera', unosTendera, name='unosTendera'),
    path('unosprojekta', unosProjekta, name='unosProjekta'),
    path('unosavansa', unosAvansa, name='unosAvansa'),
    path('unoskonta', unosKonta, name='unosKonta'),
    path('unosnabavke', unosNabavke, name='unosNabavke'),
    path('unosblagajne', unosBlagajne, name='unosBlagajne'),
    path('pregledBlagajne', pregledBlagajne, name='pregledBlagajne'),
    path('Bilans', Bilansi, name='Bilans'),
    path('Transakcije', Transakcij, name='Transakcije'),
    path('Duznici', Duznici, name='Duznici'),
    path('Duznici2', Duznici2, name='Duznici2'),
    path('unosArtikala', unosArtikala, name='unosArtikala')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
