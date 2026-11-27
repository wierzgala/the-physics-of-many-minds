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

**The number: context amplification**, written κ (kappa). It is the size of the thought divided by the bits actually needed to send it, given the shared context. Between strangers κ is low, though never as low as 1, for a reason we will come to. Between the couple at the dinner table it may be in the hundreds.

There is an old joke about this. A newcomer arrives in a prison and hears an inmate call out "forty-two!". Everyone roars with laughter. Another shouts "seventeen!", and they laugh again. His cellmate explains: we have all been here so long that we know every joke by heart, so we numbered them. That is κ. The joke about the joke is that the newcomer tries "twenty-nine" and nobody laughs, because some people just can't tell a joke. Even with a perfect code, delivery is a channel too.

## The dance, again

Now the waggle dance makes sense. Seven bits can direct a bee to a hollow tree three kilometres away because every bee is born with the codebook: angle means direction relative to the sun, duration means distance, vigour means quality. That codebook was written into the genome over millions of years of selection. Each dance is a tiny withdrawal from an enormous account.

The same is true of every working collective. Neurons share a code fixed by development and tuned by learning. Scientists share mathematics. The members of a jazz quartet share thousands of hours of listening to the same records. In each case the wire between the agents is thin, and the collective works anyway, because the wire only has to carry the difference.

## The context you were born with

The bees' codebook is in their genes. So is a large part of ours, and it is easy to overlook because we never had to learn it.

Before two people have exchanged a word, before either has a language or a culture, they already share an enormous store of context. A human genome is a text of about three billion letters, and any two people's copies are about 99.9% identical. At two bits per letter, that is some six billion bits held in common by every pair of humans who have ever met (that last figure is our arithmetic). No friendship, however long, adds shared context on that scale by talking.

What is written there is not knowledge of the world. Six billion bits could not specify the 10¹⁵ bits a brain will eventually hold. It is something more useful for communication: the plans for the same sense organs, the same emotions, the same face, and the same expectations about other faces. It is a shared decoder.

The evidence that this decoder is inherited, not learned, is striking.

- **Newborns arrive expecting faces.** In a classic experiment, 24 babies were tested within their first hour of life. They turned their heads and eyes further to follow a simple face-like pattern than to follow the same features scrambled. They had never seen a face.
- **The blind make the faces they have never seen.** Researchers photographed judo athletes at the 2004 Olympic and Paralympic Games at the moment they won or lost a medal match: 84 sighted athletes and 76 blind ones, some blind from birth. The expressions of the congenitally blind were the same as those of the sighted, down to the individual muscle movements. They could not have copied them from anyone.

So the dinner-party glance works at two depths. The eyebrow means what it means to that couple because of forty years together. But an eyebrow means *anything at all*, to any human, because of a code written long before either of them was born. A smile from a stranger in a country whose language you do not speak is a message with a very high κ, and the context it draws on is the genome.

This shows that shared context comes in layers, each built on a different clock.

| Layer | Who shares it | Time taken to build |
| --- | --- | --- |
| The chemistry of life: the genetic code itself | every living thing, bees included | billions of years |
| The human genome: senses, emotions, faces, the capacity for language | every human | hundreds of thousands of years |
| A language and a culture | millions of people | centuries |
| A profession, a field, a craft | thousands | decades |
| A friendship, a marriage, a team | a few | years |

Each layer is narrower than the one below it and quicker to write. And each rests on the ones beneath: a marriage is written in a language, a language runs on a human brain, and a human brain is built by a genome. When we count the bits a glance does not have to carry, most of them were paid for by ancestors.

Two consequences follow, and both are claims of the theory.

First, the deepest layers are also the safest. A couple's shared context dies with them. A language can die with its last speakers. The genomic layer is copied into eight billion bodies and is, for now, the most redundant store of shared context our species has. It is what makes humanity one collective at all, underneath its seven thousand languages.

Second, the hardest communication problem is not a narrow channel. It is a partner with whom the lower layers are missing. A mind that did not share our evolutionary history, whether it grew on another planet or in a data centre, would lack the layer that makes a smile readable. A machine trained on human writing inherits much of the cultural layer, which is why we can talk to it at all. It does not inherit the layer beneath. The theory predicts that misunderstandings between humans and such minds will cluster exactly there: in everything we never say because no human has ever needed to be told.

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

