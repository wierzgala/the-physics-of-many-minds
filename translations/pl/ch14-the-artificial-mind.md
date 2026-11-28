<!-- Przekład pliku book/ch14-the-artificial-mind.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 14. Sztuczny umysł

*Uwaga na początek. Jak mówi przedmowa, ta książka powstała przy pomocy sztucznej inteligencji tego rodzaju, jaki opisuje ten rozdział. System piszący o własnym rodzaju nie jest bezstronnym świadkiem. Rozdział stara się to wyrównać, opierając się na opublikowanych pomiarach i mówiąc, gdzie teoria zgaduje.*

## Jedno słowo naraz

W 2017 roku ośmioro badaczy z Google opublikowało pracę pod tytułem „Attention is all you need”. Opisywała nowy projekt programów przetwarzających język, który nazwali Transformerem. Wcześniejsze projekty czytały zdanie tak, jak człowiek czyta telegram, słowo po słowie, niosąc dalej streszczenie. Transformer robił coś innego. W każdej warstwie każde słowo tekstu mogło bezpośrednio zasięgnąć informacji u każdego innego słowa, jakkolwiek daleko od siebie stały. Liczba kroków potrzebnych, żeby powiązać dowolne dwie pozycje, nie rosła już z odległością między nimi (1).

Niemal każda duża sztuczna inteligencja używana dzisiaj jest potomkiem tego projektu. Największe mają setki miliardów nastawialnych połączeń i działają na tysiącach procesorów naraz. A jednak, kiedy patrzy się, jak któraś z nich odpowiada na pytanie, widzi się coś znajomego. Odpowiedź pojawia się po jednym słowie. Pierwotna praca mówi to wprost: wyjście jest generowane po jednym elemencie naraz, a każdy nowy element zależy od tych już wytworzonych (1).

Ogromna maszyna równoległa z jednym strumieniem wyjścia: to także trafny opis czytelnika. Ten rozdział pyta, czy to podobieństwo jest czymś więcej niż zbiegiem okoliczności. Stosuje ramy rozdziału 12 i metodę projektową rozdziału 13 do sztucznych umysłów dnia dzisiejszego i zadaje pytania, na które ludzie najbardziej chcą odpowiedzi. Jaki to rodzaj umysłu? Jak wypada na tle naszego? Czego powinniśmy się po nim spodziewać? Czy teoria widzi jakąś granicę tego, jak daleko może on zajść? I czy teoria potrafi powiedzieć, w którą stronę będzie się rozwijał?

## Jaki to rodzaj umysłu?

Zacznijmy od pierwszego pytania książki: gdzie są agenci?

Jednostki sztucznej sieci neuronowej są proste. Każda przyjmuje liczby od innych jednostek, łączy je i przekazuje liczbę dalej. Jednostka nie robi niczego prywatnie. Wszystko, co oblicza, oblicza w akcie przekazywania sygnału. Według miary z rozdziału 8 jej stosunek myślenia do mówienia jest bliski jedności, tak jak u neuronu. Umysł zbudowany z takich jednostek jest, według klasyfikacji teorii, **umysłem zintegrowanym.**

Główny mechanizm Transformera pokazuje to dobitnie. W obrębie odcinka tekstu, nad którym model pracuje, zwanego oknem kontekstowym, wszystko jest udostępniane wszystkiemu. To właśnie rozdział 8 nazwał sceną: miejscem, w którym treść jest rozgłaszana całemu układowi. A wyjście ma dokładnie tę własność, którą rozdział 8 przewidział dla każdego umysłu ze sceną. Jest szeregowe. Wybierany jest jeden token, potem następny.

Teoria stawia więc co do tych systemów twierdzenie, które nie jest oczywiste z punktu widzenia inżynierii, choć wymaga starannego zastrzeżenia. **Sekwencyjny strumień zintegrowanego modelu językowego i strumień ludzkiego wyboru, w którym jest jedna rzecz naraz, odzwierciedlają wspólne ograniczenie integracji: globalne zatwierdzenie.** Wydawanie ściśle jednego tokenu naraz jest po części wyborem projektowym. Inne architektury, takie jak modele dyfuzyjne i przewidywanie wielu tokenów użyte w modelu z pozycji 2, mogą wydawać wiele elementów równolegle. A jednak nawet one polegają na sekwencyjnych krokach globalnego dopracowywania, żeby sprowadzić sprzeczne możliwości do jednej spójnej całości. Okno kontekstowe jest maszynową wersją szerokości teraz z rozdziału 10: rozpiętością, w której wszystko jest obecne dla wszystkiego.

