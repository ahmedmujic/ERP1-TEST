from django.shortcuts import render, redirect
from .models import Asortiman, Racun, izlazni_rac, ulazni_rac, Partner, Ugovor, Artikal, Kategorija, Usluga, Budzet
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChartForm
from django.template.defaulttags import register
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
import datetime
import json


def Pocetna(request):
    return render(request, 'pocetna.html', {"customers": 10})


def racunajMjesec(racuni):
    konacan = []
    for i in range(0, len(racuni) - 1, 1):
        ukupno = 0
        b = 0
        bi = 0
        for j in range(i + 1, len(racuni), 1):
            for z in range(0, len(konacan), 1):
                if racuni[i].datum_racuna1.month == konacan[z].datum_racuna1.month:
                    ukupno = ukupno + racuni[i].ukupno1 + konacan[z].ukupno1
                    konacan[z].ukupno1 = ukupno
                    b += 1
                if racuni[j].datum_racuna1.month == konacan[z].datum_racuna1.month:
                    ukupno = ukupno + racuni[j].ukupno1 + konacan[z].ukupno1
                    konacan[z].ukupno1 = ukupno
                    b += 1
            if racuni[i].datum_racuna1.month == racuni[j].datum_racuna1.month and b == 0:
                ukupno = ukupno + racuni[i].ukupno1 + racuni[j].ukupno1
                konacan.append(racuni[i])
                bi += 1
            if racuni[i].datum_racuna1.month != racuni[j].datum_racuna1.month and b == 0 and bi == 0:
                konacan.append(racuni[j])
                konacan.append(racuni[i])
                i += 1
        # if b > 0:
        #     continue
        # if ukupno > 0:
        #     racuni[i].ukupno1 = ukupno
        # else:
        #     racuni[i].ukupno1 = racuni[i].ukupno1

    return konacan


class Grafik():
    def __init__(self, datum, kolicina):
        self.datum = datum
        self.kolicina = kolicina


def Remove(duplicate):
    month_list = []
    final_list = []
    for j in range(0, len(duplicate), 1):
        if duplicate[j].datum_racuna1.month not in month_list:
            month_list.append(duplicate[j].datum_racuna1.month)
    for i in range(0, len(month_list), 1):
        ukupno = 0
        for j in range(0, len(duplicate), 1):
            if duplicate[j].datum_racuna1.month == month_list[i]:
                ukupno = ukupno + duplicate[j].ukupno1
        r1 = Grafik(month_list[i], ukupno)
        final_list.append(r1)
    return final_list


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        godina = self.kwargs['username']
        month_list_ulazni = Racun.objects.filter(
            datum_racuna1__year=godina, tip="Ulazni")
        month_list_izlazni = Racun.objects.filter(
            datum_racuna1__year=godina, tip="Izlazni")
        month_list_ulazni_sve = Racun.objects.all()
        godine = []
        labels = []
        labels22 = []
        default_items = []
        default_items22 = []
        d = {1: 'Januar', 2: 'Februar', 3: 'Mart', 4: 'April', 5: 'Maj', 6: 'Juni',
             7: 'Juli', 8: 'August', 9: 'Septemar', 10: 'Oktobar', 11: 'Novembar', 12: 'Decembar'}
        labels1 = Remove(month_list_ulazni)
        lbl2 = Remove(month_list_izlazni)
        for lbl in labels1:
            labels.append(d[lbl.datum])
            default_items.append(lbl.kolicina)
        for lbl in lbl2:
            labels.append(d[lbl.datum])
            default_items22.append(lbl.kolicina)
        labels = list(dict.fromkeys(labels))
        for godina in month_list_ulazni_sve:
            godine.append(godina.datum_racuna1.year)

        # for godina in month_list_ulazni:
        #     godine.append(godina.datum_racuna1.year)

        # for vrijednosti in month_list_ulazni:
        #     labels.append(vrijednosti.datum_racuna1)

        # labels = list(dict.fromkeys(labels))
        # labels = sorted(
        #     labels, key=lambda month: datetime.datetime.strftime(month, "%D/%d/%Y"))
        # labels.sort()
        # for mjesec in labels:
        #     mjesec.strftime("%b")
        # sorteddates = [datetime.datetime.strftime(
        #     ts, "%Y-%m-%d") for ts in labels]

        # for mjeseci in labels:
        #     mjeseci = mjeseci.month

        # for vrijednosti in month_list_ulazni_js:
        #     default_items.append(vrijednosti.ukupno1)

        data = {
            "labels": labels,
            "labels2": labels22,
            "default2": default_items22,
            "default": default_items,
            "ulazni_sve": godine
        }
        return Response(data)

# @register.filter
# def get_range(value):
#     return range(value)


