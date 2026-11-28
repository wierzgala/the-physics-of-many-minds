<!-- Przekład pliku book/ch13-designing-a-mind.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 13. Projektowanie umysłu

## Pytanie inżyniera

Do tej pory ta książka pracowała jak przyrodnik. Przyglądała się umysłom, które istnieją, rojowi, mózgowi, stadu, gatunkowi, i pytała, dlaczego są takie, jakie są.

Inżynier zadaje to pytanie od drugiej strony. Oto zadanie. Jak musi wyglądać rzecz, która je wykonuje?

Inżynier konstruktor potrafi na to odpowiedzieć w przypadku mostu. Podaj jej rozpiętość, obciążenie i wytrzymałość stali, a powie, zanim jakikolwiek architekt narysuje kreskę, mniej więcej jak wysokie muszą być belki i ile stali most będzie potrzebował. Nie powie, jak most będzie wyglądał. Dwa mosty przez tę samą rzekę mogą być łukowy i wiszący. Ale oba będą posłuszne jej liczbom, a każdy projekt, który je narusza, runie.

Ten rozdział próbuje zrobić to samo dla umysłów, korzystając z ram rozdziału 12. Jeśli teoria jest słuszna, to podanie zadania, czyli tego, ile informacji napływa, ile musi wyjść i jak szybko, powinno ustalić zarys każdego umysłu, który potrafi je wykonać: ile poziomów, ilu agentów na wejściu, jaki rozmiar, który z dwóch rodzajów. Ten zarys to *morfologia* umysłu. Jeśli zarys da się wyprowadzić, a potem zgadza się z umysłami, które wyewoluowały, nie pytając nas o zdanie, teoria coś przewidziała. Jeśli się nie zgadza, dowiadujemy się, gdzie teoria jest błędna.

## Specyfikacja

Weźmy określone zadanie.

*Strumień surowych danych napływa w tempie dziesięciu milionów bitów na sekundę. Prawie wszystko w nim jest nieistotne. Umysł musi wydobyć z niego jeden użyteczny bit na sekundę, jedną decyzję „tak czy nie” co sekundę, i nigdy nie może spóźnić się więcej niż o sekundę.*

Zapisane w zmiennych rozdziału 12:

- informacja napływająca, R_in: 10⁷ bitów na sekundę
- informacja wychodząca, R_out: 1 bit na sekundę
- skala czasowa świata, T_w: 1 sekunda
- wymagana kompresja, R_in ÷ R_out: dziesięć milionów do jednego

Projekt można teraz opracować krok po kroku. Każdy krok korzysta z reguły z wcześniejszego rozdziału. Arytmetyka jest nasza i zgrubna. Liczy się to, czy zarys wychodzi dobrze z dokładnością do czynnika dziesięć.

## Krok 1. Jak szerokie jest wejście?

Rozdział 7 stwierdził, że koszt bitu rośnie z tempem, w jakim kanał go przenosi, tak że wiele powolnych kanałów jest tańszych niż kilka szybkich. Najtańsze kanały, jakie komórki nerwowe zdają się umieć zbudować, przenoszą coś koło dziesięciu bitów na sekundę.

Wejście powinno więc mieć około

> 10⁷ bitów na sekundę ÷ 10 bitów na sekundę na kanał = **milion równoległych kanałów**

a każdy z nich powinien być powolny. Projekt z tysiącem szybkich kanałów wykonałby to samo zadanie za znacznie wyższą cenę.

## Krok 2. Ile poziomów?

Żaden agent dość tani, żeby mieć ich milion, nie zamieni dziesięciu milionów bitów w jeden. Kompresję trzeba wykonać etapami. Jeśli każdy poziom przekazuje następnemu ułamek 1/f tego, co otrzymuje, potrzebna liczba poziomów wynosi

> poziomy = log(10⁷) ÷ log(f)

| Kompresja na poziom, f | Potrzebne poziomy |
| --- | --- |
| 100 | 3 lub 4 |
| 10 | 7 |
| 3 | około 15 |

