<!-- Przekład pliku book/ch03-what-is-an-agent.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 3. Czym jest agent?

## Najskromniejszy agent na ścianie

Termostat w twoim przedpokoju jest zaskakująco pełnym przykładem tego, co ta książka nazywa agentem. Ma pamięć: temperaturę docelową, którą ustawiłeś. Ma wejście: czujnik, który mierzy powietrze. Ma regułę, która zamienia to, co wyczuwa, i to, co pamięta, w decyzję: jeśli w pokoju jest zimniej, niż ustawiono, włącz. I ma wyjście: sygnał do kotła.

Te cztery części to cała definicja.

- **Pamięć**: stan wewnętrzny, który trwa, mierzony w bitach.
- **Wejścia**: kanały, przez które świat albo inni agenci wpływają na ten stan.
- **Reguła przetwarzania**: sposób, w jaki wejście i pamięć łączą się w nowy stan i wyjście.
- **Wyjścia**: kanały, przez które agent wpływa na świat albo na innych agentów.

Agent ma też granicę, linię między wnętrzem a zewnętrzem. W języku statystyki to, co dzieje się w środku, jest odsłonięte od zewnętrza przez wejścia i wyjścia agenta. Żeby wiedzieć, co zrobi termostat, trzeba znać jego nastawę i odczyt jego czujnika, i nic więcej o domu.

Czy termostat jest inteligentny? W jednym wąskim sensie jest bardzo sprawny: osiąga swój jedyny cel, nie potrzebując prawie żadnej informacji. Ale nie umie nic innego i nie potrafi się uczyć. Termostat pokazuje, że bycie agentem jest tanie. Inteligencja to coś, co dzieje się, gdy wielu agentów połączy się we właściwy sposób, a większość tej książki mówi o tym, co znaczy „we właściwy sposób”.

## Neuron

Neuron jest agentem znacznie bogatszym. Mózg człowieka zawiera ich około 86 miliardów (1). Każdy słucha tysięcy innych przez synapsy, łączy to, co słyszy, w swoich rozgałęzionych dendrytach i wiele razy na sekundę decyduje, czy wysłać impuls wzdłuż aksonu.

Jego pamięć mieści się głównie w synapsach: w tym, jak mocno każdemu wejściu wolno na niego wpływać. Te siły nie są dowolne. W 2015 roku zespół z Instytutu Salka zrekonstruował mały sześcian tkanki mózgu szczura z rozdzielczością nanometrową. Badacze znaleźli pary synaps łączących ten sam akson z tym samym dendrytem i porównali ich rozmiary, które odzwierciedlają ich siłę. Z dokładności dopasowania oszacowali, że istnieje co najmniej 26 rozróżnialnych sił synaptycznych, czyli około 4,7 bita informacji na synapsę (2).

Mózg człowieka, mający od stu bilionów do tysiąca bilionów synaps, może przechowywać rzędu 10¹⁵ bitów. To liczba zgrubna, ale daje agentowi zwanemu neuronem mierzalną pamięć, tak jak termostat ma swoją nastawę.

## Umysł bez mózgu

Jeśli neuron wydaje się zbyt oczywiście podobny do umysłu, weźmy śluzowca *Physarum polycephalum*. To pojedyncza komórka, żółta plama, która potrafi rozlać się po powierzchni i nie ma ani jednego neuronu. Porusza się, rozbudowując sieć rurek: pogrubia te, którymi płynie najwięcej, a pozostałym pozwala uschnąć.

W 2010 roku Atsushi Tero ze współpracownikami z Uniwersytetu Hokkaido rozłożył na mokrej szalce płatki owsiane w położeniach miast wokół Tokio, umieścił śluzowca w punkcie oznaczonym „Tokio” i użył jasnego światła, którego śluzowiec unika, w zastępstwie gór i jezior. Śluzowiec najpierw rozlał się we wszystkich kierunkach. Potem przyciął sam siebie do sieci rurek łączących płatki. Wynik miał koszt, sprawność i odporność na awarie porównywalne z prawdziwą siecią kolejową Tokio, której zaplanowanie zajęło inżynierom dziesięciolecia (3, 4).

Śluzowiec nie ma planisty ani mapy. Kładzie rurki wszędzie, wzmacnia to, co działa, i przycina to, co nie działa. Jest w pewnym sensie także zbiorowością: ogromną siecią odcinków rurek, z których każdy reaguje na lokalny przepływ, a których łączne zachowanie rozwiązuje problem, jakiego żaden z nich nie widzi.

