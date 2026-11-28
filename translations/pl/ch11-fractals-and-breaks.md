<!-- Przekład pliku book/ch11-fractals-and-breaks.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 11. Fraktale i pęknięcia

## Jak długie jest wybrzeże Wielkiej Brytanii?

W latach pięćdziesiątych XX wieku angielski matematyk Lewis Fry Richardson badał, czy kraje o dłuższych wspólnych granicach częściej toczą ze sobą wojny. Sprawdzał długości granic i stwierdził, że publikowane liczby skrajnie się różnią. Hiszpania i Portugalia, na przykład, podawały całkiem różne długości tej samej granicy.

Richardson znalazł powód. Długość krętej linii zależy od długości linijki. Zmierz wybrzeże Wielkiej Brytanii linijką stukilometrową, a pominiesz zatoki. Użyj dziesięciokilometrowej, a pójdziesz wzdłuż zatok, ale pominiesz zatoczki. Użyj metrówki, a pójdziesz wzdłuż każdej skały. Im krótsza linijka, tym dłuższe wybrzeże, bez końca.

W 1967 roku Benoit Mandelbrot zamienił ten kłopot w odkrycie. Linia brzegowa, zauważył, jest statystycznie samopodobna: każdy mały odcinek wygląda jak pomniejszona kopia całości. Taka krzywa jest zbyt pomarszczona, żeby być jednowymiarową linią, i zbyt cienka, żeby być dwuwymiarową powierzchnią. Można jej przypisać wymiar pośredni i z danych Richardsona Mandelbrot odczytał wartość około 1,25 dla zachodniego wybrzeża Wielkiej Brytanii (1). Później nazwał takie kształty fraktalami.

Dla nas liczy się tu lekcja o linijkach. W przypadku fraktala pytanie „jaki jest długi?” nie ma odpowiedzi, dopóki nie powiemy, w jakiej skali patrzymy. Ta książka zadaje podobne pytanie o umysły: ilu to agentów? Mózg to 86 miliardów neuronów albo kilkaset obszarów, albo dwie półkule, albo jeden człowiek. Rozdział 3 powiedział, że agenci się zagnieżdżają, i obiecał sposób, żeby naturalne poziomy znajdować, a nie wybierać ręcznie. Ten rozdział spełnia obietnicę. Metoda ma dwie połowy. Tam, gdzie umysł wygląda tak samo w każdej skali, jest fraktalem, a to mówi nam, że jest jednym układem. Tam, gdzie ta jednakowość pęka, zaczyna się nowy rodzaj agenta.

## Umysły bez skali

Zacznijmy od jednakowości. Kilka umysłów z tej książki, kiedy się je zmierzy, okazuje się nie mieć wyróżnionej skali.

**Lawiny.** Rozdział 3 opisał serie aktywności rozchodzące się po skrawkach kory. Mają wszelkie rozmiary, od kilku neuronów po cały skrawek, a liczba lawin maleje z rozmiarem wzdłuż linii prostej na wykresie logarytmicznym, bez typowego rozmiaru gdziekolwiek (2). To samopodobieństwo w czasie i w aktywności.

**Okablowanie.** Sieci mózgu są modularne, a moduły same składają się z mniejszych modułów, które znów składają się z mniejszych: moduły w modułach, na kilku poziomach (3). Rozdział 4 wspomniał, że mózgi i układy scalone podlegają tej samej regule wiążącej rozmiar obszaru z liczbą wychodzących z niego połączeń. Ta reguła, reguła Renta, jest stwierdzeniem, że okablowanie jest samopodobne: mały blok i duży blok mają tę samą relację między wnętrzem a zewnętrzem (4). Wykładnik tej reguły działa jak wymiar sieci i dla mózgu człowieka jest większy niż trzy: sieć jest połączona bogaciej, niż mógłby być jakikolwiek układ zamknięty w przestrzeni trójwymiarowej z samymi połączeniami lokalnymi, i dlatego potrzebuje długich kabli z rozdziału 7 (4).