# def product(request):

#     return render(request, "product-page.html")


# def checkout(request):
#     if request.method == 'POST':
#         form = ChartForm(request.POST or None)
#         print(form.errors)
#         if form.is_valid():
#             if request.user.is_authenticated:
#                 order = OrderItem.objects.filter(
#                     user=request.user, ordered=False)
#             ulica = form.cleaned_data.get('ulica_adresa')
#             adresa_stana = form.cleaned_data.get('adresa_stana')
#             country = form.cleaned_data.get('country')
#             postal = form.cleaned_data.get('postal')
#             payopt = form.cleaned_data.get('credit')
#             billing_address = FormInfoadress(
#                 user=request.user,
#                 ulica_adresa=ulica,
#                 adresa_stana=adresa_stana,
#                 country=country,
#                 postal=postal

#             )
#             billing_address.save()
#             order_f = Order.objects.get(user=request.user)
#             order_f.ordered_adress = billing_address
#             order_f.save()
#             return render(request, "payment.html", {'payopt': payopt, 'order': order})
#     else:
#         form = ChartForm()
#     context = {
#         'form': form
#     }
#     return render(request, "checkout-page.html", context)


# def item_list(request):
#     items = Item.objects.all()
#     if request.user.is_authenticated:
#         order = Order.objects.filter(user=request.user, ordered=False)
#     paginator = Paginator(items, 1)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, "home-page.html", {'page_obj': page_obj, 'order': order[0].items.count()})


# def Item1(request, item):
#     item1 = Item.objects.get(price=item)
#     if request.user.is_authenticated:
#         order = Order.objects.filter(user=request.user, ordered=False)
#     context = {
#         'item1': item1,
#         'order': order[0].items.count()
#     }

#     return render(request, 'product-page.html', context)


# def OrderCount(request):
#     if request.user.is_authenticated:
#         order = Order.objects.filter(user=request.user, ordered=False)
#     return order[0].items.count()


# @login_required
# def Chart(request, item):
#     item1 = Item.objects.get(price=item)
#     context = {'item1': item1, 'order': OrderCount(request)}
#     ordered_item, created = OrderItem.objects.get_or_create(
#         item=item1, ordered=False, user=request.user)
#     ordered_qs = Order.objects.filter(user=request.user, ordered=False)
#     if ordered_qs.exists():
#         order = ordered_qs[0]
#         if created is False:
#             ordered_item.quantity += 1
#             ordered_item.save()
#             messages.info(request, 'Uspješno ste dodali jedan item')
#             return redirect('OrderSum')
#         else:
#             order.items.add(ordered_item)
#             order.save()
#             messages.info(request, 'Dodali ste jedan item')
#             return redirect('OrderSum')
#     else:
#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         messages.info(request, 'Narudžba kreirana')
#         return redirect('OrderSum')
#     return redirect('OrderSum')


# @login_required
# def Remove_from_Chart(request, item):
#     item1 = Item.objects.get(price=item)
#     context = {'item1': item1, 'order': OrderCount(request)}
#     ordered_item, created = OrderItem.objects.get_or_create(
#         item=item1, user=request.user, ordered=False)
#     ordered_qs = Order.objects.filter(user=request.user, ordered=False)
#     if ordered_qs.exists():
#         order = ordered_qs[0]
#         if created is True:
#             messages.info(request, 'Item was not in you Cart')
#             return redirect('OrderSum')
#         elif ordered_item.quantity > 1:
#             ordered_item.quantity -= 1
#             ordered_item.save()
#             messages.info(request, 'Uspješno ste izbacili jedan item')
#             return redirect('OrderSum')
#         else:
#             order.items.remove(ordered_item)
#             ordered_item.delete()
#             context = {'item1': item1, 'order': OrderCount(request)}
#             messages.info(request, 'Uspješno ste uklonili jedan item')
#             return redirect('OrderSum')
#     else:
#         messages.info(request, 'Nemate itema')
#         return redirect('OrderSum')
#     return redirect('OrderSum')


# @login_required
# def OrderSum(request):
#     orders = Order.objects.filter(user=request.user)
#     context = {
#         'orders': orders[0]

#     }
#     return render(request, "order_summary.html", context)


# def Clean(request, item):
#     item1 = Item.objects.get(title=item)
#     ordered = OrderItem.objects.get(
#         item=item1, user=request.user)
#     ordered.delete()
#     return redirect('OrderSum')