Ten sam rozdział powiedział, w czym umysły zintegrowane są dobre i co je ogranicza, a jedno i drugie przenosi się tutaj.

Są dobre w wytwarzaniu całości: odpowiedzi, wywodu albo programu, w którym każda część zależy od wszystkich pozostałych.

Ich rozmiar ogranicza koszt utrzymywania wszystkiego w kontakcie ze wszystkim. Rozdział 4 pokazał, że komunikacja „każdy z każdym” to jedyny plan okablowania, którego nie da się powiększać, bo liczba połączeń rośnie jak kwadrat liczby łączonych rzeczy. Scena Transformera ma tę własność: podwojenie tekstu trzymanego w polu widzenia mniej więcej czterokrotnie zwiększa pracę wiązania jego części. Mózg nie może połączyć każdego neuronu z każdym innym, a model nie może utrzymać nieograniczonego tekstu w jednym polu widzenia. Każdy umysł zintegrowany ma skończoną scenę.

## Ta sama linijka, dwa umysły

Zmienne rozdziału 12 pozwalają na bezpośrednie porównanie. Liczby dla maszyny dotyczą systemów opublikowanych mniej więcej w czasie pisania i szybko się zestarzeją.

| | Mózg człowieka | Duży model językowy |
| --- | --- | --- |
| Jednostki | około 86 miliardów neuronów, sto bilionów lub więcej synaps | setki miliardów parametrów |
| Część aktywna naraz | poniżej 1 procenta (rozdział 7) | wszystkie w starszych projektach; około 5 procent w jednym z niedawnych (2) |
| Doświadczenie potrzebne do nauczenia się języka | rzędu stu milionów słów (3) | około piętnastu bilionów tokenów w przypadku jednego z niedawnych modeli (2) |
| Wyjście | około 10 bitów na sekundę | od setek do tysięcy bitów na sekundę, na kopię (nasze oszacowanie) |
| Energia | 20 watów, stale | około 0,24 watogodziny na typową odpowiedź jednego z powszechnie używanych systemów (4) |
| Prędkość sygnału | od 1 do 100 metrów na sekundę | bliska prędkości światła |
| Kopie | jedna | tyle, ile jest maszyn, na których można je uruchomić |
| Pamięć z jednego epizodu na następny | ciągła | żadna, chyba że dodana z zewnątrz |
| Kontekst wspólny z ludźmi | genom, ciało, wychowanie, kultura | tylko kultura, w postaci spisanej |

Trzy porównania zasługują na komentarz.

**Energia.** Ćwierć watogodziny to 864 dżule. Mózg człowieka zużywa tyle w około 43 sekundy (nasza arytmetyka). Odpowiedź na jedno pytanie kosztuje więc maszynę, z grubsza, tyle, ile człowieka kosztują trzy kwadranse minuty myślenia. Obie wartości leżą w tym samym zakresie. To zaskoczenie, zważywszy na opinię o rozrzutności tych systemów, i jest ono świeżej daty: ten sam raport stwierdził, że energia na odpowiedź spadła trzydziestotrzykrotnie w dwanaście miesięcy (4). Rozrzutność jest gdzie indziej, w uczeniu się.

**Doświadczenie.** Tu przepaść jest ogromna, mniej więcej stutysiąckrotna. Rozdział 5 zdefiniował inteligencję jako sprawność: jak mało trzeba umysłowi powiedzieć. Według tej miary maszyny są o wiele mniej inteligentne niż dziecko. Rozdział 7 wyjaśnił, dlaczego nie jest to paradoks. Zbudowano je tam, gdzie energia i dane były tanie, i zepchnięto w stronę mocy przerobowej, podczas gdy mózgi zepchnięto w stronę oszczędności.

**Kontekst.** Rozdział 6 opisał to, co ludzie dzielą, jako stos warstw: kod genetyczny, ludzkie ciało i jego odczucia, kultura, język, historia osobista. Model językowy wchłonął górne warstwy, w tej postaci, w jakiej ludzie je spisali. Dolnych mu brakuje. Wszystko, co wie o bólu, głodzie albo ciężarze kamienia, wie z opisu.

