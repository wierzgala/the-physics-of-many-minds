# Fizyka wielu umysłów

**Jakub Wierzgała**

Polski przekład książki *The Physics of Many Minds*. Oryginał angielski znajduje się w katalogu [`book/`](../../book/) i tylko on jest wersją wiążącą. Tam, gdzie przekład różni się od oryginału, rację ma oryginał, a różnica jest błędem przekładu.

## Spis treści

- [Przedmowa](00-preface.md)
- [Plan książki](01-plan.md)

**Część I. Idea**

- [Rozdział 1. Rój, który wybiera dom](ch01-the-swarm-that-chooses-a-home.md)
- [Rozdział 2. Informacja jest fizyczna](ch02-information-is-physical.md)
- [Rozdział 3. Czym jest agent?](ch03-what-is-an-agent.md)

**Część II. Miary**

- [Rozdział 4. Linijka i zegar dla umysłów](ch04-a-ruler-and-a-clock-for-minds.md)
- [Rozdział 5. Ile umysł musi wiedzieć?](ch05-how-much-does-a-mind-need-to-know.md)
- [Rozdział 6. Spojrzenie](ch06-the-glance.md)
- [Rozdział 7. Ile umysł może zrobić?](ch07-how-much-can-a-mind-do.md)

**Część III. Umysły w umysłach**

- [Rozdział 8. Dwa rodzaje umysłu](ch08-two-kinds-of-mind.md)
- [Rozdział 9. Jak umysł się dzieli](ch09-how-a-mind-divides.md)
- [Rozdział 10. Ta sama myśl z inną szybkością](ch10-the-same-thought-at-a-different-speed.md)
- [Rozdział 11. Fraktale i pęknięcia](ch11-fractals-and-breaks.md)

**Część IV. Teoria w działaniu**

- [Rozdział 12. Teoria na jednej stronie](ch12-the-theory-on-one-page.md)
- [Rozdział 13. Projektowanie umysłu](ch13-designing-a-mind.md)
- [Rozdział 14. Sztuczny umysł](ch14-the-artificial-mind.md)

**Część V. Krańce**

- [Rozdział 15. Gdzie jest jaźń?](ch15-where-is-the-self.md)
- [Rozdział 16. Umysły wielkości światów](ch16-minds-the-size-of-worlds.md)
- [Rozdział 17. Nowi agenci](ch17-the-new-agents.md)
- [Rozdział 18. Inteligentny kot Schrödingera](ch18-an-intelligent-schrodingers-cat.md)
- [Rozdział 19. Jak możemy się mylić](ch19-how-we-could-be-wrong.md)

**Strony końcowe** (tylko po angielsku): [współtwórcy](../../book/contributors.md), [dziennik zmian](../../book/edit-log.md).

## O przekładzie

**Kiedy.** Przekład wykonano 28 listopada 2026 roku.

**Z czego.** Z angielskiego tekstu w katalogu `book/` w wersji oznaczonej w repozytorium jako commit `037a625`. Każdy przetłumaczony plik podaje w pierwszym wierszu, w komentarzu, plik źródłowy, jego wersję i datę przekładu. Jeśli tekst angielski zmienił się od tej wersji, przekład opisuje wersję starszą.

**Kto i jak.** Przekład jest tłumaczeniem maszynowym. Wykonał go model językowy Claude Fable 5.2 firmy Anthropic, na prośbę autora, w jednym przebiegu, plik po pliku, w kolejności rozdziałów. Ten sam model pomagał autorowi przy pisaniu oryginału, co odnotowano na stronie współtwórców. Przyjęto następujący sposób pracy:

- Przed rozpoczęciem ustalono słowniczek własnych terminów książki (niżej) i trzymano się go we wszystkich plikach.
- Tłumaczono akapit po akapicie, bez skracania, dopisywania i przestawiania. Układ każdego pliku odpowiada oryginałowi: te same nagłówki, akapity, listy, tabele i wyróżnienia.
- Liczby zapisano po polsku: przecinek dziesiętny, odstęp jako separator tysięcy, bilion w znaczeniu 10¹² (angielskie *trillion*). Jednostek nie przeliczano.
- Zgodnie z regułą oryginału w tekście nie używa się myślników w funkcji wtrąceń.

**Jak sprawdzono.** Po zakończeniu każdy plik porównano z oryginałem programem `tools/check_translation.py`. Program sprawdza, czy zgadzają się: liczba akapitów, nagłówków, punktów list i wierszy tabel, numery źródeł w każdym akapicie, wszystkie odsyłacze oraz wszystkie liczby zapisane cyframi. Jedyne różnice, jakie zgłasza, są zamierzone:

- dziesięciolecia zapisane w oryginale cyframi („the 1950s”) w przekładzie zapisano słownie („lata pięćdziesiąte XX wieku”);
- identyfikatory arXiv w źródłach (na przykład 2403.19657) program odczytuje w polskim pliku jako dwie liczby, bo kropki nie uznaje za polski separator dziesiętny;
- w rozdziale 5 liczba 1,5 występuje w angielskim tytule pracy, który pozostał nieprzetłumaczony.

**Czego nie sprawdzono.** Żaden człowiek nie przeczytał jeszcze tego przekładu w całości i nie porównał go z oryginałem. Program sprawdza budowę i liczby, a nie sens ani styl. Należy się spodziewać miejsc, w których polszczyzna jest zbyt bliska angielskiej składni, oraz terminów, które specjalista z danej dziedziny nazwałby inaczej. Nazwy gatunków i terminy z neurobiologii, fizyki i informatyki podano według wiedzy modelu i nie zweryfikowano w polskich źródłach.

**Czego nie przetłumaczono.**

