# Chapter 5. How much does a mind need to know?

## Twenty questions

In the old parlour game, one player thinks of something and the other has twenty yes-or-no questions to find out what it is. Children play it badly. *Is it a giraffe? Is it my shoe?* Each of those questions, if the answer is no, rules out one thing in a world of millions.

A good player asks *Is it alive?* and throws away half the world with one word. Then half of what is left, and half again. Twenty perfect halvings single out one object from 2²⁰, a little over a million. The good player and the child receive exactly the same number of answers. One of them gets a million times further.

That difference is what this chapter proposes to call intelligence. It is not how much the player knows at the end. Both of them end up knowing the answer, if the child is allowed enough questions. It is how little each needed to be told.

## A reader who already knows the book

Claude Shannon turned a version of the game into an experiment. He showed people a passage of English with the rest hidden and asked them to guess the next letter, then the next, counting their guesses. If readers knew nothing, each letter would cost them about 4.7 bits, the price of choosing one from 26. In fact they needed something of the order of one bit per letter. Shannon's bounds were 0.6 to 1.3 bits (1, 2). About three quarters of written English is redundant to someone who knows English (1).

The text had not changed. What made it cheap was the reader. A mind with a good model of its world needs very few bits to follow what happens next, because it has already predicted most of it. Chapter 6 will find the same fact between people. Here it appears inside one head.

This suggests a definition.

> The intelligence of a system is its achievement divided by the information it had to use.

We will write it η (eta), the usual symbol for an efficiency. The bottom of the fraction is measured in bits, and that part is not negotiable. The top is a choice, and we will come to it.

## The child and the machine

The definition makes an awkward prediction about our own technology, and the prediction is right.

A child becomes a fluent speaker after hearing some tens to hundreds of millions of words. A large language model reaches fluency after hundreds of billions to trillions (3). The gap is four or five orders of magnitude between such models and children, and at least three between the models and even the most literate adults (4). On the measure proposed here, at this one task, the child is something like ten thousand to a hundred thousand times more intelligent than the machine. The machine is, of course, vastly more capable in other respects. The point of the definition is that capability and intelligence are different things.

What does the child keep from all that listening? Two researchers set out to count it, adding up what a speaker must know about sounds, words, meanings and grammar. Their best estimate was about 12.5 million bits, roughly 1.5 megabytes, the size of one photograph (5). It works out at upwards of a thousand bits learned every day for eighteen years (5). Most of it is the meanings of words. The rules of grammar, which linguists have argued about for a century, came to about 700 bits (6).

Set that against the input. A hundred million words is several hundred million bits, even at Shannon's rate. So only a few percent of what a child hears ends up as knowledge of the language (our estimate). The child is not a recorder. It is a twenty-questions player, extracting the few bits that matter from a stream that is mostly things it could already have guessed.

The same pattern shows wherever people and learning machines have been compared directly.

- **One example is often enough.** Show a person a single example of a new kind of object, such as an unfamiliar handwritten character or a strange two-wheeled vehicle, and they grasp the category. Standard learning algorithms have needed tens or hundreds of examples to do the same (7).
- **Mastery by brute repetition.** The program AlphaGo Zero became the strongest Go player in history by playing itself. In its first three days it played 4.9 million games (8). A human professional plays some tens of thousands in a lifetime (our estimate). The program is stronger. It was also given a hundred lifetimes of practice.

And the pattern is not about brain size. A honeybee, with under a million neurons, can learn the abstract ideas of *same* and *different*. Trained to pick the pattern that matches a sample, bees went on to apply the rule to stimuli they had never seen, and even to a different sense (9). An insect extracted a concept from a handful of trials. Whatever η measures, it is not the amount of hardware.

## Three kinds of bits

Before admiring the child too much, we have to do the accounts honestly. Information reaches a mind by three routes, and all three belong at the bottom of the fraction.

**Experience**: the bits that come in through the senses during a lifetime. This is the hundred million words.

**Priors**: the bits a mind starts with. The child did not arrive empty. It came with a genome of about three billion letters (10), the outcome of an immense search conducted by its ancestors, and that genome builds a brain already prepared to find words, faces and causes. The machine began with almost nothing of the kind. Some of the child's advantage is real efficiency. Some of it is an inheritance.

**Communication**: for a mind made of many agents, the bits the agents must exchange to get the job done. This is the term that matters for the swarms, teams and societies of this book, and no theory of individual intelligence includes it.