**Społeczeństwa.** Ludzkie grupy społeczne występują w warstwach liczących mniej więcej 5, 15, 50 i 150 osób i tak dalej, każda około trzech razy większa od poprzedniej (5). Stały stosunek z warstwy na warstwę to kolejna postać samopodobieństwa. Oddal obraz trzykrotnie, a wzór się powtórzy.

**Stada.** Najpiękniejszy przypadek jest na niebie nad Rzymem. Każdego zimowego wieczoru tysiące szpaków krążą nad miastem w stadach, które skręcają i przelewają się jak jedno ciało. Andrea Cavagna, Irene Giardina i ich współpracownicy fotografowali te stada z kilku kierunków naraz i odtworzyli położenie i prędkość każdego ptaka. Każdy szpak, jak ustalili wcześniej, zwraca uwagę tylko na garstkę najbliższych sąsiadów, około siedmiu (6). A jednak kiedy zmierzyli, na jaką odległość skorelowane są *fluktuacje* prędkości ptaków, odpowiedzią nie było siedem ptaków ani siedemdziesiąt. Zasięg korelacji rósł proporcjonalnie do rozmiaru stada. W stadzie dwa razy szerszym skorelowane obszary były dwa razy szersze (7). Nie ma charakterystycznej odległości, powyżej której ptaki przestają na siebie wpływać. Zmianę w locie jednego ptaka odczuwa, przez łańcuch sąsiadów, każdy inny ptak, jakkolwiek duże jest stado.

To właśnie znaczy, w liczbach, „być jednej myśli”. Rozdział 9 powiedział, że zbiorowość działa jako jedność, gdy jej sygnały wewnętrzne wyprzedzają świat. Stado pokazuje przestrzenną stronę tego samego warunku: **zbiorowość jest jednym układem, gdy korelacje jej fluktuacji sięgają tak daleko jak ona sama.** Słowo *fluktuacje* jest tu zasadnicze. W napadzie padaczkowym albo w krysztale każda jednostka porusza się sztywnym równym krokiem, bez miejsca na różnice. W stadzie szpaków całość obejmuje *zdolność reagowania*: odchylenie od średniego lotu u jednego ptaka przechodzi falą przez całą grupę. Gdyby długość korelacji była ustalona na, powiedzmy, dwadzieścia metrów, stumetrowe stado byłoby pięcioma stadami lecącymi w szyku. Ponieważ skaluje się ze stadem, stado jest jedno.

## Dlaczego umysł miałby być fraktalem

Dwa argumenty z wcześniejszych rozdziałów wyjaśniają, dlaczego umysły powinny tak wyglądać. Oba są odczytaniem ustalonych wyników przez teorię.

Pierwszy to krytyczność. Rozdział 3 dowodził, że umysły żyją na granicy między porządkiem a nieporządkiem, a układ na takiej granicy nie ma skali charakterystycznej: to niemal definicja punktu krytycznego. Bezskalowe korelacje stada i lawiny w korze to ten sam znak rozpoznawczy. Badacze szpaków sami wyciągnęli ten wniosek: stada zachowują się jak układy krytyczne, ustawione tak, by jak najsilniej reagować na zaburzenie, takie jak sokół (7).

Drugi to oszczędność. Rozdziały 4 i 7 pokazały, że rosnący umysł nie może połączyć wszystkiego ze wszystkim. Wymiana w poprzek jest droga i źle się skaluje. Najtańszy sposób, żeby duży układ pozostał połączony, to zbudować go z modułów, połączyć moduły rzadko w większe moduły i powtórzyć. Powtarzanie reguły w każdej skali jest tym, co tworzy fraktal.