Teoria nie mówi jeszcze, ile powinno wynosić f, i to jest najsłabiej określona część projektu. Daje jednak zakres: **od mniej więcej czterech do piętnastu poziomów**, przy czym łagodna kompresja na poziom oznacza, że jest ich więcej. Rozdział 11 podsuwa wskazówkę, że w przyrodzie regułą jest łagodna kompresja: warstwy ludzkich grup społecznych rosną za każdym razem mniej więcej trzykrotnie.

## Krok 3. Jak duży może być?

Umysł ma jedną sekundę na każdą decyzję. Rozdział 10 oszacował, że decyzja zajmuje kilkadziesiąt czasów przejścia w każdym umyśle, w którym to zmierzono, około pięćdziesięciu. Czas przejścia może więc wynosić najwyżej około jednej pięćdziesiątej sekundy, 20 milisekund, a rozmiar najwyżej tyle, ile sygnał pokonuje w tym czasie.

| Sygnały zrobione z | Prędkość | Maksymalny rozmiar |
| --- | --- | --- |
| cienkich włókien nerwowych | 1 m/s | 2 centymetry |
| typowych włókien nerwowych | 10 m/s | 20 centymetrów |
| najszybszych włókien nerwowych | 100 m/s | 2 metry |
| latających owadów | 7 m/s, plus minuty na dostarczenie każdej wiadomości | nie dotrzyma terminu przy żadnym rozmiarze |
| kabli elektrycznych | 200 000 km/s | 4000 kilometrów |

Umysł zbudowany z komórek nerwowych, który wykonuje to zadanie, musi **zmieścić się w przestrzeni o średnicy od kilku do kilkudziesięciu centymetrów.** Umysł zbudowany ze zwierząt, które noszą sobie nawzajem wiadomości, nie wykona go wcale.

## Krok 4. Który rodzaj umysłu?

Na wyjściu jest jedna decyzja naraz. Rozdział 8 dowodził, że pojedynczy strumień decyzji wymaga sceny: jednego rozgłaszania wspólnego dla całości. **Szczyt hierarchii musi więc być zintegrowany.**

Krok 3 pokazał, że cały umysł mieści się w odległości, którą jego sygnały zdążą pokonać w wyznaczonym czasie, więc nic nie zmusza niższych poziomów do bycia sfederowanymi. Ale krok 1 mówi, że wejście powinno składać się z bardzo wielu cienkich kanałów, a cienkie kanały między poziomami oznaczają, że każdy poziom oblicza więcej, niż przekazuje dalej. Oszczędnym projektem jest zatem stos modułów, które mało sobie mówią, zasilający zintegrowany szczyt: **sfederowany u dołu, zintegrowany u góry.**

## Krok 5. Ile to będzie kosztować?

Dolną granicą jest granica Landauera. Odrzucanie dziesięciu milionów bitów na sekundę w temperaturze ciała kosztuje około 3 × 10⁻¹⁴ wata, czyli nic.

Przy cenach, jakie komórki nerwowe rzeczywiście płacą, od dziesięciu tysięcy do dziesięciu milionów cząsteczek ATP na bit (1), przeniesienie strumienia wejściowego przez pierwszy etap kosztuje gdzieś między jedną setną mikrowata a dziesięcioma mikrowatami. Późniejsze poziomy przenoszą o wiele mniej i dokładają niewiele. Cały potok, liczony jako sam przekaz, powinien działać na **mikrowatach.**

## Krok 6. Ilu agentów w sumie?

Jeśli każdy poziom ma 1/f tylu agentów co poziom pod nim, suma jest tylko trochę większa niż pierwszy poziom: około półtora miliona agentów dla f = 3.

## Projekt i umysł, który do niego pasuje

Zebrany razem, zarys umysłu do tego zadania według teorii to:

- około miliona powolnych kanałów wejściowych, z których każdy przenosi około dziesięciu bitów na sekundę
- od czterech do piętnastu poziomów, prawdopodobnie bliżej górnej liczby
- rozmiar od centymetrów do dziesiątek centymetrów, jeśli jest zbudowany z komórek nerwowych
- luźno sprzężone moduły u dołu i jedna zintegrowana scena u góry
- koszt przekazu rzędu mikrowatów
- co najmniej milion albo dwa miliony agentów

Liczby w specyfikacji nie zostały wybrane przypadkowo. Dziesięć milionów bitów na sekundę to szacowane wyjście ludzkiego oka, a kilka bitów na sekundę to tempo, w jakim człowiek działa. Specyfikacja to, w dostatecznym przybliżeniu, *zobaczyć coś i zdecydować, co z tym zrobić*. Zarys można więc porównać z jedynymi umysłami, o których wiadomo, że wykonują to zadanie.

| Cecha | Przewidziana na podstawie zadania | Układ wzrokowy człowieka |
| --- | --- | --- |
| Kanały wejściowe | około miliona | od 0,7 do 1,5 miliona włókien w nerwie wzrokowym (2) |
| Tempo na kanał | około 10 bitów na sekundę | od 6 do 13 bitów na sekundę na włókno, zmierzone u świnki morskiej (3) |
| Które kanały przenoszą najwięcej | powolne | komórki „ospałe”, jako liczniejsze, przenoszą większość informacji (3) |
| Poziomy | od 4 do 15 | 10 poziomów kory wzrokowej, 14 razem z siatkówką oraz stacjami przed i po (4) |
| Kompresja na poziom | od 3 do 100 | około 3, jeśli milionkrotną redukcję rozłożyć na około 12 poziomów (nasze oszacowanie) |
| Rozmiar | od 2 do 20 centymetrów | około 15 centymetrów |
| Układ | moduły u dołu, jedna scena u góry | siatkówka, która sama przetwarza i wysyła streszczenie; jeden strumień wyboru u góry (5) |
| Moc przekazu | mikrowaty | o wiele więcej; zob. niżej |
| Liczba agentów | milion albo dwa | miliardy; zob. niżej |

Siedem z dziewięciu wierszy wychodzi dobrze, przy punkcie wyjścia złożonym z trzech liczb. Wejście ma właściwą szerokość, jest zbudowane z kanałów o właściwej szybkości, a ciężar niosą powolne. Głębokość mieści się w zakresie. Rozmiar się zgadza. Układ się zgadza. Kompresja około trzech na poziom jest zbieżnością ze stosunkiem między ludzkimi warstwami społecznymi, która może coś znaczyć albo nie.

Trzeba powiedzieć wprost, że nie jest to przewidywanie na ślepo. Autor wiedział, jak wygląda układ wzrokowy, zanim wykonał rachunek, a kilka z użytych reguł samo zostało wyuczone z układów nerwowych. Test jest słabszy, niż się wydaje. Staje się prawdziwym testem, kiedy te same sześć kroków zastosuje się do zwierząt, których anatomii teoretyk nie sprawdzał, a następna część mówi, jak to zrobić.

## Dwa pudła i czego uczą

Projekt mocno chybia w dwóch wierszach, a te pudła są najbardziej użyteczną częścią ćwiczenia.

Teoria mówi, że wystarczy parę milionów agentów i kilka mikrowatów. Rzeczywisty układ wzrokowy używa miliardów neuronów, u naczelnych blisko połowy kory mózgowej według jednego z podręczników (6), i dużej części dwudziestu watów mózgu (nasze oszacowanie). Co więcej, już na pierwszej stacji korowej, w pierwszorzędowej korze wzrokowej (V1), układ wcale się nie zwęża: mniej więcej milion włókien nerwu wzrokowego rozchodzi się wachlarzem na ponad sto milionów neuronów V1 (nasza zgrubna liczba ze standardowej neuroanatomii), co oznacza stukrotne rozszerzenie, zanim kompresja na dobre się zacznie.

