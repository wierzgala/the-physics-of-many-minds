<!-- Przekład pliku book/ch05-how-much-does-a-mind-need-to-know.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 5. Ile umysł musi wiedzieć?

## Dwadzieścia pytań

W starej grze towarzyskiej jeden gracz myśli o jakiejś rzeczy, a drugi ma dwadzieścia pytań typu „tak czy nie”, żeby odgadnąć, co to jest. Dzieci grają w nią źle. *Czy to żyrafa? Czy to mój but?* Każde z tych pytań, jeśli odpowiedź brzmi „nie”, wyklucza jedną rzecz w świecie, w którym są ich miliony.

Dobry gracz pyta *Czy to jest żywe?* i jednym słowem wyrzuca pół świata. Potem połowę tego, co zostało, i znów połowę. Dwadzieścia doskonałych połowień wyłania jeden przedmiot spośród 2²⁰, czyli nieco ponad miliona. Dobry gracz i dziecko otrzymują dokładnie tyle samo odpowiedzi. Jedno z nich zachodzi milion razy dalej.

Tę różnicę ten rozdział proponuje nazwać inteligencją. Nie chodzi o to, ile gracz wie na końcu. Oboje w końcu poznają odpowiedź, jeśli dziecku pozwolić na dość pytań. Chodzi o to, jak mało trzeba było każdemu z nich powiedzieć.

## Czytelnik, który już zna książkę

Claude Shannon zamienił pewną odmianę tej gry w eksperyment. Pokazywał ludziom fragment angielskiego tekstu z zakrytą resztą i prosił, żeby zgadywali następną literę, potem kolejną, i liczył ich próby. Gdyby czytelnicy nie wiedzieli nic, każda litera kosztowałaby ich około 4,7 bita, czyli tyle, ile wybór jednej z 26. W rzeczywistości potrzebowali czegoś rzędu jednego bita na literę. Granice Shannona wynosiły od 0,6 do 1,3 bita (1, 2). Około trzech czwartych pisanej angielszczyzny jest nadmiarowe dla kogoś, kto zna angielski (1).

Tekst się nie zmienił. Tanim uczynił go czytelnik. Umysł mający dobry model swojego świata potrzebuje bardzo niewielu bitów, żeby nadążać za tym, co dzieje się dalej, bo większość już przewidział. Rozdział 6 znajdzie ten sam fakt między ludźmi. Tutaj pojawia się on wewnątrz jednej głowy.

Podsuwa to definicję.

> Inteligencja układu to jego osiągnięcie podzielone przez informację, której musiał użyć.

Będziemy ją zapisywać jako η (eta), zwykłym symbolem sprawności. Mianownik ułamka mierzy się w bitach i ta część nie podlega negocjacjom. Licznik jest kwestią wyboru i jeszcze do niego dojdziemy.

## Dziecko i maszyna

Definicja daje niewygodne przewidywanie co do naszej własnej techniki i to przewidywanie jest trafne.

Dziecko zaczyna mówić płynnie po usłyszeniu od dziesiątek do setek milionów słów. Duży model językowy osiąga płynność po setkach miliardów do bilionów (3). Między takimi modelami a dziećmi przepaść wynosi cztery lub pięć rzędów wielkości, a między modelami a nawet najbardziej oczytanymi dorosłymi co najmniej trzy (4). Według miary proponowanej tutaj, w tym jednym zadaniu, dziecko jest od dziesięciu tysięcy do stu tysięcy razy inteligentniejsze niż maszyna. Maszyna jest oczywiście pod innymi względami nieporównanie zdolniejsza. Sens definicji polega na tym, że zdolność i inteligencja to różne rzeczy.

Co dziecko zatrzymuje z całego tego słuchania? Dwóch badaczy postanowiło to policzyć, sumując to, co użytkownik języka musi wiedzieć o dźwiękach, słowach, znaczeniach i gramatyce. Ich najlepsze oszacowanie wyniosło około 12,5 miliona bitów, mniej więcej 1,5 megabajta, tyle co jedna fotografia (5). Daje to ponad tysiąc bitów przyswajanych codziennie przez osiemnaście lat (5). Większość to znaczenia słów. Reguły gramatyki, o które językoznawcy spierają się od stu lat, zajęły około 700 bitów (5).