Jest i trzeci argument, starszy od obu, o tym, jak takie rzeczy w ogóle powstają. W 1962 roku ekonomista i informatyk Herbert Simon opowiedział przypowieść o dwóch zegarmistrzach, Horze i Tempusie. Każdy robił zegarki z tysiąca części i każdemu często przeszkadzał telefon. Tempus składał swoje zegarki część po części i ilekroć odkładał zegarek, żeby odebrać telefon, ten się rozpadał i trzeba było zaczynać od nowa. Hora budował swoje ze stabilnych podzespołów po dziesięć części, a te łączył w większe zespoły po dziesięć, więc przerwa kosztowała go tylko trochę pracy. Hora prosperował, a Tempus zbankrutował (8). Simon wyciągnął wniosek, że złożone układy, które ewoluują, będą niemal zawsze hierarchiami stabilnych podzespołów, bo nic innego nie przetrwa przerw. Ewolucja to zegarmistrz, któremu wciąż się przeszkadza.

Zagnieżdżanie się umysłów nie jest więc faktem ozdobnym. Dynamika krytyczna, koszty okablowania i potrzeba budowania krok po kroku popychają w tę samą stronę: ku układom zbudowanym z układów zbudowanych z układów.

## Gdzie wzór pęka

Doskonały fraktal byłby dla tej teorii bezużyteczny. Gdyby umysł wyglądał tak samo w każdej skali aż do samego dołu, nie byłoby w nim w ogóle poziomów, ani neuronów, ani ludzi, tylko zmarszczki. Rzeczywiste umysły takie nie są. Wybrzeże Wielkiej Brytanii jest samopodobne od setek kilometrów do metrów, ale nikt nie sądzi, że jest samopodobne aż do atomu. Gdzieś skały przestają być linią brzegową i stają się kryształami, a reguły się zmieniają.

Ta zmiana to druga połowa metody. **Tam, gdzie prawo skalowania się zagina, zaczyna się nowy rodzaj agenta.**

Najwyraźniejszy przykład to zużycie energii przez istoty żywe. U zwierząt tempo metabolizmu, jak wiadomo, rośnie wolniej niż masa ciała, mniej więcej jak jej potęga trzy czwarte: słoń spala na kilogram o wiele mniej niż mysz. Długo zakładano, że jakieś takie prawo obowiązuje w całym świecie żywym. W 2010 roku John DeLong ze współpracownikami zebrał dane z całego zakresu i znalazł trzy prawa, a nie jedno. U bakterii i innych prokariontów tempo metabolizmu rośnie *szybciej* niż masa. U organizmów jednokomórkowych z jądrem, protistów, rośnie wprost proporcjonalnie. Dopiero u zwierząt wielokomórkowych rośnie wolniej (9). Pęknięcia wypadają dokładnie na wielkich przejściach w historii życia: tam, gdzie proste komórki połączyły się w złożone, i tam, gdzie złożone komórki połączyły się w ciała.

Te przejścia są, w języku tej książki, punktami, w których agenci jednego poziomu stali się częściami agenta na następnym. Prawo skalowania odnotowuje każde jako załamanie. Ktoś, kto nie wiedziałby nic o biologii, a dostałby tylko wykres energii względem masy, mógłby zaznaczyć, gdzie kończy się jeden rodzaj osobnika, a zaczyna drugi.

Miasta dają drugi przykład i niespodziankę. Luís Bettencourt, Geoffrey West i ich współpracownicy zmierzyli, jak własności miast zmieniają się z liczbą ludności. Drogi, kable i stacje benzynowe rosną wolniej niż ludność, z wykładnikiem około 0,8: większe miasto potrzebuje mniej infrastruktury na głowę, tak jak większe zwierzę potrzebuje mniej energii na kilogram. Ale płace, patenty i inne miary bogactwa i wynalazczości rosną *szybciej* niż ludność, z wykładnikiem około 1,2 (10). I o ile większe zwierzę żyje wolniej, o tyle większe miasto żyje szybciej: tempo życia przyspiesza z rozmiarem (10).