Lukę wyjaśniają dwa powody fizyczne, a jeden z nich pochodzi wprost z rozdziału 7.

Po pierwsze, **rzadkość wymusza rozszerzenie.** Rozdział 7 pokazał, że budżet energetyczny kory pozwala, żeby silnie aktywnych naraz było mniej niż jeden procent neuronów. Przedstawienie strumienia wzrokowego o dziesięciu milionach bitów na sekundę przy mniej niż jednym procencie aktywnych jednostek wymaga nieporównanie więcej neuronów niż kod gęsty i rozkłada ten sam sygnał na nadmiarowy, rzadki zbiór detektorów cech (7).

Po drugie, specyfikacja coś pominęła. Opisała *jedną* decyzję: jedno ustalone pytanie, zadawane strumieniowi co sekundę. Maszyna zbudowana do odpowiadania na jedno ustalone pytanie rzeczywiście może być maleńka i tania: czujnik ruchu, czujka dymu i detektor owadów u żaby to urządzenia tego rodzaju.

Układ wzrokowy zwierzęcia nie odpowiada na jedno pytanie. Z chwili na chwilę można mu zadać dowolne z ogromnej ich liczby: czy to twarz, czy jest gniewna, czy gałąź jest w zasięgu, czy owoc jest dojrzały, co mówi to słowo. Każde z nich to inna redukcja tych samych dziesięciu milionów bitów. Rozdział 5 pokazał, czego wymaga sprawne odpowiadanie na pytanie: wiedzy wstępnej, zmagazynowanej zawczasu. Umysł, który potrafi odpowiadać na wiele pytań, musi przechowywać wiedzę wstępną do nich wszystkich.

Specyfikacja potrzebuje więc czwartej liczby, której ramy rozdziału 12 jeszcze nie zawierają: **repertuaru**, czyli liczby różnych zadań, do których umysł musi być gotowy. A lekcję można sformułować jako regułę, która jest twierdzeniem teorii:

**Tempo wejścia zadania wyznacza szerokość wejścia umysłu. Kompresja wyznacza jego głębokość. Termin wyznacza jego rozmiar. Repertuar wyznacza jego masę.**

Większość mózgu to nie potok przetwarzania. To biblioteka.

Wynika z tego przewidywanie, które można sprawdzić w anatomii porównawczej. Dwa gatunki o podobnych oczach, a więc o podobnym tempie wejścia, powinny mieć podobną liczbę włókien nerwu wzrokowego, jakkolwiek różna jest ich inteligencja. Różnić się powinny tkanką za wejściem, proporcjonalnie do różnorodności tego, co robią z tym, co widzą. Liczba włókien powinna podążać za okiem, a liczba neuronów za trybem życia.

## Drugi projekt: kiedy odpowiedzią jest rój

Zmieńmy specyfikację, a zarys zmieni się razem z nią.

*Znajdź najlepsze z kilkunastu lub więcej możliwych miejsc na gniazdo, rozrzuconych po dziesiątkach kilometrów kwadratowych lasu. Każde miejsce trzeba odwiedzić i długo oglądać. Zły wybór jest śmiertelny. Decyzja w ciągu kilku dni to dość szybko.*

Krok 3 daje teraz zupełnie inną odpowiedź. Informacja nie napływa w jedno miejsce. Jest rozłożona na obszarze, którego nie obejmie żaden pojedynczy układ nerwowy, a zebranie jej oznacza, że trzeba tam polecieć. Czas przejścia wyznacza lot, dziesiątki minut. Ale termin to dni, więc liczba spójności jest wciąż wygodnie duża: jest czas na jakieś pięćdziesiąt przejść.

Na wyjściu jest garstka bitów, jeden wybór spośród kilkunastu, jeden raz. Nie trzeba szybkiego strumienia decyzji, więc nie jest wymagana scena.

