# Chapter 11. Fractals and breaks

## How long is the coast of Britain?

In the 1950s the English mathematician Lewis Fry Richardson was studying whether countries with longer shared borders go to war more often. He looked up the lengths of borders and found that the published figures disagreed wildly. Spain and Portugal, for instance, gave quite different lengths for the same frontier.

Richardson found the reason. The length of a wiggly line depends on the length of the ruler. Measure the coast of Britain with a hundred-kilometre ruler and you skip the bays. Use a ten-kilometre ruler and you follow the bays but skip the coves. Use a metre stick and you follow every rock. The shorter the ruler, the longer the coast, without limit.

In 1967 Benoit Mandelbrot turned this nuisance into a discovery. A coastline, he pointed out, is statistically self-similar: each small stretch looks like a reduced copy of the whole. Such a curve is too crinkled to be a one-dimensional line and too thin to be a two-dimensional surface. It can be given a dimension in between, and from Richardson's data he read off a value of about 1.25 for the west coast of Britain (1). He later named such shapes fractals.

The lesson that matters here is the one about rulers. For a fractal, the question "how long is it?" has no answer until you say at what scale you are looking. This book has been asking a similar question about minds: how many agents is this? A brain is 86 billion neurons, or a few hundred areas, or two hemispheres, or one person. Chapter 3 said that agents nest and promised a way to find the natural levels instead of choosing them by hand. This chapter delivers it. The method has two halves. Where a mind looks the same at every scale, it is a fractal, and that tells us it is a single system. Where the sameness breaks, a new kind of agent begins.

## Minds without a scale

Start with the sameness. Several of the minds in this book turn out, when measured, to have no preferred scale.

**Avalanches.** Chapter 3 described the bursts of activity that spread through slices of cortex. They come in all sizes, from a few neurons to the whole slice, and the number of avalanches falls off with size along a straight line on a logarithmic plot, with no typical size anywhere (2). That is self-similarity in time and activity.

**Wiring.** Brain networks are modular, and the modules are themselves made of smaller modules, which are made of smaller ones again: modules within modules, across several levels (3). Chapter 4 mentioned that brains and computer chips obey the same rule relating the size of a region to the number of connections leaving it. That rule, Rent's rule, is the statement that the wiring is self-similar: a small block and a large block have the same relation between inside and outside (4). The exponent of the rule works like a dimension of the network, and for the human brain it is higher than three: the network is more richly connected than any arrangement confined to three-dimensional space could be with local links alone, which is why it needs the long cables of Chapter 7 (4).

**Societies.** Human social groups come in layers of roughly 5, 15, 50 and 150 people and onward, each about three times the last (5). A constant ratio from layer to layer is another form of self-similarity. Zoom out by a factor of three and the pattern repeats.

**Flocks.** The most beautiful case is in the sky over Rome. Each winter evening, thousands of starlings wheel above the city in flocks that turn and pour like a single body. Andrea Cavagna, Irene Giardina and their colleagues photographed these flocks from several angles at once and reconstructed the position and velocity of every bird. Each starling, they had found, pays attention only to its nearest handful of neighbours, about seven (6). Yet when they measured how far the *fluctuations* in the birds' velocities are correlated, the answer was not seven birds, or seventy. The range of correlation grew in proportion to the size of the flock. In a flock twice as wide, the correlated regions were twice as wide (7). There is no characteristic distance beyond which birds stop influencing one another. A change in one bird's flight is felt, through the chain of neighbours, by every other bird, however large the flock.

That is what "of one mind" means, in numbers. Chapter 9 said that a collective acts as one when its internal signals outrun the world. The flock shows the spatial side of the same condition: **a collective is one system when its correlations reach as far as it does.** If the correlation length were fixed at, say, twenty metres, a hundred-metre flock would be five flocks flying in formation. Because it scales with the flock, there is one flock.

## Why a mind should be a fractal

Two arguments from earlier chapters explain why minds should look like this. Both are the theory's reading of established results.

The first is criticality. Chapter 3 argued that minds live at the boundary between order and disorder, and a system at such a boundary has no characteristic scale: that is close to being the definition of a critical point. The flock's scale-free correlations and the cortex's avalanches are the same signature. The starling researchers drew this conclusion themselves: flocks behave as critical systems, poised to respond as strongly as possible to a disturbance such as a falcon (7).

The second is economy. Chapters 4 and 7 showed that a growing mind cannot connect everything to everything. Cross-talk is expensive and scales badly. The cheapest way to keep a large system connected is to build it from modules, connect the modules sparsely into larger modules, and repeat. Repeating a rule at every scale is what makes a fractal.