Rozdział 4 powiedział, że rozmiar kosztuje czas. Miasta zdają się łamać tę regułę. Odpowiedź teorii pochodzi z rozdziału 8, z ważnym zastrzeżeniem. Rozmiar kosztuje czas w przypadku umysłu, który musi działać jako całość, bo sygnał musi przez niego przejść. Zwierzę jest zintegrowane, a jego serce musi zaopatrzyć każdą komórkę. Miasto jest sfederowane i otwarte: nic nie musi przejść przez całe miasto, żeby na jednym rogu ulicy doszło do spotkania, a z rozmiarem rośnie gęstość lokalnych spotkań. A jednak nie każdy umysł sfederowany przyspiesza z rozmiarem: kolonie owadów społecznych skalują się podliniowo, jak pojedyncze organizmy, a w olbrzymich dziedzinach nauki obrót pojęć zwalnia, gdy uwaga się nasyca (zob. *Jak możemy się mylić*). Doprecyzowana hipoteza, którą trzeba sprawdzić, brzmi: **otwarte, niehierarchiczne, mieszające się federacje przyspieszają z rozmiarem, natomiast umysły zintegrowane oraz federacje, których wąskim gardłem jest transport albo uwaga, zwalniają.**

## Jak znaleźć agenta

Złóżmy obie połowy, a wyjdzie procedura, którą może zastosować każdy, kto ma dane.

1. Wybierz coś, co da się zmierzyć w wielu skalach: ruch wychodzący z obszaru względem rozmiaru obszaru, korelację względem odległości, aktywność względem rozmiaru grupy.
2. Wykreśl to względem skali, na osiach logarytmicznych.
3. Tam, gdzie punkty leżą na linii prostej, układ jest samopodobny. W tym zakresie skal jest jednym rodzajem rzeczy, zorganizowanym przez jedną regułę.
4. Tam, gdzie linia się zagina, reguła się zmienia. Ta skala jest granicą między poziomami. Poniżej są agenci, powyżej zbiorowość, którą tworzą.

Fizyka ma głębszą wersję tej samej idei, zwaną grupą renormalizacji, za którą Kenneth Wilson otrzymał Nagrodę Nobla (11). Jej procedura polega na oglądaniu układu przez coraz grubsze soczewki. Zastąp każdy mały blok układu jedną wartością streszczającą, potem zrób to samo z blokami bloków i patrz, jak zmienia się opis. Większość szczegółów się rozmywa. Kilka wielkości przeżywa każdy krok i tych kilka to wszystko, co większa skala kiedykolwiek musi wiedzieć o mniejszej.

Czytelnicy rozdziału 8 to rozpoznają. To lejek. Chmura molekularnych szczegółów neuronu zostaje streszczona jako impuls. Milion neuronów pszczoły zostaje streszczony jako siedmiobitowy taniec. Miliard bitów na sekundę u człowieka zostaje streszczony jako głos albo zakup. Przyroda wykonuje gruboziarniste uśrednianie fizyka naprawdę, na każdej granicy między poziomami.

Daje to teorii definicję poziomu, obiecaną w rozdziale 3. **Agent to skala, w której wystarcza streszczenie.** To blok świata, którego wpływ na wszystko poza nim da się ująć w wiadomości o wiele mniejszej niż jego stan wewnętrzny. Tam, gdzie żadne małe streszczenie nie wystarcza, nie ma granicy, a to, co wyglądało na dwie rzeczy, jest jedną. Tam, gdzie małe streszczenie wystarcza, jest agent, a prawa skalowania zaginają się, żeby to pokazać.

## Co z tego wynika

