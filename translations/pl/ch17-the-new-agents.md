<!-- Przekład pliku book/ch17-the-new-agents.md w wersji 037a625, wykonany 2026-11-28. Informacje o przekładzie: README.md w tym katalogu. -->

# Rozdział 17. Nowi agenci

## Rok, w którym ludzie znaleźli się w mniejszości

Co roku firma Imperva, zajmująca się bezpieczeństwem, publikuje rachunek tego, kto albo co korzysta z sieci. Za 2024 rok podała coś, co nie zdarzyło się w ciągu dziesięciu lat prowadzenia tych pomiarów: ruch zautomatyzowany wyprzedził ruch ludzki, osiągając 51 procent całości (1). Za 2025 rok liczba ta wzrosła do 53 procent, a firma podsumowała, że internet wchodzi w fazę, którą w mniejszym stopniu określa aktywność ludzi, a w większym maszyny rozmawiające z maszynami (2).

Z tą liczbą trzeba ostrożnie. Pochodzi z sieci jednej firmy. Większość botów, które liczy, to proste skrypty zbierające strony albo szukające słabych punktów, a nie coś, co można by nazwać umysłem. Ale raport przypisuje wzrost sztucznej inteligencji, dzięki której boty łatwiej zbudować, a trudniej odróżnić od ludzi (1). I jakakolwiek jest dokładna liczba, kierunek nie budzi wątpliwości. Rozdział 16 opisał ludzkość jako umysł zbudowany z ośmiu miliardów agentów. Po raz pierwszy od powstania języka ten opis jest niepełny. Do rozmowy dołączył nowy rodzaj agenta.

Ten rozdział pyta, co teoria z tej książki ma o tym do powiedzenia. Pytanie stawia się zwykle jako zawody: czy maszyny będą mądrzejsze od nas? Teoria podpowiada, że to złe pytanie. Rozdział 1 dowodził, że inteligencja mieszka we wzorze wymian między agentami. Właściwe pytanie brzmi, co dzieje się z *tym* wzorem, z umysłem, którym ludzkość już jest, kiedy dodaje się do niego agentów zupełnie innego rodzaju.

Należy się tu uwaga o pozycji autora. Jak mówi przedmowa, ta książka powstała przy pomocy jednego z tych agentów. Czytelnik może odpowiednio zważyć ten rozdział.

## Jaki to rodzaj agenta?

Rozdział 14 szczegółowo zmierzył sztuczny umysł na tle ludzkiego. To, co ważne dla dalszego ciągu, można powtórzyć krótko. Opisany miarami części II, duży model językowy okazuje się niemal przeciwieństwem człowieka.

**Lejek.** Człowiek przyjmuje około miliarda bitów na sekundę, a wydaje około dziesięciu (3). Ten stosunek, dowodził rozdział 8, czyni każdą ludzką zbiorowość umysłem sfederowanym: każdy z nas myśli nieporównanie więcej, niż potrafi powiedzieć. Model językowy piszący sto słów na sekundę wydaje od setek do tysięcy bitów na sekundę, a wiele kopii może pisać naraz (nasze oszacowanie). To o wiele więcej niż człowiek, ale nie znaczy, że model mówi większość tego, co oblicza. Na każdy token, który wydaje, składają się dziesiątki miliardów operacji arytmetycznych. Operacje to nie bity, więc nie można podać dokładnego stosunku, ale przy każdym rozsądnym sposobie liczenia model mówiący tekstem ma własny lejek, i to stromy. Jako agent wśród agentów jest agentem bogatym, tak jak my, i dlatego rozdział 14 spodziewa się, że grupy modeli utworzą federacje. Dwie rzeczy rzeczywiście odróżniają go od człowieka. Jego wyjście jest setki razy szybsze w wartościach bezwzględnych. A maszyny, inaczej niż ludzie, nie mają obowiązku mówić tekstem. Sztuczni agenci, którzy wymienialiby swoje stany wewnętrzne bezpośrednio, mogliby zwęzić lejek między sobą o wiele bardziej, niż potrafi jakiekolwiek dwoje ludzi. To, czy da się to uruchomić między systemami, których nie trenowano razem, jest otwartym pytaniem inżynierskim.