- Pozycji bibliograficznych: nazwisk, tytułów, czasopism i adresów. Przetłumaczono tylko dołączone do nich objaśnienia. Nagłówek *References* oddano jako „Źródła”.
- Cytatów z istniejących polskich wydań: krótkie cytaty (na przykład z Darwina) przełożono z angielskiego tekstu książki, a nie przytoczono z polskich przekładów tych dzieł.
- Strony współtwórców i dziennika zmian. Są roboczym zapisem projektu i prowadzi się je raz, po angielsku.
- Pozostałych plików repozytorium (README, CONTRIBUTING, CONVENTIONS, AGENTS, LICENSE).

**Uwagi do oryginału zauważone przy przekładzie.** Przekład ich nie poprawia, poza pierwszą:

- W rozdziale 12, w tabeli zmiennych, kolumna jednostek dla N i d zawiera w oryginale sam przecinek (ślad po usuniętym myślniku). W przekładzie wpisano „(bez jednostki)”.
- W rozdziale 15 tekst główny podaje spadek ruchu na skórze o sześć do ośmiu rzędów wielkości, a część „W skrócie” mówi o spadku mniej więcej milionkrotnym. Przekład zachowuje obie wersje.

## Słowniczek

Terminy własne książki i przyjęte odpowiedniki. Kto poprawia przekład, powinien zmieniać termin we wszystkich plikach naraz i odnotować to tutaj.

| Angielski | Polski | Uwagi |
| --- | --- | --- |
| mind, collective mind | umysł, umysł zbiorowy | |
| agent | agent | l. mn. „agenci”; o pszczołach zgodnie z rodzajem („zwiadowczynie”) |
| collective | zbiorowość | |
| integrated / federated mind | umysł zintegrowany / sfederowany | |
| share code, not beliefs | dziel się kodem, nie przekonaniami | |
| shared code / shared belief | wspólny kod / wspólne przekonanie | |
| shared context | wspólny kontekst | |
| context amplification (κ) | wzmocnienie kontekstowe | |
| efficiency (η) | sprawność | jak sprawność silnika: czysta liczba, najwyżej 1 |
| capacity | moc przerobowa | bity na sekundę; nie „wydajność”, żeby nie mylić ze sprawnością |
| capacity of a link, bandwidth | przepustowość | |
| cross-talk | wymiana w poprzek | |
| bisection bandwidth | przepustowość bisekcji | |
| crossing time | czas przejścia | |
| coherence number | liczba spójności | |
| thought to talk | myślenie do mówienia | |
| outside against inside, boundary number | zewnętrze do wnętrza, liczba graniczna | |
| pure number | czysta liczba | liczba bezwymiarowa |
| the funnel | lejek | |
| the stage | scena | |
| broadcast | rozgłaszanie, rozgłośnia | |
| ceiling | górna granica | |
| floor (Landauer) | dolna granica | |
| priors | wiedza wstępna | |
| repertoire | repertuar | |
| bulk (of a brain) | masa | |
| library / pipeline | biblioteka / potok przetwarzania | |
| cognitive time, tick | czas poznawczy, tyknięcie | |
| thought budget | budżet myśli | |
| similarity principle | zasada podobieństwa | |
| data collapse | kolaps danych | |
| drift (of a code) | dryf | |
| scaling law, break | prawo skalowania, pęknięcie | |
| coarse-graining | gruboziarniste uśrednianie | |
| self, subject | jaźń, podmiot | |
| self-model | model siebie | |
| belonging | przynależność | |
| poised | w stanie zawieszenia, zrównoważony | o układzie w pobliżu punktu krytycznego |
| disrupt / develop (teams) | burzyć / rozwijać | |
| seizure | napad padaczkowy | |
| echo chamber | komora pogłosowa | |
| stampede | owczy pęd | |
| waggle dance | taniec wywijany | |
| piping | popiskiwanie | |
| greenish warbler | wójcik | *Phylloscopus trochiloides* |
| model collapse | załamanie modelu | |
| relative actuality | urzeczywistnienie względne | nie „aktualność”: to słowo znaczy po polsku co innego |
| a fact is actual for an agent | fakt jest urzeczywistniony dla agenta | |
| Local Friendliness | „Local Friendliness” (lokalna przyjazność) | nazwa własna założenia |
| established findings / the theory's claims / speculation | ustalone wyniki / twierdzenia teorii / spekulacje | |
| In short | W skrócie | stały tytuł części |
| How we could be wrong | Jak możemy się mylić | stały tytuł części i rozdziału 19 |
| References | Źródła | |

## Licencja i zgłaszanie błędów

Przekład jest opracowaniem książki i podlega tej samej [licencji](../../LICENSE) co oryginał. W tym repozytorium wolno go czytać, cytować z podaniem autora (Jakub Wierzgała), tytułu i odsyłacza do repozytorium https://github.com/wierzgala/the-physics-of-many-minds oraz tworzyć rozwidlenia (*fork*) na platformie GitHub wyłącznie w celu sprawdzenia tekstu lub przygotowania poprawek zgłaszanych z powrotem do tego repozytorium. Wszelkie prawa do wydawania, rozpowszechniania i sprzedaży każdej wersji książki oraz jej przekładów, zarówno drukiem (w tym w druku na żądanie), w wydaniach i dystrybucjach elektronicznych (w tym jako pliki PDF, EPUB i inne e-booki), jak i w formie nagrań audio, są zastrzeżone wyłącznie dla autora.

Błędy przekładu najlepiej zgłaszać jako *issue* w repozytorium albo od razu jako poprawkę, według zasad opisanych w pliku [CONTRIBUTING.md](../../CONTRIBUTING.md) (rodzaj wkładu: *translation*). Uwagi merytoryczne do samej teorii powinny dotyczyć tekstu angielskiego.