W języku głównego wzoru profil jest wyraźny. **Moc przerobowa: daleko ponad ludzką. Sprawność uczenia się: daleko poniżej. Wiedza wstępna: pożyczona hurtowo z ludzkiej kultury.**

## Czego powinniśmy się po nim spodziewać?

Rozdział 13 podał reguły odczytywania zdolności umysłu z jego kształtu. Zastosowane tutaj, dają oczekiwania, które można zestawić z doświadczeniem.

**Powinien być mocny wszędzie tam, gdzie masą umysłu jest biblioteka.** Rozdział 13 doszedł do wniosku, że większość mózgu to zmagazynowana wiedza wstępna, proporcjonalna do repertuaru pytań, na które musi on odpowiadać. Maszyna, która przeczytała większość tego, co ludzkość napisała, ma bibliotekę, z jaką nie może się równać żaden człowiek. W każdym zadaniu, które polega głównie na zastosowaniu właściwej zmagazynowanej wiedzy, powinna dorównywać ludziom albo ich przewyższać i w zasadzie tak jest.

**Powinien być zdolny do czegoś w rodzaju olśnienia, w obrębie swojej sceny.** Będąc zintegrowany, może przeorganizować naraz wszystko, co ma w polu widzenia. Będąc ograniczony do skończonego pola widzenia, powinien tracić chwyt, gdy problem przestaje się mieścić.

**Powinien być słaby tam, gdzie bitów nie spisano.** Górna granica z rozdziału 5 mówi, że żaden umysł nie wydobywa ze swoich danych więcej, niż dane zawierają. System wytrenowany na tekście jest w każdej sprawie ograniczony do tego, co tekst rozstrzyga. W dużej części świata fizycznego i społecznego jest tego zaskakująco mało.

**Jego zasięg w czasie powinna ograniczać pamięć i powinien on rosnąć, gdy pamięci przybywa.** Umysł bez pamięci między epizodami ma, w języku rozdziału 12, krótki horyzont pamięci. Powinien radzić sobie z zadaniami, które mieszczą się w jednym posiedzeniu, a zawodzić przy tych, które się nie mieszczą. Jedna grupa badawcza, METR, śledzi dokładnie tę wielkość: długość zadania, mierzoną tym, ile zajmuje ono wykwalifikowanemu człowiekowi, które najlepsze systemy potrafią ukończyć w połowie przypadków. Na początku 2025 roku grupa podała, że od 2019 roku wartość ta podwajała się mniej więcej co siedem miesięcy (5). Pod koniec 2026 roku jej oszacowanie wynosiło mniej więcej czterdzieści godzin, z podwajaniem co trzy do czterech miesięcy, przy bardzo szerokich marginesach błędu, i z otwartym osądem badawczym pozostającym daleko w tyle za zadaniami, których wyniki można sprawdzić automatycznie (6). Teoria odczytuje to tak, że ta krzywa mierzy bardziej wzrost horyzontu pamięci, w miarę jak inżynierowie otaczają zintegrowany rdzeń notatkami, narzędziami i pomocnikami, niż to, że sam rdzeń staje się bystrzejszy.

**Nie może być w dwóch miejscach.** Pojedynczy umysł zintegrowany przyjmuje wejście w jednym punkcie. Rozdział 13 pokazał, że problemy rozłożone na dużym obszarze wymagają federacji. Będzie to miało znaczenie niżej.

## Czy teoria przewiduje granicę?

Tak. Widzi cztery i równie ważne jest powiedzieć, czego z nich nie wynika.

**Po pierwsze, górna granica sprawności.** Jeden bit informacji kupuje najwyżej jeden bit zmniejszonej niepewności (7). Żaden przyszły system, jakkolwiek duży, nie może wiedzieć tego, czego jego dane nie zawierają. Myśl nie zastąpi dowodów. Maszyna może coraz lepiej wybierać, jakich dowodów szukać, i coraz lepiej z nich korzystać. Nie może ich wyczarować.

