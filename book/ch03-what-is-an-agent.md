# Chapter 3. What is an agent?

## The humblest agent on the wall

The thermostat in your hallway is a surprisingly complete example of what this book calls an agent. It has a memory: the target temperature you set. It has an input: a sensor that measures the air. It has a rule that turns what it senses and what it remembers into a decision: if the room is colder than the target, switch on. And it has an output: a signal to the boiler.

Those four parts are the whole definition.

- **Memory**: an internal state that persists, measured in bits.
- **Inputs**: channels through which the world, or other agents, affect that state.
- **A processing rule**: how input and memory combine into a new state and an output.
- **Outputs**: channels through which the agent affects the world, or other agents.

An agent also has a boundary, a line between inside and outside. In the language of statistics, what happens inside is screened off from the outside by the agent's inputs and outputs. To know what a thermostat will do, you need to know its setting and what its sensor reads, and nothing else about the house.

Is the thermostat intelligent? In one narrow sense it is very efficient: it achieves its single goal with almost no information. But it can do nothing else, and it cannot learn. The thermostat shows that being an agent is cheap. Intelligence is what happens when many agents are put together in the right way, and most of this book is about what "the right way" means.

## The neuron

A neuron is a far richer agent. A human brain contains about 86 billion of them. Each one listens to thousands of others through synapses, combines what it hears in its branching dendrites, and decides, many times a second, whether to fire a pulse down its axon.

Its memory lives mostly in its synapses: how strongly each input is allowed to influence it. These strengths are not arbitrary. In 2015, a team at the Salk Institute reconstructed a small cube of rat brain tissue at nanometre resolution. They found pairs of synapses from the same axon onto the same dendrite and compared their sizes, which reflect their strengths. From the precision of the match they estimated at least 26 distinguishable synaptic strengths, about 4.7 bits of information per synapse.

With somewhere between a hundred trillion and a thousand trillion synapses, a human brain may store on the order of 10¹⁵ bits. That is a rough figure, but it gives the agent called a neuron a measurable memory, just as the thermostat has its setting.

## A mind without a brain

If the neuron seems too obviously mind-like, consider the slime mould *Physarum polycephalum*. It is a single cell, a yellow blob that can spread across a surface, with no neurons at all. It moves by extending a network of tubes, thickening the ones that carry the most flow and letting the others wither.

In 2010, Atsushi Tero and colleagues at Hokkaido University placed oat flakes on a wet dish in the positions of the cities around Tokyo, put the mould at the spot marked "Tokyo", and used bright light, which the mould avoids, to stand in for mountains and lakes. The mould first spread out in all directions. Then it pruned itself back to a network of tubes linking the oat flakes. The result had cost, efficiency and fault tolerance comparable to Tokyo's real rail network, which took engineers decades to plan.

The slime mould has no planner and no map. It lays down tubes everywhere, strengthens whatever works and cuts back whatever does not. It is, in a sense, a collective too: a vast network of tube segments, each responding to local flow, whose combined behaviour solves a problem none of them can see.

This points to an important feature of agents: **they nest**. A molecule can be part of a cell, a cell part of a bee, a bee part of a swarm. Whether we call something "an agent" or "a collective of agents" depends on the level at which we look. Chapter 9 offers a way to find the natural levels in data rather than choosing them by hand.

## Not every crowd is a mind

If intelligence came simply from many interacting parts, the most intelligent thing in your kitchen would be the air. A litre of air contains about 10²² molecules, colliding billions of times a second, each collision an exchange of information about position and speed. Yet the air does not think.

It does not think because it lacks three things that agents need.

1. **Persistent memory.** A gas molecule forgets its history almost immediately. Every collision scrambles its state. Nothing is stored.
2. **Selective communication.** A molecule interacts with whatever it bumps into. There is no structure, no preference, no channel that carries one message rather than another.
3. **A flow of energy.** Left alone, a gas settles into equilibrium, the state of maximum disorder, and stays there. A living agent, by contrast, is constantly fed energy that keeps it far from equilibrium, so it can maintain its memory and do work.

