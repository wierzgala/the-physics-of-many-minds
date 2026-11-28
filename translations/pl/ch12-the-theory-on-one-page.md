<!-- Przekład pliku book/ch12-the-theory-on-one-page.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 12. Teoria na jednej stronie

*Ten rozdział różni się od pozostałych. Nie ma w nim opowieści. Wykłada teorię tak, jak zrobiłby to podręcznik fizyki: wielkości, ich jednostki, zbudowane z nich czyste liczby, granice i zależności, które teoria między nimi głosi. To jedyny rozdział ze wzorami, a po każdym wzorze następuje to samo stwierdzenie słowami. Czytelnicy, którzy wolą narrację, mogą przejść od razu do rozdziału 13, który zaprzęga tę maszynerię do pracy, i wracać tutaj jak do ściągawki.*

## Po co to spisywać

Pierwsze trzy części tej książki wprowadzały sposób opisywania umysłów po jednej idei naraz, każdą z własnymi pszczołami, mózgami i ptakami. Teoria fizyczna musi być czymś więcej niż zbiorem dobrych przykładów. Potrzebuje krótkiej listy mierzalnych wielkości, stwierdzenia, jak się one łączą, i granic, których żaden układ nie może przekroczyć. Mając to w ręku, dwie osoby, które nie zgadzają się co do jakiegoś umysłu, mogą zrobić to, co robią fizycy: zmierzyć, policzyć i zobaczyć, kto ma rację.

Wzorem jest termodynamika. Opisuje silniki parowe, gwiazdy i żywe komórki garścią zmiennych, takich jak temperatura, ciśnienie, objętość i entropia, oraz kilkoma prawami, które je wiążą, i nie musi wiedzieć, co robi każda cząsteczka. Cel jest tu taki sam: opisać umysł zbiorowy kilkoma liczbami, bez śledzenia każdego agenta.

To, co następuje, to ramy, a nie gotowa jeszcze teoria. Ostatnia część mówi, czego brakuje.

## Wielkości podstawowe

Wystarczą cztery wymiary fizyczne.

| Wymiar | Jednostka | Co tutaj mierzy |
| --- | --- | --- |
| Informacja | bit | ile niepewności zostaje usunięte, zapisane albo wysłane |
| Czas | sekunda | jak długo coś trwa |
| Długość | metr | jak daleko od siebie są agenci |
| Energia | dżul | ile to wszystko kosztuje |

Liczba agentów jest czystą liczbą bez jednostki. Temperatura wchodzi tylko przez cenę bita, niżej.

Traktowanie bita jako jednostki fizycznej na równi z sekundą i metrem to krok, od którego zależy wszystko inne. Uzasadnienie podał rozdział 2: informacja ma koszt energetyczny, który zmierzono w laboratorium (1), a każdy zebrany bit kupuje najwyżej jeden bit sterowania światem (2).

## Zmienne umysłu

Żeby określić umysł zbiorowy, trzeba podać poniższe liczby. Prawe kolumny pokazują zgrubne wartości dla dwóch znanych przypadków. To nasze oszacowania, zebrane z wcześniejszych rozdziałów.

| Symbol | Wielkość | Jednostka | Mózg człowieka | Rój pszczół |
| --- | --- | --- | --- | --- |
| N | liczba agentów | (bez jednostki) | około 10¹¹ neuronów | około 10⁴ pszczół, kilkaset zwiadowczyń |
| d | połączenia na agenta | (bez jednostki) | około 10⁴ synaps | kilka obejrzanych tańców |
| m | pamięć na agenta | bit | około 10⁵ | duża: tyle, ile mieści mózg |
| r | tempo przetwarzania na agenta | bit/s | kilka | bardzo duże: milion neuronów |
| c | przepustowość jednego połączenia | bit/s | kilka | około 7 bitów na taniec |
| L | rozmiar zbiorowości | m | 0,15 | kilka tysięcy |
| v | prędkość sygnału | m/s | od 1 do 100 | lot pszczoły, około 7 |
| T_w | skala czasowa świata, z którym ma do czynienia | s | od 0,1 do 1 | od godzin do dni |
| R_in | informacja napływająca z zewnątrz | bit/s | około 10⁹ | to, co widzą zwiadowczynie |
| R_out | informacja wychodząca jako działanie | bit/s | około 10 | kilka bitów na dobę |
| P | moc | W | 20 | kilka watów |
| S | kontekst wspólny agentom | bit | genom, rozwój, doświadczenie | kod tańca |