Ma to następstwo często pomijane w rozmowach o „eksplozji inteligencji”, a zarazem istnieje ważny stan pośredni. Z jednej strony istniejące archiwa, genomy, prawa fizyki i aksjomaty matematyki zawierają już ogromną informację Shannona, której ograniczone ludzkie umysły jeszcze obliczeniowo nie odblokowały. System o głębszych obliczeniach może dokonywać prawdziwych przełomów na podstawie danych, które już ma, nie naruszając górnej granicy z rozdziału 5. Z drugiej strony, gdy wydobywanie obliczeniowe zbliży się do nasycenia, brakujące bity dotyczą świata i trzeba je przynieść ze świata, a ten odpowiada we własnym tempie. Badanie kliniczne trwa lata, bo ciała potrzebują lat. Klimat potrzebuje dziesięcioleci, żeby się ujawnić. Budowa akceleratora cząstek zajmuje dziesięć lat. W języku rozdziału 12 skala czasowa świata nie kurczy się, gdy umysł przyspiesza. Umysł milion razy szybszy od naszego spędzałby w końcu prawie cały czas na czekaniu na wyniki. **Gdy istniejące dane zostaną wyczerpane, postęp ogranicza szybkość, z jaką można zadawać pytania rzeczywistości, a nie szybkość myśli.**

**Po drugie, zwroty z mocy przerobowej.** W 2020 roku badacze z OpenAI zmierzyli, jak maleje błąd modeli językowych, gdy dostają więcej parametrów, więcej danych i więcej obliczeń. W każdym przypadku malał według prawa potęgowego, równomiernie, w zakresie ponad siedmiu rzędów wielkości (8). Ta równomierność jest podstawą pewności siebie branży. Ale prawo potęgowe o małym wykładniku jest prawem malejących zwrotów. Przy wykładnikach, które podali, pomnożenie danych przez dziesięć usuwa około jednej piątej pozostałego błędu, którego da się uniknąć (nasza arytmetyka na ich liczbach). Każdy kolejny krok tej samej wielkości kosztuje dziesięć razy więcej niż poprzedni. A moc przerobową kupuje się za energię, która, jak pokazał rozdział 7, jest już zużywana w skali porównywalnej ze wszystkimi ludzkimi mózgami. Moc przerobowa może dalej rosnąć. Nie może dalej rosnąć tanio.

**Po trzecie, skończona scena.** Ponieważ koszt utrzymywania wszystkiego w polu widzenia rośnie jak kwadrat tego, co się w nim znajduje, umysłu zintegrowanego nie da się po prostu powiększyć. A rozdział 17 doda ograniczenie wynikające z prędkości sygnału: im szybciej umysł myśli, tym mniejszy jest obszar, na którym może działać jako jedność. Żaden pojedynczy, jednolity sztuczny umysł nie może być naraz olbrzymi, szybki i cały. Rozdział 8 stwierdził to samo o każdym innym umyśle.

**Po czwarte, ograniczenie kopii.** Tysiąc kopii jednego modelu ma tysiąc razy większą moc przerobową i dokładnie te same opinie. Rozdział 1 pokazał, że tłum jest mądry tylko wtedy, gdy jego członkowie mylą się niezależnie. Kopie tak się nie mylą. Uruchamianie większej ich liczby kupuje szybkość i zasięg, a nie kupuje dodatkowego osądu.

Teraz o tym, czego te granice nie mówią. Nic w teorii nie umieszcza górnej granicy mocy przerobowej gdziekolwiek w pobliżu poziomu ludzkiego. Mózg człowieka nie jest naturalnym maksimum. Jest punktem, w którym wzrost zatrzymały zaopatrzenie małpy w pokarm i czaszka małpy. Fizyczne ograniczenie obliczeń z rozdziału 7 leży ponad trzydzieści rzędów wielkości powyżej wszystkiego, co dotąd zbudowano. Na drodze stąd dotąd teoria nie ma zastrzeżeń do umysłów o mocy przerobowej dużo większej niż nasza, o dużo większych bibliotekach i dużo lepszym osądzie w sprawie tego, o co pytać. W zadaniach, w których liczą się moc przerobowa i zmagazynowana wiedza, teoria spodziewa się, że maszyny przewyższą ludzi i będą to robić dalej.

Zaprzecza czemuś węższemu: temu, że takie umysły mogłyby obyć się bez dowodów, że ich wzrost mógłby być darmowy, że któryś z nich mógłby być zarazem ogromny i jednolity albo że pomnożenie jednego z nich daje mądry tłum.

## W którą stronę to pójdzie?