There is a third argument, older than both, about how such things get built at all. In 1962 the economist and computer scientist Herbert Simon told a parable of two watchmakers, Hora and Tempus. Each made watches of a thousand parts, and each was often interrupted by the telephone. Tempus assembled his watches piece by piece, and whenever he put one down to answer the phone it fell apart, and he had to start again. Hora built his from stable sub-assemblies of ten parts, and those into larger assemblies of ten, so an interruption cost him only a little work. Hora prospered and Tempus went out of business (8). Simon's conclusion was that complex systems that evolve will almost always be hierarchies of stable sub-assemblies, because nothing else survives the interruptions. Evolution is a watchmaker who is always being interrupted.

So the nesting of minds is not a decorative fact. Critical dynamics, wiring costs and the need to be built step by step all push in the same direction: towards systems made of systems made of systems.

## Where the pattern breaks

A perfect fractal would be useless to this theory. If a mind looked the same at every scale all the way down, there would be no levels in it at all, no neurons and no people, just crinkle. Real minds are not like that. The coast of Britain is self-similar from hundreds of kilometres down to metres, but nobody thinks it is self-similar down to the atom. Somewhere the rocks stop being a coastline and become crystals, and the rules change.

That change is the second half of the method. **Where a scaling law bends, a new kind of agent begins.**

The clearest example is in the energy use of living things. For animals, metabolic rate famously grows more slowly than body mass, as roughly its three-quarter power: an elephant burns far less per kilogram than a mouse. It was long assumed that some such law held across all of life. In 2010 John DeLong and his colleagues assembled the data across the full range, and found three laws, not one. In bacteria and other prokaryotes, metabolic rate rises *faster* than mass. In single-celled organisms with nuclei, the protists, it rises in direct proportion. Only in many-celled animals does it rise more slowly (9). The breaks fall exactly at the great transitions in the history of life: where simple cells merged to form complex ones, and where complex cells joined to form bodies.

Those transitions are, in this book's terms, the points where agents of one level became the parts of an agent at the next. The scaling law registers each one as a kink. Someone who knew nothing of biology, given only a plot of energy against mass, could mark where one kind of individual ends and another begins.

Cities give a second example, and a surprise. Luís Bettencourt, Geoffrey West and their colleagues measured how the properties of cities change with population. Roads, cables and petrol stations grow more slowly than population, with an exponent of about 0.8: a bigger city needs less infrastructure per head, as a bigger animal needs less energy per kilogram. But wages, patents and other measures of wealth and invention grow *faster* than population, with an exponent of about 1.2 (10). And where a larger animal lives more slowly, a larger city lives faster: the pace of life quickens with size (10).

Chapter 4 said that size costs time. Cities seem to break the rule. The theory's answer comes from Chapter 8. Size costs time for a mind that must act as a whole, because a signal has to cross it. An animal is integrated, and its heart must supply every cell. A city is federated. Nothing has to cross the whole of it for a meeting to happen on one street corner. What grows with a city's size is the number of different people each inhabitant can reach, and so the rate of local encounters. The hypothesis that follows, and it is a claim to be tested, is that the direction in which a collective's output bends with size tells which kind of mind it is: **integrated collectives slow down as they grow, and federated ones speed up.** The exponent crossing one would then be a mark of the boundary between the two kinds, just as the metabolic exponent marks the boundaries between kinds of organism.

## How to find an agent

Put the two halves together and the result is a procedure that anyone with data can follow.

1. Choose something that can be measured at many scales: the traffic leaving a region against the size of the region; correlation against distance; activity against the size of the group.
2. Plot it against scale, on logarithmic axes.
3. Where the points fall on a straight line, the system is self-similar. Across that range of scales it is one kind of thing, organised by one rule.
4. Where the line bends, the rule changes. That scale is a boundary between levels. Below it are the agents; above it, the collective they form.

Physics has a deeper version of the same idea, called the renormalization group, for which Kenneth Wilson received a Nobel prize (11). Its procedure is to look at a system through progressively coarser lenses. Replace each small block of the system by a single summary value, then do the same to blocks of blocks, and watch how the description changes. Most details wash out. A few quantities survive each step, and those few are all that the larger scale ever needs to know about the smaller one.

Readers of Chapter 8 will recognise this. It is the funnel. A neuron's cloud of molecular detail is summarised as a spike. A bee's million neurons are summarised as a dance of seven bits. A person's billion bits per second are summarised as a vote or a purchase. Nature performs the physicist's coarse-graining for real, at every boundary between levels.

That gives the theory its definition of a level, promised in Chapter 3. **An agent is a scale at which a summary is enough.** It is a block of the world whose effect on everything outside it can be captured by a message far smaller than its internal state. Where no small summary will do, there is no boundary, and what looked like two things is one. Where a small summary suffices, there is an agent, and the scaling laws bend to show it.

## What this predicts