Leave out any of the three and the measure can be cheated. A table that lists the answer to every question on an exam will score perfectly while learning nothing; all its intelligence is in the priors, put there by whoever wrote the table. The computer scientist François Chollet made this point forcefully in 2019. Measuring skill alone, he argued, falls short of measuring intelligence, because unlimited prior knowledge or unlimited training data lets an experimenter simply buy any level of skill. He proposed that intelligence be defined as the efficiency with which a system acquires new skills, taking its priors and its experience into account (11). This chapter takes his proposal, gives it units, and adds the third kind of bit.

## What goes on top

Now the top of the fraction. There are three reasonable choices, and each gives intelligence a different unit.

**Count what was accomplished.** Tasks solved, weighted by how hard and how new they were. Then η is measured in achievements per bit. This is the most intuitive version and the hardest to make precise, because someone has to do the weighting.

**Count the work extracted.** Chapter 2 described Szilárd's engine, which turns one bit of knowledge into a fixed amount of energy. A mind could be scored by the useful work it gets from the world per bit it learns. There is a beautiful version of this for money. In 1956 John Kelly, a colleague of Shannon's, considered a gambler who receives tips over a noisy telephone line. He proved that the fastest rate at which the gambler's capital can grow is exactly the rate at which information arrives over the line (12). Bits become wealth at a fixed exchange rate, and no betting strategy can beat it.

**Count the uncertainty removed.** Measure the top in bits as well: how far the mind narrowed down the state of the world, or steered it toward a goal. Then η is bits per bit, a pure number. And for this version there is a theorem. Touchette and Lloyd proved that for each bit a controller gathers about a system, it can reduce that system's disorder by at most one bit more than it could have done blind (13).

The third choice is the one this book adopts, because of that theorem. It means that **intelligence, properly measured, has a maximum, and the maximum is one.** The perfect twenty-questions player sits exactly at the limit: one bit of the world settled for every bit received. Nothing can do better.

## The consequences of a ceiling

This is a stronger statement than it looks, and what follows from it is the theory's own claim.

**There is such a thing as perfect intelligence, and it is not far away.** For a given problem, a mind is perfectly intelligent when it wastes none of what it learns. Humans playing twenty questions get close. So does a good doctor choosing which test to order. Perfection in this sense is not a property of gods. It is a property of well-chosen questions.

**A superintelligence cannot be smarter per bit than a perfect human.** If the ceiling is one, a mind far beyond ours cannot extract two bits of control from one bit of data. It can only do three things: gather more bits, which is capacity, the subject of Chapter 7; start with better priors; or choose better which bits to gather. Much of what is imagined about superhuman minds is really about capacity. The theory separates the two cleanly, as the engineer separates the size of an engine from its efficiency: **what a mind can do is its capacity multiplied by its η.**

**Curiosity is the engine of efficiency.** The child's question *is it a giraffe?* and the adult's *is it alive?* cost the same and are worth wildly different amounts. A mind raises its η not by thinking harder about the answers but by choosing questions whose answers it cannot predict. An experiment in a laboratory is such a question. So is a scout bee's flight to a place no bee has been. On this view, curiosity is not a decoration on intelligence. It is how intelligence is done.

**Understanding is compression.** A mind that needs fewer bits to follow the world is a mind with a shorter description of the world. Shannon's readers needed one bit per letter because they carried English in their heads. To understand something is to be able to predict it cheaply. The scientist who replaces a table of ten thousand measurements with one equation has not just tidied up. By this book's definition, she has become more intelligent about that part of the world, and so has everyone she tells.

**Most of your intelligence was learned by someone else.** That last clause matters more than it seems. Newton's laws fit in a few hundred bits. Finding them cost humanity centuries. A student receives them in an afternoon. Every person alive is handed priors, in genes and in culture, that they could never have earned alone, and the accounts of η say plainly where a person's apparent brilliance comes from: overwhelmingly, from the bottom of the fraction having been paid by others. Chapter 6 calls this shared context, and Chapter 13 will argue that it is the reason one species came to run the planet.

## Why collectives look wasteful

Apply the measure to the swarm of Chapter 1, and something odd appears. The swarm's decision is a choice among about a dozen sites, which is under four bits. To make it, hundreds of scouts flew out, and hundreds of dances were performed, each carrying a location and repeated for many circuits (14). Thousands of bits were spent to settle four. By the fraction, the swarm looks stupid.

It is not, and the reason is instructive. A single bee's judgement of a cavity is noisy. The repetition, the independent inspections and the slow build-up to a quorum are what make the final four bits *reliable*. Shannon showed that sending information accurately over a noisy channel always costs redundancy; the three quarters of English that readers can guess is what lets us understand each other in a crowded room. A collective is a noisy channel made of minds, and it pays the same tax.