Każde oględziny wymagają zdolnego obserwatora, który potrafi nawigować, ocenić dziuplę i zapamiętać drogę powrotną, więc każdy agent musi być bogaty. Bogaci agenci wysyłający krótkie raporty to, według rozdziału 8, zadatek na umysł sfederowany. A ponieważ zły wybór jest śmiertelny, projekt powinien przedkładać trafność nad szybkość i znosić utratę dowolnego osobnika: znowu sfederowany.

Zarys jest taki: **wielu ruchliwych, zdolnych agentów; kilka bitów na raport; brak centrum; decyzja przez powolne gromadzenie ze wzajemnym tłumieniem.** To rój pszczół miodnych z rozdziału 1, ze swoimi zwiadowczyniami i siedmiobitowymi tańcami (8, 9).

Oba projekty wyrażają główną myśl rozdziału. Ta sama teoria, dostawszy dwa różne zadania, zwraca dla jednego mózg, a dla drugiego rój. Żaden nie jest lepszym umysłem. Każdy jest kształtem swojego problemu.

## Mapa możliwych umysłów

Oba przykłady podsuwają mapę ogólną. Większość pracy wykonują dwie z czystych liczb: liczba spójności, która mówi, czy umysł nadąża za swoim światem, i liczba myślenia do mówienia, która mówi, czy jego agenci dzielą się większością tego, co obliczają.

| | Agenci dzielą się większością tego, co obliczają (zintegrowany) | Agenci dzielą się niewielką częścią (sfederowany) |
| --- | --- | --- |
| **Nadąża za swoim światem** | Mózgi. Szybkie, małe, szeregowe, zdolne być kimś. Odpowiednie do szybkich, lokalnych problemów. | Roje, kolonie, firmy, nauki. Powolne, duże, równoległe, odporne. Odpowiednie do rozległych, powolnych problemów. |
| **Za wolny na swój świat** | Nie trwa długo. Umysł zintegrowany, który nie nadąża, nic nie zyskuje na integracji, a płaci jej pełny koszt. | Nie jest umysłem. Tłum, rozproszony gatunek, cywilizacja rozciągnięta zbyt cienko: agenci, którzy dzielą kod, ale nie potrafią razem decydować. |

A jeden narożnik tej przestrzeni jest pusty z mocy prawa. Rozdział 8 doszedł do wniosku, że żaden umysł nie może być naraz duży, szybki i jednolity. W języku tego rozdziału zadanie, które wymaga szerokiego zasięgu, krótkiego terminu i jednego strumienia decyzji, nie ma rozwiązania. Nie spełnia go żadna morfologia. Praktyczna odpowiedź, w przyrodzie i w ludzkich organizacjach, jest zawsze taka sama: rozbić zadanie, tak żeby szybkie decyzje lokalne podejmowały małe umysły zintegrowane, a powolne globalne ich federacja.

## Puszczając to wstecz

To samo rozumowanie można poprowadzić w drugą stronę, od danego umysłu do zadań, które są poza jego zasięgiem. To także są przewidywania.

- **Rój nie złapie piłki** ani nie zrobi niczego innego, na co termin jest krótszy niż jego czas przejścia. Żadna liczba dodatkowych pszczół nie pomoże.
- **Jeden mózg nie przeszuka lasu.** Jego wejście ogranicza się do tego, co dociera w jedno miejsce.
- **Umysł sfederowany nie może doznać olśnienia**, w sensie przebudowania całego swojego obrazu za jednym zamachem, bo żadna jego część nie ma całego obrazu. Może się poprawiać tylko częściami. Komisja potrafi zredagować dokument, a nie potrafi go wymyślić.
- **Umysł zintegrowany nie może robić dwóch rzeczy naraz** na poziomie wyboru.
- **Ludzkość nie może odpowiedzieć jako jedność** na nic, co rozgrywa się szybciej niż jej własny czas przejścia, który w sprawach wymagających rzeczywistej zgody wciąż mierzy się w latach.
- **Umysł nie odpowie na pytanie, do którego brakuje mu wiedzy wstępnej**, szybciej, niż zdoła zebrać bity, jakakolwiek jest jego moc przerobowa. Zabrania tego górna granica z rozdziału 5.

