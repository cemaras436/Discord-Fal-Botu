import random

class Falim:
    @staticmethod
    def fal_sec():
        fallar = ['Kısmetinde var biri\nMutlu eder seni\nHem maddi hem manevi\nÜyelikten romantik biri',
                  'Aşkın etmiş onu şair\nHer gün yazar bir şiir\nSensin ilham perisi\nTüm satırlar sana dair',
                  'Fazla şey beklemez senden\nİster hayatında çekidüzen\nEvliliktir bunun sonu\nSeversen onu gönülden',
                  'Boynunda var bir kolye\nİki resim bağlı zincire\nBiri o, diğeri sen\nAçar bakar her saniye',
                  'Atmışsın ona bir bakış\nGözlerine tutulmuş kalmış\nKendini bulmuş o anda\nAşkın ona pek yaramış',
                  'Senden bekler hareket\nEdemez konuşmaya cesaret\nSen bir adım atsan ona\nO on adım gelecek',
                  'Bir görünüp bir kayboluyor\nOnu yakalamak zor mu zor\nGöremeyince üzülüyorsun\nSenin de yüreğine düşmüş kor',
                  'Çıkar sık sık şehir dışına\nBir gün gelecek senin oraya\nKopamayacak sonra senden\nYerleşecek evinin yanına',
                  'Her gün bakar aynaya\nGüzel görünmek için sana\nBeğendirecek kendini\nGelirseniz yan yana',
                  'Bir ev döşemiş zevki süper\nBazen pop bazen caz dinler\nHayvanlara sevgisinden\nOkumuş olmuş veteriner',
                  'Sen aramazsan o arar\nSana askı dunya kadar\nDinini de bilir cocuk\nTertemiz bir ahlakı var',
                  'Bir bakışı huzur demek\nHer haliyle o bir melek\nEşin olacak bu genci\nAilen de beğenecek',
                  'Okumuş adamdır kendisi\nGüler yüzlü, sevmez kaprisi\nDoğaya hayran, sık gezer\nYârin bilgisayar mühendisi',
                  'Uzaktan sana bakıyor hep\nBu gence ne oldu acep\nSensin onun sarhoş gibi\nDolanıp durmasına sebep',
                  'Fethedecek kalbini işgali\nEdecek sana evlenme teklifi\nÇok fazla naz yapma\nBu adam çok aceleci',
                  'Sana nimet ondaki sabır\nÇocuklarla iyi anlasır\nBir diğer erdemi bağlılık\nSorumluluğu bilinçte taşır',
                  'Hayatında var bir dönemeç\nGerisi heyecanlı bir süreç\nDişleri beyaz inci gibi\nYüzü de pek bir güleç',
                  'Aklında var bir ikilem\nBu aşk çok bilinmeyenli bir denklem\nHer şey girecek yoluna\nYoktur çözümsüz problem',
                  'İçinde var bir endişe\nVermelisin ona neşe\nGönlünü hoş tutarsan\nVerecek sana her gece',
                  'En yakın dostuna seni anlatıyor\nKonuşurken bire bin katıyor\n"Ya o da hoşlanıyorsa" diyerek\nHer akşam kulağını çınlatıyor',
                  'Seni seven insanoğlu\nBakacak buğulu buğulu\nYüzünden belli o da\nSenin gibi iyi huylu',
                  'İnadını kır bu sefer\nGel bir şans daha ver\nDostluktan öte sevgisi\nBir kez denemeye değer',
                  'Aranızda var bir resmiyet\nAma değişecek bu vaziyet\nÇok uzun sürmeyecek\nOluşacak samimiyet',
                  'Diyar diyar gezeceksin\nÇok kişiyi göreceksin\nİki vaktin sonunda\nDüğün dernek edeceksin',
                  'Gelecek uzun yoldan\nYapacak güzel bir plan\nGönlün ona kayınca\nEdecek aşkını ilan',
                  'Vereceğim sana bir öneri\nGöstermelisin özveri\nİki kişiliktir aşk ama\nDeğildir sahnede gösteri',
                  'Yanakları hep al al\nSanarsın ki yapısal\nHeyecandan aslında\nAşkı verir sinyal',
                  'Lafları biraz imalı\nHepsi de senle alâkalı\nMesaj vermek istiyor\nAzıcık kalbi yaralı',
                  'Bir iki kelâm et\nKurulacak muhabbet\nİki imza var sonunda\nNikâhta var keramet',
                  'Onunla tez geçiyor saat\nKonuşmaya kalmıyor fırsat\nSana söyleyecekleri var\nBu kez zamanı sen ayır',
                  'Aklı bir karış havada olsa\nKeserdi ilişkiyi kısa\nTakma kafana söylenenleri\nSeviyor seni nasılsa',
                  'İçinde şüphe kalmamış\nSana olan aşkını anlamış\nEvet dersen sen de\nGelecek sana tıpış tıpış',
                  'Deme konu komşu ne der\nAğzı olan bi şey söyler\nSen hayal kurmaya devam et\nOlacak içinden geçenler',
                  'Arkandan koşmuş yetişememiş\nBağırmış sesi kesilmiş\nDuy artık şu biçareyi\nAşkın onu derbeder etmiş',
                  'Huyunuz suyunuz aynı\nEtmez hiç vıdı vıdı\nSenin için biçilmiş kaftan\nSevginiz de karşılıklı',
                  'Konuşması çok canayakın\nAma bugünlerde biraz dalgın\nÂşık olmuş sana\nİçinde var büyük yangın',
                  'Eksik olmaz dilinden iltifat\nYaptığı iş de ihracat\nHastalanırsan korkma\nEder bir ömür refakat',
                  'Gelecek bir sürprizle\nBekle doğum gününde\nGörünce şaşıracaksın\nAlmadın böyle hediye',
                  'Sonbahar hüzünlü mevsim\nSana getirecek verim\nİşlerin girecek yoluna\nEğer edersen azim',
                  'Aşk milyon yıllık hikâye\nKimse bulamamış bir çare\nKaçamazsın seni de bulur\nVar sana da kavalye',
                  'Dinliyor kalbinin sesini\nKapatıp güzel gözlerini\nDüşünüyor saatlerce\nSensin en büyük hayali',
                  'Gelecek bütün kalbiyle\nSöz verecek olmaya seninle\nBirlikte uzun yıllar geçecek\nAşkınız ölmeyecek evlilikle'
                  ]

        fal = random.choice(fallar)
        return (fal)