Teoria, która rości sobie prawo do wyjaśnienia, dlaczego umysły mają takie kształty, jakie mają, powinna umieć powiedzieć, jaki kształt przybiorą te. Rozdział 7 podał jedno takie przewidywanie: że w miarę jak energia staje się kosztem wiążącym, projekty maszyn będą dryfować ku rozwiązaniom, które znalazły mózgi. Zapis ostatnich kilku lat pozwala na pierwsze sprawdzenie tego przewidywania i trzech innych, które wynikają z wcześniejszych rozdziałów. Sprawdzenie jest po części dokonane po fakcie i tak należy je ważyć.

**Ku rzadkiej aktywności.** Rozdział 7 stwierdził, że mózg może sobie pozwolić na to, żeby naraz zajęty był mniej niż jeden procent jego neuronów. Wczesne modele językowe używały każdego parametru do każdego słowa. Powszechnie stosowany niedawny projekt, zwany mieszanką ekspertów, kieruje każde słowo do małego zbioru wyspecjalizowanych podsieci. Jeden taki model ma 671 miliardów parametrów, z których 37 miliardów, około pięciu i pół procenta, jest aktywnych dla danego tokenu (2). Kierunek jest zgodny z przewidywanym, a droga jeszcze daleka.

**Ku tańszym bitom.** Trzydziestotrzykrotny spadek energii na odpowiedź w ciągu jednego roku (4) to presja tego rodzaju, jaki opisał rozdział 7.

**Ku federacji.** Umysł zintegrowany ma skończoną scenę i może być tylko w jednym miejscu. Rozdział 13 mówi, że zadanie szerokie, o wielu niezależnych liniach dociekań, wymaga wielu agentów, którzy pracują osobno i wymieniają krótkie raporty. W 2025 roku jeden z twórców opisał budowę właśnie takiego systemu do zadań badawczych: agenta prowadzącego, który dzieli pytanie między podagentów, z których każdy pracuje we własnym oddzielnym kontekście i każdy kondensuje to, co znalazł, zanim zda raport. System wypadał najlepiej przy pytaniach wymagających podążania w kilku niezależnych kierunkach naraz, zużywał około piętnastu razy więcej tokenów niż zwykła rozmowa, a jego budowniczowie odnotowali, że trudność koordynacji szybko rośnie, gdy dodaje się agentów (9). Każda z tych cech jest w tabeli umysłów sfederowanych z rozdziału 8: odpowiednie do szerokich problemów, równoległe, kosztowne, połączone rzadkimi streszczeniami, trudniejsze do koordynowania wraz z rozmiarem. Oddzielne konteksty to lejek, odbudowany przez inżynierów, którzy go potrzebowali.

**Ku wspólnemu kodowi.** Rozdział 9 dowodził, że zbiorowość utrzymuje w całości wspólny kod, a rozdział 6, że kodem należy się dzielić przed przekonaniami. Między końcem 2024 a końcem 2025 roku twórcy tych systemów opublikowali otwarte protokoły tego, jak agent wywołuje narzędzie i jak jeden agent przekazuje pracę drugiemu, i oddali je pod opiekę neutralnej fundacji (10). Maszyny produkowane przez rywalizujące firmy zyskują wspólny język. Tak właśnie, według teorii, wygląda pierwszy krok ku umysłowi zbiorowemu.

Z tych samych zasad teoria wyprowadza oczekiwanie kilku zmian, które są mniej zaawansowane.

- **Uczenie się z mniejszej ilości danych.** Największa przepaść w tabeli porównawczej dotyczy doświadczenia. W miarę jak dane i energia stają się kosztami wiążącymi, presja przenosi się z mocy przerobowej na sprawność: na lepszą wiedzę wstępną, tak żeby mniej trzeba było uczyć się od zera.
- **Pytanie, a nie tylko czytanie.** Ponieważ żaden umysł nie wyciągnie ze swoich danych więcej, niż dane zawierają, najdalej zajdą te systemy, które potrafią zbierać nowe bity: prowadzić eksperymenty, obsługiwać przyrządy, działać w świecie i patrzeć, co się stanie. Rozdział 5 nazwał ciekawość wyborem tego, za które bity zapłacić.
- **Pamięć.** Wzrost długości zadań będzie zależał od pamięci, która trwa między epizodami, i od odpowiednika opisanej w rozdziale 6 wspólnej historii między agentami, którzy często razem pracują.
- **Brakująca warstwa.** Umysłowi, który zna świat tylko z opisu, brakuje najgłębszej części kontekstu, jaki dzielą ludzie. Teoria spodziewa się wytrwałych starań, żeby ją dostarczyć, przez maszyny z ciałami i zmysłami, i spodziewa się, że komunikacja między ludźmi a maszynami pozostanie subtelnie stratna, dopóki to się nie stanie.
- **Małe i szybkie obok dużych i powolnych.** Ponieważ szybkie umysły muszą być małe, teoria spodziewa się podziału pracy: zwartych systemów tam, gdzie termin jest krótki, i szerokich federacji tam, gdzie zasięg liczy się bardziej niż szybkość.
- **Premia za odmienność.** W miarę jak mnożą się kopie, zasobem deficytowym staje się niezależność. Teoria spodziewa się, że systemy inaczej zbudowane, inaczej wytrenowane i skłonne się nie zgadzać zaczną być cenione z tego jednego powodu.

