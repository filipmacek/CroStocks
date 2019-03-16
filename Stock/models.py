from django.db import models
from CroStocks import settings
# Create your models here.
class Stock(models.Model):
    ticker=models.CharField(max_length=5)
    company=models.TextField(max_length=70)
    isin=models.TextField(max_length=30,default="")
    num_stocks=models.IntegerField()
    nominal=models.TextField()
    issuance_date=models.TextField(max_length=20,default="")
    url=models.TextField(max_length=60,default="")

    def __str__(self):
        return self.ticker





class BilancaAktiva(models.Model):
    #Primary keys
    stock=models.ForeignKey(Stock)
    period=models.CharField(max_length=12,primary_key=True)
    kons=models.BooleanField(primary_key=True)

    #Fields
    potrazivanja_upisanikapital=models.DecimalField("Potrazivanja za upisani,a neuplaceni kapital")
    dugotrajna_imovina=models.DecimalField("Dugotrajna imovina")

    #DUGOTRAJNA IMOVINA
    #MATERIJALNA IMOVINA

    nemat_imovina=models.DecimalField("Nematerijalna imovinina")
    nemat_imovina_1=models.DecimalField("Izdaci za razvoj")
    nemat_imovina_2=models.DecimalField("Koncesije,patenti,licencije,rubne i usluzne marke,softver i ostala prava")
    nemat_imovina_3=models.DecimalField("Goodwill")
    nemat_imovina_4=models.DecimalField("Predujmovi za nabavu materijalne imovine")
    nemat_imovina_5=models.DecimalField("Nematerijalna imovina u pripremi")
    nemat_imovina_6=models.DecimalField("Ostala nematerijalna imovina")


    #MATERIJALNA IMOVINA
    mat_imovina=models.DecimalField("Materijalna imovina")
    mat_imovina_1=models.DecimalField("Zemljiste")
    mat_imovina_2=models.DecimalField("Gradevinski objekti")
    mat_imovina_3=models.DecimalField("Postrojenje i oprema")
    mat_imovina_4=models.DecimalField("Alati,pogonski inventar i transportna imovina")
    mat_imovina_5=models.DecimalField("Bioloska imovina")
    mat_imovina_6=models.DecimalField("Predujmovi za materijalnu imovinu")
    mat_imovina_7=models.DecimalField("Materijelna imovina u pripremi")
    mat_imovina_8=models.DecimalField("Ostala materijalna imovina")
    mat_imovina_9=models.DecimalField("Ulaganje u nekretnine")

   #DUGOTRAJNA FINANCIJSKA IMOVINA
    dugfin_imovina=models.DecimalField("Dugotrajana financijska imovina")
    dugfin_imovina_1=models.DecimalField("Udjeli(dionice) kod povezanih poduzetnika")
    dugfin_imovina_2=models.DecimalField("Dani zajmovi povezanim poduzetnicima")
    dugfin_imovina_3=models.DecimalField("Sudjelujuci interesi(udjeli)")
    dugfin_imovina_4=models.DecimalField("Zajmovi dani poduzetnicima u kojima postoje sudjelujuci interesi")
    dugfin_imovina_5=models.DecimalField("Ulaganja u vrijednosne papire")
    dugfin_imovina_6=models.DecimalField("Dani zajmovi,depoziti i slicno")
    dugfin_imovina_7=models.DecimalField("Ostala dugotrajna financijska imovina")
    dugfin_imovina_8=models.DecimalField("Ulaganja koje se obracunavaju metodom udjela")

    #Potrazivanja dugorocna
    dug_potrazivanja=models.DecimalField("Potrazivanja")
    dug_potrazivanja_1=models.DecimalField("Potrazivanja od povezanih poduzetnika")
    dug_potrazivanja_2=models.DecimalField("Potrazivanja po osnovi prodaje na kredit")
    dug_potrazivanja_3=models.DecimalField("Ostala potrazivanja")

    #ODGODENA POREZNA IMOVINA
    odgporezna_imovina=models.DecimalField("Odgodena porezna imovina")

    #KRATKOTRAJNA IMOVINA
    krat_imovina=models.DecimalField("Kratkotrajna imovina")
    #ZALIHE
    zalihe=models.DecimalField("Zalihe")
    zalihe_1=models.DecimalField("Sirovine i materijal")
    zalihe_2=models.DecimalField("Proizvodnja u tijeku")
    zalihe_3=models.DecimalField("Gotovi proizvodi")
    zalihe_4=models.DecimalField("Trgovacka roba")
    zalihe_5=models.DecimalField("Predujmovi za zalihe")
    zalihe_6=models.DecimalField("Dugotrajna imovina namijenjena prodaji")
    zalihe_7=models.DecimalField("Bioloska imovina")

    #KRATKOTRAJNA POTRAZIVANJA
    krat_potrazivanja=models.DecimalField("Potrazivanja")
    krat_potrazivanja_1=models.DecimalField("Potrazivanja od povezanih poduzetnika")
    krat_potrazivanja_2=models.DecimalField("Potrazivanja od kupaca")
    krat_potrazivanja_3=models.DecimalField("Potrazivanja od sudjelujucih poduzetnika")
    krat_potrazivanja_4=models.DecimalField("Potrazivanja od zaposlenika i clanova poduzetnika")
    krat_potrazivanja_5=models.DecimalField("Potrazivanje od drzave i drugih institucija")
    krat_potrazivanja_6=models.DecimalField("Ostala potrazivanja")

    #KRATKOTRAJNA FINANCIJSKA IMOVINA
    kratfin_imovina=models.DecimalField("Kratkotrajna financijska imovina")
    kratfin_imovina_1=models.DecimalField("Udjeli(dionice) kod povezanih poduzetnika")
    kratfin_imovina_2=models.DecimalField("Dani zajmovi povezanim poduzetnicima")
    kratfin_imovina_3=models.DecimalField("Sudjelujuci interesi(udjeli)")
    kratfin_imovina_4=models.DecimalField("Zajmovi dani poduzetnicima u kojima postoje sudjelujuci interesi")
    kratfin_imovina_5=models.DecimalField("Ulaganja u vrijednosne papire")
    kratfin_imovina_6=models.DecimalField("Dani zajmovi,depoziti i slicno")
    kratfin_imovina_7=models.DecimalField("Ostala financijska imovina")

    novac=models.DecimalField("Novac u banci i blagajni")
    placeni_troskovi=models.DecimalField("Placeni troskovi buduceg razdoblja i obracunati prihodi")
    ukupno_aktiva=models.DecimalField("Ukupno aktiva")
    izvan_bilancni_zapisi=models.DecimalField("Izvanbilancni zapisi")

    class Meta:
        unique_together=('stock','period','kons',)

class BilancaPasiva(models.Model):
    kapital_rezerve=models.DecimalField("Kapital i rezerve")
    temeljni_upisani_kapital=models.DecimalField("Temeljni upisani kapital")
    kapitalne_rezerve=models.DecimalField("Kapitalne rezerve")

    #Rezerve iz dobiti
    rezerve_dobiti=models.DecimalField("Rezerve iz dobiti")
    rezerve_dobiti_1=models.DecimalField("Zakonske rezerve")
    rezerve_dobiti_2=models.DecimalField("Rezerve za vlastite dionice")
    rezerve_dobiti_3=models.DecimalField("Vlastite dionice i udjeli(odbitna stavka)")
    rezerve_dobiti_4=models.DecimalField("Statutorne rezerve")
    rezerve_dobiti_5=models.DecimalField("Ostale rezerve")

    revalorizacijske_rezerve=models.DecimalField("")




class NematerijalnaImovina(models.Model):
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    date
    izdaci_za_razvoj4=models.IntegerField()
    koncesije_patenti5