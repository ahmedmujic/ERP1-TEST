from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from datetime import timezone
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


class Asortiman(models.Model):
    naziv = models.CharField(max_length=100)
    cijena_bez_pdv = models.FloatField(default=100)
    cijena_s_pd = models.FloatField(default=1.0)
    opis = models.TextField(default="ovo je to")
    popust = models.FloatField(default=0)
    kolicina = models.FloatField(default=0)

    def cijena_s_pdv(self, cijena, popust):
        self.cijena_s_pd = cijena + ((17 / 100) * cijena)
        self.cijena_s_pd = (self.cijena_s_pd -
                            (self.cijena_s_pd * (popust / 100.0)))


class Kategorija(models.Model):
    naziv = models.CharField(max_length=50)


class Artikal(Asortiman):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)


class Usluga(Asortiman):
    rok_izvrsenja = models.DateField(blank=True, null=True)


TIP_RACUNA = [
    ('ulazni', 'Ulazni'),
    ('izlazni', 'Izlazni')
]


class ulazni_rac(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class izlazni_rac(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)


class Ugovor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    sadrzaj_ugovora = models.TextField()
    datum_potpisivanja = models.DateField()
    vazenje = models.DateField()
    file_ugovor = models.FileField(upload_to='documents/%Y/%m/%d')


class Komercijala(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    glavni_komercijalista = models.CharField(max_length=50)
    ugovor = models.ManyToManyField(Ugovor)


class Partner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    naziv = models.CharField(max_length=100, default="Firma")
    email = models.EmailField()
    drzava = CountryField(blank_label='(Izaberite državu)')
    porezni_broj = models.IntegerField()
    adresa = models.CharField(max_length=100)
    ugovor = models.ManyToManyField(Ugovor)


class Racun(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    asortiman = models.ManyToManyField(Asortiman)
    racuni_izlazni = models.ForeignKey(
        izlazni_rac, on_delete=models.CASCADE, related_name='izlazni_rac_id_id', null=True, blank=True)

    racuni_ulazni = models.ForeignKey(
        ulazni_rac, on_delete=models.CASCADE, related_name='ulazni_rac_id_id', null=True, blank=True)

    partner = models.ForeignKey(
        Partner, on_delete=models.CASCADE, related_name='Partner_id_id', null=True, blank=True)
    tip = models.CharField(
        max_length=120, choices=TIP_RACUNA, default='Ulazni')
    datum_racuna1 = models.DateField()
    rok_otplate1 = models.DateField()
    ukupno1 = models.FloatField(default=0.0)
    osnovica = models.FloatField(default=0.0)
    pdv = models.FloatField(default=0.0)

    def pdv_km(self):
        for artikal in self.asortiman.all():
            self.ukupno1 = (
                self.ukupno1 + (artikal.cijena_s_pd * artikal.kolicina))
        self.pdv = (self.ukupno1 * 0.17)

    # def osnovica(self):
    #     for artikal in self.asortiman.all():
    #         self.ukupno1 = (
    #             self.ukupno1 + (artikal.cijena_s_pd * artikal.kolicina))
    #     self.osnovica = (self.ukupno1 - (self.ukupno1 * 0.17))

    def get_ukupno_racun(self):
        for artikal in self.asortiman.all():
            self.ukupno1 = (
                self.ukupno1 + (artikal.cijena_s_pd * artikal.kolicina))
        return self.ukupno1