Wskazuje to na ważną cechę agentów: **zagnieżdżają się**. Cząsteczka może być częścią komórki, komórka częścią pszczoły, pszczoła częścią roju. To, czy coś nazwiemy „agentem”, czy „zbiorowością agentów”, zależy od poziomu, na którym patrzymy. Rozdział 11 podaje sposób, żeby naturalne poziomy znajdować w danych, a nie wybierać je ręcznie.

## Nie każdy tłum jest umysłem

Gdyby inteligencja brała się po prostu z wielu oddziałujących części, najinteligentniejszą rzeczą w twojej kuchni byłoby powietrze. Litr powietrza zawiera około 10²² cząsteczek, które zderzają się miliardy razy na sekundę, a każde zderzenie jest wymianą informacji o położeniu i prędkości. A jednak powietrze nie myśli.

Nie myśli, bo brakuje mu trzech rzeczy, których agenci potrzebują.

1. **Trwała pamięć.** Cząsteczka gazu niemal natychmiast zapomina swoją historię. Każde zderzenie miesza jej stan. Nic nie zostaje zapisane.
2. **Wybiórcza komunikacja.** Cząsteczka oddziałuje z czymkolwiek, na co wpadnie. Nie ma struktury, nie ma preferencji, nie ma kanału, który niósłby jedną wiadomość zamiast innej.
3. **Przepływ energii.** Gaz pozostawiony sam sobie dochodzi do równowagi, stanu największego nieuporządkowania, i w nim zostaje. Żywy agent jest natomiast stale zasilany energią, która trzyma go daleko od równowagi, tak że może utrzymywać pamięć i wykonywać pracę.

Rozważmy teraz przeciwną skrajność: kryształ. Jego atomy są zamknięte w doskonałej sieci. Położenie każdego atomu jest skorelowane z położeniem każdego innego. Jest tu, w pewnym sensie, pamięć i jest mnóstwo porządku. Ale nie ma swobody. Nic nie może się zmienić, jeśli nie zmieni się wszystko. Kryształ ma nie więcej umysłu niż gaz.

Inteligencja wydaje się mieszkać między tymi skrajnościami: między chaosem gazu a sztywnością kryształu. Fizycy nazywają granicę między porządkiem a nieporządkiem **punktem krytycznym**, a układy, które się tam znajdują, mają szczególny znak rozpoznawczy. Aktywność rozchodzi się kaskadami wszelkich rozmiarów, bez typowej skali.

Mózg wykazuje dokładnie ten znak rozpoznawczy. W 2003 roku John Beggs i Dietmar Plenz zarejestrowali spontaniczną aktywność w skrawkach kory szczura. Serie wyładowań rozchodziły się po tkance jak lawiny. Ich rozmiary podlegały prawu potęgowemu z wykładnikiem −3/2, czyli wartością przewidywaną dla układu zrównoważonego w punkcie krytycznym, w którym każdy aktywny neuron pobudza średnio dokładnie jeden inny (5).

## Kiedy mózgi wypadają z równowagi

Awarie samego mózgu pokazują, co się dzieje, gdy zsuwa się on z tej równowagi w jedną albo w drugą stronę.

**Za dużo sprzężenia.** W napadzie padaczkowym wielkie populacje neuronów wyładowują się równym krokiem. Komunikacja jest maksymalna, każdy zgadza się z każdym. I myślenie ustaje. Napad może całkowicie znieść świadomość, ponieważ mózg, w którym każdy neuron robi to samo, jest informacyjnie jednym neuronem powtórzonym miliardy razy. To neuronalna wersja tłumu, którego wszystkie oszacowania zbiegają się na jednej błędnej odpowiedzi.

**Za mało integracji.** W znieczuleniu ogólnym i w głębokim śnie bez marzeń sennych dzieje się coś odwrotnego. Neurony wciąż się wyładowują, ale aktywność pozostaje lokalna. Obszary przestają wymieniać się informacją.

Tę różnicę da się dziś zmierzyć. Zespół kierowany przez Marcella Massiminiego opracował test, w którym do skóry głowy przykłada się krótki impuls magnetyczny i rejestruje elektryczne „echo” mózgu. U osoby przytomnej echo rozchodzi się szeroko i przybiera złożony, zróżnicowany kształt: jest zintegrowane *i* zróżnicowane. W głębokim śnie, w znieczuleniu albo w śpiączce echo jest albo lokalne, albo jednorodne (6, 7). Jedna liczba obliczona z echa, wskaźnik złożoności perturbacyjnej, rozdziela te stany zadziwiająco dobrze i u niektórych niereagujących pacjentów wskazała możliwą ukrytą zdolność do świadomości (7, 8).

