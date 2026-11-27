# Chapter 12. The theory on one page

*This chapter is different from the others. It contains no stories. It sets out the theory the way a physics text would: the quantities, their units, the pure numbers built from them, the limits, and the relations the theory claims between them. It is the only chapter with formulas, and each formula is followed by the same statement in words. Readers who prefer the narrative can go straight to Chapter 13, which puts this machinery to work, and return here for reference.*

## Why write it down

The first three parts of this book introduced a way of describing minds one idea at a time, each with its own bees, brains and birds. A physical theory has to be more than a collection of good examples. It needs a short list of measurable quantities, a statement of how they combine, and limits that no system can exceed. With those in hand, two people who disagree about a mind can do what physicists do: measure, calculate and see who is right.

Thermodynamics is the model. It describes steam engines, stars and living cells with a handful of variables, such as temperature, pressure, volume and entropy, and a few laws relating them, without needing to know what each molecule is doing. The aim here is the same: to describe a collective mind by a few numbers, without following each agent.

What follows is a framework, not yet a finished theory. The last section says what is missing.

## The base quantities

Four physical dimensions are enough.

| Dimension | Unit | What it measures here |
| --- | --- | --- |
| Information | bit | how much uncertainty is removed, stored or sent |
| Time | second | how long things take |
| Length | metre | how far apart agents are |
| Energy | joule | what it all costs |

The number of agents is a pure count with no unit. Temperature enters only through the price of a bit, below.

Treating the bit as a physical unit on a level with the second and the metre is the step everything else depends on. Chapter 2 gave the justification: information has an energy cost that has been measured in the laboratory (1), and each bit gathered buys at most one bit of control over the world (2).

## The variables of a mind

To specify a collective mind, give these numbers. The right-hand columns show rough values for two familiar cases; they are our estimates, collected from the earlier chapters.

| Symbol | Quantity | Unit | Human brain | Bee swarm |
| --- | --- | --- | --- | --- |
| N | number of agents | — | about 10¹¹ neurons | about 10⁴ bees, a few hundred scouts |
| d | links per agent | — | about 10⁴ synapses | a few dances watched |
| m | memory per agent | bit | about 10⁵ | large: a brain's worth |
| r | processing rate per agent | bit/s | a few | very large: a million neurons |
| c | capacity of one link | bit/s | a few | about 7 bits per dance |
| L | size of the collective | m | 0.15 | several thousand |
| v | signal speed | m/s | 1 to 100 | a bee's flight, about 7 |
| T_w | timescale of the world it deals with | s | 0.1 to 1 | hours to days |
| R_in | information arriving from outside | bit/s | about 10⁹ | what the scouts see |
| R_out | information leaving as action | bit/s | about 10 | a few bits per day |
| P | power | W | 20 | a few watts |
| S | context shared among agents | bit | genome, development, experience | the dance code |

Two points about this table matter more than any entry in it.

First, most of these can be measured with existing methods. Counting agents and links is anatomy. Capacities and rates have been measured for neurons, for speech and for the waggle dance. Signal speeds have been known since Helmholtz.

Second, the two columns differ by many orders of magnitude in almost every row. The claim of this book is that despite this, the two systems can be compared, because what governs their behaviour is not these numbers but certain ratios between them.

## Derived quantities

A few combinations appear so often that they deserve names.

**Crossing time.** The time for a signal to travel across the collective.

> t_x = L / v

For a brain it is tens of milliseconds. For a swarm, tens of minutes. For humanity before the telegraph, months. Chapter 10 proposed that this is each mind's natural unit of time.

**Total processing.** What all the agents compute between them, N × r.

**Cross-talk.** The information per second that can pass across a surface cutting the collective in half. Call it B. It is fixed by how many links cross the cut and how much each carries. This is the quantity Chapter 4 called the bandwidth through a surface, and it limits how much the two halves can tell each other.

**Capacity.** The information per second that the collective as a whole can bring to bear on a single decision. Call it C. It can be no larger than what arrives, no larger than what the agents can process, and, when the whole must act as one, no larger than what can cross between its parts.

> C ≤ the smallest of R_in, N × r and, for unified action, B

**Efficiency.** The fraction of the information used that ends up as reduced uncertainty about what to do. Chapter 5 called it η.

> η = bits of uncertainty about the goal removed ÷ bits of information used

**Meaning conveyed.** What a message delivers is what it carries plus what the receiver already shares with the sender (Chapter 6).

> meaning = bits sent + bits of shared context that the message activates

**Context amplification.** How much shorter a message becomes because of what is shared. If describing a situation from scratch takes H bits, and describing it to someone who shares your context takes H_S bits, then

> κ = H / H_S

It is 1 between total strangers and can reach hundreds between people who know each other well. The effective capacity of a link is then κ × c.

## The pure numbers

Chapter 4 explained why pure numbers matter: a ratio with no units is the same whatever system of measurement is used, and two systems with the same pure numbers behave alike however different they look. The theory rests on the following set. The first seven were in its original formulation. The last three were added by the chapters of Part III.

