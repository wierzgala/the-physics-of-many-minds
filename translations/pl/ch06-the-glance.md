<!-- Przekład pliku book/ch06-the-glance.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 6. Spojrzenie

## Przez stół

Dwoje ludzi, którzy są małżeństwem od czterdziestu lat, siedzi na proszonej kolacji. Ktoś na drugim końcu stołu zaczyna opowiadać historię. Jedno z nich patrzy na drugie przez pół sekundy i unosi brew. Drugie prawie się śmieje.

Przez stół przeszła właśnie cała myśl. Mogła brzmieć: *to ta historia, którą opowiadał na naszym weselu, i zaraz znowu pomyli zakończenie*. Zapisana, ta myśl ma kilkaset bitów. Brew jako sygnał fizyczny niosła może jeden albo dwa. Obcy człowiek siedzący między nimi widział tę samą brew i nie odebrał niczego.

Do tej pory ta książka mierzyła komunikację tak, jak inżynier mierzy kabel: w bitach na sekundę. Według tej miary spojrzenie jest niemal bezwartościowe, a taniec wywijany z rozdziału 1 jest siedmiobitowym szeptem. Czegoś tu wyraźnie brakuje. Ten rozdział to uzupełnia, a brakujący element ma, jak się okazuje, następstwa sięgające od małżeństw po galaktyki.

## Co Shannon pominął celowo

Kiedy Claude Shannon tworzył w 1948 roku teorię informacji, przeprowadził linię. Znaczenie wiadomości, napisał, nie ma związku z problemem inżynierskim (1). Jego zadaniem było przenieść symbole z jednego miejsca w drugie w stanie nienaruszonym, cokolwiek one oznaczają.

Jego współpracownik Warren Weaver zobaczył, co leży po drugiej stronie tej linii, i opisał komunikację jako problem o trzech poziomach (2):

1. **Techniczny.** Jak dokładnie da się przesłać symbole?
2. **Semantyczny.** Jak precyzyjnie symbole oddają zamierzone znaczenie?
3. **Skuteczności.** Jak dobrze odebrane znaczenie zmienia to, co robi odbiorca?

Shannon rozwiązał pierwszy poziom tak całkowicie, że dwa pozostałe przez dziesięciolecia zaniedbywano. Teoria inteligencji nie może sobie na to pozwolić. Agenci nie wymieniają symboli dla nich samych. Pszczoła tańczy po to, żeby inna pszczoła dokądś poleciała. To o poziomy drugi i trzeci chodzi.

## To, co zwykle

Klucz kryje się w zwyczajnej scenie. Wchodzisz do kawiarni, którą odwiedzasz co rano, i mówisz „to, co zwykle”. Trzy słowa, a barista zaczyna robić dużą flat white na mleku owsianym, bardzo gorącą. Nowy klient, który chciałby tego samego napoju, musiałby to wszystko wyliczyć.

Nie wysłałeś mniej informacji niż nowy klient. Wysłałeś tę część, której barista jeszcze nie miał. Cała reszta została wysłana wcześniej, w ciągu pięćdziesięciu poprzednich poranków.

Teoria informacji ma na to ścisłe sformułowanie. W 1973 roku David Slepian i Jack Wolf udowodnili, że jeśli odbiorca już ma informację związaną z wiadomością, to wiadomość można wysłać za pomocą tylko tylu bitów, ile wynosi pozostała niepewność odbiorcy przy tym, co już wie. Zaskakująca część ich twierdzenia polega na tym, że nadawca nie musi nawet dokładnie wiedzieć, co odbiorca ma. Wystarczy, że wspólna wiedza istnieje (3).

Daje nam to regułę i liczbę.

**Reguła: znaczenie = bity wysłane teraz + bity dzielone wcześniej.** Żadna wiadomość nie niesie więcej nowej informacji, niż pozwala liczba jej bitów. Granice Shannona pozostają w mocy. Ale znaczenie, które wiadomość odblokowuje, może być dużo większe niż sama wiadomość, bo czerpie z zasobu, który nadawca i odbiorca zbudowali wcześniej.