## Czego potrzebuje agent, a czego umysł

Zbierzmy to razem:

- **Agent** potrzebuje trwałej pamięci, wybiórczych wejść i wyjść, reguły przetwarzania oraz dopływu energii, który trzyma go z dala od równowagi. Warunki te spełniają termostaty, neurony, pszczoły i rurki śluzowca.
- **Umysł zbudowany z agentów** potrzebuje, żeby ci agenci byli sprzężeni na tyle, by się integrować, tak aby informacja z jednej części mogła dotrzeć do pozostałych i je zmienić. Muszą jednak pozostać na tyle niezależni, by się różnić, tak aby całość mogła przedstawiać wiele odrębnych stanów. Zbyt silne sprzężenie daje napad padaczkowy albo komorę pogłosową, zbyt słabe daje odłamki.

Rój z rozdziału 1 mieści się w tym oknie: zwiadowczynie wymieniają się informacją przez tańce, ale każda sama ogląda miejsca. Mieści się w nim też mózg, zawieszony w pobliżu punktu krytycznego. Część II zamienia ten jakościowy obraz w liczby.

## W skrócie

- Agent to ograniczony układ z pamięcią, wejściami, regułą przetwarzania i wyjściami. Agenci mogą być bardzo prości.
- Pamięć neuronu jest mierzalna: około 4,7 bita na synapsę według jednego starannego badania.
- Jednokomórkowy śluzowiec potrafi zaprojektować sieć równie dobrą jak kolej zaprojektowana przez inżynierów, co pokazuje, że inteligentne zachowanie nie wymaga neuronów i że agenci zagnieżdżają się jedni w drugich.
- Wiele oddziałujących części to za mało. Gazowi brakuje trwałej pamięci, wybiórczej komunikacji i przepływu energii, kryształowi brakuje swobody.
- Umysły wydają się działać w pobliżu punktu krytycznego między porządkiem a nieporządkiem. Napady padaczkowe (za dużo sprzężenia) i znieczulenie (za mało integracji) znoszą świadomość, a różnicę między nimi da się zmierzyć.

## Jak możemy się mylić

Twierdzenie, że umysły potrzebują krytyczności, zostałoby osłabione, gdyby się okazało, że dobrze działające mózgi pracują daleko od punktu krytycznego albo że lawiny o rozkładzie potęgowym powstają równie łatwo w układach bez żadnej szczególnej równowagi. Niektórzy badacze opowiadają się za tym drugim. Twierdzenie, że gaz nie jest umysłem, jest bezpieczne. Trudniejsze pytanie brzmi, gdzie dokładnie przebiega linia, a do tego potrzeba miar z części II.

## Źródła

1. F. A. C. Azevedo et al. (2009), "Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain", *Journal of Comparative Neurology* 513:532–541. https://pubmed.ncbi.nlm.nih.gov/19226510/
2. T. M. Bartol et al. (2015), "Nanoconnectomic upper bound on the variability of synaptic plasticity", *eLife* 4:e10778. https://elifesciences.org/articles/10778v1
3. A. Tero, S. Takagi, T. Saigusa, K. Ito, D. P. Bebber, M. D. Fricker, K. Yumiki, R. Kobayashi and T. Nakagaki (2010), "Rules for biologically inspired adaptive network design", *Science* 327:439–442. https://pubmed.ncbi.nlm.nih.gov/20093467/
4. E. Yong, opis doświadczenia z pozycji 3, *National Geographic*. https://www.nationalgeographic.com/science/article/slime-mould-attacks-simulates-tokyo-rail-network
5. J. M. Beggs and D. Plenz (2003), "Neuronal avalanches in neocortical circuits", *Journal of Neuroscience* 23:11167–11177. https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045
6. M. Massimini, F. Ferrarelli, R. Huber, S. K. Esser, H. Singh and G. Tononi (2005), "Breakdown of cortical effective connectivity during sleep", *Science* 309:2228–2232.
7. A. G. Casali et al. (2013), "A theoretically based index of consciousness independent of sensory processing and behavior", *Science Translational Medicine* 5:198ra105. https://orbi.uliege.be/handle/2268/171542
8. D. O. Sinitsyn et al. (2020), "Detecting the potential for consciousness in unresponsive patients using the perturbational complexity index", *Brain Sciences* 10:917. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7760168/

Liczby podane bez numeru źródła to nasze własne zgrubne oszacowania albo wartości standardowe: liczba synaps, całkowita pojemność pamięci mózgu oraz liczba cząsteczek w litrze powietrza.