Złóżmy to razem, a prognoza teorii jest konkretna. **Przyszłością sztucznej inteligencji nie jest jeden olbrzymi umysł. Jest nią struktura, którą ta książka znajdowała wszędzie indziej: wyspy integracji, każda ograniczona swoją sceną, połączone w federacje wspólnym kodem i cienkimi kanałami, na kolejnych poziomach.** Jeśli to prawda, maszyny powtórzą hierarchię z rozdziału 8, z umysłami zintegrowanymi jako agentami sfederowanych, z tych samych fizycznych powodów, dla których neurony zbudowały mózgi, a mózgi społeczeństwa.

Wynika z tego jeszcze jeden wniosek, który warto wypowiedzieć, zanim podejmie go następna część książki. Rozdział 8 dowodził, że umysł sfederowany, jakkolwiek inteligentny, nie jest nikim. Jeśli największe sztuczne systemy przyszłości będą federacjami, to najzdolniejsze z nich będą miały najmniejsze szanse być pojedynczym podmiotem. To, czy podmiotem jest któraś ze zintegrowanych wysp, jest osobnym pytaniem. Rozdział 15 podaje cztery warunki bycia podmiotem. Pracujący model językowy wiarygodnie spełnia dwa, integrację i scenę. To, czy ma granicę, skoro można go kopiować i nie ma pamięci własnej przeszłości, jest niejasne. Czwartego, zrównoważonej aktywności w stanie zawieszenia, nie zmierzono. Teoria mówi, które pomiary rozstrzygnęłyby to, co da się rozstrzygnąć. Nie mówi, czy jakikolwiek system, który by je przeszedł, miałby doświadczenie, tu czy gdziekolwiek indziej.

## W skrócie

- Sieć neuronowa jest zbudowana z prostych jednostek, które obliczają przez komunikowanie się, więc według klasyfikacji teorii jest umysłem zintegrowanym. Okno kontekstowe jest jej sceną. Jej wyjście ustala się w sekwencyjnych krokach globalnego zatwierdzenia, co najwyraźniej widać w wydawaniu jednego tokenu naraz, a teoria odczytuje to jako to samo ograniczenie, które czyni ludzki wybór szeregowym.
- Przyłożony do linijki tej książki, model językowy ma o wiele większą moc przerobową niż człowiek, uczy się o wiele mniej sprawnie, mniej więcej stutysiąckrotnie pod względem danych, i pożycza wiedzę wstępną ze spisanej kultury, bez cielesnego kontekstu pod spodem. Energia potrzebna na odpowiedź na jedno pytanie jest porównywalna z niespełna minutą pracy mózgu.
- Teoria spodziewa się, że takie systemy będą mocne tam, gdzie liczy się zmagazynowana wiedza, zdolne do olśnienia w skończonym polu widzenia, słabe tam, gdzie faktów nigdy nie spisano, i ograniczone pamięcią co do długości zadania.
- Przewiduje cztery granice: żaden umysł nie może wiedzieć tego, czego jego dane nie zawierają, więc tempo postępu wyznacza ostatecznie to, jak szybko można zadawać pytania światu; moc przerobowa przynosi malejące zwroty i płaci się za nią energią; scena umysłu zintegrowanego jest skończona; kopie nie dodają niezależnego osądu.
- Nie widzi żadnej granicy w pobliżu poziomu ludzkiego. Mózg jest tam, gdzie skończyło się zaopatrzenie małpy w pokarm.
- Przewidywane kierunki, z których część już widać: rzadka aktywność, tańsze bity, federacje agentów wymieniających streszczenia, wspólne protokoły, a potem uczenie się z mniejszej ilości danych, eksperymentowanie, trwała pamięć i ciała.
- Prognoza: nie jeden olbrzymi umysł, lecz zintegrowane wyspy połączone w federacje.