Zestawmy to z wejściem. Sto milionów słów to kilkaset milionów bitów, nawet według stawki Shannona. Tylko kilka procent tego, co dziecko słyszy, zostaje więc jako znajomość języka (nasze oszacowanie). Dziecko nie jest magnetofonem. Jest graczem w dwadzieścia pytań, który wydobywa nieliczne ważne bity ze strumienia złożonego głównie z rzeczy, które i tak mógłby odgadnąć.

Ten sam wzór widać wszędzie tam, gdzie bezpośrednio porównywano ludzi i uczące się maszyny.

- **Często wystarcza jeden przykład.** Pokaż człowiekowi jeden przykład nowego rodzaju przedmiotu, na przykład nieznany odręczny znak albo dziwny dwukołowy pojazd, a uchwyci kategorię. Standardowe algorytmy uczące się potrzebowały do tego dziesiątek albo setek przykładów (6).
- **Mistrzostwo przez toporne powtarzanie.** Program AlphaGo Zero został najsilniejszym graczem w go w dziejach, grając sam ze sobą. W ciągu pierwszych trzech dni rozegrał 4,9 miliona partii (7). Zawodowy gracz rozgrywa ich w życiu kilkadziesiąt tysięcy (nasze oszacowanie). Program jest silniejszy. Dostał też sto żywotów treningu.

I nie chodzi tu o wielkość mózgu. Pszczoła miodna, mająca niespełna milion neuronów, potrafi nauczyć się abstrakcyjnych pojęć *taki sam* i *inny*. Pszczoły wytrenowane, by wybierać wzór pasujący do próbki, stosowały potem tę regułę do bodźców, których nigdy nie widziały, a nawet do innego zmysłu (8). Owad wydobył pojęcie z garstki prób. Cokolwiek mierzy η, nie jest to ilość sprzętu.

## Trzy rodzaje bitów

Zanim zaczniemy za bardzo podziwiać dziecko, musimy uczciwie zrobić rachunek. Informacja dociera do umysłu trzema drogami i wszystkie trzy należą do mianownika ułamka.

**Doświadczenie**: bity, które wchodzą przez zmysły w ciągu życia. To owe sto milionów słów.

**Wiedza wstępna**: bity, z którymi umysł zaczyna. Dziecko nie przyszło puste. Przyszło z genomem liczącym około trzech miliardów liter (9), wynikiem ogromnych poszukiwań prowadzonych przez jego przodków, a ten genom buduje mózg już przygotowany do znajdowania słów, twarzy i przyczyn. Maszyna zaczynała prawie bez niczego w tym rodzaju. Część przewagi dziecka to rzeczywista sprawność. Część to spadek.

**Komunikacja**: w przypadku umysłu złożonego z wielu agentów są to bity, które agenci muszą wymienić, żeby wykonać zadanie. To ten składnik liczy się dla rojów, zespołów i społeczeństw z tej książki, a żadna teoria inteligencji jednostkowej go nie uwzględnia.

Wystarczy pominąć którykolwiek z tych trzech rodzajów, a miarę da się oszukać. Tabela, która wymienia odpowiedź na każde pytanie egzaminacyjne, zdobędzie komplet punktów, niczego się nie ucząc: cała jej inteligencja tkwi w wiedzy wstępnej, włożonej tam przez tego, kto tabelę napisał. Informatyk François Chollet dobitnie wyłożył tę myśl w 2019 roku. Samo mierzenie umiejętności, dowodził, nie jest jeszcze mierzeniem inteligencji, bo nieograniczona wiedza wstępna albo nieograniczone dane treningowe pozwalają eksperymentatorowi po prostu kupić dowolny poziom umiejętności. Zaproponował, żeby inteligencję zdefiniować jako sprawność, z jaką układ nabywa nowe umiejętności, z uwzględnieniem jego wiedzy wstępnej i doświadczenia (10). Ten rozdział bierze jego propozycję, nadaje jej jednostki i dodaje trzeci rodzaj bitów.

## Co idzie do licznika

Teraz licznik ułamka. Są trzy rozsądne wybory i każdy daje inteligencji inną jednostkę.

**Liczyć to, co osiągnięto.** Rozwiązane zadania, ważone tym, jak były trudne i jak nowe. Wtedy η mierzy się w osiągnięciach na bit. To wersja najbardziej intuicyjna i najtrudniejsza do uściślenia, bo ktoś musi ustalić wagi.

