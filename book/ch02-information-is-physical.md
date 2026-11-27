# Chapter 2. Information is physical

## A warm forehead

Put your hand on a laptop that has been working hard, and it is warm. Put your hand on your own forehead after an hour of difficult thinking, and the same is true, in a quieter way. The human brain is about 2% of the body's mass, yet it consumes about 20% of the body's energy budget (1). Roughly 20 watts, the power of a dim light bulb, go into keeping you thinking.

Why should thinking cost anything at all? A thought seems weightless. It has no mass and takes up no room. The answer to that question, which took physics about a century to settle, is the foundation of everything in this book. Information is not abstract. It is a physical quantity, with a price in energy, and that price can be measured.

## The demon in the box

The story begins in the 1860s with James Clerk Maxwell, who imagined a box of gas divided by a wall with a tiny door. A small, intelligent being, later nicknamed Maxwell's demon, watches the molecules. When a fast molecule approaches from the left, it opens the door and lets it through. When a slow one approaches from the right, it lets that one through the other way.

After a while, the right side is hot and the left is cold. The demon has created a temperature difference, which could drive an engine, without doing any work itself. It seems to have broken the second law of thermodynamics, the most robust law in physics, which says that such differences only ever even out on their own. And it has done so using nothing but *information*: knowledge of which molecules are fast.

The puzzle stood for decades. In 1929 Leó Szilárd sharpened it into its simplest form. Take a box with a single molecule. Slide a partition into the middle; the molecule is now on the left or the right. If you know which side, one bit of information, you can let the molecule push the partition like a piston and extract a fixed amount of work from the surrounding heat: kT ln 2, where T is the temperature and k is Boltzmann's constant. In Szilárd's protocol, a hypothetical intelligence turns information into work (2).

So one bit is worth kT ln 2 of energy. At room temperature that is about 3 × 10⁻²¹ joules: unimaginably small, but not zero.

## The price of forgetting

If information can be turned into work, why can't the demon run forever and beat the second law? The answer came from Rolf Landauer in 1961 (3), and was later applied to the demon by Charles Bennett (4). The demon has to remember what it saw. Its memory fills up. To keep working, it must erase old records, and **erasing information has an unavoidable energy cost**.

Landauer's principle states that any logically irreversible operation, such as wiping one bit of memory back to zero, must release at least kT ln 2 of heat. The demon gains at most kT ln 2 per bit it learns and pays at least kT ln 2 per bit it forgets. The books balance, and the second law survives.

For fifty years this remained a theoretical argument. Then experimenters learned to manipulate single microscopic particles precisely enough to test it.

- **2010, Tokyo.** Shoichi Toyabe and colleagues watched a tiny bead jiggling in water under random thermal kicks, inside an electric field shaped like a spiral staircase. Whenever the bead happened to hop up a step, they moved a barrier behind it, using only information about where it was. The bead climbed the staircase, gaining energy, driven by information alone. This was a real Szilárd engine (5).
- **2012, Lyon.** Antoine Bérut and colleagues built a one-bit memory: a single glass bead in a trap with two wells, "left" for 0 and "right" for 1. They erased the bit again and again, measuring the heat released. As the erasure was done more and more slowly, the average heat approached exactly the Landauer limit (6). Forgetting, as one commentator put it, always takes a little energy (7).

These experiments turn a philosophical puzzle into laboratory physics. Information has an exchange rate with energy, and the exchange rate depends only on temperature.

## What this means for minds

If information is physical, so is anything that processes it, including a mind. That is why this book treats bits as a physical quantity, standing alongside metres, seconds and joules.

It also gives us a first yardstick. A human brain runs on about 20 watts and handles very roughly 10¹⁴ to 10¹⁵ synaptic events per second. That works out at about 10⁻¹⁴ joules per event, which is some ten million times above Landauer's floor. This is a rough estimate, and the comparison is not exact, since a synaptic event is not a single erased bit. But it shows the scale. Brains are extraordinarily efficient compared with our machines, and still nowhere near the physical limit. There is room at the bottom, for evolution and for engineers.

## Measurement: where information comes from

The demon has one more lesson. Before it can use information, it has to get it, by measuring. Measurement is the only way any agent, from a bacterium to a scientist, learns about the world.

There is a precise result about what measurement buys. In 2000, Hugo Touchette and Seth Lloyd showed that a controller that observes a system and acts on what it sees can reduce the system's disorder by at most one extra bit for each bit of information it gathers, compared with acting blindly (8). Information is the currency of control, and the exchange rate has a ceiling.

