# Chapter 1. The swarm that chooses a home

## A beard of bees

In late spring, a crowded beehive splits in two. The old queen leaves with several thousand workers, and the cloud of bees settles a few metres away, usually on a tree branch. There it hangs for hours or days: a dense, humming beard of up to 10,000 insects, clinging to one another and to the queen at the centre.

The swarm is homeless and exposed. It carries only the honey in its members' stomachs, so it cannot wait long. Somewhere within a few kilometres there must be a hollow tree or a cavity in a wall that will shelter the colony for years. The swarm has to find it, judge it against the alternatives, and fly there together.

No bee is in charge. The queen does not choose; she is carried along. No scout visits every candidate site, and no bee ever compares them all. And yet, in most cases, the swarm picks well. This chapter is about how that happens, and about why it is the right place to begin a physical theory of intelligence.

## Dances without pollen

The first person to look closely was the German biologist Martin Lindauer, in the 1950s. Watching swarms, including one hanging outside the Zoological Institute in Munich, he noticed bees dancing on the surface of the cluster. These were waggle dances, the figure-of-eight runs that foragers use in the hive to report the direction and distance of flowers.

But these dancers carried no nectar and no pollen. Lindauer guessed they were reporting something else: places to live. He marked each new dancer with a dot of paint and recorded which location her dance pointed to. At first the dances pointed in many directions. Over hours, the number of advertised sites shrank, until all the dancers pointed the same way. Then the swarm lifted off and flew in that direction (1).

Decades later, Thomas Seeley and his colleagues reconstructed the process in detail, labelling thousands of bees and filming every dance (1).

## How a swarm decides

The decision is made by a few hundred scouts out of the thousands of bees in the swarm. The rest wait quietly, saving energy for the flight. The scouts fly out, find cavities, inspect them and come back to dance. A swarm typically finds a dozen or more candidate sites.

Bees are fussy about real estate. They prefer a cavity larger than about 20 litres, with an entrance smaller than about 30 square centimetres, several metres off the ground, facing south, with the entrance near the floor. A scout that has found such a place dances long and hard. On her first return from an excellent site she may perform 100 or more dance circuits. From a mediocre site, she performs about a dozen (1).

Three details of the procedure matter for everything that follows.

**Dances fade.** Each time a scout returns to her site and dances again, her dance is about 15 circuits shorter (1). Even an enthusiastic scout eventually falls silent. Support for a site therefore survives only if new scouts keep being recruited to it. A site that is merely first, or merely loudly promoted, cannot win on momentum alone.

**Recruits check for themselves.** A bee that follows a dance does not simply adopt the dancer's opinion. She flies to the site, inspects it, and dances only if she finds it good, with a vigour that reflects her own assessment. Information passes between bees, but judgement stays local. Each scout remains an independent sensor.

**The decision is a quorum, not a vote.** Scouts at a candidate site can sense how many others are there. When roughly 15 or more bees are present at one site at once, which corresponds to about 150 scouts committed to it overall, they return and start piping (2). Piping is a short buzzing signal, about 0.8 seconds long, that tells the waiting bees to warm their flight muscles to 33–35 °C. Warming up takes an hour or more. Then the swarm takes off (1).

In one swarm studied in 1997, the whole process took about 16 hours of dancing spread over three days. In an experiment with five nest boxes, one excellent (40 litres) and four mediocre (15 litres each), swarms chose the excellent box in four of five trials (1).

## Where is the decision?

Think about what no bee knows. Most scouts have seen one site, perhaps two. No bee holds a list of candidates with their scores. No bee computes which is best. No bee decides when the debate is over.

The comparison happens in the population. Good sites recruit faster because their dances are longer. Weak sites fade because their supporters fall silent and are not replaced. The decision is reached when one population of scouts grows large enough to be noticed at the site itself. The choice is a property of the whole system of bees and their exchanges, not of any part of it.

That is the claim at the heart of this book. **Intelligence emerges from many agents that each store and process information independently, and communicate with each other.** The swarm has exactly these ingredients:

- **Agents**: scouts, each with a small brain of about 960,000 neurons (3), able to judge a cavity and remember it.
- **Communication**: the dance, a channel that carries a location and a quality signal.
- **Structure**: rules about who listens to whom, how support fades, and when to stop.

## The same decision in a brain

The swarm's procedure would look familiar to a neuroscientist. When a monkey decides whether a cloud of dots drifts left or right, two populations of neurons in its brain accumulate evidence for the two options. When one population's activity crosses a threshold, the choice is made (4).

In 2012, Seeley and his colleagues showed that swarms share one more feature with brains. Scouts committed to one site deliver "stop signals", a brief buzz and a head-butt, to dancers advertising a rival site. Neurons do the same thing to each other, and it is called cross-inhibition (5). Earlier work by James Marshall and colleagues had shown that this kind of competition between evidence-accumulating populations can make decisions statistically optimal, in brains and colonies alike (6).

So a swarm and a brain are not just loosely similar. They seem to run the same algorithm, on completely different hardware: neurons in one case, bees in the other. If that is true, the algorithm is the important thing, and the hardware is a detail. This is the first piece of evidence that intelligence might be described by physics that does not care what the agents are made of.

It also raises a stranger possibility, which Chapter 10 takes seriously: that the swarm's sixteen hours of dancing and the monkey's half-second of neural firing are the same thought, played at two different speeds.

## A very thin conversation

Here is the puzzle that will occupy several later chapters. A waggle dance carries surprisingly little information. A careful analysis of dance accuracy estimates about 2.9 bits for direction and 4.5 bits for distance: roughly 7 bits per location, about as much as one letter of text (7).