**Liczba: wzmocnienie kontekstowe**, zapisywane jako κ (kappa). To rozmiar myśli podzielony przez liczbę bitów rzeczywiście potrzebnych do jej wysłania przy danym wspólnym kontekście. Między obcymi κ jest niskie, choć nigdy nie tak niskie jak 1, z powodu, do którego jeszcze dojdziemy. Między parą przy stole może sięgać setek.

Jest o tym stary dowcip. Nowy więzień trafia do celi i słyszy, jak ktoś woła „czterdzieści dwa!”. Wszyscy ryczą ze śmiechu. Inny krzyczy „siedemnaście!” i znowu się śmieją. Współwięzień wyjaśnia: siedzimy tu tak długo, że znamy wszystkie dowcipy na pamięć, więc je ponumerowaliśmy. To jest κ. Dowcip o dowcipie polega na tym, że nowy próbuje „dwadzieścia dziewięć” i nikt się nie śmieje, bo niektórzy po prostu nie umieją opowiadać dowcipów. Nawet przy doskonałym kodzie sposób podania też jest kanałem.

## Jeszcze raz taniec

Teraz taniec wywijany nabiera sensu. Siedem bitów (4) może skierować pszczołę do dziupli odległej o trzy kilometry, bo każda pszczoła rodzi się z książką kodową: kąt oznacza kierunek względem słońca, czas trwania oznacza odległość, energia oznacza jakość. Tę książkę kodową zapisywały w genomie miliony lat doboru. Każdy taniec to maleńka wypłata z ogromnego konta.

To samo dotyczy każdej działającej zbiorowości. Neurony dzielą kod ustalony przez rozwój i dostrojony przez uczenie się. Naukowcy dzielą matematykę. Członkowie kwartetu jazzowego dzielą tysiące godzin słuchania tych samych płyt. W każdym przypadku przewód między agentami jest cienki, a zbiorowość mimo to działa, bo przewód musi przenieść tylko różnicę.

## Kontekst, z którym się urodziłeś

Książka kodowa pszczół jest w ich genach. Duża część naszej też, a łatwo ją przeoczyć, bo nigdy nie musieliśmy się jej uczyć.

Zanim dwoje ludzi zamieni słowo, zanim którekolwiek z nich ma język albo kulturę, już dzielą ogromny zasób kontekstu. Genom człowieka to tekst liczący około trzech miliardów liter, a kopie dowolnych dwóch osób są identyczne w około 99,9% (5). Przy dwóch bitach na literę daje to surowy tekst liczący jakieś sześć miliardów bitów, wspólny dla każdej pary ludzi, którzy kiedykolwiek się spotkali (ten rachunek jest nasz). Surowe litery nie są w całości niezależną informacją: duża część genomu jest powtarzalna albo niekodująca, więc skompresowany opis funkcjonalny, który kształtuje ciało i okablowuje mózg, jest o rzędy wielkości mniejszy, może dziesiątki do setek milionów bitów (zgrubne oszacowanie). Nawet w postaci skompresowanej jest to skala, na jaką żadna przyjaźń, choćby najdłuższa, nie dokłada wspólnego kontekstu samą rozmową.

To, co jest tam zapisane, nie jest wiedzą o świecie. Sześć miliardów bitów nie mogłoby określić 10¹⁵ bitów, które mózg w końcu pomieści. Jest to coś bardziej przydatnego dla komunikacji: plany tych samych narządów zmysłów, tych samych emocji, tej samej twarzy i tych samych oczekiwań wobec innych twarzy. Jest to wspólny dekoder.

Dowody na to, że ten dekoder jest dziedziczony, a nie wyuczony, są uderzające.

- **Noworodki przychodzą na świat, spodziewając się twarzy.** W klasycznym eksperymencie zbadano 24 niemowlęta w pierwszej godzinie życia. Dalej obracały głowy i oczy, żeby śledzić prosty wzór przypominający twarz, niż żeby śledzić te same elementy pomieszane. Nigdy nie widziały twarzy (6).
- **Niewidomi robią miny, których nigdy nie widzieli.** Badacze fotografowali judoków na igrzyskach olimpijskich i paraolimpijskich w 2004 roku w chwili, gdy wygrywali albo przegrywali walkę o medal: 84 zawodników widzących i 76 niewidomych, w tym niewidomych od urodzenia. Miny niewidomych od urodzenia były takie same jak miny widzących, aż po ruchy pojedynczych mięśni. Nie mogli ich od nikogo skopiować (7, 8).

