# Chapter 13. Designing a mind

## The engineer's question

Until now this book has worked like a naturalist. It has looked at minds that exist, a swarm, a brain, a flock, a species, and asked why they are the way they are.

An engineer asks the question the other way round. Here is a job. What must the thing that does it look like?

A structural engineer can answer that for a bridge. Tell her the span, the load and the strength of steel, and she can say, before any architect has drawn a line, roughly how deep the beams must be and how much steel the bridge will need. She cannot say what the bridge will look like. Two bridges for the same river may be an arch and a suspension bridge. But both will obey her numbers, and any design that violates them will fall down.

This chapter tries to do the same for minds, using the framework of Chapter 12. If the theory is right, then stating a task, how much information arrives, how much must come out, and how quickly, should fix the outline of any mind that can perform it: how many levels, how many agents at the entrance, how large, which of the two kinds. That outline is the mind's *morphology*. If the outline can be derived and then matches minds that evolved without consulting us, the theory has predicted something. If it does not match, we learn where the theory is wrong.

## A specification

Take a definite job.

*A stream of raw data arrives at ten million bits per second. Almost all of it is irrelevant. The mind must extract from it one useful bit per second, a single yes-or-no decision every second, and must never be more than a second late.*

Written in the variables of Chapter 12:

- information arriving, R_in: 10⁷ bits per second
- information leaving, R_out: 1 bit per second
- timescale of the world, T_w: 1 second
- compression required, R_in ÷ R_out: ten million to one

The design can now be worked out step by step. Each step uses a rule from an earlier chapter. The arithmetic is ours and is rough; what matters is whether the outline comes out right to within a factor of ten.

## Step 1. How wide is the entrance?

Chapter 7 found that the cost of a bit rises with the rate at which a channel carries it, so that many slow channels are cheaper than a few fast ones. The cheapest channels that nerve cells seem able to build carry something like ten bits per second.

So the entrance should be about

> 10⁷ bits per second ÷ 10 bits per second per channel = **a million parallel channels**

each of them slow. A design with a thousand fast channels would do the same job at a much higher price.

## Step 2. How many levels?

No agent that is cheap enough to have a million of can turn ten million bits into one. The compression has to be done in stages. If each level passes on to the next a fraction 1/f of what it receives, the number of levels needed is

> levels = log(10⁷) ÷ log(f)

| Compression per level, f | Levels needed |
| --- | --- |
| 100 | 3 or 4 |
| 10 | 7 |
| 3 | about 15 |

The theory does not yet say what f should be, and this is the least constrained part of the design. But it gives a range: **between about four and fifteen levels**, with gentle compression per level meaning more of them. Chapter 11 offers a hint that gentle compression is the rule in nature: the layers of human social groups grow by a factor of about three each time.

## Step 3. How big can it be?

The mind has one second for each decision. Chapter 10 estimated that a decision takes some tens of crossing times in every mind where it has been measured, about fifty. So the crossing time must be no more than about a fiftieth of a second, 20 milliseconds, and the size no more than the distance a signal covers in that time.

| Signals made of | Speed | Maximum size |
| --- | --- | --- |
| thin nerve fibres | 1 m/s | 2 centimetres |
| typical nerve fibres | 10 m/s | 20 centimetres |
| the fastest nerve fibres | 100 m/s | 2 metres |
| flying insects | 7 m/s, plus minutes to deliver each message | cannot meet the deadline at any size |
| electrical cables | 200,000 km/s | 4,000 kilometres |

A mind made of nerve cells that does this job must **fit in a space a few centimetres to a few tens of centimetres across.** A mind made of animals that carry messages to one another cannot do it at all.

## Step 4. Which kind of mind?

The output is one decision at a time. Chapter 8 argued that a single stream of decisions needs a stage: one broadcast shared by the whole. So **the top of the hierarchy must be integrated.**

Step 3 showed that the whole mind fits inside the distance its signals can cross in time, so nothing forces the lower levels to be federated. But step 1 says that the entrance should be a great many thin channels, and thin channels between levels mean that each level computes more than it passes on. The economical design is therefore a stack of modules that say little to each other, feeding an integrated top: **federated below, integrated above.**

## Step 5. What will it cost?