Chapter 5 builds on this. If intelligence is achievement per bit of information used, then this theorem says there is a maximum efficiency for any agent, of any kind, anywhere.

## The great funnel

Our own senses show how much measuring a mind does, and how much it throws away. The human retina sends about 10 million bits per second to the brain, comparable to an old office network connection (9, 10). Add the other senses, and a person gathers information at an estimated rate of about a billion bits per second (11).

Now measure what comes out. Typing, speaking, solving a Rubik's cube blindfolded, playing a video game: in study after study, the rate at which human behaviour carries information is about 10 bits per second. Jieyu Zheng and Markus Meister, who gathered these measurements, point out that the ratio between input and output is about a hundred million (11).

One caution. Ten bits per second is a count of raw bits, not of meaning. Between two people who know each other well, a few bits can select a large, precise thought, because most of the thought is already present in both heads. Chapter 6 shows how to count that.

A mind, then, is a kind of demon that measures a flood and acts on a trickle. Most of what it learns is discarded or compressed into a few decisions. This funnel will turn out to matter enormously in Part III, because when minds are built from minds, the trickle is all that the higher level ever sees.

## In short

- Information has a physical price. Erasing one bit costs at least kT ln 2 of energy, about 3 × 10⁻²¹ joules at room temperature, and this has been confirmed in the laboratory.
- Information can also be turned into work, as a real Szilárd engine has shown.
- Because information is physical, minds can be described with the tools of physics: bits alongside metres, seconds and joules.
- The brain operates about ten million times above the thermodynamic floor, by a rough estimate.
- Each bit gathered by measurement can buy at most one extra bit of control. This sets a ceiling on the efficiency of any intelligence.
- Human minds take in about a billion bits per second and act on about ten.

## How we could be wrong

Landauer's principle itself is about as secure as physics gets. The risk lies in how this book uses it. We assume that the energy and information budgets of a mind can be counted meaningfully, and that synaptic events, dances or spoken words can be translated into bits without losing what matters. If it turned out that the information that matters to a mind cannot be estimated, even roughly, from physical measurements, the framework would lose its footing. Chapter 4 begins the work of showing that it can.

## References

1. M. E. Raichle and D. A. Gusnard (2002), "Appraising the brain's energy budget", *PNAS* 99:10237–10239. https://pmc.ncbi.nlm.nih.gov/articles/PMC124895
2. L. Szilárd (1929), "Über die Entropieverminderung in einem thermodynamischen System bei Eingriffen intelligenter Wesen", *Zeitschrift für Physik* 53:840–856.
3. R. Landauer (1961), "Irreversibility and heat generation in the computing process", *IBM Journal of Research and Development* 5:183–191.
4. C. H. Bennett (1982), "The thermodynamics of computation: a review", *International Journal of Theoretical Physics* 21:905–940.
5. S. Toyabe, T. Sagawa, M. Ueda, E. Muneyuki and M. Sano (2010), "Experimental demonstration of information-to-energy conversion and validation of the generalized Jarzynski equality", *Nature Physics* 6:988–992. https://www.nature.com/articles/nphys1821
6. A. Bérut, A. Arakelyan, A. Petrosyan, S. Ciliberto, R. Dillenschneider and E. Lutz (2012), "Experimental verification of Landauer's principle linking information and thermodynamics", *Nature* 483:187–189. https://pubmed.ncbi.nlm.nih.gov/22398556/
7. *Nature* News (2012), report on the experiment of reference 6. https://www.nature.com/doifinder/10.1038/nature.2012.10186
8. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
9. K. Koch, J. McLean, R. Segev, M. A. Freed, M. J. Berry, V. Balasubramanian and P. Sterling (2006), "How much the eye tells the brain", *Current Biology* 16:1428–1434. https://pmc.ncbi.nlm.nih.gov/articles/PMC1564115
10. University of Pennsylvania (2006), "Penn researchers calculate how much the eye tells the brain", press release giving the human estimate of about 10 million bits per second. https://www.sciencedaily.com/releases/2006/07/060726180933.htm
11. J. Zheng and M. Meister (2025), "The unbearable slowness of being: why do we live at 10 bits/s?", *Neuron* 113:192–204. https://arxiv.org/abs/2408.10234

Figures given without a reference number are our own rough estimates: the brain's power of about 20 watts, its rate of synaptic events, and the comparison of both with Landauer's limit.
