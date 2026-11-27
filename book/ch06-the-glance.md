# Chapter 6. The glance

## Across the table

Two people who have been married for forty years are at a dinner party. Someone at the far end of the table starts telling a story. One of the two looks at the other for half a second and raises an eyebrow. The other almost laughs.

A whole thought has just crossed the table. It might be: *this is the story he told at our wedding, and he is about to get the ending wrong again*. Written out, that thought is a few hundred bits. The eyebrow, as a physical signal, carried perhaps one or two. A stranger sitting between them saw the same eyebrow and received nothing.

Until now this book has measured communication the way an engineer measures a cable: in bits per second. By that measure the glance is almost worthless, and the waggle dance of Chapter 1 is a seven-bit whisper. Something is obviously missing. This chapter supplies it, and the missing piece turns out to have consequences that reach from marriages to galaxies.

## What Shannon left out on purpose

When Claude Shannon founded information theory in 1948, he drew a line. The meaning of a message, he wrote, is irrelevant to the engineering problem. His task was to get symbols from one place to another intact, whatever they stood for.

His colleague Warren Weaver saw what lay on the other side of the line and described communication as a problem at three levels:

1. **Technical.** How accurately can the symbols be transmitted?
2. **Semantic.** How precisely do the symbols convey the intended meaning?
3. **Effectiveness.** How well does the received meaning change what the receiver does?

Shannon solved the first level so completely that the other two were neglected for decades. A theory of intelligence cannot afford that. Agents do not exchange symbols for their own sake. A bee dances so that another bee will fly somewhere. Levels two and three are the point.

## The usual

The key is hidden in an ordinary scene. You walk into the café you visit every morning and say "the usual". Two words, and the barista starts making a large flat white with oat milk, extra hot. A newcomer who wanted the same drink would have to spell out all of it.

You did not send less information than the newcomer. You sent the part the barista did not already have. Everything else was sent earlier, on the fifty previous mornings.

Information theory has an exact statement of this. In 1973 David Slepian and Jack Wolf proved that if a receiver already holds information related to a message, the message can be sent using only as many bits as the receiver is still uncertain about, given what it knows. The surprising part of their theorem is that the sender does not even need to know exactly what the receiver holds. It is enough that the shared knowledge exists.

This gives us a rule and a number.

**The rule: meaning = bits sent now + bits shared before.** No message carries more new information than its bit count allows; Shannon's limits stand. But the meaning a message unlocks can be far larger than the message, because it draws on a store that sender and receiver built earlier.

**The number: context amplification**, written κ (kappa). It is the size of the thought divided by the bits actually needed to send it, given the shared context. Between strangers κ is close to 1. Between the couple at the dinner table it may be in the hundreds.

There is an old joke about this. A newcomer arrives in a prison and hears an inmate call out "forty-two!". Everyone roars with laughter. Another shouts "seventeen!", and they laugh again. His cellmate explains: we have all been here so long that we know every joke by heart, so we numbered them. That is κ. The joke about the joke is that the newcomer tries "twenty-nine" and nobody laughs, because some people just can't tell a joke. Even with a perfect code, delivery is a channel too.

## The dance, again

Now the waggle dance makes sense. Seven bits can direct a bee to a hollow tree three kilometres away because every bee is born with the codebook: angle means direction relative to the sun, duration means distance, vigour means quality. That codebook was written into the genome over millions of years of selection. Each dance is a tiny withdrawal from an enormous account.

The same is true of every working collective. Neurons share a code fixed by development and tuned by learning. Scientists share mathematics. The members of a jazz quartet share thousands of hours of listening to the same records. In each case the wire between the agents is thin, and the collective works anyway, because the wire only has to carry the difference.

## What the evidence says

If shared context is a real quantity, groups that have more of it should perform better than their raw abilities predict. They do.

**Couples.** The psychologist Daniel Wegner studied memory in 118 people who were in close relationships. He found that close couples hold an implicit structure for dividing up what each will remember, a system he called transactive memory, and that this joint system is larger than either partner's memory alone. Each partner stores less, because each knows what the other knows.

**Teams.** A study of 1,015 software projects at a large Indian software firm asked what predicts a team's performance. The experience of individual members, such as their years at the firm, was not consistently related to it. What mattered was how much the members had worked with *each other* before.

**Groups of strangers.** Anita Woolley and colleagues gave 192 small groups a wide range of tasks and found that a group's ability on one task predicted its ability on others: groups have a general collective intelligence. It was not strongly related to the average intelligence of the members, or to that of the cleverest member. It was related to the members' social sensitivity, and to how evenly they took turns speaking. Social sensitivity was measured with a test in which you look at a photograph of a person's eyes and say what they are feeling.

That last finding is this chapter's opening scene in a laboratory. The groups that thought best were the ones whose members were best at reading a glance.

## Four consequences

Everything so far is established science assembled in a new order. What follows are the theory's own claims.

### A relationship is a compression algorithm

A friendship, a marriage, a team and a scientific field are all, among other things, shared codebooks. Their value can in principle be stated in bits: the total context the members share. Building that store is expensive. It takes years of slow, redundant, high-bit-rate conversation. But the cost is paid once and then spread over every later exchange.

This predicts that the efficiency of a collective rises with its age, long after its members have stopped improving individually. It also predicts what breaks a collective. Replacing a member destroys the context that was stored between that member and all the others. A team of brilliant strangers is, by this measure, a team that has not yet been built.

It predicts something about loss as well. If part of your memory system is held in another person, then losing that person removes part of your own mind's working machinery. On this view the disorientation of grief is partly a literal one.