So η has to be quoted together with reliability, the way a car's fuel economy has to be quoted at a given speed. And the comparison becomes interesting. The question to ask of any collective, a swarm, a jury, a scientific field, is how many bits of talk it spends per bit of dependable decision, and how close that comes to the least that any procedure could spend. Computer scientists have a name for that minimum, communication complexity, and it has hardly been applied to living collectives at all.

## In short

- Intelligence is proposed as an efficiency: achievement per bit of information used. It measures how little a mind needs to be told.
- People predict English at about one bit per letter because they already model the language. A good model makes the world cheap to follow.
- Children learn language from four or five orders of magnitude less data than large language models, storing only about 1.5 megabytes of knowledge. People learn concepts from one example; a bee can learn *same* and *different*.
- Three kinds of bits must be counted: experience, priors and communication. Ignoring priors lets a lookup table pass as a genius.
- If achievement is measured in bits of uncertainty removed, a theorem caps η at one. Perfect intelligence exists and consists of wasting nothing.
- The theory's claims: a superintelligence can exceed us in capacity and priors but not in efficiency beyond one; curiosity is how efficiency is raised; understanding is compression; most of any person's intelligence is inherited priors.
- Collectives spend many bits per bit decided because reliability costs redundancy. Their efficiency should be judged against the minimum communication the task requires.

## How we could be wrong

The measure fails if it cannot be made operational: if no defensible way is found to weight achievements, or to count the priors in a genome or a culture, then η is a metaphor and not a quantity. The comparison between children and language models may be unfair if the two are not doing the same task, or if children's far richer sensory experience is counted as language input; some researchers attribute the gap to exactly that (4). The ceiling of one applies to a specific, formal notion of control, and extending it to all of intelligence is our hypothesis, not the theorem's. The claim about superintelligence would be refuted by any system shown to gain more control over an environment than the information it acquired about it.

## References

1. C. E. Shannon (1951), "Prediction and entropy of printed English", *Bell System Technical Journal*. https://sites.socsci.uci.edu/~rfutrell/teaching/itl-davis/readings/shannon1951prediction.pdf
2. Review of Shannon's bounds of 0.6 to 1.3 bits per letter, in "A new look at the classical entropy of written English". https://arxiv.org/pdf/0911.2284
3. S. Y. Feng, N. D. Goodman and M. C. Frank (2024), "Is child-directed speech effective training data for language models?". https://arxiv.org/pdf/2408.03617
4. M. C. Frank (2023), "Bridging the data gap between children and large language models", *Trends in Cognitive Sciences*. https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Frank2023_ChildrenLLMs.pdf
5. F. Mollica and S. T. Piantadosi (2019), "Humans store about 1.5 megabytes of information during language acquisition", *Royal Society Open Science*; figures as reported by the University of California, Berkeley. https://www.sciencedaily.com/releases/2019/03/190327134547.htm
6. Report on the same study, giving the estimate for syntax. https://medicalxpress.com/news/2019-03-approximately-megabytes-language-brain.pdf
7. B. M. Lake, R. Salakhutdinov and J. B. Tenenbaum (2015), "Human-level concept learning through probabilistic program induction", *Science*. https://www.cnbc.cmu.edu/~tai/microns_papers/LakeEtAl2015Science.pdf
8. "AlphaGo Zero", Wikipedia, citing D. Silver et al. (2017), *Nature*. https://en.wikipedia.org/wiki/AlphaGo_Zero
9. M. Giurfa, S. Zhang, A. Jenett, R. Menzel and M. V. Srinivasan (2001), "The concepts of 'sameness' and 'difference' in an insect", *Nature*. https://ideas.repec.org/a/nat/nature/v410y2001i6831d10.1038_35073582.html
10. National Human Genome Research Institute, "Human genomic variation". https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genomic-variation
11. F. Chollet (2019), "On the measure of intelligence". https://arxiv.org/pdf/1911.01547
12. J. L. Kelly Jr. (1956), "A new interpretation of information rate", *Bell System Technical Journal*. https://homepage.sns.it/marmi/esameIUE/kelly.pdf
13. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters*. https://arxiv.org/abs/chao-dyn/9905039
14. T. D. Seeley, P. K. Visscher and K. M. Passino (2006), "Group decision making in honey bee swarms", *American Scientist*. https://bees.ucr.edu/media/156/download

Figures given without a reference number are our own rough estimates: the share of a child's language input that is retained, the number of games a human professional plays, the bit counts for the swarm's decision, and the size of Newton's laws in bits.