Each bee, meanwhile, carries a brain whose neurons exchange signals far faster than any dance. The swarm's "conversation" is many orders of magnitude thinner than the thinking inside any one of its members. And yet the swarm solves a problem that no single bee can solve.

Part of the resolution is that seven bits are not as little as they look. A dance means something only because every bee is born knowing the code: that the angle of the run stands for a direction relative to the sun, and its length for a distance. That shared code was paid for over millions of years of evolution, and each dance draws on it. A message is never just the bits it contains. It is those bits plus everything sender and receiver already share. Chapter 6 turns this into a measurable quantity.

The other part is that the swarm does not win by thinking harder than a bee. It wins by reaching further. Hundreds of scouts sample kilometres of countryside in parallel, and each compresses what she found into a few bits. The swarm trades depth for breadth. We will see in Part III that this trade is not a quirk of bees, but something that happens every time minds are built out of minds.

## The wisdom of crowds, and its fragility

The idea that many modest judgements can add up to a good one has a famous human example. In 1906, at a livestock fair in Plymouth, England, 787 people paid sixpence each to guess the weight of an ox after slaughter. Many were butchers and farmers; many were not. Francis Galton collected the cards. The middle guess was 1,207 pounds. The actual dressed weight was 1,198 pounds, an error of under one percent (8). (A later re-examination of Galton's papers puts the error at 11 pounds, which hardly changes the point (9).)

No individual guesser was that accurate. The accuracy appeared only when independent errors cancelled out. The word *independent* is doing all the work. A 2011 experiment showed that even mild social influence, simply letting people see what others guessed, narrows the spread of opinions and undermines the crowd's accuracy without improving it (10).

This is the central tension of every collective mind, and the bees have solved it with care. Their agents must communicate enough for a decision to emerge, but not so much that they simply copy one another. Recruits inspect the site themselves. Dances fade. Rival opinions are actively inhibited, not ignored. Too little coupling and there is no collective; too much and there is only an echo.

Notice what the bees share and what they do not. They share a code: every bee reads a dance the same way. They do not share conclusions: every scout forms her own opinion of a site. A common language with independent judgement is the recipe, and human groups that get it backwards, agreeing on what is true before agreeing on what words mean, should expect to be stupid. Chapter 3 shows the same tension inside the brain, where too much coupling has a medical name.

## In short

- A honeybee swarm chooses a nest site through a process in which no individual compares the options. The choice exists only in the pattern of interactions.
- The swarm's procedure matches the one brains use to decide: competing populations accumulate evidence, inhibit each other, and stop at a threshold.
- The swarm's communication is extremely thin, a few bits per message, yet it outperforms any individual. It trades depth for reach.
- Collective intelligence depends on a balance: enough communication to integrate, enough independence to keep errors from becoming correlated.

## How we could be wrong

The premise would be in trouble if collective decisions like the swarm's turned out to depend on a hidden leader or a privileged individual, such as a few scouts whose judgement simply overrides the rest. It would also be weakened if swarms performed just as well when the scouts copied each other without inspecting sites, since that would mean independence is not essential. Both can be tested by manipulating swarms, and so far the evidence points the other way.

## References

1. T. D. Seeley, P. K. Visscher and K. M. Passino (2006), "Group decision making in honey bee swarms", *American Scientist* 94:220–229. Source for Lindauer's observations, scout numbers, cavity preferences, dance circuits and their decline, piping, the 1997 swarm and the five-box test. https://bees.ucr.edu/media/156/download
2. T. D. Seeley and P. K. Visscher (2004), "Quorum sensing during nest-site selection by honeybee swarms", *Behavioral Ecology and Sociobiology* 56:594–601. https://www.doi.org/10.1007/S00265-003-0664-6
3. R. Menzel and M. Giurfa (2001), "Cognitive architecture of a mini-brain: the honeybee", *Trends in Cognitive Sciences* 5:62–71; figure as listed in BioNumbers. https://bionumbers.hms.harvard.edu/bionumber.aspx?id=109328
4. J. I. Gold and M. N. Shadlen (2007), "The neural basis of decision making", *Annual Review of Neuroscience* 30:535–574. https://doi.org/10.1146/annurev.neuro.29.051605.113038
5. T. D. Seeley, P. K. Visscher, T. Schlegel, P. M. Hogan, N. R. Franks and J. A. R. Marshall (2012), "Stop signals provide cross inhibition in collective decision-making by honeybee swarms", *Science* 335:108–111; summary by Cornell University. https://news.cornell.edu/node/271186
6. J. A. R. Marshall, R. Bogacz, A. Dornhaus, R. Planqué, T. Kovacs and N. R. Franks (2009), "On optimal decision-making in brains and social insect colonies", *Journal of the Royal Society Interface* 6:1065–1074. https://ora.ox.ac.uk/objects/uuid:e1bddf33-2467-4a42-846c-0ba4a556b138
7. R. Schürch and F. L. W. Ratnieks (2015), "The spatial information content of the honey bee waggle dance", *Frontiers in Ecology and Evolution* 3:22. https://www.frontiersin.org/articles/10.3389/fevo.2015.00022
8. F. Galton (1907), "Vox populi", *Nature* 75:450–451. https://galton.org/cgi-bin/searchImages/search/essays/pages/galton-1907-vox-populi_1.htm
9. K. F. Wallis (2014), "Revisiting Francis Galton's forecasting competition", *Statistical Science* 29:420–424. https://arxiv.org/pdf/1410.3989
10. J. Lorenz, H. Rauhut, F. Schweitzer and D. Helbing (2011), "How social influence can undermine the wisdom of crowd effect", *PNAS* 108:9020–9025. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299

The comparison between the swarm and the brain, and the reading of the dance's shared code as stored context, are the theory's own.