The floor is Landauer's limit. Discarding ten million bits a second at body temperature costs about 3 × 10⁻¹⁴ watts, which is nothing.

At the prices nerve cells actually pay, between ten thousand and ten million molecules of ATP per bit (1), carrying the input stream across the first stage costs somewhere between a hundredth of a microwatt and ten microwatts. The later levels carry far less and add little. The whole pipeline, counted as transmission alone, should run on **microwatts.**

## Step 6. How many agents in all?

If each level has 1/f as many agents as the one below, the total is only a little more than the first level: about one and a half million agents for f = 3.

## The design, and a mind that matches it

Collected, the theory's outline of a mind for this task is:

- about a million slow input channels, each carrying about ten bits per second
- four to fifteen levels, probably nearer the upper figure
- a size of centimetres to tens of centimetres if built from nerve cells
- loosely coupled modules at the bottom and a single integrated stage at the top
- a transmission cost of microwatts
- at least a million or two agents

The numbers in the specification were not chosen at random. Ten million bits per second is the estimated output of the human eye, and a few bits per second is the rate at which a person acts. The specification is, near enough, *seeing something and deciding what to do about it*. So the outline can be checked against the only minds known to do that job.

| Feature | Predicted from the task | Human visual system |
| --- | --- | --- |
| Input channels | about a million | 0.7 to 1.5 million fibres in the optic nerve (2) |
| Rate per channel | about 10 bits per second | 6 to 13 bits per second per fibre, measured in guinea pig (3) |
| Which channels carry most | the slow ones | the "sluggish" cells, being more numerous, carry most of the information (3) |
| Levels | 4 to 15 | 10 levels of visual cortex, 14 counting the retina and the stations before and after (4) |
| Compression per level | 3 to 100 | about 3, if a million-fold reduction is spread over about 12 levels (our estimate) |
| Size | 2 to 20 centimetres | about 15 centimetres |
| Arrangement | modules below, one stage above | a retina that does its own processing and sends a summary; a single stream of choice at the top (5) |
| Transmission power | microwatts | far more; see below |
| Number of agents | a million or two | billions; see below |

Seven of the nine rows come out right, from a starting point of three numbers. The entrance is the right width, built from channels of the right speed, with the slow ones carrying the load. The depth is in range. The size is right. The arrangement is right. A compression of about three per level is a coincidence with the ratio between human social layers that may or may not mean something.

It should be said plainly that this is not a blind prediction. The author knew what a visual system looks like before doing the sum, and several of the rules used were themselves learned from nervous systems. The test is weaker than it appears. It becomes a real test when the same six steps are applied to animals whose anatomy the theorist has not looked up, and the next section says how.

## The two misses, and what they teach

The design misses badly in two rows, and the misses are the most useful part of the exercise.

The theory says that a couple of million agents and a few microwatts are enough. The real visual system uses billions of neurons, close to half of the cerebral cortex in a primate by one textbook's account (6), and a large share of the brain's twenty watts (our estimate).

The reason is that the specification left something out. It described *one* decision: one fixed question, asked of the stream every second. A machine built to answer one fixed question can indeed be that small. A motion detector, a smoke alarm and a frog's bug-detector are all devices of this kind, and they are tiny and cheap.

An animal's visual system is not answering one question. It can be asked, from moment to moment, any of an enormous number: is that a face, is it angry, is the branch within reach, is the fruit ripe, what does this word say. Each of those is a different reduction of the same ten million bits. Chapter 5 showed what answering a question efficiently requires: prior knowledge, stored in advance. A mind that can answer many questions must store the priors for all of them.

So the specification needs a fourth number, which the framework of Chapter 12 does not yet contain: the **repertoire**, the number of different tasks the mind must be ready to perform. And the lesson can be stated as a rule, which is a claim of the theory:

**The input rate of a task sets the width of a mind's entrance. The compression sets its depth. The deadline sets its size. The repertoire sets its bulk.**

Most of a brain is not pipeline. It is library.

That yields a prediction that can be checked against comparative anatomy. Two species with similar eyes, and so similar input rates, should have similar numbers of optic nerve fibres however different their intelligence. Where they should differ is in the tissue behind the entrance, in proportion to the variety of what they do with what they see. The number of fibres should follow the eye; the number of neurons should follow the life.