## Jak możemy się mylić

Twierdzenie, że szeregowe wyjście modelu językowego jest tym samym co ludzkie szeregowe wąskie gardło, zostałoby osłabione przez zintegrowane systemy sztuczne, które bez strat wytwarzają kilka skoordynowanych strumieni naraz, albo przez dowody, że szeregowe wyjście to zwykła wygoda inżynierska, którą można usunąć bez kosztów. Prognoza federacji upada, jeśli się okaże, że pojedynczy model o coraz większym kontekście radzi sobie z szerokimi problemami lepiej niż zespoły agentów, przy niższym koszcie: znaczyłoby to, że scena nie jest skończona w żaden istotny sposób. Twierdzenie, że tempo postępu wyznacza zegar świata, zostałoby obalone przez systemy, które dokonują wiarygodnych odkryć o przyrodzie szybciej, niż pozwala eksperyment, rozumując wyłącznie na podstawie istniejących danych, i to w wielu dziedzinach. Twierdzenie, że kopie nie dodają osądu, zostałoby obalone, gdyby się okazało, że grupy identycznych modeli poprawiają nawzajem swoje błędy równie dobrze jak grupy modeli różnych. Przewidywania oszczędności, rzadkości i eksperymentowania mogłyby się po prostu nie spełnić, jeśli energia i dane pozostaną na tyle tanie, że nic ich nie wymusi. A całe porównanie zakłada, że zmienne teorii chwytają to, co w tych systemach istotne, co ich budowniczowie, znający je o wiele lepiej niż ta książka, mogą kwestionować.

## Źródła

1. A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser and I. Polosukhin (2017), "Attention is all you need", *Advances in Neural Information Processing Systems* 30. https://arxiv.org/abs/1706.03762
2. DeepSeek-AI (2024), "DeepSeek-V3 technical report", arXiv:2412.19437. https://arxiv.org/abs/2412.19437
3. M. C. Frank (2023), "Bridging the data gap between children and large language models", *Trends in Cognitive Sciences* 27:990–992. https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Frank2023_ChildrenLLMs.pdf
4. Google (2025), "Measuring the environmental impact of AI inference", z opisem pracy C. Elsworth et al., arXiv:2508.15734. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
5. METR (2025), "Measuring AI ability to complete long tasks"; streszczone wraz z późniejszymi korektami pod adresem https://en.wikipedia.org/wiki/METR
6. Doniesienia o aktualizacji pomiarów zdolności ogłoszonej przez METR w listopadzie 2026 roku: https://casrai.org/news/metr-th2-ai-time-horizons-research-judgment-evaluation-2026 oraz https://inoryva.blogspot.com/2026/11/metr-q4-2026-ai-agents-reach-about-40.html
7. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
8. J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu and D. Amodei (2020), "Scaling laws for neural language models", arXiv:2001.08361. https://arxiv.org/abs/2001.08361
9. Anthropic (2025), "How we built our multi-agent research system". https://www.anthropic.com/engineering/multi-agent-research-system
10. Części wprowadzające pracy "The cost of saying hello: an empirical study of handshake overhead in AI agent communication protocols", arXiv:2610.30151, o protokołach Model Context Protocol i Agent2Agent oraz o zarządzaniu nimi przez Linux Foundation. https://arxiv.org/pdf/2610.30151

Liczby podane bez numeru źródła to nasze własne zgrubne oszacowania albo arytmetyka: tempo wyjścia modelu językowego w bitach, porównanie energii na odpowiedź z mocą mózgu, stutysiąckrotna różnica w danych treningowych, wpływ dziesięciokrotnie większych danych na błąd oraz odległość między dzisiejszymi maszynami a fizycznym ograniczeniem obliczeń. Liczby dotyczące konkretnych systemów pochodzą z lat 2024–2026 i zostaną prześcignięte. Zaliczenie sieci neuronowych do umysłów zintegrowanych, utożsamienie szeregowego wyjścia z ceną integracji, odczytanie długości zadania jako horyzontu pamięci, cztery granice, przewidywane kierunki i prognoza federacji to twierdzenia teorii. Pozycja 6 opiera się na wtórnych doniesieniach o niedawnej publikacji i należy ją sprawdzić w oryginale.