Now consider the opposite extreme: a crystal. Its atoms are locked into a perfect lattice. Every atom's position is correlated with every other's. There is memory, in a sense, and plenty of order. But there is no freedom. Nothing can change without everything changing. A crystal has no more of a mind than a gas.

Intelligence seems to live between these extremes: between the chaos of the gas and the rigidity of the crystal. Physicists call the boundary between order and disorder a **critical point**, and systems poised there have a special signature. Activity spreads in cascades of all sizes, with no typical scale.

The brain shows exactly this signature. In 2003, John Beggs and Dietmar Plenz recorded spontaneous activity in slices of rat cortex. Bursts of firing spread across the tissue like avalanches. Their sizes followed a power law with an exponent of −3/2, the value predicted for a system balanced at the critical point, where each active neuron triggers, on average, exactly one other.

## When brains leave the balance

The brain's own failures show what happens when it slides away from that balance, in either direction.

**Too much coupling.** In an epileptic seizure, large populations of neurons fire in lockstep. Communication is maximal; everyone is in agreement with everyone. And thinking stops. A seizure can abolish consciousness entirely, because a brain in which every neuron does the same thing is, informationally, a single neuron repeated billions of times. This is the neural version of the crowd whose guesses all converge on one wrong answer.

**Too little integration.** Under general anaesthesia, and in dreamless deep sleep, the opposite happens. Neurons keep firing, but activity stays local. Regions stop sharing information with each other.

This contrast can now be measured. A team led by Marcello Massimini developed a test in which a brief magnetic pulse is applied to the scalp and the brain's electrical "echo" is recorded. In an awake person, the echo spreads widely and takes a complex, varied shape: integrated *and* differentiated. In deep sleep, under anaesthesia or in coma, the echo is either local or uniform. A single number computed from the echo, the perturbational complexity index, separates these states remarkably well, and has flagged a possible hidden capacity for consciousness in some unresponsive patients.

## What an agent needs, and what a mind needs

Putting the pieces together:

- **An agent** needs persistent memory, selective inputs and outputs, a processing rule, and a supply of energy that keeps it away from equilibrium. Thermostats, neurons, bees and slime-mould tubes all qualify.
- **A mind made of agents** needs those agents to be coupled enough to integrate, so that information from one part can reach and change the others. But they must remain independent enough to differ, so that the whole can represent many distinct states. Too much coupling gives a seizure or an echo chamber; too little gives fragments.

The swarm from Chapter 1 sits in this window: scouts share information through dances, but each inspects sites for herself. The brain sits there too, poised near the critical point. Part II turns this qualitative picture into numbers.

## In short

- An agent is a bounded system with memory, inputs, a processing rule and outputs. Agents can be very simple.
- A neuron's memory is measurable: about 4.7 bits per synapse in one careful study.
- A single-celled slime mould can design a network as good as an engineered railway, which shows that intelligent behaviour does not require neurons and that agents nest inside one another.
- Many interacting parts are not enough. A gas lacks persistent memory, selective communication and an energy flow; a crystal lacks freedom.
- Minds seem to work near a critical point between order and disorder. Seizures (too much coupling) and anaesthesia (too little integration) both abolish consciousness, and the difference can be measured.

## How we could be wrong

The claim that minds need criticality would be weakened if well-functioning brains were found to operate far from the critical point, or if power-law avalanches turned out to arise just as easily in systems with no special balance; some researchers argue the latter. The claim that a gas is not a mind is safe. The harder question is where exactly the line falls, and that requires the measures of Part II.

## Notes

- 86 billion neurons in the human brain: [Azevedo et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19226510/).
- About 4.7 bits per synapse: [Bartol et al. 2015, eLife](https://elifesciences.org/articles/10778v1).
- Slime mould and the Tokyo rail network: [Tero et al. 2010, Science](https://pubmed.ncbi.nlm.nih.gov/20093467/); description of the experiment: [Ed Yong, National Geographic](https://www.nationalgeographic.com/science/article/slime-mould-attacks-simulates-tokyo-rail-network).
- Neuronal avalanches: [Beggs & Plenz 2003](https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045).
- Perturbational complexity index: [Casali et al. 2013](https://orbi.uliege.be/handle/2268/171542); use in unresponsive patients: [Sinitsyn et al. 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7760168/).