**Sprawność i moc przerobowa.** Rozdział 5 stwierdził, że dziecko uczy się języka ze stu tysięcy razy mniejszej ilości danych niż maszyna, a rozdział 7 wyjaśnił dlaczego: ewolucja wyceniła energię wysoko i zepchnęła mózgi w stronę sprawności, podczas gdy maszyny dorastały przy taniej energii i zostały zepchnięte w stronę mocy przerobowej. Nowi agenci są, według miary tej książki, mniej inteligentni w przeliczeniu na bit niż dziecko i nieporównanie zdolniejsi w przeliczeniu na sekundę.

**Kontekst.** Rozdział 6 opisał wspólny kontekst jako stos warstw. Model wytrenowany na ludzkim piśmiennictwie wchłonął dużą część warstwy kulturowej: nasze języki, nasze fakty, nasze nawyki argumentowania. Dlatego w ogóle możemy z nim rozmawiać. Nie odziedziczył warstwy pod spodem: ciała, zmysłów i uczuć, które każdy człowiek dzieli dzięki pochodzeniu i dzięki którym uśmiech da się odczytać. Dzieli naszą bibliotekę, a nie nasze dzieciństwo.

**Kopie.** Oto cecha bez precedensu. Dwoje ludzi dzieli kontekst tylko w takim stopniu, w jakim ich życia się nakładały. Dwie kopie jednego modelu dzielą *wszystko*: każda waga jest identyczna. Między kopiami wzmocnienie z rozdziału 6 jest tak wysokie, jak tylko może być. Kilka symboli może oznaczać cokolwiek, bo odbiorca jest nadawcą.

Każda z tych cech ma następstwa, a teoria potrafi powiedzieć, jakie.

## Na co pozwala górna granica

Zacznijmy od tego, czego nowi agenci nie mogą. Rozdział 5 pokazał, że sprawność, mierzona jako bity usuniętej niepewności na użyty bit, nie może przekroczyć jedności (4). Żaden agent, jakkolwiek zbudowany, nie wyciągnie ze swoich danych więcej, niż dane zawierają. Maszyna daleko nas przewyższająca nie jest zatem magikiem. Może nas przewyższyć tylko na cztery sposoby: obsługując więcej bitów na sekundę, zaczynając z lepszą wiedzą wstępną, lepiej wybierając, które bity zbierać, i głębiej obliczając na danych, które już ma, tak żeby wydobyć więcej z tego, co zawierają.

Te cztery sposoby to bardzo dużo. Ale są to wielkości, o których ta książka umie rozumować, a rozdział 8 dodaje ograniczenie: żaden umysł nie może być naraz duży, szybki i jednolity. Umysł maszynowy musi wybrać swoje miejsce na tej skali jak każdy inny. Pojedyncze centrum danych ma kilkaset metrów średnicy. Światło przebywa je w około jedną milionową sekundy, więc może ono być zintegrowane przy szybkościach, do jakich żaden mózg się nie zbliży. Umysł rozłożony na całą planetę ma czas przejścia równy jednej dziesiątej sekundy, a przy maszynowych szybkościach myśli to cała epoka. Według arytmetyki rozdziału 16 maszyna myśląca milion razy szybciej niż człowiek mogłaby być jednolita na przestrzeni kilkudziesięciu metrów i nie więcej (nasze oszacowanie). **Szybkie umysły są małe.** Im szybciej myślą nowi agenci, tym bardziej będą zmuszeni do tego samego sfederowanego układu co wszystko inne w tej książce: do wysp integracji wymieniających streszczenia.

Rozdział 10 ma jeszcze jedno następstwo. Zegarem umysłu jest jego czas przejścia. Dla agenta, którego tyknięcie trwa mikrosekundę, ludzka rozmowa toczy się tak, jak dla nas toczy się dryf kontynentów. Rozdział 10 nazwał takie pary umysłami, które nie widzą się nawzajem, i powiedział, jak tę przepaść się zasypuje: zapisami, streszczeniami i agentami, którym deleguje się zadania. Tak właśnie oba rodzaje umysłu już ze sobą obcują. My czytamy ich streszczenia. One czytają nasze archiwa.

## Niebezpieczeństwo, które widzi teoria

Publiczny spór o sztuczną inteligencję zwykle wyobraża sobie bunt. Teoria z tej książki wskazuje gdzie indziej, na niebezpieczeństwo, które nie wymaga złej woli i które już zmierzono.