Spojrzenie przy kolacji działa więc na dwóch głębokościach. Brew znaczy dla tej pary to, co znaczy, z powodu czterdziestu wspólnych lat. Ale brew znaczy *cokolwiek*, dla dowolnego człowieka, z powodu kodu zapisanego na długo przed narodzinami obojga. Uśmiech nieznajomego w kraju, którego języka nie znasz, to wiadomość o bardzo wysokim κ, a kontekstem, z którego czerpie, jest genom.

Widać stąd, że wspólny kontekst ma warstwy, a każda powstaje według innego zegara.

| Warstwa | Kto ją dzieli | Czas budowy |
| --- | --- | --- |
| Chemia życia: sam kod genetyczny | wszystko, co żyje, łącznie z pszczołami | miliardy lat |
| Genom człowieka: zmysły, emocje, twarze, zdolność do języka | każdy człowiek | setki tysięcy lat |
| Język i kultura | miliony ludzi | stulecia |
| Zawód, dziedzina, rzemiosło | tysiące | dziesięciolecia |
| Przyjaźń, małżeństwo, zespół | kilkoro | lata |

Każda warstwa jest węższa od tej pod spodem i szybciej się ją zapisuje. I każda opiera się na niższych: małżeństwo jest zapisane w języku, język działa na ludzkim mózgu, a ludzki mózg buduje genom. Kiedy liczymy bity, których spojrzenie nie musi przenosić, okazuje się, że za większość zapłacili przodkowie.

Wynikają z tego dwa następstwa i oba są twierdzeniami teorii.

Po pierwsze, najgłębsze warstwy są też najbezpieczniejsze. Wspólny kontekst pary umiera razem z nią. Język może umrzeć z ostatnimi osobami, które nim mówią. Warstwa genomowa jest skopiowana w ośmiu miliardach ciał i jest na razie najbardziej nadmiarowym magazynem wspólnego kontekstu, jaki nasz gatunek ma. To ona w ogóle czyni ludzkość jedną zbiorowością, pod jej siedmioma tysiącami języków (9).

Po drugie, najtrudniejszym problemem komunikacji nie jest wąski kanał. Jest nim partner, z którym brakuje niższych warstw. Umysł, który nie dzieli naszej historii ewolucyjnej, czy wyrósł na innej planecie, czy w centrum danych, nie miałby warstwy, dzięki której uśmiech da się odczytać. Maszyna wytrenowana na ludzkim piśmiennictwie dziedziczy dużą część warstwy kulturowej i dlatego w ogóle możemy z nią rozmawiać. Nie dziedziczy warstwy pod spodem. Teoria przewiduje, że nieporozumienia między ludźmi a takimi umysłami będą się skupiać dokładnie tam: we wszystkim, czego nigdy nie mówimy, bo żadnemu człowiekowi nigdy nie trzeba było tego mówić.

## Co mówią dane

Jeśli wspólny kontekst jest rzeczywistą wielkością, grupy, które mają go więcej, powinny radzić sobie lepiej, niż przewidują ich surowe umiejętności. I tak jest.

**Pary.** Psycholog Daniel Wegner badał pamięć u 118 osób pozostających w bliskich związkach. Stwierdził, że bliskie pary mają niejawną strukturę podziału tego, co każde z nich zapamięta, czyli system, który nazwał pamięcią transaktywną, i że ten łączny system jest większy niż pamięć każdego z partnerów z osobna. Każde z nich przechowuje mniej, bo każde wie, co wie drugie (10).