Dwie uwagi o tej tabeli znaczą więcej niż którakolwiek jej pozycja.

Po pierwsze, większość tych wielkości da się zmierzyć istniejącymi metodami. Liczenie agentów i połączeń to anatomia. Przepustowości i tempa zmierzono dla neuronów, dla mowy i dla tańca wywijanego. Prędkości sygnałów są znane od czasów Helmholtza.

Po drugie, obie kolumny różnią się o wiele rzędów wielkości w prawie każdym wierszu. Ta książka twierdzi, że mimo to oba układy można porównywać, bo ich zachowaniem rządzą nie te liczby, lecz pewne stosunki między nimi.

## Wielkości pochodne

Kilka kombinacji pojawia się tak często, że zasługują na nazwy.

**Czas przejścia.** Czas, w jakim sygnał przebywa zbiorowość.

> t_x = L / v

Dla mózgu to dziesiątki milisekund. Dla roju dziesiątki minut. Dla ludzkości przed telegrafem miesiące. Rozdział 10 zaproponował, że to jest naturalna jednostka czasu każdego umysłu.

**Całkowite przetwarzanie.** To, co obliczają razem wszyscy agenci, N × r.

**Wymiana w poprzek.** Informacja na sekundę, która może przejść przez powierzchnię przecinającą zbiorowość na pół. Nazwijmy ją B. Wyznacza ją to, ile połączeń przechodzi przez cięcie i ile niesie każde z nich. To ta wielkość, którą rozdział 4 nazwał przepustowością przez powierzchnię, i ogranicza ona to, ile dwie połowy mogą sobie nawzajem powiedzieć.

**Moc przerobowa.** Informacja na sekundę, którą zbiorowość jako całość potrafi zaangażować w jedną decyzję. Nazwijmy ją C. Nie może być większa niż to, co napływa, nie większa niż to, co agenci potrafią przetworzyć, i, gdy całość musi działać jako jedność, nie większa niż to, co może przejść między jej częściami.

> C ≤ najmniejsza z wielkości R_in, N × r oraz, przy działaniu jako jedność, B

**Sprawność.** Część użytej informacji, która kończy jako zmniejszona niepewność co do tego, co zrobić. Rozdział 5 nazwał ją η.

> η = usunięte bity niepewności co do celu ÷ bity użytej informacji

**Przekazane znaczenie.** Wiadomość dostarcza to, co niesie, oraz to, co odbiorca już dzieli z nadawcą (rozdział 6).

> znaczenie = bity wysłane + bity wspólnego kontekstu, które wiadomość uruchamia

**Wzmocnienie kontekstowe.** O ile krótsza staje się wiadomość dzięki temu, co wspólne. Jeśli opisanie sytuacji od zera wymaga H bitów, a opisanie jej komuś, kto dzieli twój kontekst, wymaga H_S bitów, to

> κ = H / H_S

Wynosi 1 między zupełnie obcymi i może sięgać setek między ludźmi, którzy dobrze się znają. Efektywna przepustowość połączenia wynosi wtedy κ × c.

## Czyste liczby

Rozdział 4 wyjaśnił, dlaczego czyste liczby są ważne: stosunek bez jednostek jest taki sam bez względu na użyty układ miar, a dwa układy o tych samych czystych liczbach zachowują się podobnie, jakkolwiek różnie wyglądają. Teoria opiera się na poniższym zestawie. Pierwszych siedem było w jej pierwotnym sformułowaniu. Trzy ostatnie dodały rozdziały części III.