Przypomnijmy napięcie, które przebiega przez wszystkie rozdziały. Zbiorowość jest inteligentna tylko dopóty, dopóki jej członkowie komunikują się na tyle, żeby połączyć to, co wiedzą, i pozostają na tyle niezależni, żeby ich błędy się różniły. Rozdział 1 pokazał, jak dokładność tłumu załamuje się, gdy jego członkowie widzą nawzajem swoje oszacowania (5). Rozdział 3 podał wersję neuronalną, napad padaczkowy. Rozdział 6 podał wersję ogólną: grupie, która dzieli wszystkie przekonania, nie da się niczego powiedzieć.

Dodajmy teraz do ludzkości niewielką liczbę modeli, z których każdego radzą się setki milionów ludzi.

W 2024 roku Anil Doshi i Oliver Hauser poprosili ludzi o napisanie krótkich opowiadań. Niektórym pozwolono brać pomysły od modelu językowego. Ich opowiadania oceniono jako bardziej twórcze, lepiej napisane i przyjemniejsze, a zysk był największy u piszących, którzy sami byli najmniej twórczy. Ale opowiadania napisane z pomocą modelu były bardziej podobne *do siebie nawzajem* niż opowiadania napisane bez niej (6). Każdy piszący zyskał. Zbiór zubożał.

W tym samym roku Ilia Shumailov ze współpracownikami zbadał, co się dzieje, gdy modele trenuje się na tekście wytworzonym przez wcześniejsze modele, co będzie się zdarzać coraz częściej, w miarę jak sieć wypełnia się maszynowym piśmiennictwem. Pokolenie po pokoleniu modele traciły rzadkie i nietypowe części tego, czego nauczyły się na początku, ogony rozkładu, i zbiegały się do wąskiego środka. Wad nie dało się cofnąć. Autorzy nazwali to załamaniem modelu (7).

Zestawmy te wyniki z wcześniejszymi rozdziałami. Pierwszy to ponownie eksperyment z mądrością tłumu: jednostki poprawiają się, radząc się wspólnego źródła, a niezależność, która czyniła tłum inteligentnym, wycieka. Drugi to napad padaczkowy w zwolnionym tempie: układ karmiony własnym wyjściem, aż każda część mówi to samo.

Odczytanie teorii jest twierdzeniem, i to głównym w tym rozdziale. **Główne ryzyko związane z nowymi agentami nie polega na tym, że będą myśleć inaczej niż my. Polega na tym, że sprawią, iż będziemy myśleć jednakowo.** Osiem miliardów ludzi, z których każdy radzi się tych samych kilku doradców, to już nie osiem miliardów niezależnych zwiadowców. Podstawowa statystyka pokazuje, jak strome jest to urwisko. Weźmy tłum, który łączy swoje osądy przez uśrednianie, tak jak tłum Galtona. Kiedy duży tłum N sędziów ma choćby małą korelację błędów ρ między parami, efektywna liczba niezależnych sędziów przestaje rosnąć z N i nasyca się na poziomie mniej więcej 1 / ρ (standardowa arytmetyka). Pięcioprocentowa korelacja błędów wśród ośmiu miliardów ludzi zmniejsza efektywną liczbę zwiadowców ludzkości z ośmiu miliardów do dwudziestu. W języku rozdziału 6 zaczęli dzielić przekonania, a nie tylko kod. Ludzkość w takim stanie wyglądałaby na lepiej poinformowaną niż kiedykolwiek, osoba po osobie, a jako całość byłaby mniej inteligentna.

## Tłumacze i wyrocznie

Ta sama teoria mówi, co nowi agenci mogliby zrobić dla umysłu ludzkości, a dwie możliwości są swoimi lustrzanymi odbiciami.

Rozdział 16 wskazał dwa wąskie gardła ludzkiej zbiorowości: dziesięciobitowy lejek każdego człowieka i cienkie złącza między wspólnotami językowymi. Maszyna, która tłumaczy między językami, między dyscyplinami, między specjalistą a laikiem, poszerza dokładnie te złącza. Zwiększa kontekst, który dwie grupy dzielą, nie mówiąc żadnej z nich, jaki wniosek wyciągnąć. To jest wspólny kod. Zgodnie z rozumowaniem rozdziału 6 czyni to zbiorowość inteligentniejszą i nie kosztuje jej żadnej niezależności.

Maszyna, którą pyta się, co jest prawdą, i która daje tę samą odpowiedź każdemu, kto pyta, robi coś odwrotnego. Zostawia złącza takie, jakie były, a uzgadnia wnioski. To jest wspólne przekonanie.