There are two ways to make a channel carry more meaning: widen it, or share more context. Widening has hard physical costs in energy and wiring, as Chapter 7 shows. Context has no such ceiling, and as we have seen, every human collective starts with billions of bits of it already in place, inherited. So as collectives grow and their wires grow thinner relative to their size, they should lean more and more on context. The swarm does. Human civilisation does: a single equation on a blackboard can redirect a thousand careers, because of the decades of training its readers share.

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

Counted in meaning, the gap narrows. For two people with decades of shared context, each spoken bit does the work of hundreds. They remain two selves, by many orders of magnitude. But they are measurably closer to being one system than two strangers are. That raises two questions: is the pair smarter than its members, and what is it like to be half of one?

### Are two heads better than one?

Sometimes, and the conditions have been measured. In a well-known experiment, pairs of volunteers looked for a faint target in a visual display, first deciding alone and then, when they disagreed, talking it over. When the two had similar eyesight, the pair did better than its better member. When their abilities were very different, the pair did *worse* than its better member would have done alone. And the benefit appeared only when they could talk freely; being told afterwards who had been right was not enough. The explanation that fitted the data was that partners were telling each other how confident they were, and a pair can combine two opinions well only if each can read the other's confidence accurately.

A long-established couple is close to the ideal case for this. Their shared code is deep, so "I'm fairly sure" means the same thing to both. Each knows what the other is reliable about. By the argument of this chapter, their joint η should exceed either's alone.

But the theory attaches the same condition it attaches to every collective. The gain comes from combining *independent* judgements. A couple who have come to believe all the same things are two copies of one opinion, and two copies are worth one. So the theory predicts that a couple's joint intelligence can rise and then fall over the years: understanding keeps improving, but if the two stop disagreeing, and stop bringing home different experiences, the advantage drains away. The most intelligent couples should be those who understand each other perfectly and still argue.

### What it feels like

Psychologists have measured the merging that couples describe. In one study, married people were shown a list of traits and asked to press a button for "me" or "not me". They were slower, and made more errors, on traits that were true of them but not of their spouse, or the reverse, as if they had to stop and work out which of the two the trait belonged to. The researchers called this including the other in the self. In another part of the same work, people sharing out money treated a close friend almost as they treated themselves.

The cost of losing that other half is also on record. Combining studies of more than two million people, one analysis found that the risk of dying is raised by about 41 percent in the first six months after a spouse's death, and by about 14 percent after that. Bereavement harms people in many ways, so this is not proof of the idea. It is what the idea would lead one to expect.

Here is the theory's reading, and it is a claim. The couple is not a self. By the measure above, there is no joint experience; the feeling of "us" occurs separately in each partner. What has changed is each partner's model of themselves. It has stretched to include things that are stored in the other: memories, judgements, the ability to predict what happens next. Your self no longer ends at your skin, because part of the machinery you rely on to be yourself is in someone else's head.

If that is right, it answers a question that the hierarchy of minds keeps raising. What is it like to be part of a larger intelligence? It is not like thinking the larger mind's thoughts. Chapter 10 argues that those are out of reach: a neuron has no access to the thought it takes part in, and we have none to humanity's. What reaches us is something else. It is the experience of *belonging*: of a self whose boundary has moved outward to take in others. A marriage produces it at full strength. A team, a regiment, a congregation and a nation may produce the same thing more faintly, by the same mechanism. Loyalty, on this view, is what participation in a larger mind feels like from inside. That last step is speculation.

## In short

- Information theory measures bits and deliberately ignores meaning. A theory of intelligence cannot.
- A receiver who shares context with the sender needs only the bits it could not have guessed. Meaning = bits sent now + bits shared before.
- Context amplification κ measures how much thought each transmitted bit unlocks. It is a property of a pair of agents, not of a channel.
- Couples, experienced teams and socially sensitive groups outperform what their individual abilities predict, as the idea requires.
- Two heads beat one when the pair can communicate confidence accurately and their judgements stay independent. Couples measurably include each other in their sense of self.
- The theory's claims: relationships are compression algorithms whose cost is amortised; context can substitute for bandwidth but never for speed; mature collectives communicate by exception, and their silence is meaningful; perfect understanding carries no information, so collectives must share codes while keeping beliefs diverse.