**Liczyć wydobytą pracę.** Rozdział 2 opisał silnik Szilárda, który zamienia jeden bit wiedzy w ustaloną ilość energii. Umysł można by oceniać według użytecznej pracy, jaką uzyskuje ze świata na każdy bit, którego się dowiaduje. Istnieje piękna wersja tego dla pieniędzy. W 1956 roku John Kelly, kolega Shannona, rozważył gracza, który dostaje typy przez zaszumioną linię telefoniczną. Udowodnił, że największe tempo, w jakim może rosnąć kapitał gracza, jest dokładnie równe tempu, w jakim przez linię napływa informacja (11). Bity stają się majątkiem po stałym kursie i żadna strategia obstawiania go nie pobije.

**Liczyć usuniętą niepewność.** Mierzyć licznik także w bitach: o ile umysł zawęził stan świata albo przesterował go w stronę celu. Wtedy η to bity na bit, czysta liczba. I dla tej wersji istnieje twierdzenie. Touchette i Lloyd udowodnili, że na każdy bit, który sterownik zbierze o układzie, może on zmniejszyć nieuporządkowanie tego układu najwyżej o jeden bit więcej, niż potrafiłby na ślepo (12).

Ta książka przyjmuje trzeci wybór, właśnie z powodu tego twierdzenia. Znaczy ono, że **inteligencja, właściwie zmierzona, ma maksimum i to maksimum wynosi jeden.** Doskonały gracz w dwadzieścia pytań znajduje się dokładnie na granicy: jeden bit świata rozstrzygnięty na każdy otrzymany bit. Nic nie może wypaść lepiej.

## Następstwa górnej granicy

To stwierdzenie mocniejsze, niż wygląda, a to, co z niego wynika, jest twierdzeniem samej teorii.

**Istnieje coś takiego jak inteligencja doskonała i nie jest ona daleko.** W danym problemie umysł jest doskonale inteligentny wtedy, gdy nie marnuje niczego z tego, czego się dowiaduje. Ludzie grający w dwadzieścia pytań są tego blisko. Podobnie dobry lekarz, który wybiera, jakie badanie zlecić. Doskonałość w tym sensie nie jest własnością bogów. Jest własnością dobrze dobranych pytań.

**Superinteligencja nie może być mądrzejsza w przeliczeniu na bit niż doskonały człowiek.** Jeśli górna granica wynosi jeden, umysł daleko wykraczający poza nasz nie wydobędzie dwóch bitów sterowania z jednego bitu informacji wzajemnej zebranej o swoim świecie. Może zrobić tylko cztery rzeczy: zbierać więcej bitów, a to jest moc przerobowa, temat rozdziału 7; zaczynać z lepszą wiedzą wstępną; lepiej wybierać, które bity zbierać; albo dzięki głębszym obliczeniom odblokować więcej informacji już zakopanej w istniejących danych. Ten czwarty punkt jest ważny: skończony umysł rzadko wydobywa całą informację Shannona, którą jego dane już zawierają, więc większa głębia obliczeń może wyglądać jak magia, pozostając ściśle poniżej granicy równej jeden. Teoria czysto rozdziela moc przerobową i sprawność, tak jak inżynier oddziela wielkość silnika od jego sprawności: **to, co umysł może zrobić, jest jego mocą przerobową pomnożoną przez jego η.**

**Ciekawość jest silnikiem sprawności.** Pytanie dziecka *czy to żyrafa?* i pytanie dorosłego *czy to jest żywe?* kosztują tyle samo, a są warte skrajnie różne kwoty. Umysł podnosi swoje η nie przez intensywniejsze myślenie o odpowiedziach, lecz przez wybieranie pytań, na które odpowiedzi nie potrafi przewidzieć. Takim pytaniem jest eksperyment w laboratorium. Jest nim też lot pszczoły zwiadowczyni w miejsce, w którym nie była żadna pszczoła. W tym ujęciu ciekawość nie jest ozdobą inteligencji. Jest sposobem, w jaki inteligencję się uprawia.

**Rozumienie to kompresja.** Umysł, który potrzebuje mniej bitów, żeby nadążać za światem, to umysł mający krótszy opis świata. Czytelnicy Shannona potrzebowali jednego bita na literę, bo nosili angielszczyznę w głowach. Rozumieć coś to umieć to tanio przewidywać. Uczona, która zastępuje tabelę dziesięciu tysięcy pomiarów jednym równaniem, nie tylko posprzątała. Według definicji z tej książki stała się inteligentniejsza w odniesieniu do tej części świata, a wraz z nią każdy, komu o tym powie.

