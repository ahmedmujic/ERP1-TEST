from django.shortcuts import render, redirect
from .models import Asortiman, Racun, izlazni_rac, ulazni_rac, Partner, Ugovor, Artikal, Kategorija, Usluga
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChartForm
from django.template.defaulttags import register


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
        selekcija = request.POST.getlist('kategorija', False)
        for i in range(len(naziv)):
            kategorija, created = Kategorija.objects.get_or_create(
                naziv=selekcija[i])
            novi_racun = Artikal.objects.create(
                naziv=naziv[i], opis=opis[i], kolicina=kolicina[i], cijena_bez_pdv=cijena[i], popust=float(popust[i]), kategorija=kategorija)

            novi_racun.cijena_s_pdv(float(cijena[i]), float(popust[i]))
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
            novi_racun.cijena_s_pdv(float(cijena[i]), float(popust[i]))
            novi_racun.save()
            novi_racun1.asortiman.add(novi_racun)
        if selekcija == "Ulazni":
            novi_racun1.racuni_izlazni = izlazni_rac.objects.get(
                user=request.user)
        elif selekcija == "Izlazni":
            novi_racun1.racuni_ulazni = ulazni_rac.objects.get(
                user=request.user)
        novi_racun1.partner = novi_partner

        # novi_racun1.osnovica()
        novi_racun1.pdv

        novi_racun1.save
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
