from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from datetime import timezone
import computed_property
CHATEGORY_CHOISES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOISES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    chategory = models.CharField(
        choices=CHATEGORY_CHOISES, max_length=2, default='primary')
    label = models.CharField(choices=LABEL_CHOISES,
                             max_length=2, default='primary')


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title

    def get_ukupno(self):
        return self.item.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    oredered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    ordered_adress = models.ForeignKey(
        'FormInfoadress', on_delete=models.SET_NULL, blank=True, null=True)
    promoCode = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    def get_total(self):
        sum = 0
        for order in self.items.all():
            sum = sum + order.get_ukupno()
        return sum


class FormInfoadress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ulica_adresa = models.CharField(max_length=100)
    adresa_stana = models.CharField(max_length=100)
    country = CountryField()
    postal = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class GlavnaKnjiga(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Asortiman(models.Model):
    naziv = models.CharField(max_length=100)
    cijena_bez_pdv = models.FloatField(default=100)
    cijena_s_pdvom = models.FloatField(default=1.0)
    opis = models.TextField(default="ovo je to")
    popust = models.FloatField(default=0)
    kolicina = models.FloatField(default=0)

    def cijena_s_pdv(self, cijena, popust):
        cijena_s_pdv = cijena + ((17 / 100) * cijena)
        return (cijena_s_pdv - (cijena_s_pdv * (popust / 100.0)))


class Kategorija(models.Model):
    naziv = models.CharField(max_length=50)


class Usluga(Asortiman):
    rok_izvrsenja = models.DateField(blank=True, null=True)


TIP_RACUNA = [
    ('ulazni', 'Ulazni'),
    ('izlazni', 'Izlazni')
]


class ulazni_rac(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(default="Ulazni_Racun", max_length=50)

    def __str__(self):
        return self.title


class izlazni_rac(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(default="Izlazni_Racun", max_length=50)

    def __str__(self):
        return self.title


TIP_UGOVORA = [
    ('ugovor o djelu', 'Ugovor o djelu'),
    ('na daljinu', 'Na daljinu'),
    ('potpisani', 'Potpisani')
]


class Ugovor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    sadrzaj_ugovora = models.TextField()
    datum_potpisivanja = models.DateField()
    vazenje = models.DateField()
    tip = models.CharField(
        max_length=120, choices=TIP_UGOVORA, default='Ugovor o djelu')
    file_ugovor = models.FileField(upload_to='documents/%Y/%m/%d')
    glavna_knjiga1 = models.ForeignKey(
        GlavnaKnjiga, on_delete=models.CASCADE, related_name='GlavnaKnjiga_id_id_id_id', null=True, blank=True)


class Komercijala(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    glavni_komercijalista = models.CharField(max_length=50)
    ugovor = models.ManyToManyField(Ugovor)


class DugPartner(models.Model):
    iznos = models.FloatField(default=0.0)


class Partner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    naziv = models.CharField(max_length=100, default="Firma")
    email = models.EmailField()
    drzava = CountryField(blank_label='(Izaberite državu)')
    porezni_broj = models.IntegerField()
    adresa = models.CharField(max_length=100)
    ugovor = models.ManyToManyField(Ugovor)
    dugovanje = models.ManyToManyField(DugPartner)


class Avans(models.Model):
    iznos = models.FloatField(default=0.0)
    datum_validnosti = models.DateField()
    napomena = models.TextField()
    partner = models.ManyToManyField(Partner)


class Artikal(Asortiman):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    dobavljac = models.ForeignKey(
        Partner, on_delete=models.CASCADE, related_name='Partner_id1_id', null=True, blank=True)


class Racun(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    asortiman = models.ManyToManyField(Asortiman)
    racuni_izlazni = models.ForeignKey(
        izlazni_rac, on_delete=models.CASCADE, null=True, blank=True)

    racuni_ulazni = models.ForeignKey(
        ulazni_rac, on_delete=models.CASCADE, null=True, blank=True)

    partner = models.ForeignKey(
        Partner, on_delete=models.CASCADE, related_name='Partner_id_id', null=True, blank=True)
    glavna_knjiga = models.ForeignKey(
        GlavnaKnjiga, on_delete=models.CASCADE, related_name='GlavnaKnjiga_id_id', null=True, blank=True)
    tip = models.CharField(
        max_length=120, choices=TIP_RACUNA, default='Ulazni')
    datum_racuna1 = models.DateField()
    rok_otplate1 = models.DateField()
    ukupno1 = models.FloatField(default=0.0)
    osnovica1 = models.FloatField(default=0.0)
    pdv = models.FloatField(default=0.0)

    def pdv_km(self):
        for artikal in self.asortiman.all():
            self.ukupno1 = (
                self.ukupno1 + (artikal.cijena_s_pdvom * artikal.kolicina))
        return round((self.ukupno1 * 0.17), 2)

    def osnovica(self):
        return round((self.ukupno1 - (self.ukupno1 * 0.17)), 2)

    def get_ukupno_racun(self, cijena):
        return round(cijena, 2)


class Budzet(models.Model):
    title = models.CharField(default="Budzet", max_length=50)
    ukupno = models.FloatField(default=0.0)
    troskovi = models.FloatField(default=0.0)
    prihodi = models.FloatField(default=0.0)
    glavna_knjiga = models.ForeignKey(
        GlavnaKnjiga, on_delete=models.CASCADE, related_name='GlavnaKnjiga_id_id_id', null=True, blank=True)

    def __str__(self):
        return self.title

    def ukupno_budzet(self):
        self.ukupno = self.prihodi - self.troskovi