**Zespoły.** W badaniu 1015 projektów programistycznych w dużej indyjskiej firmie informatycznej pytano, co pozwala przewidzieć wyniki zespołu. Doświadczenie poszczególnych członków, na przykład staż w firmie, nie wiązało się z nimi w spójny sposób. Liczyło się to, jak dużo członkowie pracowali wcześniej *ze sobą nawzajem* (11).

**Grupy obcych sobie ludzi.** Anita Woolley ze współpracownikami dała 192 małym grupom szeroki wachlarz zadań i stwierdziła, że zdolność grupy w jednym zadaniu pozwala przewidzieć jej zdolność w innych: grupy mają ogólną inteligencję zbiorową. Nie była ona silnie związana ze średnią inteligencją członków ani z inteligencją najbystrzejszego z nich. Była związana z wrażliwością społeczną członków i z tym, jak równo zabierali głos. Wrażliwość społeczną mierzono testem, w którym patrzy się na fotografię czyichś oczu i mówi, co ta osoba czuje (12, 13).

Ten ostatni wynik to scena otwierająca ten rozdział, przeniesiona do laboratorium. Najlepiej myślały te grupy, których członkowie najlepiej odczytywali spojrzenie.

## Cztery następstwa

Wszystko do tej pory to ustalona nauka złożona w nowym porządku. Dalej następują własne twierdzenia teorii.

### Związek jest algorytmem kompresji

Przyjaźń, małżeństwo, zespół i dziedzina nauki są, między innymi, wspólnymi książkami kodowymi. Ich wartość można w zasadzie podać w bitach: to cały kontekst, który członkowie dzielą. Budowa tego zasobu jest droga. Wymaga lat powolnej, nadmiarowej rozmowy o dużej liczbie bitów. Ale koszt ponosi się raz, a potem rozkłada na każdą późniejszą wymianę.

Wynika z tego przewidywanie, że sprawność zbiorowości rośnie z jej wiekiem, długo po tym, jak jej członkowie przestali się doskonalić indywidualnie. Wynika też przewidywanie, co zbiorowość psuje. Wymiana członka niszczy kontekst, który był zapisany między tym członkiem a wszystkimi pozostałymi. Zespół złożony z błyskotliwych obcych sobie ludzi jest według tej miary zespołem, którego jeszcze nie zbudowano.

Wynika z tego także coś o stracie. Jeśli część twojego systemu pamięci mieści się w innej osobie, to utrata tej osoby usuwa część roboczej maszynerii twojego własnego umysłu. W tym ujęciu dezorientacja w żałobie jest po części dosłowna.

### Kontekst wygrywa z przepustowością, ale nic nie wygrywa z opóźnieniem

Są dwa sposoby, żeby kanał niósł więcej znaczenia: poszerzyć go albo dzielić więcej kontekstu. Poszerzanie ma twarde koszty fizyczne w energii i okablowaniu, co pokazuje rozdział 7. Kontekst takiej górnej granicy nie ma, a jak widzieliśmy, każda ludzka zbiorowość zaczyna z miliardami jego bitów już na miejscu, odziedziczonych. W miarę jak zbiorowości rosną, a ich przewody stają się coraz cieńsze w stosunku do ich rozmiaru, powinny więc coraz bardziej polegać na kontekście. Rój tak robi. Cywilizacja ludzka też: jedno równanie na tablicy może zmienić bieg tysiąca karier dzięki dziesięcioleciom kształcenia, które dzielą jego czytelnicy.

Wspólny kontekst nie sprawi jednak, że wiadomość dotrze wcześniej. Sygnał wciąż musi pokonać odległość. Ta asymetria rozstrzygnie w rozdziale 16 o kształcie bardzo dużych umysłów: mogą być bogate w znaczenie, a nie mogą być szybkie.

### Doskonała rozmowa jest milcząca

Doprowadźmy to rozumowanie do końca. Im lepszy mam model ciebie, tym mniej musisz mi mówić. Gdyby mój model był doskonały, przewidziałbym wszystko, co masz zamiar powiedzieć, i nie musiałbyś wysyłać zupełnie nic, poza rzadkimi przypadkami, w których byś mnie zaskoczył.