## A second design: when the answer is a swarm

Change the specification and the outline changes with it.

*Find the best of a dozen or more possible nest sites scattered over tens of square kilometres of forest. Each site has to be visited and inspected at length. A wrong choice is fatal. A decision within a few days is soon enough.*

Step 3 now gives a completely different answer. The information is not arriving at one place. It is spread over an area that no single nervous system can span, and gathering it means going there. The crossing time is set by flight, tens of minutes. But the deadline is days, so the coherence number is still comfortably large: there is time for some fifty crossings.

The output is a handful of bits, one choice among a dozen, once. No fast stream of decisions is needed, so no stage is required.

Each inspection demands a capable observer, able to navigate, judge a cavity and remember the way back, so each agent must be rich. Rich agents sending short reports are, by Chapter 8, the makings of a federated mind. And since a wrong choice is fatal, the design should favour accuracy over speed and tolerate the loss of any individual: again federated.

The outline is: **many mobile, capable agents; a few bits per report; no centre; a decision by slow accumulation with mutual suppression.** That is the honeybee swarm of Chapter 1, with its scouts and its seven-bit dances (7, 8).

The two designs make the chapter's main point. The same theory, given two different tasks, returns a brain for one and a swarm for the other. Neither is the better mind. Each is the shape of its problem.

## The map of possible minds

The two examples suggest a general map. Two of the pure numbers do most of the work: the coherence number, which says whether the mind can keep up with its world, and the thought-to-talk number, which says whether its agents share most of what they compute.

| | Agents share most of what they compute (integrated) | Agents share little (federated) |
| --- | --- | --- |
| **Keeps up with its world** | Brains. Fast, small, serial, able to be someone. Suited to fast, local problems. | Swarms, colonies, firms, sciences. Slow, large, parallel, robust. Suited to wide, slow problems. |
| **Too slow for its world** | Does not last. An integrated mind that cannot keep up gains nothing from its integration and pays its full cost. | Not a mind. A crowd, a scattered species, a civilisation spread too thin: agents that share a code but cannot decide together. |

And one corner of the space is empty by law. Chapter 8 concluded that no mind can be large, fast and unified at once. In the terms of this chapter, a task that demands wide coverage, a quick deadline and a single stream of decisions has no solution. No morphology meets it. The practical response, in nature and in human organisations, is always the same: break the task up, so that fast local decisions are made by small integrated minds and slow global ones by a federation of them.

## Running it backwards

The same reasoning can be run the other way, from a given mind to the tasks that are beyond it. These are predictions too.

- **A swarm cannot catch a ball**, or do anything else whose deadline is shorter than its crossing time. No amount of extra bees helps.
- **A single brain cannot survey a forest.** Its input is limited to what reaches one place.
- **A federated mind cannot have an insight**, in the sense of rebuilding its whole picture at one stroke, because no part of it holds the whole picture. It can only improve by parts. A committee can edit a document and cannot conceive one.
- **An integrated mind cannot do two things at once** at the level of choice.
- **Humanity cannot respond as one** to anything that unfolds faster than its own crossing time, which for matters needing real agreement is still measured in years.
- **A mind cannot answer a question for which it lacks the priors** faster than it can gather the bits, whatever its capacity. Chapter 5's ceiling forbids it.

## What an engineer of minds could now do

If these rules hold, they apply to the minds we build as well as to those we find. A company, a research programme, an emergency service and a system of artificial agents are all collectives with a task. The six steps can be asked of each.

- How fast does information arrive, and how much must come out? That sets the width of the entrance and the depth of the hierarchy. An organisation with too few levels for its compression drowns its top in detail. One with too many is slow.
- What is the deadline? That sets the largest group that can decide as one. An emergency room must be a small, integrated team. A standards body can be the whole world.
- Is the information in one place or many? If many, the lower levels must be federated, and their reports must be short.
- How large is the repertoire? That sets how much must be stored and trained in advance, which is most of the cost.
- Is one stream of decisions needed? If so, there must be a single stage, and it will be a bottleneck. If not, do not build one.

None of this is new to a good manager or a good systems engineer. What the theory adds, if it is right, is the claim that these are not rules of thumb. They are consequences of the physics of information, and they could be calculated. The next chapter applies them to the minds now being built.