| Name | Definition | What it decides | Chapter |
| --- | --- | --- | --- |
| Coherence number | T_w / t_x | whether the collective can act as one on its world; it must be well above 1 | 4 |
| Thought to talk | r / (d × c) | integrated when near 1, federated when far above 1 | 4, 8 |
| Memory horizon | N × m / (R_in × T_w) | how many world-times of experience it can hold | 4 |
| Boundary number | traffic across the outer edge / B | whether it is a self; it must be far below 1 | 4, 14 |
| Cost above the floor | energy per bit / Landauer's limit | how far from the thermodynamic minimum it runs | 2, 7 |
| Correlation ratio | correlation length / L | whether it is one system; it must be near 1 | 11 |
| Context amplification | κ | how much each bit conveys | 6 |
| Exchange to drift | rate of exchange between parts / rate at which their codes drift | whether it stays one kind; it must exceed a threshold | 9 |
| Cognitive time | t / t_x | the clock on which different minds can be compared | 10 |
| Wiring dimension | D, defined by B ∝ N^(1−1/D) | how well cross-talk keeps up with size | 4, 11 |

Three of these are the conditions for unity that Chapter 9 gathered into one law. Written together:

> acts as one when T_w ≫ t_x
>
> is a self when the traffic across its edge ≪ B
>
> stays one kind when exchange ≫ drift

In each, the traffic inside the collective is compared with a competing rate. That is the sense in which the theory says that unity is a ratio of rates.

## The limits

Five bounds are borrowed from established physics and information theory. No mind of any kind can exceed them.

**The price of a bit.** Erasing one bit of information dissipates at least

> E = k_B × Θ × ln 2

where k_B is Boltzmann's constant and Θ the temperature: about 3 × 10⁻²¹ joules at room temperature. This is Landauer's limit, confirmed by experiment (1, 3). It sets the minimum power for a given rate of processing.

**The return on a bit.** One bit of information about a system allows at most one bit of reduction in its uncertainty (2). Hence

> η ≤ 1

**The capacity of a channel.** A link of given bandwidth and noise can carry only so much, as Shannon proved (4). This bounds c.

**The speed of signals.** Nothing travels faster than light, so for any mind that must act as one within a time t,

> L ≤ (speed of light) × t

and in practice L ≤ v × t for whatever its signals are made of. This is the limit on size from Chapter 15.

**The speed of change.** A system with energy E can pass through at most 2E / πħ distinguishable states per second, where ħ is Planck's constant (5). Applied to a kilogram of matter this gives the ceiling on capacity from Chapter 7 (6).

## The scaling relations

How the quantities change as a mind grows.

**Cross-talk grows more slowly than size.**

> B ∝ N^(1−1/D)

With only local links in three dimensions, D is 3, and doubling the agents multiplies the cross-talk by about 1.6. All-to-all wiring would keep pace with size but cannot be built. Real brains and computer chips have D above 3, bought with long cables (7).

**Crossing time grows with size.** At constant density, t_x ∝ N^(1/3) / v.

**Cables grow faster than the tissue they serve.** Across mammals, white matter scales as the 4/3 power of grey matter (8).

**The price of a bit rises with the rate.** In the neurons where it has been measured, a channel carrying more bits per second pays more for each one (9). The rule that many slow channels beat one fast one follows from this.

**Brain energy is proportional to neuron number.** The cost per neuron is roughly constant across species (10).

Combining the first two gives the result of Chapter 7 in one line. For a collective with local links, the cross-talk per agent falls as N^(−1/3) while the delay rises as N^(1/3). The larger a mind grows, the less each part can tell the rest, and the later it arrives.

## What the theory claims

The quantities and limits above are either definitions or established results. The theory's own content is the following set of relations. Each is a hypothesis.

1. **Intelligent output is capacity times efficiency.** The rate at which a mind reduces uncertainty about what to do is C × η, with η at most 1 and C bounded as above.
2. **Meaning is bits sent plus context shared**, and the effective capacity of a link is κ × c.
3. **Unity is a ratio of rates**, in the three forms given above.
4. **Similarity.** Two collectives with the same pure numbers perform the same computations when time is counted in units of t_x. A decision takes tens of crossing times in any of them.
5. **Kind follows from the thought-to-talk number.** Near 1, a collective is fast, limited in size, serial and capable of being a subject. Far above 1, it is slow, unlimited in size, parallel and no one.
6. **Levels are where scaling breaks.** A boundary between agents and the collective they form appears as a change of exponent in some scaling relation, and an agent is a block whose effect on the outside can be summarised in far fewer bits than its internal state.
7. **Balance.** A collective's intelligence is greatest when the correlation ratio is near 1 while its agents' judgements remain independent: shared code without shared belief.

## How well defined is each piece?

A framework is only as good as its weakest definition. This table is an honest account.