- Każda granica między poziomami umysłu powinna ujawniać się jako pęknięcie w jakimś prawie skalowania: w okablowaniu, w korelacji albo w przepływie informacji. Mózg powinien wykazywać jedno między neuronem a lokalnym obwodem, a kolejne w skali obszarów i półkul.
- W obrębie jednego poziomu zdrowa zbiorowość powinna mieć korelacje sięgające na całą jej rozciągłość, tak jak stado. Zbiorowość, której długość korelacji jest krótsza niż jej rozmiar, już rozpadła się na kilka, cokolwiek mówi jej nazwa albo jej granice. Daje to pytaniu rozdziału 9, jeden umysł czy dwa, pomiar.
- Mniej więcej trzykrotny stosunek między warstwami ludzkich grup powinno się dać wyjaśnić kosztami komunikacji, a podobne stałe stosunki powinny pojawiać się między poziomami innych umysłów sfederowanych.
- Wytwory zbiorowości sfederowanych powinny rosnąć szybciej niż ich liczebność, a zintegrowanych wolniej.
- Propozycja rozdziału 16, żeby zarejestrować ludzkość jak mózg, zyskuje pierwszy krok: wykreślić, jak korelacje aktywności maleją z odległością, w przestrzeni i w języku. Jeśli leżą na jednej linii od wiosek po kontynenty, ludzkość jest jednym układem. Jeśli linia zagina się w skali wspólnoty językowej, tam są jej agenci.

## W skrócie

- Fraktal nie ma wyróżnionej skali: każda część przypomina całość. W przypadku takiego obiektu pomiary zależą od skali linijki.
- Umysły są fraktalne pod wieloma względami. Lawiny neuronalne, zagnieżdżone moduły i okablowanie mózgów, warstwy ludzkich grup i korelacje w stadach szpaków nie mają skali charakterystycznej.
- W stadzie szpaków każdy ptak obserwuje około siedmiu sąsiadów, a mimo to korelacje obejmują całe stado, jakkolwiek duże. Zbiorowość jest jednym układem, gdy jej korelacje sięgają tak daleko jak ona sama.
- Krytyczność, koszt okablowania i potrzeba składania ze stabilnych części popychają umysły ku strukturze zagnieżdżonej i samopodobnej.
- Poziomy ujawniają się tam, gdzie samopodobieństwo pęka. Skalowanie metabolizmu zmienia się przy każdym wielkim przejściu w historii życia. Miasta, inaczej niż zwierzęta, przyspieszają i stają się bardziej wynalazcze w przeliczeniu na głowę, gdy rosną.
- Twierdzenia teorii: pęknięcie w prawie skalowania oznacza granicę między poziomami; agent to skala, w której wystarcza streszczenie; zbiorowości zintegrowane zwalniają z rozmiarem, podobnie jak federacje ograniczone transportem lub uwagą, takie jak kolonie owadów i bardzo duże dziedziny nauki; otwarte federacje, których członkowie swobodnie się mieszają, takie jak miasta, przyspieszają.

## Jak możemy się mylić

Prawa potęgowe łatwo zobaczyć, a trudno udowodnić. Wiele opublikowanych linii prostych na wykresach logarytmicznych obejmuje zakres zbyt wąski, żeby wykluczyć inne krzywe, a niektóre rzekomo bezskalowe wzory nie przetrwały lepszej statystyki. Jeśli przytoczone tu prawa dla lawin i okablowania okażą się nie być prawdziwymi prawami potęgowymi, fraktalna połowa rozdziału słabnie, choć metoda szukania pęknięć by pozostała. Twierdzenie, że pęknięcia oznaczają granice między poziomami, upadłoby, gdyby znane granice, takie jak między komórką a organizmem albo człowiekiem a grupą, nie wykazywały zmiany w żadnej zależności skalowania albo gdyby ostre pęknięcia pojawiały się tam, gdzie nie ma żadnego nowego rodzaju agenta. Wynik dotyczący miast kwestionowano na tej podstawie, że wykładniki zależą od tego, jak wytyczy się granice miasta. Co więcej, dwie sztandarowe zbiorowości sfederowane z tej książki już teraz podważają każdą prostą regułę, zgodnie z którą wszystkie federacje przyspieszają: całe kolonie owadów społecznych skalują się podliniowo pod względem tempa metabolizmu, podobnie jak pojedyncze organizmy (12), a analiza 90 milionów artykułów naukowych wykazała, że postęp pojęciowy zwalnia i kostnieje, gdy dziedziny stają się bardzo duże (13). Wykładnik skalowania odzwierciedla zatem geometrię sieci i wąskie gardła, a nie samą federację.