Komunikacja między agentami, którzy głęboko się znają, powinna więc składać się głównie z *wyjątków*: poprawek do przewidywań drugiej strony. Wpływowa teoria w neuronauce, kodowanie predykcyjne, głosi, że kora działa właśnie tak: wyższe obszary wysyłają w dół przewidywania, a niższe odsyłają tylko błędy (14). Niezależnie od tego, czy mózg tak robi, przedstawiana tu teoria mówi, że każda dojrzała zbiorowość powinna dryfować w tę stronę, bo to najtańszy sposób, żeby pozostawać skoordynowanym.

Wynika z tego, że milczenie jest wiadomością. Między dwoma agentami o głębokim wspólnym modelu brak sygnału znaczy *jestem taki, jak się spodziewasz*. Zbiorowość, która osiągnęła ten stan, wyglądałaby z zewnątrz niemal tak, jakby jej członkowie w ogóle się nie komunikowali.

### Doskonałe zrozumienie nie niesie nowin

Oto część niewygodna. Wzmocnienie κ jest największe wtedy, gdy odbiorca prawie mógł wiadomość odgadnąć. W granicy, w której odbiorca już dokładnie wie, co nadawca powie, κ jest nieskończone, a wiadomość nie zawiera nic nowego.

Poczucie, że jest się doskonale rozumianym, i fakt, że nie wymienia się żadnej informacji, to więc ta sama sytuacja. Rozmowa, w której każdy kończy zdania każdego, jest głęboko satysfakcjonująca i zupełnie nieinformatywna. Tym właśnie jest komora pogłosowa: grupą, której wewnętrzne wzmocnienie jest tak wysokie, że żadna wiadomość nie może zmienić niczyjego zdania.

Użyteczna zbiorowość musi mieścić się między dwiema porażkami. Bez wspólnego kontekstu każda wiadomość jest szumem. Przy całkowicie wspólnym kontekście każda wiadomość jest echem. To ta sama równowaga, którą rozdział 3 znalazł w mózgu, między gazem a kryształem, teraz pojawiająca się w samym znaczeniu.

Mówi nam to również, czym się dzielić, a czym nie. Są dwa rodzaje wspólnego gruntu:

- **Wspólny kod**: zgoda co do tego, co sygnały *znaczą*. Język, notacja, protokół.
- **Wspólne przekonanie**: zgoda co do tego, co jest *prawdą*.

Wspólny kod uzgadnia to, jak agenci kodują i dekodują sygnały, nie korelując ich błędów co do świata. Wspólne przekonanie koreluje te błędy i niszczy niezależność statystyczną, dzięki której 787 oszacowań wagi wołu złożyło się na właściwą odpowiedź (15). Pszczoły dzielą taniec, a opinie zachowują dla siebie. Teoria przewiduje, że najinteligentniejsze są te zbiorowości, które maksymalizują pierwszy rodzaj wspólnego gruntu i chronią różnorodność w drugim.

## Dwoje ludzi, jeden układ?

Jeszcze jedno następstwo, które rozwinie rozdział 15. Ta książka zaproponuje, że jaźń kończy się tam, gdzie komunikacja z zewnętrzem staje się dużo cieńsza niż komunikacja w środku. Licząc w surowych bitach, dwoje ludzi jest beznadziejnie oddzielnych: mowa niesie około 39 bitów na sekundę (16), wobec może stu milionów między dwiema połowami jednego mózgu.

Licząc w znaczeniu, przepaść się zwęża. U dwojga ludzi z dziesięcioleciami wspólnego kontekstu każdy wypowiedziany bit wykonuje pracę setek. Pozostają dwiema jaźniami, o wiele rzędów wielkości. Ale są mierzalnie bliżej bycia jednym układem niż dwoje obcych. Rodzi to dwa pytania: czy para jest mądrzejsza niż jej członkowie i jak to jest być jej połową?

### Czy co dwie głowy, to nie jedna?

