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
    stock=models.OneToOneField(Stock,on_delete=models.CASCADE)
    year=models.IntegerField()
    kvartal=models.CharField(max_length=2)
    kons=models.BooleanField()

    class Meta:
        unique_together = ('stock', 'year', 'kvartal', 'kons',)


    #Fields
    potrazivanja_upisanikapital=models.DecimalField("Potrazivanja za upisani,a neuplaceni kapital",decimal_places=2,max_digits=14,blank=True)
    dugotrajna_imovina=models.DecimalField("Dugotrajna imovina",decimal_places=2,max_digits=14,blank=True)

    #DUGOTRAJNA IMOVINA
    #MATERIJALNA IMOVINA

    nemat_imovina=models.DecimalField("Nematerijalna imovinina",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_1=models.DecimalField("Izdaci za razvoj",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_2=models.DecimalField("Koncesije,patenti,licencije,rubne i usluzne marke,softver i ostala prava",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_3=models.DecimalField("Goodwill",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_4=models.DecimalField("Predujmovi za nabavu materijalne imovine",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_5=models.DecimalField("Nematerijalna imovina u pripremi",decimal_places=2,max_digits=14,blank=True)
    nemat_imovina_6=models.DecimalField("Ostala nematerijalna imovina",decimal_places=2,max_digits=14,blank=True)


    #MATERIJALNA IMOVINA
    mat_imovina=models.DecimalField("Materijalna imovina",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_1=models.DecimalField("Zemljiste",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_2=models.DecimalField("Gradevinski objekti",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_3=models.DecimalField("Postrojenje i oprema",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_4=models.DecimalField("Alati,pogonski inventar i transportna imovina",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_5=models.DecimalField("Bioloska imovina",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_6=models.DecimalField("Predujmovi za materijalnu imovinu",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_7=models.DecimalField("Materijelna imovina u pripremi",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_8=models.DecimalField("Ostala materijalna imovina",decimal_places=2,max_digits=14,blank=True)
    mat_imovina_9=models.DecimalField("Ulaganje u nekretnine",decimal_places=2,max_digits=14,blank=True)

   #DUGOTRAJNA FINANCIJSKA IMOVINA
    dugfin_imovina=models.DecimalField("Dugotrajana financijska imovina",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_1=models.DecimalField("Udjeli(dionice) kod povezanih poduzetnika",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_2=models.DecimalField("Dani zajmovi povezanim poduzetnicima",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_3=models.DecimalField("Sudjelujuci interesi(udjeli)",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_4=models.DecimalField("Zajmovi dani poduzetnicima u kojima postoje sudjelujuci interesi",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_5=models.DecimalField("Ulaganja u vrijednosne papire",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_6=models.DecimalField("Dani zajmovi,depoziti i slicno",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_7=models.DecimalField("Ostala dugotrajna financijska imovina",decimal_places=2,max_digits=14,blank=True)
    dugfin_imovina_8=models.DecimalField("Ulaganja koje se obracunavaju metodom udjela",decimal_places=2,max_digits=14,blank=True)

    #Potrazivanja dugorocna
    dug_potrazivanja=models.DecimalField("Potrazivanja",decimal_places=2,max_digits=14,blank=True)
    dug_potrazivanja_1=models.DecimalField("Potrazivanja od povezanih poduzetnika",decimal_places=2,max_digits=14,blank=True)
    dug_potrazivanja_2=models.DecimalField("Potrazivanja po osnovi prodaje na kredit",decimal_places=2,max_digits=14,blank=True)
    dug_potrazivanja_3=models.DecimalField("Ostala potrazivanja",decimal_places=2,max_digits=14,blank=True)

    #ODGODENA POREZNA IMOVINA
    odgporezna_imovina=models.DecimalField("Odgodena porezna imovina",decimal_places=2,max_digits=14,blank=True)

    #KRATKOTRAJNA IMOVINA
    krat_imovina=models.DecimalField("Kratkotrajna imovina",decimal_places=2,max_digits=14,blank=True)
    #ZALIHE
    zalihe=models.DecimalField("Zalihe",decimal_places=2,max_digits=14,blank=True)
    zalihe_1=models.DecimalField("Sirovine i materijal",decimal_places=2,max_digits=14,blank=True)
    zalihe_2=models.DecimalField("Proizvodnja u tijeku",decimal_places=2,max_digits=14,blank=True)
    zalihe_3=models.DecimalField("Gotovi proizvodi",decimal_places=2,max_digits=14,blank=True)
    zalihe_4=models.DecimalField("Trgovacka roba",decimal_places=2,max_digits=14,blank=True)
    zalihe_5=models.DecimalField("Predujmovi za zalihe",decimal_places=2,max_digits=14,blank=True)
    zalihe_6=models.DecimalField("Dugotrajna imovina namijenjena prodaji",decimal_places=2,max_digits=14,blank=True)
    zalihe_7=models.DecimalField("Bioloska imovina",decimal_places=2,max_digits=14,blank=True)

    #KRATKOTRAJNA POTRAZIVANJA
    krat_potrazivanja=models.DecimalField("Potrazivanja",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_1=models.DecimalField("Potrazivanja od povezanih poduzetnika",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_2=models.DecimalField("Potrazivanja od kupaca",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_3=models.DecimalField("Potrazivanja od sudjelujucih poduzetnika",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_4=models.DecimalField("Potrazivanja od zaposlenika i clanova poduzetnika",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_5=models.DecimalField("Potrazivanje od drzave i drugih institucija",decimal_places=2,max_digits=14,blank=True)
    krat_potrazivanja_6=models.DecimalField("Ostala potrazivanja",decimal_places=2,max_digits=14,blank=True)

    #KRATKOTRAJNA FINANCIJSKA IMOVINA
    kratfin_imovina=models.DecimalField("Kratkotrajna financijska imovina",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_1=models.DecimalField("Udjeli(dionice) kod povezanih poduzetnika",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_2=models.DecimalField("Dani zajmovi povezanim poduzetnicima",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_3=models.DecimalField("Sudjelujuci interesi(udjeli)",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_4=models.DecimalField("Zajmovi dani poduzetnicima u kojima postoje sudjelujuci interesi",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_5=models.DecimalField("Ulaganja u vrijednosne papire",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_6=models.DecimalField("Dani zajmovi,depoziti i slicno",decimal_places=2,max_digits=14,blank=True)
    kratfin_imovina_7=models.DecimalField("Ostala financijska imovina",decimal_places=2,max_digits=14,blank=True)

    novac=models.DecimalField("Novac u banci i blagajni",decimal_places=2,max_digits=14,blank=True)
    placeni_troskovi=models.DecimalField("Placeni troskovi buduceg razdoblja i obracunati prihodi",decimal_places=2,max_digits=14,blank=True)
    ukupno_aktiva=models.DecimalField("Ukupno aktiva",decimal_places=2,max_digits=14,blank=True)
    izvan_bilancni_zapisi=models.DecimalField("Izvanbilancni zapisi",decimal_places=2,max_digits=14,blank=True)



class BilancaPasiva(models.Model):
    #Primary key

    stock = models.OneToOneField(Stock,on_delete=models.CASCADE)
    year = models.IntegerField()
    kvartal = models.CharField(max_length=2,)
    kons = models.BooleanField()

    # One to one relationship
    aktiva = models.OneToOneField(BilancaAktiva, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('stock', 'year', 'kvartal', 'kons',)

    kapital_rezerve=models.DecimalField("Kapital i rezerve",decimal_places=2,max_digits=14,blank=True)
    temeljni_upisani_kapital=models.DecimalField("Temeljni upisani kapital",decimal_places=2,max_digits=14,blank=True)
    kapitalne_rezerve=models.DecimalField("Kapitalne rezerve",decimal_places=2,max_digits=14,blank=True)

    #Rezerve iz dobiti
    rezerve_dobiti=models.DecimalField("Rezerve iz dobiti",decimal_places=2,max_digits=14,blank=True)
    rezerve_dobiti_1=models.DecimalField("Zakonske rezerve",decimal_places=2,max_digits=14,blank=True)
    rezerve_dobiti_2=models.DecimalField("Rezerve za vlastite dionice",decimal_places=2,max_digits=14,blank=True)
    rezerve_dobiti_3=models.DecimalField("Vlastite dionice i udjeli(odbitna stavka)",decimal_places=2,max_digits=14,blank=True)
    rezerve_dobiti_4=models.DecimalField("Statutorne rezerve",decimal_places=2,max_digits=14,blank=True)
    rezerve_dobiti_5=models.DecimalField("Ostale rezerve",decimal_places=2,max_digits=14,blank=True)

    revalorizacijske_rezerve=models.DecimalField("Revalorizacijske rezerve",decimal_places=2,max_digits=14,blank=True)

    #Zadrzana dobit ili preneseni gubitak
    zadrzana_dobit_gubitak=models.DecimalField("Zadrzana dobit ili preneseni gubitak",decimal_places=2,max_digits=14,blank=True)
    zadrzana_dobit_gubitak_1=models.DecimalField("Zadrzana dobit",decimal_places=2,max_digits=14,blank=True)
    zadrzana_dobit_gubitak_2=models.DecimalField("Preneseni gubitak",decimal_places=2,max_digits=14,blank=True)

    #Dobit ili gubitak poslovne godine
    dobit_gubitak_posgodine=models.DecimalField("Dobit ili gubitak poslovne godine",decimal_places=2,max_digits=14,blank=True)
    dobit_gubitak_posgodine_1=models.DecimalField("Dobit poslovne godine",decimal_places=2,max_digits=14,blank=True)
    dobit_gubitak_posgodine_2=models.DecimalField("Gubitak poslovne godine",decimal_places=2,max_digits=14,blank=True)

    manjinski_interes=models.DecimalField("Manjinski interes",decimal_places=2,max_digits=14,blank=True)

    #REZERVIRANJA
    rezerviranja=models.DecimalField("Rezerviranja",decimal_places=2,max_digits=14,blank=True)
    rezerviranja_1=models.DecimalField("Rezerviranja za mirovine,otpremnine i slicne obveze",decimal_places=2,max_digits=14,blank=True)
    rezerviranja_2=models.DecimalField("Rezerviranja za porezne obveze",decimal_places=2,max_digits=14,blank=True)
    rezerviranja_3=models.DecimalField("Druga rezerviranja",decimal_places=2,max_digits=14,blank=True)

    #DUGOROCNE OBVEZE
    dugorocne_obveze=models.DecimalField("Dugorocne obveze",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_1=models.DecimalField("Obveze prema povezanim poduzetnicima",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_2=models.DecimalField("Obveze za zajmove,depozite i slicno",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_3=models.DecimalField("Obveze prema bankama i drugim financijskim institucijama",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_4=models.DecimalField("Obveze za predujmove",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_5=models.DecimalField("Obveze prema dobavljacima",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_6=models.DecimalField("Obveze po vrijednosnim papirima",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_7=models.DecimalField("Obveze prema poduzetnicima u kojima postoje sudjelujuci interesi",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_8=models.DecimalField("Ostale dugorocne obveze",decimal_places=2,max_digits=14,blank=True)
    dugorocne_obveze_9=models.DecimalField("Odgodena porezna obveza",decimal_places=2,max_digits=14,blank=True)


    #KRATKOROCNE OBVEZE
    kratkorocne_obveze=models.DecimalField("Kratkorocne obveze",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_1=models.DecimalField("Obveze prema poveaznim poduzetnicima",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_2=models.DecimalField("Obveze za zajmove,depozite i slicno",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_3=models.DecimalField("Obveze prema bankama i drugim financijskim institucijama",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_4=models.DecimalField("Obveze za predujmove",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_5=models.DecimalField("Obveze prema dobavljacima",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_6=models.DecimalField("Obveze po vrijednosnim papirima",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_7=models.DecimalField("Obveze prema poduzetnicima u kojima postoji sudjelujuci interesi",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_8=models.DecimalField("Obveze prema zaposlenicima",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_9=models.DecimalField("Obveze za poreze,doprinose i slicna davanja",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_10=models.DecimalField("Obveze s osnove udjela u rezultatu",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_11=models.DecimalField("Obveze po osnovi dugotrajne imovine namijenjene prodaji",decimal_places=2,max_digits=14,blank=True)
    kratkorocne_obveze_12=models.DecimalField("Ostale kratkotocne obveze",decimal_places=2,max_digits=14,blank=True)

    odgodeno_placanje_troskova=models.DecimalField("Odgodeno placanje troskova i prihoda buduceg razdoblja",decimal_places=2,max_digits=14,blank=True)
    ukupna_pasiva=models.DecimalField("Ukupna pasiva",decimal_places=2,max_digits=14,blank=True)
    izvanbilancni_zapisi=models.DecimalField("Izvanbilancni zapisi",decimal_places=2,max_digits=14,blank=True)

    #Kapital i rezerve
    pripisano_kapital_matice=models.DecimalField("Pripisano imateljima kapitala matice",decimal_places=2,max_digits=14,blank=True)
    pripisano_manjinskom_interesu=models.DecimalField("Pripisano manjinskom interesu",decimal_places=2,max_digits=14,blank=True)