## Co mógłby teraz zrobić inżynier umysłów

Jeśli te reguły obowiązują, stosują się do umysłów, które budujemy, tak samo jak do tych, które znajdujemy. Firma, program badawczy, służba ratunkowa i system sztucznych agentów to zbiorowości z zadaniem. Każdej można zadać sześć kroków.

- Jak szybko napływa informacja i ile musi wyjść? To wyznacza szerokość wejścia i głębokość hierarchii. Organizacja o zbyt małej liczbie poziomów jak na swoją kompresję topi swój szczyt w szczegółach. Organizacja o zbyt wielu poziomach jest powolna.
- Jaki jest termin? To wyznacza największą grupę, która może decydować jako jedność. Izba przyjęć musi być małym, zintegrowanym zespołem. Organem normalizacyjnym może być cały świat.
- Czy informacja jest w jednym miejscu, czy w wielu? Jeśli w wielu, niższe poziomy muszą być sfederowane, a ich raporty muszą być krótkie.
- Jak duży jest repertuar? To wyznacza, ile trzeba zmagazynować i wytrenować zawczasu, a to większość kosztu.
- Czy potrzebny jest jeden strumień decyzji? Jeśli tak, musi być jedna scena i będzie ona wąskim gardłem. Jeśli nie, nie należy jej budować.

Nic z tego nie jest nowe dla dobrego menedżera albo dobrego inżyniera systemów. Teoria dodaje, jeśli jest słuszna, twierdzenie, że nie są to reguły praktyczne. Są następstwami fizyki informacji i dałoby się je obliczyć. Następny rozdział stosuje je do umysłów, które właśnie powstają.

## W skrócie

- Ramy rozdziału 12 można puścić do przodu: od zadania do zarysu umysłu, który potrafi je wykonać.
- Dla zadania o dziesięciu milionach bitów na sekundę na wejściu i jednej decyzji na sekundę na wyjściu teoria daje około miliona powolnych kanałów wejściowych, od czterech do piętnastu poziomów, rozmiar od centymetrów do dziesiątek centymetrów w tkance nerwowej, moduły u dołu i jedną scenę u góry.
- Zgadza się to z układem wzrokowym człowieka pod siedmioma względami z dziewięciu, w tym co do liczby włókien nerwu wzrokowego, tempa, jakie każde przenosi, i liczby poziomów przetwarzania. Ta zgodność to sprawdzian spójności, a nie przewidywanie na ślepo.
- Chybia co do liczby neuronów i zużywanej mocy, tysiąckrotnie albo bardziej. Wynikają z tego dwie lekcje. Rzadka aktywność wymusza stukrotne rozszerzenie na pierwszym etapie korowym, zanim zacznie się jakakolwiek kompresja. A masę mózgu wyznacza jego repertuar, czyli liczba różnych pytań, na które musi być gotów odpowiedzieć. Większość mózgu to biblioteka, a nie potok przetwarzania.
- Dla zadania polegającego na powolnym przeszukiwaniu rozległego obszaru ze śmiertelnym kosztem błędu te same kroki dają rój.
- Umysły można nanieść na mapę za pomocą dwóch czystych liczb. Jeden obszar mapy, duży, szybki i jednolity, jest pusty.
- Reguły mówią też, czego każdy rodzaj umysłu nie potrafi, i można je stosować do organizacji i systemów sztucznych.

## Jak możemy się mylić