| Nazwa | Definicja | O czym rozstrzyga | Rozdział |
| --- | --- | --- | --- |
| Liczba spójności | T_w / t_x | czy zbiorowość może działać jako jedność wobec swojego świata; musi być dużo większa od 1 | 4 |
| Myślenie do mówienia | r / s, gdzie s to tempo niezależnej informacji, którą agent wysyła; sygnał skopiowany na wszystkie d jego połączeń liczy się raz, więc dla agenta rozgłaszającego, takiego jak neuron, s wynosi najwyżej c | zintegrowana, gdy blisko 1, sfederowana, gdy dużo powyżej 1 | 4, 8 |
| Horyzont pamięci | N × m / (R_in × T_w) | ile czasów świata doświadczenia może pomieścić | 4 |
| Liczba graniczna | ruch przez zewnętrzny brzeg / B | czy jest jaźnią; musi być dużo mniejsza od 1 | 4, 15 |
| Koszt ponad dolną granicę | energia na bit / granica Landauera | jak daleko od minimum termodynamicznego działa | 2, 7 |
| Stosunek korelacji | długość korelacji / L | czy jest jednym układem; musi być bliski 1 | 11 |
| Wzmocnienie kontekstowe | κ | ile przekazuje każdy bit | 6 |
| Wymiana do dryfu | tempo wymiany między częściami / tempo dryfu ich kodów | czy pozostaje jednym rodzajem; musi przekraczać próg | 9 |
| Czas poznawczy | t / t_x | zegar, na którym można porównywać różne umysły | 10 |
| Wymiar okablowania | D, zdefiniowany przez B ∝ N^(1−1/D) | jak dobrze wymiana w poprzek nadąża za rozmiarem | 4, 11 |

Trzy z nich to warunki jedności, które rozdział 9 zebrał w jedno prawo. Zapisane razem:

> działa jako jedność, gdy T_w ≫ t_x
>
> jest jaźnią, gdy ruch przez jej brzeg ≪ B
>
> pozostaje jednym rodzajem, gdy wymiana ≫ dryf

W każdym z nich ruch wewnątrz zbiorowości porównuje się z konkurencyjnym tempem. W tym sensie teoria mówi, że jedność jest stosunkiem temp.

## Granice

Pięć ograniczeń jest zapożyczonych z ustalonej fizyki i teorii informacji. Żaden umysł jakiegokolwiek rodzaju nie może ich przekroczyć.

**Cena bita.** Wymazanie jednego bita informacji rozprasza co najmniej

> E = k_B × Θ × ln 2

gdzie k_B to stała Boltzmanna, a Θ temperatura: około 3 × 10⁻²¹ dżula w temperaturze pokojowej. To granica Landauera, potwierdzona doświadczalnie (1, 3). Wyznacza minimalną moc dla danego tempa przetwarzania.

**Zwrot z bita.** Jeden bit informacji o układzie pozwala zmniejszyć jego niepewność najwyżej o jeden bit (2). Stąd

> η ≤ 1

**Przepustowość kanału.** Połączenie o danym paśmie i szumie może przenieść tylko określoną ilość, co udowodnił Shannon (4). Ogranicza to c.

**Prędkość sygnałów.** Nic nie porusza się szybciej niż światło, więc dla każdego umysłu, który musi działać jako jedność w czasie t,

> L ≤ (prędkość światła) × t

a w praktyce L ≤ v × t dla tego, z czego zrobione są jego sygnały. To ograniczenie rozmiaru z rozdziału 16.

**Szybkość zmian.** Układ o energii E może przejść najwyżej przez 2E / πħ rozróżnialnych stanów na sekundę, gdzie ħ to zredukowana stała Plancka (5). Zastosowane do kilograma materii daje to górną granicę mocy przerobowej z rozdziału 7 (6).