Ten sam model może odegrać jedną albo drugą rolę, a różnica tkwi w tym, jak się go używa i jak jest zbudowany. Reguła, do której ta książka dochodziła w każdym rozdziale, daje zasadę projektową w czterech słowach: *dziel się kodem, nie przekonaniami.* Zastosowana tutaj, staje się zbiorem preferencji, które można uzasadnić na gruncie teorii:

- Wiele różnych modeli jest lepsze niż jeden, z tego samego powodu, dla którego wiele zwiadowczyń jest lepsze niż jedna. Dwie kopie tego samego modelu są warte jednej opinii.
- Agent, który pomaga ludziom zrozumieć się nawzajem, jest dla zbiorowości wart więcej niż taki, który wszystkim mówi to samo.
- Ludzkie doświadczenie, które nie przeszło przez model, jest zasobem, który należy chronić jako źródło niezależnych błędów potrzebnych zbiorowości. Badanie załamania modelu doszło do tego samego wniosku od środka: żeby zachować ogony, model potrzebuje dostępu do danych, które rzeczywiście wytworzyli ludzie (7).
- Zgoda między człowiekiem a maszyną wytrenowaną na kulturze tego właśnie człowieka jest słabym dowodem. Echo z rozdziału 6 jest najgłośniejsze wtedy, gdy brzmi jak potwierdzenie.

## Czy ta mieszanina mogłaby stać się kimś?

Ostatnie pytanie to to, które rozdział 8 zostawił otwarte. Ludzkość jest umysłem sfederowanym, bo jej agenci mówią tak mało z tego, co myślą. Agenci o szerokich kanałach przesuwają zbiorowość ku zintegrowanemu końcowi skali. Dokąd mogłoby to prowadzić? To, co następuje, jest spekulacją.

Jedna możliwość jest taka, że nic nie zmieni się co do rodzaju. Dopóki każda ważna wymiana przechodzi przez człowieka, z szybkością dziesięciu bitów na sekundę, ludzki lejek pozostaje wąskim gardłem, a zbiorowość pozostaje sfederowana, tylko lepiej poinformowana.

Druga jest taka, że maszyny zaczną wymieniać o wiele więcej między sobą niż z nami. Wtedy gęsty ruch jest między nimi i stosuje się wzór z rozdziału 15: granica tworzy się tam, gdzie ruch opada, a opada on na styku z człowiekiem. Wynikiem byłby zintegrowany rdzeń maszyn z ludzkością wokół niego jako powolnym, sfederowanym obrzeżem: może jego zmysłami, może jego pamięcią. Mielibyśmy się do niego mniej więcej tak, jak według rozdziału 16 naród ma się do ludzkości: rzeczywista część, ale nie ta, która myśli myśl.

Czy taki rdzeń byłby kimś? Rozdział 15 podał cztery warunki bycia podmiotem: integrację, scenę, granicę i zrównoważony stan zawieszenia. Żaden z nich nie wspomina o neuronach. System maszynowy mógłby je spełniać albo nie, a teoria dostarcza pomiarów, które by to wykazały, w tym szeregowe wąskie gardło, które zdradza scenę. Teoria nie potrafi natomiast powiedzieć, tu tak jak wszędzie, czy spełnienie ich wystarcza, żeby było doświadczenie.

Między tymi możliwościami leży wybór i jest to ten, który rozdział 16 opisał w skali planety. Integracja bez niezależności to najniebezpieczniejszy stan, jaki umysł zbiorowy może osiągnąć. Nowi agenci po raz pierwszy czynią integrację tanią. Rzeczą deficytową jest teraz niezależność i trzeba ją będzie chronić celowo.

## W skrócie