## How we could be wrong

The central claim fails if shared context turns out not to be measurable, even roughly, in real pairs of agents. It would also fail if long-established teams showed no advantage once individual skill is accounted for, or if groups with uniform beliefs turned out to solve hard, novel problems as well as groups with diverse ones. The claim about communication by exception predicts that message rates between partners should fall as their shared history grows while their coordination improves. If coordination in long-lived teams instead required ever more talk, the claim would be wrong.

The account of couples predicts a rise and fall. If pairs who agree about everything decide as well as pairs who understand each other and still differ, the independence condition is wrong. If long-married partners turn out to be no better than strangers at reading each other's confidence, the shared-code argument fails for them.

## Notes

- Shannon's exclusion of meaning and Weaver's three levels: [Weaver 1949, *The Mathematics of Communication*](https://Monoskop.org/images/b/b3/Weaver_Warren_1949_1973_The_Mathematics_of_Communication.pdf); Shannon quoted in [this technical report](https://apps.dtic.mil/sti/pdfs/ADA544137.pdf).
- Coding with side information at the receiver: Slepian & Wolf 1973, summarised in [this overview](https://arxiv.org/pdf/2403.07409).
- Information content of the waggle dance: [Schürch & Ratnieks 2015](https://www.frontiersin.org/articles/10.3389/fevo.2015.00022).
- Human genomes of about three billion letters, about 99.9% identical between people: [NHGRI, Human Genomic Variation](https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genomic-variation). The six-billion-bit figure, the layer table and its timescales are our own estimates.
- Newborns tracking face-like patterns in the first hour of life: [Johnson, Dziurawiec, Ellis & Morton 1991](https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Newborns-preferential-tracking-of-face-like-stimuli/991005543269907891); review: [this review of infant face perception](https://pmc.ncbi.nlm.nih.gov/articles/PMC3090162). Some studies have failed to replicate the effect, though most of the literature supports it.
- Facial expressions of congenitally blind athletes: [Matsumoto & Willingham 2009](https://pubmed.ncbi.nlm.nih.gov/19210060/); numbers of athletes: [APA press release](https://www.apa.org/news/press/releases/2008/12/facial-expressions).
- Transactive memory in close couples: [Wegner, Erber & Raymond 1991](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/dwegner/files/wegnererberraymond1991.pdf).
- Team familiarity and performance in 1,015 software projects: [Huckman, Staats & Upton 2009](https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:1:p:85-100); summary: [strategy+business](https://strategy-business.com/article/re00013).
- Collective intelligence factor in 192 groups: [Woolley et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20929725/); the eyes test: [Harvard summary](https://www.gap.hks.harvard.edu/evidence-collective-intelligence-factor-performance-human-groups).
- Pairs outperforming or underperforming their better member: [Bahrami et al. 2010, "Optimally interacting minds", Science](https://pmc.ncbi.nlm.nih.gov/articles/3371582); the need for free discussion: [Wellcome Trust summary](https://wellcome.org/press-release/two-heads-are-better-one-right-partner).
- Including the other in the self, the "me / not me" experiment and the money-allocation experiment: [Aron, Aron, Tudor & Nelson 1991](https://www.proquest.com/docview/614329106); review: [Branand, Mashek & Aron 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6821680).
- Mortality after the death of a spouse: [Moon, Kondo, Glymour & Subramanian 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3157386).
- The rise-and-fall prediction for couples and the account of belonging are the theory's claims.
- Speech at about 39 bits per second: [Coupé et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970). The figure for traffic between brain hemispheres is a rough estimate of ours.
- The ox-weighing crowd: see the notes to Chapter 1.
- The dinner-table and café scenes are illustrations, not data. The values of κ quoted for them are guesses; measuring κ in real pairs is an open problem.