## Zależności skalowania

Jak zmieniają się wielkości, gdy umysł rośnie.

**Wymiana w poprzek rośnie wolniej niż rozmiar.**

> B ∝ N^(1−1/D)

Przy samych połączeniach lokalnych w trzech wymiarach D wynosi 3, a podwojenie liczby agentów mnoży wymianę w poprzek mniej więcej przez 1,6. Okablowanie „każdy z każdym” nadążałoby za rozmiarem, ale nie da się go zbudować. Rzeczywiste mózgi i układy scalone mają D powyżej 3, kupione długimi kablami (7).

**Czas przejścia rośnie z rozmiarem.** Przy stałej gęstości t_x ∝ N^(1/3) / v.

**Kable rosną szybciej niż tkanka, którą obsługują.** U ssaków istota biała skaluje się jak istota szara w potędze 4/3 (8).

**Cena bita rośnie z tempem.** W neuronach, w których ją zmierzono, kanał przenoszący więcej bitów na sekundę płaci więcej za każdy z nich (9). Wynika z tego reguła, że wiele powolnych kanałów wygrywa z jednym szybkim.

**Energia mózgu jest proporcjonalna do liczby neuronów.** Koszt na neuron jest mniej więcej stały u różnych gatunków (10).

Połączenie dwóch pierwszych daje wynik rozdziału 7 w jednej linijce. W zbiorowości o połączeniach lokalnych wymiana w poprzek na agenta maleje jak N^(−1/3), a opóźnienie rośnie jak N^(1/3). Im większy staje się umysł, tym mniej każda część może powiedzieć reszcie i tym później to dociera.

## Co teoria głosi

Powyższe wielkości i granice są albo definicjami, albo ustalonymi wynikami. Własną treścią teorii jest poniższy zestaw zależności. Każda jest hipotezą.

1. **Inteligentny wynik to moc przerobowa razy sprawność.** Tempo, w jakim umysł zmniejsza niepewność co do tego, co zrobić, wynosi C × η, przy η równym najwyżej 1 i C ograniczonym jak wyżej.
2. **Znaczenie to bity wysłane plus kontekst wspólny**, a efektywna przepustowość połączenia wynosi κ × c.
3. **Jedność jest stosunkiem temp**, w trzech postaciach podanych wyżej.
4. **Podobieństwo.** Dwie zbiorowości o tych samych czystych liczbach wykonują te same obliczenia, gdy czas liczy się w jednostkach t_x. Decyzja zajmuje w każdej z nich kilkadziesiąt czasów przejścia.
5. **Rodzaj wynika z liczby myślenia do mówienia.** Blisko 1 zbiorowość jest szybka, ograniczona w rozmiarze, szeregowa i zdolna być podmiotem. Dużo powyżej 1 jest powolna, nieograniczona w rozmiarze, równoległa i nie jest nikim.
6. **Poziomy są tam, gdzie pęka skalowanie.** Granica między agentami a zbiorowością, którą tworzą, ujawnia się jako zmiana wykładnika w jakiejś zależności skalowania, a agent to blok, którego wpływ na zewnętrze da się streścić w o wiele mniejszej liczbie bitów niż jego stan wewnętrzny.
7. **Równowaga.** Inteligencja zbiorowości jest największa, gdy stosunek korelacji jest bliski 1, a osądy jej agentów pozostają niezależne: wspólny kod bez wspólnych przekonań.

## Jak dobrze zdefiniowany jest każdy element?

Ramy są tylko tak dobre, jak ich najsłabsza definicja. Ta tabela to uczciwy rachunek.