**Większości twojej inteligencji nauczył się ktoś inny.** Ta ostatnia uwaga znaczy więcej, niż się wydaje. Prawa Newtona mieszczą się w kilkuset bitach. Ich znalezienie kosztowało ludzkość stulecia. Uczeń dostaje je w jedno popołudnie. Każdy żyjący człowiek otrzymuje wiedzę wstępną, w genach i w kulturze, której nigdy nie zdobyłby sam, a rachunek η mówi wprost, skąd bierze się pozorna błyskotliwość człowieka: w przeważającej mierze stąd, że mianownik ułamka opłacili inni. Rozdział 6 nazywa to wspólnym kontekstem, a rozdział 9 będzie dowodził, że to z tego powodu jeden gatunek zaczął rządzić planetą.

## Dlaczego zbiorowości wyglądają na rozrzutne

Przyłóżmy tę miarę do roju z rozdziału 1, a pojawi się coś dziwnego. Decyzja roju to wybór spośród kilkunastu miejsc, czyli mniej niż cztery bity. Żeby ją podjąć, wyleciały setki zwiadowczyń i wykonano setki tańców, z których każdy niósł położenie i był powtarzany przez wiele obiegów (13). Wydano tysiące bitów, żeby rozstrzygnąć cztery. Według ułamka rój wygląda na głupi.

Nie jest głupi, a powód jest pouczający. Osąd pojedynczej pszczoły o dziupli jest zaszumiony. Powtórzenia, niezależne oględziny i powolne dochodzenie do kworum sprawiają, że końcowe cztery bity są *niezawodne*. Shannon pokazał, że dokładne przesłanie informacji przez zaszumiony kanał zawsze kosztuje nadmiarowość: te trzy czwarte angielszczyzny, które czytelnicy potrafią odgadnąć, pozwalają nam rozumieć się w zatłoczonym pokoju. Zbiorowość to zaszumiony kanał zbudowany z umysłów i płaci ten sam podatek.

Wartość η trzeba więc podawać razem z niezawodnością, tak jak zużycie paliwa przez samochód trzeba podawać dla określonej prędkości. I porównanie robi się ciekawe. Każdą zbiorowość, rój, ławę przysięgłych, dziedzinę nauki, należy pytać o to, ile bitów rozmowy wydaje na jeden bit decyzji, na której można polegać, i jak blisko jest to najmniejszej ilości, jaką mogłaby wydać jakakolwiek procedura. Informatycy mają na to minimum nazwę, złożoność komunikacyjna, i prawie wcale nie stosowano jej do żywych zbiorowości.

## W skrócie

- Inteligencję proponujemy rozumieć jako sprawność: osiągnięcie na bit użytej informacji. Mierzy ona, jak mało trzeba umysłowi powiedzieć.
- Ludzie przewidują angielski tekst kosztem około jednego bita na literę, bo mają już model tego języka. Dobry model sprawia, że za światem nadąża się tanio.
- Dzieci uczą się języka z danych mniejszych o cztery lub pięć rzędów wielkości niż duże modele językowe i zapisują tylko około 1,5 megabajta wiedzy. Ludzie uczą się pojęć z jednego przykładu, a pszczoła potrafi nauczyć się pojęć *taki sam* i *inny*.
- Trzeba liczyć trzy rodzaje bitów: doświadczenie, wiedzę wstępną i komunikację. Jeśli pominąć wiedzę wstępną, tablica gotowych odpowiedzi uchodzi za geniusza.
- Jeśli osiągnięcie mierzy się w bitach usuniętej niepewności, twierdzenie ogranicza η z góry przez jeden. Inteligencja doskonała istnieje i polega na tym, żeby niczego nie marnować.
- Twierdzenia teorii: superinteligencja może nas przewyższyć mocą przerobową i wiedzą wstępną, ale nie sprawnością ponad jeden; sprawność podnosi się ciekawością; rozumienie to kompresja; większość inteligencji każdego człowieka to odziedziczona wiedza wstępna.
- Zbiorowości wydają wiele bitów na jeden rozstrzygnięty bit, bo niezawodność kosztuje nadmiarowość. Ich sprawność należy oceniać względem najmniejszej komunikacji, jakiej wymaga zadanie.