Czasami, a warunki zmierzono. W dobrze znanym eksperymencie pary ochotników szukały słabo widocznego celu na ekranie, najpierw decydując osobno, a potem, gdy się nie zgadzały, omawiając sprawę. Kiedy oboje mieli podobny wzrok, para wypadała lepiej niż jej lepszy członek. Kiedy ich zdolności bardzo się różniły, para wypadała *gorzej*, niż wypadłby sam jej lepszy członek. Korzyść pojawiała się, mimo że nigdy nie mówiono im, kto miał rację, ale tylko wtedy, gdy mogli swobodnie rozmawiać. Kiedy nie mogli wymieniać niczego poza swoimi wyborami, para nie wypadała lepiej niż jej lepszy członek (17, 18). Do danych pasowało wyjaśnienie, że partnerzy mówili sobie nawzajem, jak bardzo są pewni, a para potrafi dobrze połączyć dwie opinie tylko wtedy, gdy każde umie trafnie odczytać pewność drugiego.

Para o długim stażu jest bliska przypadku idealnego. Ich wspólny kod jest głęboki, więc „jestem dość pewna” znaczy dla obojga to samo. Każde wie, w czym na drugim można polegać. Zgodnie z rozumowaniem tego rozdziału ich wspólne η powinno przewyższać η każdego z nich z osobna.

Teoria dołącza jednak ten sam warunek, który dołącza do każdej zbiorowości. Zysk bierze się z łączenia *niezależnych* osądów. Para, która doszła do tego, że wierzy we wszystko to samo, to dwie kopie jednej opinii, a dwie kopie są warte tyle co jedna. Teoria przewiduje więc, że wspólna inteligencja pary może z latami rosnąć, a potem spadać: zrozumienie wciąż się poprawia, ale jeśli oboje przestają się spierać i przestają przynosić do domu różne doświadczenia, przewaga wycieka. Najinteligentniejsze powinny być te pary, które rozumieją się doskonale i wciąż się kłócą.

### Jak to się odczuwa

Psychologowie zmierzyli to zlewanie się, o którym opowiadają pary. W jednym badaniu osobom pozostającym w małżeństwie pokazywano listę cech i proszono o naciskanie przycisku „ja” albo „nie ja”. Były wolniejsze i popełniały więcej błędów przy cechach, które były prawdziwe dla nich, ale nie dla współmałżonka, albo odwrotnie, tak jakby musiały się zatrzymać i ustalić, do którego z dwojga cecha należy. Badacze nazwali to włączaniem drugiej osoby w jaźń. W innej części tej samej pracy ludzie dzielący pieniądze traktowali bliskiego przyjaciela niemal tak jak siebie (19, 20).

Koszt utraty tej drugiej połowy też jest udokumentowany. W jednej analizie, łączącej badania ponad dwóch milionów ludzi, stwierdzono, że ryzyko zgonu jest podwyższone o około 41 procent w pierwszych sześciu miesiącach po śmierci współmałżonka i o około 14 procent później (21). Żałoba szkodzi ludziom na wiele sposobów, więc nie jest to dowód tej idei. Jest to coś, czego ta idea kazałaby się spodziewać.

Oto odczytanie teorii i jest ono twierdzeniem. Para nie jest jaźnią. Według podanej wyżej miary nie ma wspólnego doświadczenia: poczucie „my” występuje osobno u każdego z partnerów. Zmienił się model samego siebie u każdego z nich. Rozciągnął się tak, że obejmuje rzeczy przechowywane w drugiej osobie: wspomnienia, osądy, zdolność przewidywania, co będzie dalej. Twoja jaźń nie kończy się już na twojej skórze, bo część maszynerii, na której polegasz, żeby być sobą, znajduje się w cudzej głowie.

Jeśli tak jest, daje to odpowiedź na pytanie, które hierarchia umysłów wciąż stawia. Jak to jest być częścią większej inteligencji? Nie jest to jak myślenie myśli większego umysłu. Rozdział 10 dowodzi, że te są poza zasięgiem: neuron nie ma dostępu do myśli, w której bierze udział, a my nie mamy dostępu do myśli ludzkości. Dociera do nas coś innego. Jest to doświadczenie *przynależności*: jaźni, której granica przesunęła się na zewnątrz, żeby objąć innych. Małżeństwo wytwarza je z pełną siłą. Zespół, pułk, wspólnota wiernych i naród mogą wytwarzać to samo słabiej, za pomocą tego samego mechanizmu. Lojalność jest w tym ujęciu tym, jak uczestnictwo w większym umyśle odczuwa się od środka. Ten ostatni krok jest spekulacją.