| Wielkość | Stan |
| --- | --- |
| N, d, L, v, t_x, P | mierzone rutynowo |
| c, r dla neuronów, mowy, tańców | zmierzone w konkretnych układach |
| R_in, R_out dla człowieka | zmierzone, ze sporem o metodę |
| B, D dla mózgów i układów scalonych | oszacowane z anatomii |
| Liczba spójności, czas poznawczy | obliczalne z powyższych |
| Stosunek korelacji | zmierzony w stadach i w korze |
| Liczba myślenia do mówienia | tylko oszacowana; brak uzgodnionego sposobu mierzenia wewnętrznego przetwarzania agenta w bitach |
| Liczba graniczna | tylko oszacowana |
| Liczba wymiany do dryfu | zmierzona w genetyce populacji; jeszcze nie dla języków ani organizacji |
| κ, wspólny kontekst | zdefiniowane; jeszcze niezmierzone w żadnej rzeczywistej parze |
| η | zdefiniowana dla zadań, które sprowadzają się do usuwania niepewności; brak ogólnej miary osiągnięcia |
| C dla umysłu sfederowanego | niedobrze zdefiniowana; nie jest jasne, co znaczy „zaangażować w jedną decyzję”, gdy nic nie jest rozgłaszane |

Praca do wykonania jest w czterech dolnych wierszach.

## Czego brakuje

Sześć rzeczy dzieli te ramy od pełnej teorii fizycznej.

**Równania ruchu.** Termodynamika mówi, które stany są możliwe. Dopiero mechanika statystyczna powiedziała, jak układy się między nimi przemieszczają. Te ramy mają granice i stosunki. Nie mają jeszcze równań, które biorą zmienne zbiorowości w jednej chwili i dają je w następnej. Modele gromadzenia i hamowania z rozdziału 1 są takimi równaniami dla jednego rodzaju decyzji i są naturalnym punktem wyjścia.

**Wyprowadzenie progów.** Teoria mówi, że liczba spójności musi być „dużo większa” od 1, a liczba graniczna „dużo mniejsza”. Gotowa teoria powiedziałaby, o ile i dlaczego, tak jak teoria przejść fazowych podaje dokładną temperaturę wrzenia wody.

**Definicje operacyjne dla czterech ostatnich wierszy** powyższej tabeli.

**Zmienna dla repertuaru.** Rozdział 13 pokaże, że ramy zastosowane do rzeczywistego mózgu wyjaśniają jego kształt, a mocno zaniżają jego masę, bo nic na powyższej liście nie mówi, do ilu różnych zadań umysł musi być gotowy.

**Miara niezależności.** Samo wzmocnienie kontekstowe κ nie oddziela wspólnego kodu od wspólnych przekonań. Pełny zestaw czystych liczb wymaga jawnej miary tego, jak niezależne pozostają błędy agentów pod warunkiem stanu świata (za pomocą narzędzi takich jak warunkowa informacja wzajemna albo częściowa dekompozycja informacji), co zamieniłoby regułę „dziel się kodem, nie przekonaniami” w ilościowy diagram fazowy.

**Zgodność celów agentów.** Powyższe zmienne zakładają współpracujących agentów o wspólnym celu, takich jak neurony albo klonalne pszczoły. Na rynkach, w organizacjach i w ekosystemach częściowo wrodzy sobie agenci zatajają informację, blefują albo przejmują wspólne kody, dodając tarcie opisywane przez teorię gier, które obniża efektywną przepustowość kanału i wymusza kosztowne sygnalizowanie.

Żadna z tych rzeczy nie jest poza zasięgiem. Każdą można zaatakować symulacją komputerową kilku tysięcy prostych agentów, w której każdą zmienną z tego rozdziału da się ustawić, a każdą czystą liczbę dokładnie zmierzyć. To prawdopodobnie najbardziej użyteczna pojedyncza praca, jakiej teoria teraz potrzebuje.

## W skrócie