- Every boundary between levels of a mind should appear as a break in some scaling law: in wiring, in correlation, or in the flow of information. The brain should show one between the neuron and the local circuit, and others at the scale of areas and hemispheres.
- Within a level, a healthy collective should have correlations that reach across its whole extent, as the flock's do. A collective whose correlation length is shorter than its size has already come apart into several, whatever its name or its borders say. This gives Chapter 9's question, one mind or two, a measurement.
- The roughly threefold ratio between layers of human groups should be explicable from the costs of communication, and similar constant ratios should appear between the levels of other federated minds.
- Federated collectives should grow faster than their numbers in output, and integrated ones slower.
- Chapter 13's proposal to record humanity like a brain acquires a first step: plot how correlations in activity fall off with distance, in space and in language. If they follow one line from villages to continents, humanity is one system. If the line bends at the scale of the language community, that is where its agents are.

## In short

- A fractal has no preferred scale: each part resembles the whole. For such an object, measurements depend on the scale of the ruler.
- Minds are fractal in many respects. Neuronal avalanches, the nested modules and wiring of brains, the layers of human groups and the correlations in starling flocks all lack a characteristic scale.
- In a starling flock each bird watches about seven neighbours, yet correlations span the whole flock, however large. A collective is one system when its correlations reach as far as it does.
- Criticality, the cost of wiring and the need to be assembled from stable parts all push minds toward nested, self-similar structure.
- Levels show up where self-similarity breaks. Metabolic scaling changes at each major transition in the history of life. Cities, unlike animals, speed up and grow more inventive per head as they grow.
- The theory's claims: a break in a scaling law marks a boundary between levels; an agent is a scale at which a summary is enough; integrated collectives slow with size and federated ones accelerate.

## How we could be wrong

Power laws are easy to see and hard to prove. Many published straight lines on logarithmic plots span too narrow a range to exclude other curves, and some claimed scale-free patterns have not survived better statistics. If the avalanche and wiring laws cited here turn out not to be true power laws, the fractal half of the chapter weakens, though the method of looking for breaks would remain. The claim that breaks mark boundaries between levels would fail if known boundaries, such as that between cell and organism or person and group, showed no change in any scaling relation, or if sharp breaks appeared where no new kind of agent exists. The city result has been disputed on the grounds that the exponents depend on how a city's limits are drawn. If the superlinear growth of cities proves to be an artefact of such choices, the proposed difference between integrated and federated collectives loses its best evidence.

## References

1. B. B. Mandelbrot (1967), "How long is the coast of Britain? Statistical self-similarity and fractional dimension", *Science* 156:636–638. https://ui.adsabs.harvard.edu/abs/1967Sci...156..636M/abstract
2. J. M. Beggs and D. Plenz (2003), "Neuronal avalanches in neocortical circuits", *Journal of Neuroscience* 23:11167–11177. https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045
3. D. Meunier, R. Lambiotte and E. T. Bullmore (2010), "Modular and hierarchically modular organization of brain networks", *Frontiers in Neuroscience* 4:200. https://doi.org/10.3389/fnins.2010.00200
4. D. S. Bassett et al. (2010), "Efficient physical embedding of topologically complex information processing networks in brains and computer circuits", *PLOS Computational Biology* 6:e1000748. https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671
5. W.-X. Zhou, D. Sornette, R. A. Hill and R. I. M. Dunbar (2005), "Discrete hierarchical organization of social group sizes", *Proceedings of the Royal Society B* 272:439–444. https://pmc.ncbi.nlm.nih.gov/articles/PMC1634986/
6. A. Cavagna et al. (2009), "Scale-free correlations in bird flocks", arXiv:0911.4393, citing the group's earlier finding on interaction with about seven neighbours. https://www.arxiv.org/pdf/0911.4393
7. A. Cavagna, A. Cimarelli, I. Giardina, G. Parisi, R. Santagati, F. Stefanini and M. Viale (2010), "Scale-free correlations in starling flocks", *PNAS* 107:11865–11870. https://pmc.ncbi.nlm.nih.gov/articles/PMC2900681
8. H. A. Simon (1962), "The architecture of complexity", *Proceedings of the American Philosophical Society* 106:467–482.
9. J. P. DeLong, J. G. Okie, M. E. Moses, R. M. Sibly and J. H. Brown (2010), "Shifts in metabolic scaling, production, and efficiency across major evolutionary transitions of life", *PNAS* 107:12941–12945. https://pmc.ncbi.nlm.nih.gov/articles/PMC2919978
10. L. M. A. Bettencourt, J. Lobo, D. Helbing, C. Kühnert and G. B. West (2007), "Growth, innovation, scaling, and the pace of life in cities", *PNAS* 104:7301–7306. https://pmc.ncbi.nlm.nih.gov/articles/PMC1852329
11. K. G. Wilson (1975), "The renormalization group: critical phenomena and the Kondo problem", *Reviews of Modern Physics* 47:773–840.

Richardson's work on borders is described from Mandelbrot's account. The readings of scale-free correlation as the mark of a single system, of scaling breaks as boundaries between levels, of the funnel as nature's coarse-graining, the definition of an agent as a scale at which a summary is enough, and the proposed difference in scaling between integrated and federated collectives are the theory's claims.