| Quantity | Status |
| --- | --- |
| N, d, L, v, t_x, P | measured routinely |
| c, r for neurons, speech, dances | measured in particular systems |
| R_in, R_out for a person | measured, with debate about the method |
| B, D for brains and chips | estimated from anatomy |
| Coherence number, cognitive time | computable from the above |
| Correlation ratio | measured in flocks and cortex |
| Thought-to-talk number | estimated only; no agreed way to measure an agent's internal processing in bits |
| Boundary number | estimated only |
| Exchange-to-drift number | measured in population genetics; not yet for languages or organisations |
| κ, shared context | defined; not yet measured in any real pair |
| η | defined for tasks that reduce to removing uncertainty; no general measure of achievement |
| C for a federated mind | not well defined; it is unclear what "brought to bear on one decision" means when nothing is broadcast |

The bottom four rows are where the work is.

## What is missing

Four things separate this framework from a complete physical theory.

**Equations of motion.** Thermodynamics says which states are possible; it took statistical mechanics to say how systems move between them. This framework has limits and ratios. It does not yet have equations that take a collective's variables at one moment and give them at the next. The accumulate-and-inhibit models of Chapter 1 are such equations for one kind of decision, and they are the natural starting point.

**A derivation of the thresholds.** The theory says that the coherence number must be "well above" 1 and the boundary number "far below" it. A finished theory would say how far, and why, as the theory of phase transitions gives the exact temperature at which water boils.

**Operational definitions for the last four rows** of the table above.

**A variable for repertoire.** Chapter 13 will show that the framework, applied to a real brain, accounts for its shape and badly underestimates its bulk, because nothing in the list above says how many different tasks a mind must be ready to perform.

None of these is out of reach. Each could be attacked with a computer simulation of a few thousand simple agents, in which every variable in this chapter can be set and every pure number measured exactly. That is probably the most useful single piece of work the theory now needs.

## In short

- The theory uses four dimensions, the bit, the second, the metre and the joule, and describes a collective mind by about a dozen variables.
- From these it builds derived quantities, including crossing time, cross-talk, capacity, efficiency and context amplification, and ten pure numbers.
- Five limits from established physics apply to every mind: the price of a bit, the return on a bit, channel capacity, signal speed and the maximum rate of change.
- Scaling relations say how cross-talk, delay, cabling and cost change with size.
- The theory's own claims are seven relations, among them that output is capacity times efficiency, that unity is a ratio of rates, and that minds with the same pure numbers think alike.
- Several quantities are not yet measurable, and the framework lacks equations of motion and derived thresholds.

## How we could be wrong

A framework of this kind fails in a particular way: not by being contradicted, but by being useless. If the pure numbers listed here do not sort real collectives into groups that behave alike, so that systems with matching numbers differ and systems with different numbers match, then the choice of variables is wrong, however reasonable each looked. If the quantities in the bottom rows of the status table cannot be given definitions that different investigators measure the same way, the central formula cannot be tested. And if a simulation of simple agents shows that behaviour depends strongly on details the framework ignores, such as the exact rule each agent follows, then a description by a dozen numbers is too coarse, and minds are not the kind of thing that thermodynamics-style theories can capture.

## References

1. A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider and E. Lutz (2012), "Experimental verification of Landauer's principle linking information and thermodynamics", *Nature* 483:187–189. https://pubmed.ncbi.nlm.nih.gov/22398556/
2. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
3. R. Landauer (1961), "Irreversibility and heat generation in the computing process", *IBM Journal of Research and Development* 5:183–191.
4. C. E. Shannon (1948), "A mathematical theory of communication", *Bell System Technical Journal* 27:379–423 and 623–656.
5. N. Margolus and L. B. Levitin (1998), "The maximum speed of dynamical evolution", *Physica D* 120:188–195.
6. S. Lloyd (2000), "Ultimate physical limits to computation", *Nature* 406:1047–1054. https://arxiv.org/abs/quant-ph/9908043
7. D. S. Bassett et al. (2010), "Efficient physical embedding of topologically complex information processing networks in brains and computer circuits", *PLOS Computational Biology* 6:e1000748. https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671
8. K. Zhang and T. J. Sejnowski (2000), "A universal scaling law between gray matter and white matter of cerebral cortex", *PNAS* 97:5621–5626. https://pmc.ncbi.nlm.nih.gov/articles/PMC25878
9. S. B. Laughlin, R. R. de Ruyter van Steveninck and J. C. Anderson (1998), "The metabolic cost of neural information", *Nature Neuroscience* 1:36–41. https://doi.org/10.1038/236
10. S. Herculano-Houzel (2011), "Scaling of brain metabolism with a fixed energy budget per neuron: implications for neuronal activity, plasticity and evolution", *PLoS ONE* 6:e17514. https://pmc.ncbi.nlm.nih.gov/articles/PMC3046985

The example values in the table of variables are our own rough estimates, drawn from earlier chapters. The choice of variables, the definitions of capacity, meaning and the pure numbers, the seven relations and the assessment of what is missing are the theory's own.