- Teoria używa czterech wymiarów, bita, sekundy, metra i dżula, i opisuje umysł zbiorowy kilkunastoma zmiennymi.
- Buduje z nich wielkości pochodne, w tym czas przejścia, wymianę w poprzek, moc przerobową, sprawność i wzmocnienie kontekstowe, oraz dziesięć czystych liczb.
- Do każdego umysłu stosuje się pięć granic z ustalonej fizyki: cena bita, zwrot z bita, przepustowość kanału, prędkość sygnału i maksymalna szybkość zmian.
- Zależności skalowania mówią, jak wymiana w poprzek, opóźnienie, okablowanie i koszt zmieniają się z rozmiarem.
- Własne twierdzenia teorii to siedem zależności, wśród nich to, że wynik to moc przerobowa razy sprawność, że jedność jest stosunkiem temp i że umysły o tych samych czystych liczbach myślą podobnie.
- Kilku wielkości nie da się jeszcze zmierzyć, a ramom brakuje równań ruchu i wyprowadzonych progów.

## Jak możemy się mylić

Ramy tego rodzaju zawodzą w szczególny sposób: nie przez to, że coś im zaprzecza, lecz przez to, że są bezużyteczne. Jeśli wymienione tu czyste liczby nie sortują rzeczywistych zbiorowości w grupy, które zachowują się podobnie, tak że układy o zgodnych liczbach się różnią, a układy o różnych liczbach się zgadzają, to wybór zmiennych jest zły, jakkolwiek rozsądnie każda wyglądała. Jeśli wielkościom z dolnych wierszy tabeli stanu nie da się nadać definicji, według których różni badacze mierzą tak samo, głównego wzoru nie można sprawdzić. A jeśli symulacja prostych agentów pokaże, że zachowanie silnie zależy od szczegółów, które ramy pomijają, takich jak dokładna reguła, której trzyma się każdy agent, to opis kilkunastoma liczbami jest zbyt zgrubny, a umysły nie są rzeczami tego rodzaju, jakie potrafią uchwycić teorie w stylu termodynamiki.

## Źródła

1. A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider and E. Lutz (2012), "Experimental verification of Landauer's principle linking information and thermodynamics", *Nature* 483:187–189. https://pubmed.ncbi.nlm.nih.gov/22398556/
2. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
3. R. Landauer (1961), "Irreversibility and heat generation in the computing process", *IBM Journal of Research and Development* 5:183–191.
4. C. E. Shannon (1948), "A mathematical theory of communication", *Bell System Technical Journal* 27:379–423 i 623–656.
5. N. Margolus and L. B. Levitin (1998), "The maximum speed of dynamical evolution", *Physica D* 120:188–195.
6. S. Lloyd (2000), "Ultimate physical limits to computation", *Nature* 406:1047–1054. https://arxiv.org/abs/quant-ph/9908043
7. D. S. Bassett et al. (2010), "Efficient physical embedding of topologically complex information processing networks in brains and computer circuits", *PLOS Computational Biology* 6:e1000748. https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671
8. K. Zhang and T. J. Sejnowski (2000), "A universal scaling law between gray matter and white matter of cerebral cortex", *PNAS* 97:5621–5626. https://pmc.ncbi.nlm.nih.gov/articles/PMC25878
9. S. B. Laughlin, R. R. de Ruyter van Steveninck and J. C. Anderson (1998), "The metabolic cost of neural information", *Nature Neuroscience* 1:36–41. https://doi.org/10.1038/236
10. S. Herculano-Houzel (2011), "Scaling of brain metabolism with a fixed energy budget per neuron: implications for neuronal activity, plasticity and evolution", *PLoS ONE* 6:e17514. https://pmc.ncbi.nlm.nih.gov/articles/PMC3046985

Przykładowe wartości w tabeli zmiennych to nasze własne zgrubne oszacowania, zaczerpnięte z wcześniejszych rozdziałów. Wybór zmiennych, definicje mocy przerobowej, znaczenia i czystych liczb, siedem zależności oraz ocena tego, czego brakuje, pochodzą od samej teorii.