## Jak możemy się mylić

Miara zawodzi, jeśli nie da się jej uczynić operacyjną: jeśli nie znajdzie się dającego się obronić sposobu ważenia osiągnięć, rozkładania kosztu wiedzy wstępnej wielokrotnego użytku obok doświadczenia i komunikacji przypadających na jedno zadanie albo odróżniania surowych bitów kanału od informacji wzajemnej, to η jest metaforą, a nie wielkością. Porównanie dzieci z modelami językowymi może być nieuczciwe, jeśli jedne i drugie nie wykonują tego samego zadania albo jeśli o wiele bogatsze doświadczenie zmysłowe dzieci liczy się jako wejście językowe. Niektórzy badacze przypisują przepaść właśnie temu (4). Górna granica równa jeden dotyczy określonego, formalnego pojęcia sterowania w pętli zamkniętej (informacji wzajemnej zebranej ponad to, co osiąga sterowanie w pętli otwartej), a rozciągnięcie jej na całą inteligencję jest naszą hipotezą, a nie treścią twierdzenia. Co więcej, przy ograniczeniach obliczeniowych duża część informacji Shannona obecnej już w istniejących danych pozostaje zamknięta, dopóki nie wydobędzie jej silniejszy predyktor (14). Twierdzenie o superinteligencji zabrania więc wydobywania większego sterowania, niż dane zawierają w zasadzie, a nie odkrywania czegoś więcej przez intensywniejsze myślenie o danych, które już się ma.

## Źródła

1. C. E. Shannon (1951), "Prediction and entropy of printed English", *Bell System Technical Journal* 30:50–64. https://sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/readings/shannon1951prediction.pdf
2. F. G. Guerrero (2009), "A new look at the classical entropy of written English", arXiv:0911.2284, z przeglądem granic Shannona od 0,6 do 1,3 bita na literę. https://arxiv.org/pdf/0911.2284
3. S. Y. Feng, N. D. Goodman and M. C. Frank (2024), "Is child-directed speech effective training data for language models?", arXiv:2408.03617. https://arxiv.org/pdf/2408.03617
4. M. C. Frank (2023), "Bridging the data gap between children and large language models", *Trends in Cognitive Sciences* 27:990–992. https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Frank2023_ChildrenLLMs.pdf
5. F. Mollica and S. T. Piantadosi (2019), "Humans store about 1.5 megabytes of information during language acquisition", *Royal Society Open Science* 6:181393. https://doi.org/10.1098/rsos.181393
6. B. M. Lake, R. Salakhutdinov and J. B. Tenenbaum (2015), "Human-level concept learning through probabilistic program induction", *Science* 350:1332–1338. https://www.cnbc.cmu.edu/~tai/microns_papers/LakeEtAl2015Science.pdf
7. D. Silver et al. (2017), "Mastering the game of Go without human knowledge", *Nature* 550:354–359. https://doi.org/10.1038/nature24270
8. M. Giurfa, S. Zhang, A. Jenett, R. Menzel and M. V. Srinivasan (2001), "The concepts of 'sameness' and 'difference' in an insect", *Nature* 410:930–933. https://ideas.repec.org/a/nat/nature/v410y2001i6831d10.1038_35073582.html
9. National Human Genome Research Institute, "Human genomic variation". https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genomic-variation
10. F. Chollet (2019), "On the measure of intelligence", arXiv:1911.01547. https://arxiv.org/pdf/1911.01547
11. J. L. Kelly Jr. (1956), "A new interpretation of information rate", *Bell System Technical Journal* 35:917–926. https://homepage.sns.it/marmi/esameIUE/kelly.pdf
12. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
13. T. D. Seeley, P. K. Visscher and K. M. Passino (2006), "Group decision making in honey bee swarms", *American Scientist* 94:220–229. https://bees.ucr.edu/media/156/download
14. Y. Xu, S. Zhao, J. Song, R. Stewart and S. Ermon (2020), "A theory of usable information under computational constraints", *ICLR 2020* / arXiv:2002.10689. https://arxiv.org/abs/2002.10689

Liczby podane bez numeru źródła to nasze własne zgrubne oszacowania: zatrzymywana część językowego wejścia dziecka, liczba partii rozgrywanych przez zawodowego gracza, liczby bitów w decyzji roju oraz rozmiar praw Newtona w bitach.