## Źródła

1. B. B. Mandelbrot (1967), "How long is the coast of Britain? Statistical self-similarity and fractional dimension", *Science* 156:636–638. https://ui.adsabs.harvard.edu/abs/1967Sci...156..636M/abstract
2. J. M. Beggs and D. Plenz (2003), "Neuronal avalanches in neocortical circuits", *Journal of Neuroscience* 23:11167–11177. https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045
3. D. Meunier, R. Lambiotte and E. T. Bullmore (2010), "Modular and hierarchically modular organization of brain networks", *Frontiers in Neuroscience* 4:200. https://doi.org/10.3389/fnins.2010.00200
4. D. S. Bassett et al. (2010), "Efficient physical embedding of topologically complex information processing networks in brains and computer circuits", *PLOS Computational Biology* 6:e1000748. https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671
5. W.-X. Zhou, D. Sornette, R. A. Hill and R. I. M. Dunbar (2005), "Discrete hierarchical organization of social group sizes", *Proceedings of the Royal Society B* 272:439–444. https://pmc.ncbi.nlm.nih.gov/articles/PMC1634986/
6. A. Cavagna et al. (2009), "Scale-free correlations in bird flocks", arXiv:0911.4393, z powołaniem na wcześniejszy wynik tej grupy o oddziaływaniu z około siedmioma sąsiadami. https://www.arxiv.org/pdf/0911.4393
7. A. Cavagna, A. Cimarelli, I. Giardina, G. Parisi, R. Santagati, F. Stefanini and M. Viale (2010), "Scale-free correlations in starling flocks", *PNAS* 107:11865–11870. https://pmc.ncbi.nlm.nih.gov/articles/PMC2900681
8. H. A. Simon (1962), "The architecture of complexity", *Proceedings of the American Philosophical Society* 106:467–482.
9. J. P. DeLong, J. G. Okie, M. E. Moses, R. M. Sibly and J. H. Brown (2010), "Shifts in metabolic scaling, production, and efficiency across major evolutionary transitions of life", *PNAS* 107:12941–12945. https://pmc.ncbi.nlm.nih.gov/articles/PMC2919978
10. L. M. A. Bettencourt, J. Lobo, D. Helbing, C. Kühnert and G. B. West (2007), "Growth, innovation, scaling, and the pace of life in cities", *PNAS* 104:7301–7306. https://pmc.ncbi.nlm.nih.gov/articles/PMC1852329
11. K. G. Wilson (1975), "The renormalization group: critical phenomena and the Kondo problem", *Reviews of Modern Physics* 47:773–840.
12. C. Hou, M. Kaspari, H. B. Vander Zanden and J. F. Gillooly (2010), "Energetic basis of colonial living in social insects", *PNAS* 107:3634–3638. https://doi.org/10.1073/pnas.0908071107
13. J. S. G. Chu and J. A. Evans (2021), "Slowed canonical progress in large fields of science", *PNAS* 118:e2021636118. https://doi.org/10.1073/pnas.2021636118

Prace Richardsona o granicach opisano za relacją Mandelbrota. Odczytania bezskalowej korelacji jako znaku jednego układu, pęknięć skalowania jako granic między poziomami, lejka jako gruboziarnistego uśredniania dokonywanego przez przyrodę, definicja agenta jako skali, w której wystarcza streszczenie, oraz proponowana różnica w skalowaniu między zbiorowościami zintegrowanymi a sfederowanymi to twierdzenia teorii.