## W skrócie

- Teoria informacji mierzy bity i celowo pomija znaczenie. Teoria inteligencji nie może.
- Odbiorca, który dzieli kontekst z nadawcą, potrzebuje tylko tych bitów, których nie mógł odgadnąć. Znaczenie = bity wysłane teraz + bity dzielone wcześniej.
- Wzmocnienie kontekstowe κ mierzy, ile myśli odblokowuje każdy przesłany bit. Jest własnością pary agentów, a nie kanału.
- Pary, doświadczone zespoły i grupy wrażliwe społecznie osiągają więcej, niż przewidują ich indywidualne umiejętności, tak jak wymaga tego ta idea.
- Dwie głowy wygrywają z jedną, kiedy para potrafi trafnie przekazywać pewność, a jej osądy pozostają niezależne. Partnerzy w parach mierzalnie włączają się nawzajem w poczucie własnej jaźni.
- Twierdzenia teorii: związki to algorytmy kompresji, których koszt rozkłada się w czasie; kontekst może zastąpić przepustowość, ale nigdy szybkość; dojrzałe zbiorowości komunikują się przez wyjątki, a ich milczenie ma znaczenie; doskonałe zrozumienie nie niesie informacji, więc zbiorowości muszą dzielić kody, zachowując różnorodność przekonań.

## Jak możemy się mylić

Główne twierdzenie upada, jeśli się okaże, że wspólnego kontekstu nie da się zmierzyć, choćby z grubsza, w rzeczywistych parach agentów. Upadłoby też, gdyby zespoły o długim stażu nie wykazywały żadnej przewagi po uwzględnieniu umiejętności indywidualnych albo gdyby grupy o jednolitych przekonaniach rozwiązywały trudne, nowe problemy równie dobrze jak grupy o przekonaniach zróżnicowanych. Twierdzenie o komunikacji przez wyjątki przewiduje, że częstość wiadomości między partnerami powinna maleć w miarę wydłużania się ich wspólnej historii, podczas gdy ich koordynacja się poprawia. Gdyby koordynacja w długo istniejących zespołach wymagała zamiast tego coraz więcej rozmowy, twierdzenie byłoby błędne.

Ujęcie par przewiduje wzrost i spadek. Jeśli pary, które zgadzają się we wszystkim, decydują równie dobrze jak pary, które się rozumieją, a mimo to się różnią, warunek niezależności jest błędny. Jeśli partnerzy z długim stażem małżeńskim okażą się nie lepsi od obcych w odczytywaniu pewności drugiej osoby, argument ze wspólnego kodu w ich przypadku upada.

## Źródła