### Context beats bandwidth, but nothing beats latency

There are two ways to make a channel carry more meaning: widen it, or share more context. Widening has hard physical costs in energy and wiring, as Chapter 7 shows. Context has no such ceiling. So as collectives grow and their wires grow thinner relative to their size, they should lean more and more on context. The swarm does. Human civilisation does: a single equation on a blackboard can redirect a thousand careers, because of the decades of training its readers share.

But shared context cannot make a message arrive sooner. A signal still has to cross the distance. This asymmetry will decide the shape of very large minds in Chapter 13: they can be rich in meaning, and they cannot be fast.

### The perfect conversation is silent

Follow the logic to its end. The better my model of you, the less you need to tell me. If my model were perfect, I could predict everything you were about to say, and you would need to send nothing at all, except on the rare occasions when you surprised me.

So communication between agents who know each other deeply should consist mostly of *exceptions*: corrections to the other's predictions. An influential theory in neuroscience, predictive coding, holds that the cortex works this way, with higher areas sending predictions down and lower areas sending back only the errors. Whether or not the brain does this, the theory here says that any mature collective should drift in that direction, because it is the cheapest way to stay coordinated.

It follows that silence is a message. Between two agents with a deep shared model, no signal means *I am as you expect*. A collective that has reached this state would look, from outside, almost as if its members were not communicating at all.

### Perfect understanding carries no news

Here is the uncomfortable part. Amplification κ is highest when the receiver could nearly have guessed the message. In the limit, where the receiver already knows exactly what the sender will say, κ is infinite and the message contains nothing new.

So the feeling of being perfectly understood and the fact of exchanging no information are the same situation. A conversation in which everyone finishes everyone else's sentences is deeply satisfying and completely uninformative. That is what an echo chamber is: a group whose internal amplification is so high that no message can change anyone's mind.

A useful collective has to sit between two failures. With no shared context, every message is noise. With total shared context, every message is an echo. This is the same balance Chapter 3 found in the brain, between the gas and the crystal, now showing up in meaning itself.

It also tells us what to share and what not to. There are two kinds of common ground:

- **Shared code**: agreement about what signals *mean*. A language, a notation, a protocol.
- **Shared belief**: agreement about what is *true*.

Shared code raises κ without costing independence. Shared belief raises κ by destroying independence, and independence is what made 787 guesses about an ox add up to the right answer. The bees share the dance and keep their opinions. The theory predicts that the most intelligent collectives are those that maximise the first kind of common ground and protect diversity in the second.

## Two people, one system?

One more consequence, to be developed in Chapter 12. This book will propose that a self ends where communication with the outside becomes much thinner than communication within. Counted in raw bits, two people are hopelessly separate: speech carries about 39 bits per second, against perhaps a hundred million between the two halves of one brain.

Counted in meaning, the gap narrows. For two people with decades of shared context, each spoken bit does the work of hundreds. They remain two selves, by many orders of magnitude. But they are measurably closer to being one system than two strangers are, and the theory says that "we" is, for them, a slightly more literal word.

## In short

- Information theory measures bits and deliberately ignores meaning. A theory of intelligence cannot.
- A receiver who shares context with the sender needs only the bits it could not have guessed. Meaning = bits sent now + bits shared before.
- Context amplification κ measures how much thought each transmitted bit unlocks. It is a property of a pair of agents, not of a channel.
- Couples, experienced teams and socially sensitive groups outperform what their individual abilities predict, as the idea requires.
- The theory's claims: relationships are compression algorithms whose cost is amortised; context can substitute for bandwidth but never for speed; mature collectives communicate by exception, and their silence is meaningful; perfect understanding carries no information, so collectives must share codes while keeping beliefs diverse.

## How we could be wrong

The central claim fails if shared context turns out not to be measurable, even roughly, in real pairs of agents. It would also fail if long-established teams showed no advantage once individual skill is accounted for, or if groups with uniform beliefs turned out to solve hard, novel problems as well as groups with diverse ones. The claim about communication by exception predicts that message rates between partners should fall as their shared history grows while their coordination improves. If coordination in long-lived teams instead required ever more talk, the claim would be wrong.

## Notes

- Shannon's exclusion of meaning and Weaver's three levels: [Weaver 1949, *The Mathematics of Communication*](https://Monoskop.org/images/b/b3/Weaver_Warren_1949_1973_The_Mathematics_of_Communication.pdf); Shannon quoted in [this technical report](https://apps.dtic.mil/sti/pdfs/ADA544137.pdf).
- Coding with side information at the receiver: Slepian & Wolf 1973, summarised in [this overview](https://arxiv.org/pdf/2403.07409).
- Information content of the waggle dance: [Schürch & Ratnieks 2015](https://www.frontiersin.org/articles/10.3389/fevo.2015.00022).
- Transactive memory in close couples: [Wegner, Erber & Raymond 1991](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/dwegner/files/wegnererberraymond1991.pdf).
- Team familiarity and performance in 1,015 software projects: [Huckman, Staats & Upton 2009](https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:1:p:85-100); summary: [strategy+business](https://strategy-business.com/article/re00013).
- Collective intelligence factor in 192 groups: [Woolley et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20929725/); the eyes test: [Harvard summary](https://www.gap.hks.harvard.edu/evidence-collective-intelligence-factor-performance-human-groups).
- Speech at about 39 bits per second: [Coupé et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970). The figure for traffic between brain hemispheres is a rough estimate of ours.
- The ox-weighing crowd: see the notes to Chapter 1.
- The dinner-table and café scenes are illustrations, not data. The values of κ quoted for them are guesses; measuring κ in real pairs is an open problem.