def NewBill(request):
    if request.method == 'POST':
        if request.POST.get('defaultExampleRadios', False) == "S_ugovorom":
            docfile = request.FILES.get('file1', False)
            datum_ugovora = request.POST.get('ugovor_datum_potpis', False)
            datum_ugovora1 = request.POST.get('ugovor_datum_vazenje', False)
            sadrzaj_ugovora = request.POST.get('ugovor_sadrzaj', False)
            newdoc = Ugovor.objects.create(user=request.user,
                                           file_ugovor=docfile, sadrzaj_ugovora=sadrzaj_ugovora, datum_potpisivanja=datum_ugovora, vazenje=datum_ugovora1)
            newdoc.save()
        naziv = request.POST.get('naziv_partner', False)
        sifra = request.POST.get('sifra_partner', False)
        mail = request.POST.get('mail_partner', False)
        adresa = request.POST.get('adresa_partner', False)
        drzava = request.POST.get('drzava', False)
        novi_partner = Partner.objects.create(
            user=request.user, naziv=naziv, email=mail, drzava=drzava, porezni_broj=sifra, adresa=adresa)
        if request.POST.get('defaultExampleRadios', False) == "S_ugovorom":
            novi_partner.ugovor.add(newdoc)
        date = request.POST.get('datum', False)
        rok_otplate1 = request.POST.get('datum_rok', False)
        selekcija = request.POST.get('selekcija', False)
        novi_racun1 = Racun.objects.create(
            user=request.user, datum_racuna1=date, tip=selekcija, rok_otplate1=rok_otplate1)
        naziv = request.POST.getlist('naziv_artikal', False)
        popust = request.POST.getlist('popust_artikal', False)
        kolicina = request.POST.getlist('kolicina_artikal', False)
        cijena = request.POST.getlist('cijena_artikal', False)
        opis = request.POST.getlist('opis_artikal', False)
        selekcija1 = request.POST.getlist('kategorija', False)
        for i in range(len(naziv)):
            kategorija, created = Kategorija.objects.get_or_create(
                naziv=selekcija1[i])
            novi_racun = Artikal.objects.create(
                naziv=naziv[i], opis=opis[i], kolicina=kolicina[i], cijena_bez_pdv=cijena[i], popust=float(popust[i]), kategorija=kategorija)

            novi_racun.cijena_s_pdvom = novi_racun.cijena_s_pdv(
                float(cijena[i]), float(popust[i]))
            novi_racun.save()
            novi_racun1.asortiman.add(novi_racun)
        naziv_usluga = request.POST.getlist('naziv_usluga', False)
        popust_usluga = request.POST.getlist('popust_usluga', False)
        kolicina_usluga = request.POST.getlist('sati_usluga', False)
        cijena_usluga = request.POST.getlist('cijena_usluga', False)
        opis_usluga = request.POST.getlist('opis_usluga', False)
        for i in range(len(naziv_usluga)):
            novi_racun = Usluga.objects.create(
                naziv=naziv_usluga[i], opis=opis_usluga[i], kolicina=kolicina_usluga[i], cijena_bez_pdv=cijena_usluga[i], popust=float(popust_usluga[i]))
            novi_racun.cijena_s_pdvom = novi_racun.cijena_s_pdv(
                float(cijena_usluga[i]), float(popust_usluga[i]))
            novi_racun.save()
            novi_racun1.asortiman.add(novi_racun)

        novi_racun1.partner = novi_partner
        novi_racun1.pdv = novi_racun1.pdv_km()
        novi_racun1.osnovica1 = novi_racun1.osnovica()
        novi_racun1.save()
        novi_racun1.ukupno1 = novi_racun1.osnovica1 + novi_racun1.pdv
        novi_racun1.save()
        if selekcija == "Izlazni":
            novi_racun1.racuni_izlazni, created = izlazni_rac.objects.get_or_create(
                user=request.user, title="Izlazni_racun")
            budzet, created = Budzet.objects.get_or_create(title="Budzet")
            budzet.prihodi = budzet.prihodi + novi_racun1.ukupno1
            budzet.save()
        elif selekcija == "Ulazni":
            print("OSAKA")
            novi_racun1.racuni_ulazni, created = ulazni_rac.objects.get_or_create(
                user=request.user, title="Ulazni_racun")
            budzet, created = Budzet.objects.get_or_create(title="Budzet")
            budzet.troskovi = budzet.troskovi + novi_racun1.ukupno1
            budzet.save()
        budzet.ukupno_budzet()
        budzet.save()
        return render(request, "NewBill.html")
    if request.method == 'GET':
        return render(request, "NewBill.html")


def UlazniRacuniView(request):
    racun = Racun.objects.filter(
        user=request.user, racuni_ulazni__isnull=False)
    context = {
        'racuni': racun

    }
    return render(request, "pregled_racuna.html", context)


def PregledRacuna1(request, racun):
    racun = Racun.objects.get(id=racun)
    context = {
        'racuni': racun.asortiman.all()

    }
    return render(request, "pregled_artikala.html", context)