Ten rozdział stawia najłatwiejsze do sprawdzenia twierdzenia teorii. Zastosujmy sześć kroków do zwierząt, których anatomii nie sprawdzano zawczasu, oszacujmy tempo wejścia wzrokowego każdego gatunku na podstawie optyki jego oka i przewidźmy liczbę włókien w jego nerwie wzrokowym oraz liczbę etapów przed zachowaniem. Jeśli liczby włókien nie podążają za tempem wejścia albo podążają za nim przy tempie na włókno, które bardzo różni się między gatunkami, reguła szerokości wejścia jest błędna. Jeśli głębokość hierarchii zmysłowych nie ma związku z kompresją, którą wykonują, reguła głębokości jest błędna. Jeśli gatunki o podobnych oczach i bardzo różnych repertuarach zachowań mają podobną ilość mózgu wzrokowego, twierdzenie o repertuarze jest błędne. Jeśli znajdzie się zbiorowość, która decyduje jako jedność na odległości, jakiej jej sygnały nie mogą pokonać w jej terminie, reguła rozmiaru jest błędna, a wraz z nią duża część książki. A jeśli się okaże, że zarys umysłu zależy głównie od rzeczy, które specyfikacja pomija, od ewolucyjnego przypadku, od materiałów, od konkretnego algorytmu, to zadania nie wyznaczają morfologii, a pytanie inżyniera nie ma ogólnej odpowiedzi.

## Źródła

1. S. B. Laughlin, R. R. de Ruyter van Steveninck and J. C. Anderson (1998), "The metabolic cost of neural information", *Nature Neuroscience* 1:36–41. https://doi.org/10.1038/236
2. C. A. Curcio and K. A. Allen (1990), "Topography of ganglion cells in human retina", *Journal of Comparative Neurology* 300:5–25. https://pubmed.ncbi.nlm.nih.gov/2229487/
3. K. Koch, J. McLean, R. Segev, M. A. Freed, M. J. Berry, V. Balasubramanian and P. Sterling (2006), "How much the eye tells the brain", *Current Biology* 16:1428–1434. https://pmc.ncbi.nlm.nih.gov/articles/PMC1564115
4. D. J. Felleman and D. C. Van Essen (1991), "Distributed hierarchical processing in the primate cerebral cortex", *Cerebral Cortex* 1:1–47. https://chd.ucsd.edu/_files/fall2008/Felleman.1991.CC_Part1.pdf
5. H. Pashler (1994), "Dual-task interference in simple tasks: data and theory", *Psychological Bulletin* 116:220–244. https://pubmed.ncbi.nlm.nih.gov/7972591/
6. M. Meister and M. Tessier-Lavigne, "Low-level visual processing: the retina", w: E. R. Kandel et al. (eds), *Principles of Neural Science*, McGraw-Hill. https://www.weizmann.ac.il/brain-sciences/labs/ulanovsky/sites/neurobiology.labs.ulanovsky/files/uploads/chapter_22_low-level_visual_processing_the_retina.pdf
7. B. A. Olshausen and D. J. Field (1996), "Emergence of simple-cell receptive field properties by learning a sparse code for natural images", *Nature* 381:607–609. https://doi.org/10.1038/381607a0
8. T. D. Seeley, P. K. Visscher and K. M. Passino (2006), "Group decision making in honey bee swarms", *American Scientist* 94:220–229. https://bees.ucr.edu/media/156/download
9. R. Schürch and F. L. W. Ratnieks (2015), "The spatial information content of the honey bee waggle dance", *Frontiers in Ecology and Evolution* 3:22. https://www.frontiersin.org/articles/10.3389/fevo.2015.00022

Cała arytmetyka w krokach projektu jest nasza i zgrubna: liczba kanałów, liczba poziomów, ograniczenia rozmiaru, oszacowania mocy, liczby agentów i liczba neuronów pierwszorzędowej kory wzrokowej. Wartość dziesięciu bitów na sekundę dla oszczędnego kanału pochodzi z pomiarów z pozycji 3 i jest założeniem, gdy stosuje się ją gdzie indziej. Sześć kroków projektu, twierdzenie, że rzadkość wymusza rozszerzenie kory, reguła wiążąca tempo wejścia, kompresję, termin i repertuar z szerokością, głębokością, rozmiarem i masą umysłu, mapa możliwych umysłów oraz lista tego, czego każdy rodzaj nie potrafi, to twierdzenia teorii.