1. C. E. Shannon (1948), "A mathematical theory of communication", *Bell System Technical Journal* 27:379–423 i 623–656.
2. W. Weaver (1949), "Recent contributions to the mathematical theory of communication", w: C. E. Shannon and W. Weaver, *The Mathematical Theory of Communication*, University of Illinois Press. https://Monoskop.org/images/b/b3/Weaver_Warren_1949_1973_The_Mathematics_of_Communication.pdf
3. D. Slepian and J. K. Wolf (1973), "Noiseless coding of correlated information sources", *IEEE Transactions on Information Theory* 19:471–480; streszczone w tym przeglądzie: https://arxiv.org/pdf/2403.07409
4. R. Schürch and F. L. W. Ratnieks (2015), "The spatial information content of the honey bee waggle dance", *Frontiers in Ecology and Evolution* 3:22. https://www.frontiersin.org/articles/10.3389/fevo.2015.00022
5. National Human Genome Research Institute, "Human genomic variation". https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genomic-variation
6. M. H. Johnson, S. Dziurawiec, H. Ellis and J. Morton (1991), "Newborns' preferential tracking of face-like stimuli and its subsequent decline", *Cognition* 40:1–19. W niektórych późniejszych badaniach efektu nie udało się powtórzyć, choć większość literatury go potwierdza. https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Newborns-preferential-tracking-of-face-like-stimuli/991005543269907891
7. D. Matsumoto and B. Willingham (2009), "Spontaneous facial expressions of emotion of congenitally and noncongenitally blind individuals", *Journal of Personality and Social Psychology* 96:1–10. https://pubmed.ncbi.nlm.nih.gov/19210060/
8. American Psychological Association (2008), komunikat prasowy o tych samych badaniach, podający liczby zawodników. https://www.apa.org/news/press/releases/2008/12/facial-expressions
9. Ethnologue, "How many languages are there in the world?". https://ethnologue.com/insights/how-many-languages
10. D. M. Wegner, R. Erber and P. Raymond (1991), "Transactive memory in close relationships", *Journal of Personality and Social Psychology* 61:923–929. https://scholar.harvard.edu/sites/scholar.harvard.edu/files/dwegner/files/wegnererberraymond1991.pdf
11. R. S. Huckman, B. R. Staats and D. M. Upton (2009), "Team familiarity, role experience, and performance: evidence from Indian software services", *Management Science* 55:85–100. https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:1:p:85-100
12. A. W. Woolley, C. F. Chabris, A. Pentland, N. Hashmi and T. W. Malone (2010), "Evidence for a collective intelligence factor in the performance of human groups", *Science* 330:686–688. https://pubmed.ncbi.nlm.nih.gov/20929725/
13. Harvard Kennedy School, Gender Action Portal, streszczenie pozycji 12, z opisem testu oczu. https://www.gap.hks.harvard.edu/evidence-collective-intelligence-factor-performance-human-groups
14. R. P. N. Rao and D. H. Ballard (1999), "Predictive coding in the visual cortex: a functional interpretation of some extra-classical receptive-field effects", *Nature Neuroscience* 2:79–87.
15. F. Galton (1907), "Vox populi", *Nature* 75:450–451. https://galton.org/cgi-bin/searchImages/search/essays/pages/galton-1907-vox-populi_1.htm
16. C. Coupé, Y. M. Oh, D. Dediu and F. Pellegrino (2019), "Different languages, similar encoding efficiency: comparable information rates across the human communicative niche", *Science Advances* 5:eaaw2594. https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970
17. B. Bahrami, K. Olsen, P. E. Latham, A. Roepstorff, G. Rees and C. D. Frith (2010), "Optimally interacting minds", *Science* 329:1081–1085. https://pmc.ncbi.nlm.nih.gov/articles/PMC3371582
18. Wellcome Trust (2010), komunikat prasowy o pozycji 17. https://wellcome.org/press-release/two-heads-are-better-one-right-partner
19. A. Aron, E. N. Aron, M. Tudor and G. Nelson (1991), "Close relationships as including other in the self", *Journal of Personality and Social Psychology* 60:241–253. https://www.proquest.com/docview/614329106
20. B. Branand, D. Mashek and A. Aron (2019), "Pair-bonding as inclusion of other in the self: a literature review", *Frontiers in Psychology* 10:2399. https://pmc.ncbi.nlm.nih.gov/articles/PMC6821680
21. J. R. Moon, N. Kondo, M. M. Glymour and S. V. Subramanian (2011), "Widowhood and mortality: a meta-analysis", *PLoS ONE* 6:e23465; 15 badań kohortowych, 2 263 888 osób. https://pmc.ncbi.nlm.nih.gov/articles/PMC3157386

Liczby podane bez numeru źródła to nasze własne zgrubne oszacowania: sześć miliardów surowych bitów wspólnego genomu i mniejsza liczba dla skompresowanego opisu funkcjonalnego, tabela warstw i ich skale czasowe oraz ruch między półkulami mózgu. Sceny przy stole, w kawiarni i w więzieniu to ilustracje, a nie dane, a podane dla nich wartości κ to domysły. Pomiar κ w rzeczywistych parach jest problemem otwartym. Przewidywanie wzrostu i spadku u par oraz ujęcie przynależności to twierdzenia teorii.