## In short

- The framework of Chapter 12 can be run forwards: from a task to the outline of a mind that can perform it.
- For a task of ten million bits per second in, one decision per second out, the theory gives about a million slow input channels, four to fifteen levels, a size of centimetres to tens of centimetres in nerve tissue, modules below and one stage above.
- That matches the human visual system in seven of nine respects, including the number of optic nerve fibres, the rate each carries and the number of processing levels. The match is a consistency check, not a blind prediction.
- It misses on the number of neurons and the power used, by factors of a thousand or more. The lesson: a brain's bulk is set by its repertoire, the number of different questions it must be ready to answer. Most of a brain is library, not pipeline.
- For a task of slow, wide-area search with a fatal cost of error, the same steps give a swarm.
- Minds can be mapped by two pure numbers. One region of the map, large, fast and unified, is empty.
- The rules also say what each kind of mind cannot do, and can be applied to organisations and artificial systems.

## How we could be wrong

This chapter makes the theory's most checkable claims. Apply the six steps to animals whose anatomy was not consulted in advance, estimate each species' visual input rate from the optics of its eye, and predict the number of fibres in its optic nerve and the number of stages before behaviour. If the fibre counts do not follow the input rate, or follow it with a rate per fibre that varies widely between species, the rule for the width of the entrance is wrong. If the depth of sensory hierarchies bears no relation to the compression they perform, the rule for depth is wrong. If species with similar eyes and very different behavioural repertoires have similar amounts of visual brain, the claim about repertoire is wrong. If a collective is found that decides as one across a distance its signals cannot cross within its deadline, the rule for size is wrong, and with it much of the book. And if the outline of a mind turns out to depend mainly on things the specification leaves out, on evolutionary accident, on materials, on the particular algorithm, then tasks do not determine morphology, and the engineer's question has no general answer.

## References

1. S. B. Laughlin, R. R. de Ruyter van Steveninck and J. C. Anderson (1998), "The metabolic cost of neural information", *Nature Neuroscience* 1:36–41. https://doi.org/10.1038/236
2. C. A. Curcio and K. A. Allen (1990), "Topography of ganglion cells in human retina", *Journal of Comparative Neurology* 300:5–25. https://pubmed.ncbi.nlm.nih.gov/2229487/
3. K. Koch, J. McLean, R. Segev, M. A. Freed, M. J. Berry, V. Balasubramanian and P. Sterling (2006), "How much the eye tells the brain", *Current Biology* 16:1428–1434. https://pmc.ncbi.nlm.nih.gov/articles/PMC1564115
4. D. J. Felleman and D. C. Van Essen (1991), "Distributed hierarchical processing in the primate cerebral cortex", *Cerebral Cortex* 1:1–47. https://chd.ucsd.edu/_files/fall2008/Felleman.1991.CC_Part1.pdf
5. H. Pashler (1994), "Dual-task interference in simple tasks: data and theory", *Psychological Bulletin* 116:220–244. https://pubmed.ncbi.nlm.nih.gov/7972591/
6. M. Meister and M. Tessier-Lavigne, "Low-level visual processing: the retina", in E. R. Kandel et al. (eds), *Principles of Neural Science*, McGraw-Hill. https://www.weizmann.ac.il/brain-sciences/labs/ulanovsky/sites/neurobiology.labs.ulanovsky/files/uploads/chapter_22_low-level_visual_processing_the_retina.pdf
7. T. D. Seeley, P. K. Visscher and K. M. Passino (2006), "Group decision making in honey bee swarms", *American Scientist* 94:220–229. https://bees.ucr.edu/media/156/download
8. R. Schürch and F. L. W. Ratnieks (2015), "The spatial information content of the honey bee waggle dance", *Frontiers in Ecology and Evolution* 3:22. https://www.frontiersin.org/articles/10.3389/fevo.2015.00022

All arithmetic in the design steps is our own and is rough: the channel count, the number of levels, the size limits, the power estimates and the agent counts. The figure of ten bits per second for an economical channel is taken from the measurements in reference 3 and is an assumption when applied elsewhere. The six design steps, the rule relating input rate, compression, deadline and repertoire to a mind's width, depth, size and bulk, the map of possible minds, and the list of what each kind cannot do are the theory's claims.