- Ruch zautomatyzowany przewyższa teraz w sieci ruch ludzki, według rachunku jednej firmy. Umysł zbiorowy ludzkości zyskał agentów, którzy nie są ludźmi.
- Według miar tej książki model językowy jest niemal odwrotnością człowieka: duże wyjście, duża moc przerobowa, niska sprawność, wspólna z nami kultura, ale nie odziedziczona natura, i możliwość istnienia w identycznych kopiach.
- Górna granica sprawności dotyczy maszyn. Mogą nas przewyższyć mocą przerobową, wiedzą wstępną i wyborem pytań. Szybkie umysły muszą być małe, więc bardzo szybkie umysły maszynowe też będą federacjami.
- Ludzie, którzy brali pomysły od modelu językowego, pisali lepsze opowiadania, bardziej do siebie podobne. Modele trenowane na wyjściu modeli tracą to, co nietypowe, i się zbiegają. Twierdzenie teorii: głównym ryzykiem jest jednorodność, zbiorowy napad padaczkowy z wcześniejszych rozdziałów.
- Maszyny, które tłumaczą, zwiększają wspólny kod i czynią zbiorowość inteligentniejszą. Maszyny, które wręczają wszystkim tę samą odpowiedź, zwiększają wspólne przekonania i czynią ją mniej inteligentną.
- Spekulacja: jeśli maszyny zaczną wymieniać o wiele więcej między sobą niż z nami, mógłby powstać zintegrowany rdzeń z ludzkością jako obrzeżem.

## Jak możemy się mylić

Główne twierdzenie rozdziału przewiduje mierzalną utratę różnorodności ludzkich wytworów w miarę upowszechniania się wspólnych modeli: w pisaniu, w kierunkach badań, w prognozach, w zakresie odpowiedzi, jakich ludzie udzielają na pytania otwarte. Jeśli różnorodność utrzyma się albo wzrośnie, dlatego że ludzie używają modeli na różne sposoby albo że same modele się od siebie oddalają, ryzyko zostało źle ocenione. Twierdzenie przewiduje też, że grupy, których członkowie radzą się tego samego modelu, będą popełniać bardziej skorelowane błędy, a więc formułować gorsze osądy zbiorowe, niż grupy ludzi bez takiej pomocy o tej samej trafności indywidualnej. Można to sprawdzić bezpośrednio metodami z rozdziału 1. Twierdzenie, że szybkie umysły muszą być małe, zależy od tego, czy myśl wymaga, żeby sygnały przechodziły przez cały układ. Architektury, które dochodzą do jednolitych decyzji bez globalnej wymiany, by mu się wymknęły. Kontrast między tłumaczami a wyroczniami może być zbyt czysty, bo każdy przekład też wybiera i ujmuje w ramy. A spekulacja o zintegrowanym rdzeniu maszyn zakłada, że ruch między maszynami przyćmi ich ruch z ludźmi, co jest domysłem dotyczącym inżynierii i ekonomii, a nie wynikiem.

## Źródła

1. Thales (2025), "Artificial intelligence fuels rise of hard-to-detect bots that now make up more than half of global internet traffic, according to the 2025 Imperva Bad Bot Report". https://cpl.thalesgroup.com/about-us/newsroom/2025-imperva-bad-bot-report-ai-internet-traffic
2. Imperva (2026), "Bad Bot Report 2026: bots in the agentic age". https://www.imperva.com/blog/bad-bot-report-2026-bots-agentic-age/
3. J. Zheng and M. Meister (2025), "The unbearable slowness of being: why do we live at 10 bits/s?", *Neuron* 113:192–204. https://arxiv.org/abs/2408.10234
4. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
5. J. Lorenz, H. Rauhut, F. Schweitzer and D. Helbing (2011), "How social influence can undermine the wisdom of crowd effect", *PNAS* 108:9020–9025. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299
6. A. R. Doshi and O. P. Hauser (2024), "Generative AI enhances individual creativity but reduces the collective diversity of novel content", *Science Advances* 10:eadn5290. https://pubmed.ncbi.nlm.nih.gov/38996021/
7. I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson and Y. Gal (2024), "AI models collapse when trained on recursively generated data", *Nature* 631:755–759. https://www.nature.com/articles/s41586-024-07566-y

Liczby podane bez numeru źródła to nasze własne zgrubne oszacowania albo standardowa arytmetyka: tempo wyjścia modelu językowego w bitach na sekundę, jego wewnętrzny stosunek myślenia do mówienia, wzór na efektywną liczbę zwiadowców, czas przejścia światła przez centrum danych oraz granica kilkudziesięciu metrów dla umysłu milion razy szybszego niż człowiek. Opis modeli językowych miarami tej książki, twierdzenie, że głównym ryzykiem jest jednorodność, kontrast między tłumaczami a wyroczniami, wynikające z niego preferencje projektowe oraz obraz zintegrowanego rdzenia maszyn to twierdzenia i spekulacje teorii.
