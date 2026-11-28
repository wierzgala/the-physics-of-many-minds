# A Physical Theory of Collective Intelligence: Foundations

**Jakub Wierzgała** · version 0.6 · 27 November 2026

> **Reference document.** This is the compact, technical statement of the theory as it stood before the book was written. It is kept as a frame of mind for thinking about the theory, and it has not been updated since. Where it differs from the book, the book is the current text. The known differences are listed in [README.md](README.md) in this folder.

## Status and purpose

This is version 0.6 of the theory's foundational document. It fixes the premise, terms and assumptions so that each can later be tested, refined or dropped one at a time.

Every claim carries one of four labels:

| Label | Meaning |
| --- | --- |
| **Axiom** | Taken as given for now. Changing it changes the theory. |
| **Hypothesis** | A claim the theory makes and must test against facts. |
| **Estimate** | An order-of-magnitude number, to be checked against primary sources. |
| **Open** | A choice not yet made. |

Numbers are orders of magnitude unless stated otherwise. Brain figures are collected once, in the appendix.

## Core premise

Intelligence is a physical property of collectives. It emerges when many agents each store and process information locally and exchange it over finite channels. Neurons in a brain and bees in a swarm are the two reference cases.

The theory adds two quantities to the usual physical description of a system: **information** (in bits) and **agent count** (N). Neither is a new dimension in the strict sense. Entropy is already information measured in J/K, and Landauer's principle prices erasing one bit at kT ln 2. Counting entities already has a precedent in the mole. The step taken here is to treat both as state variables, alongside energy, length and time, and to look for laws that connect them.

The central claim in one line: **intelligent output = capacity × efficiency**.

- **Capacity** is how much information the collective can move and hold, in bits/s and bits. It is set by N, the channels, the distances and the energy budget.
- **Efficiency** (η) is how much the collective achieves per bit of information it uses. This is what we intuitively call "how smart".
- Physics bounds both factors: Landauer's limit caps bits per joule, and information-theoretic control limits cap achievement per bit.

```
                 intelligent output  =  capacity  ×  efficiency η

what it is       achievement            bits moved and held    achievement per bit used
                 per second             (bit/s, bit)           ("how smart")

set by                                  N, channels,           the bits used: built in,
                                        distances, energy      learned, exchanged

ceiling                                 Landauer:              control limit:
                                        bits per joule         achievement per bit
```

Physical variables set capacity, the bits used set efficiency, and each factor has a physical ceiling. The whole holds only while the collective can integrate faster than its environment changes.

## Primitive concepts

Six terms carry the theory. Everything later is built from them.

- **Agent.** A bounded physical subsystem with four parts: internal state (memory m, in bits), inputs, a processing rule that maps state + input to a new state + output (rate r, in operations/s), and outputs to other agents. Its boundary is statistical: the inside is screened from the outside by its inputs and outputs (a Markov blanket).
- **Information.** Shannon information, in bits. It is physical: storing, moving and erasing it costs energy.
- **Channel.** A link between two agents, with capacity C (bits/s), latency τ (s) and physical length ℓ (m).
- **Collective.** N agents plus the graph of channels between them. Its topology is described by the mean degree k, clustering, modularity and depth of hierarchy.
- **Environment.** Everything outside the collective's boundary. It is described by its entropy rate h\_env (bits/s) and its characteristic timescale τ\_env (s). Intelligence is always measured relative to an environment.
- **Nesting.** An agent may itself be a collective: molecules → cell → bee → hive. The level of description is a choice, fixed separately for each question.

## Inventory of core assumptions

The theory rests on 21 assumptions: 7 axioms, 10 hypotheses to test and 4 open choices. A8 and A11 are the two choices with the largest effect on everything that follows.

| # | Assumption | Group | Status |
| --- | --- | --- | --- |
| A1 | An agent is a bounded subsystem with memory, inputs, a processing rule and outputs. | Agents | Axiom |
| A2 | Locality: each agent updates only from its own state and its inputs. There is no global controller. | Agents | Axiom |
| A3 | Agents communicate over finite channels with capacity, latency and a topology. | Agents | Axiom |
| A4 | Nesting: an agent can itself be a collective. The level is chosen per question. | Agents | Axiom |
| A5 | Information is physical: it is bounded by Landauer's limit, the Bekenstein bound and the speed of light. | Information | Axiom |
| A6 | Every agent and channel can be described in bits: memory m, processing rate r, capacity C. | Information | Axiom |
| A7 | Intelligence belongs to the pattern of interaction, not to any single agent. | Emergence | Hypothesis |
| A8 | Intelligence grows smoothly with N, or it appears at a phase transition in size or connectivity. | Emergence | Open |
| A9 | Substrate independence: only the information-processing organization matters, not the material. | Emergence | Hypothesis |
| A10 | N plus communication is not sufficient. It also takes persistent memory, selective communication and an energy flow that keeps the system far from equilibrium. | Emergence | Hypothesis |
| A11 | Intelligence is measured as efficiency η (achievement per bit used). The unit of achievement is still to be chosen. | Measurement | Open |
| A12 | Intelligent output = capacity × η, and both factors have physical upper bounds. | Measurement | Hypothesis |
| A13 | Intelligent collectives operate between order and chaos, near a critical point. | Dynamics | Hypothesis |
| A14 | Consciousness takes more than intelligence: information that is both integrated and differentiated, and possibly a self-model. | Consciousness | Hypothesis |
| A15 | Scope: the theory explains the functional signatures of consciousness, not necessarily why there is experience at all. | Consciousness | Open |
| A16 | Relative actuality: an event becomes actual for an agent to the degree σ that the agent has extracted useful information from it; for other agents it remains in superposition. | Quantum | Hypothesis |
| A17 | Information shared between agents must be classical (no-broadcasting), so collective intelligence works on decohered information. | Quantum | Axiom |
| A18 | Rival: sufficiently integrated agents trigger objective collapse for everyone. Decided by the AI-friend test. | Quantum | Open |
| A19 | Useful communication is meaning, not raw bits: what a message conveys depends on the context sender and receiver already share (amplification κ ≥ 1), and building that context has a cost. | Information | Hypothesis |
| A20 | The hierarchy continues above humans: humanity is a federated collective whose modules follow shared language and culture; every higher level is slower and less unified, and a unified mind is capped in size at about c·τ. | Emergence | Hypothesis |
| A21 | Similarity: two agents think the same thought, at different speeds, when their dimensionless groups match; each mind's time is measured in its own crossing times. | Dynamics | Hypothesis |

## State variables and dimensional framework

The framework uses three base dimensions: **bit \[B\]**, **second \[T\]** and **meter \[L\]**. Energy \[E\] enters through the power budget and temperature. Counts such as N and k are pure numbers.

| Symbol | Meaning | Units |
| --- | --- | --- |
| N | number of agents | pure number |
| k | mean number of links per agent | pure number |
| m | memory per agent | B |
| r | processing rate per agent | B/T |
| C | capacity per link | B/T |
| ℓ | mean physical length of a link | L |
| d | mean spacing between agents | L |
| v | signal propagation speed | L/T |
| R | size of the collective | L |
| τ\_env | timescale on which the environment changes | T |
| C\_ext | bandwidth across the collective's outer boundary | B/T |
| P | power budget | E/T |
| T | temperature (enters as kT) | E |

### Derived quantities

Hop latency and the crossing time, the fastest the whole collective can agree on anything. D is the graph diameter in hops, and τ\_syn the processing delay at each agent:

```math
\tau_{hop} = \frac{\ell}{v} + \tau_{syn}, \qquad \tau_{cross} \approx \max\left(\frac{R}{v},\; D\,\tau_{hop}\right)
```

Total internal bandwidth (extensive) and bandwidth density (intensive):

```math
B_{int} = \tfrac{1}{2} N k C, \qquad \rho_B = \frac{k C}{2 d^{3}} \;\; [\mathrm{bit\,s^{-1}\,m^{-3}}]
```

Bits in flight on one link, to compare with m: does the collective hold its information in its agents or in its wires?

```math
b_{flight} = C \, \frac{\ell}{v}
```

Energy per bit, to compare with Landauer's floor:

```math
\varepsilon = \frac{P}{B_{int}}
```

### Information flux through a surface

Information flux density J (bits per second per square meter) through a surface is a real and central quantity. Integrated over a cut through the middle of the collective, it gives the **bisection bandwidth** B\_bis: how much can flow between the two halves per second. It is the best single candidate for whether a collective can act as one.

How B\_bis scales with N depends on the wiring:

| Wiring | B\_bis scales as | Consequence |
| --- | --- | --- |
| Only local links (length ≈ d) in 3D | N^(2/3) | The parts talk less and less relative to their size, so the collective fragments as it grows. |
| Full-bisection networks (hypercube-like) | N | Communication keeps pace with size, but wiring volume grows faster than the collective. |
| All-to-all | N² | Physically impossible beyond small N. |

Real brains sit between the first two rows. They follow **Rent's rule**: a block of n agents has about n^p external links, with 0 < p < 1. Their exponents look similar to those of well-designed chips. So brain topology looks like a solution to the trade-off between flux and wiring volume. **\[Hypothesis\]**

### Intensive versus extensive

Densities (ρ\_B, J) are intensive, like temperature or pressure. They describe the **quality of the substrate**, not how much intelligence there is. Totals (N, B\_int, N·m) are extensive. The working hypothesis is that intelligence needs both: enough total capacity, and high enough density to keep latency low. Corvids and parrots, with forebrain neuron densities well above primates' and abilities beyond what their brain mass predicts, are the first piece of evidence. **\[Hypothesis\]**

## Dimensionless groups

Any law of the theory can depend only on dimensionless combinations of the variables. The core set has 8 variables (N, k, m, r, C, ℓ, v, τ\_env) and 3 base dimensions (B, T, L), so Buckingham's Π theorem leaves 5 independent groups. N and k are two of them, and Π₁–Π₃ are the other three. Adding the outer boundary (C\_ext) and energy (P, kT) gives Π₄ and Π₅, and the correlation length gives Π₆. Shared context between agents gives Π₇.

| Group | Definition | Question it answers | Human brain **\[Estimate\]** | Prediction **\[Hypothesis\]** |
| --- | --- | --- | --- | --- |
| Π₁ Coherence number | τ\_env / τ\_cross | Can the collective integrate information before the world changes? | ≈ 10 (catching a ball: \~0.3 s vs. \~30 ms) | Below 1, the collective cannot act as one agent on that task, however large N is. |
| Π₂ Talk-to-compute ratio | r / (k·C) | Does an agent mostly compute or mostly communicate? | ≈ 1: computation happens at the synapse, the point of communication | Brain-like intelligence sits near 1. Far below means agents that only chatter; far above means isolated thinkers. Von Neumann computers are far above. |
| Π₃ Memory horizon | m / (k·C·τ\_env) | How many environment-timescales of its own raw input can an agent store? | ≈ 5 for τ\_env ≈ 1 s | Memory must be compressive: plasticity is slow and stores statistics, not raw input. |
| Π₄ Biot number of the self | C\_ext / B\_bis | Is the collective's outer bandwidth small compared with its internal bandwidth? | ≈ 0.05–0.1 (optic nerve vs. corpus callosum). Between two people, ≈ 10⁻⁷. | Below about 0.1 the collective behaves as one unified self. This threshold is borrowed from heat transfer and is **\[Open\]**. |
| Π₅ Landauer efficiency | kT ln 2 / ε | How close is the collective to the thermodynamic floor for each bit? | ≈ 10⁻⁷ | It allows brains, hives and computers to be compared on one scale. |
| Topology numbers | Rent exponent p, clustering, modularity, hierarchy depth, diameter D | How is the wiring organized? | p similar to that of efficient chips | Large intelligent collectives are sparse, modular and hierarchical. |
| Π₆ Correlation ratio | ξ / R (correlation length / size) | Does correlated activity reach across the whole collective? | Not yet measured at whole-brain scale | Near criticality ξ grows with R, so coherence does not fade with N. Below about 1, the collective splits into parts. See Scale section. |
| Π₇ Context amplification | κ = H(X) / H(X\|S), with S the shared context | How much content does one transmitted bit carry, thanks to what sender and receiver already share? | Not yet measured | High in close couples and stable teams. Effective bandwidth κC, not raw C, sets integration (Π₄) and collective capacity. See Communication section. |

The Biot analogy is exact in form. In heat transfer, a body whose surface exchange is small compared with its internal conduction (Bi < 0.1) behaves as a single lump at one temperature. Here, a collective whose outer exchange is small compared with its internal exchange behaves as a single self.

The lifetime version of Π₃ makes the compression argument sharper. Total memory (\~10¹⁵ bits) divided by lifetime sensory input (\~10⁷ bit/s × 2.5×10⁹ s) is about 0.04. A human brain must compress its input at least \~25-fold. **\[Estimate\]**

## Communication: bits and meaning

Channel capacity in bits is not the amount of meaning two agents can exchange. Meaning depends on what the agents already share: a protocol, a code, a common context. With rich shared context, a few bits can select a large and precise meaning. **\[Hypothesis\]**, raised while reading the book draft.

### The observation

Someone who knows you well can read a whole thought from a glance. A stranger gets almost nothing from the same glance. The channel is identical; the difference is shared knowledge. Until now this theory has counted only raw bits per second, which misses that difference.

### What information theory already says

- Shannon deliberately set meaning aside: for his theory, the semantic aspects of communication are irrelevant to the engineering problem ([report quoting Shannon 1948](https://apps.dtic.mil/sti/pdfs/ADA544137.pdf)). Weaver distinguished three levels: technical (are the symbols transmitted accurately?), semantic (do they convey the intended meaning?) and effectiveness (does the meaning change conduct as intended?) ([Weaver 1949](https://Monoskop.org/images/b/b3/Weaver_Warren_1949_1973_The_Mathematics_of_Communication.pdf)). So far this theory has worked only at the technical level.
- **Side information.** If the receiver already holds information Y correlated with the message X, X can be sent at a rate of only H(X|Y) bits instead of H(X), even when the sender does not know Y ([Slepian & Wolf 1973, as summarised here](https://arxiv.org/pdf/2403.07409)). Shared context is exactly this kind of side information.

### Formalization

- **Shared context S** between two agents: the mutual information between their internal models, in bits. It is a stock, built up by past communication or inherited (a genome, a culture, a language).
- **Context amplification κ**: how much content one transmitted bit carries, measured against an outsider who shares nothing.
- **Effective bandwidth**: raw capacity times κ.
- **Communication cost** in η's denominator includes the bits spent building the shared context, amortised over later messages.

```math
\kappa = \frac{H(X)}{H(X \mid S)} \ge 1, \qquad C_{eff} = \kappa\, C, \qquad I_{comm} = \sum_i b_i \; + \; I_{build}
```

This does not break Shannon's limits. A bit never carries more than one bit of *new* information for its receiver. The extra content was transmitted earlier, when the shared context was built: **meaning = bits sent now + bits shared before**.

### Evidence

- **The waggle dance.** About 7 bits per dance are useful only because every bee shares the same genetically inherited protocol, built over evolutionary time.
- **Couples.** Close couples develop a transactive memory, a shared system for encoding, storing and retrieving information, that is greater than either partner's memory alone ([Wegner, Erber & Raymond 1991](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/dwegner/files/wegnererberraymond1991.pdf)).
- **Teams.** In a study of 1,015 software project teams, members' prior shared work predicted team performance, while individual members' years at the firm did not consistently do so ([Huckman, Staats & Upton 2009](https://econpapers.repec.org/RePEc:inm:ormnsc:v:55:y:2009:i:1:p:85-100)).
- **Collective intelligence.** A group's general ability across tasks correlates only weakly with its members' average or maximum individual intelligence. It correlates with social sensitivity, measured by how well members read others' thoughts and feelings from their eyes, and with equal turn-taking ([Woolley et al. 2010](https://pubmed.ncbi.nlm.nih.gov/20929725/)). Reading eyes is decoding meaning from a very low-bandwidth channel.

### Consequences for the theory

1. **Integration uses effective bandwidth.** Π₄ (the Biot number of the self) and the bisection bandwidth should be computed with κC, not raw C. Two people with deep shared context are more integrated than their \~39 bit/s of speech suggests.
2. **Abstractions are pointers.** The compressed messages that pass up the hierarchy (H2) work only because sender and receiver share the code that unpacks them. A level's vocabulary is part of its shared context.
3. **Shared code versus shared beliefs.** Shared protocol helps communication; shared beliefs destroy the independence that collective intelligence needs (H4). The best collectives should maximise the first while keeping the second diverse.
4. **Efficiency grows with familiarity.** Because the cost of building shared context is amortised, η of a stable pair or team should rise over time, as the team-familiarity evidence suggests.
5. **A new dimensionless group, Π₇ = κ**, added to the table above.

## Measuring intelligence

Intelligence is measured as an **efficiency**: achievement per bit of information used. A genius is someone who needs little information to get far. The leading candidate unit is bits of uncertainty removed per bit used, a dimensionless number with a proven ceiling of 1. **\[Open\]**

### The efficiency η

```math
\eta = \frac{G}{I_{prior} + I_{exp} + I_{comm}}, \qquad \eta_{marginal} = \frac{dG}{dI}
```

G is achievement. The denominator counts every bit the collective used:

- **I\_prior**: bits built in before learning (genome, hard-wired structure, hand-coded rules).
- **I\_exp**: bits taken in from the environment.
- **I\_comm**: bits the agents exchanged to reach the result. This term is new to a multi-agent theory. Its minimum for a given task is what computer science calls communication complexity.

The marginal form, the slope of the learning curve, avoids dividing by zero and rewards learning rather than stored answers.

### Candidate units of achievement

The choice of G fixes the units of η:

| Option | Achievement G measured as | Units of η | Physical ceiling | Example |
| --- | --- | --- | --- | --- |
| A | A count of tasks solved, weighted by difficulty | bit⁻¹ | None known | Chollet-style skill-acquisition efficiency |
| **B** | Bits of uncertainty removed, or control exerted, beyond what is possible without feedback | dimensionless | η ≤ 1 (Touchette–Lloyd) | Twenty questions: a perfect player resolves 1 bit per yes/no answer |
| C | Work extracted from the environment | J/bit | kT ln 2 per bit (Szilard) | Maxwell's demon |

Option B is preferred. It makes intelligence a pure number with a theorem behind its upper limit, much as Carnot efficiency is for heat engines. Bits are logarithmic, so "per bit" means "per halving of uncertainty", not "per item".

### Capacity and intelligent output

Efficiency says how well a collective uses information, not how much it can handle. The two combine into intelligent output:

```math
\dot{G} = \underbrace{\dot{I}}_{\text{capacity [bit/s]}} \times \underbrace{\eta}_{\text{efficiency}}, \qquad \frac{G}{E} = \frac{\dot{I}}{P} \times \eta
```

It works like an engine, where power = fuel flow × efficiency. The dimensional framework above describes the fuel flow, and η describes the efficiency. A whale's brain may have more flow, and a crow's better η.

### First estimate: human versus language model

This rough comparison shows that η can be computed. **\[Estimate\]**

- **A child** hears on the order of 10⁸ words before adolescence. Adding the genome as priors (\~6×10⁹ bits) gives about 10¹⁰ bits in total.
- **A large language model** trains on about 10¹³ tokens, roughly 10¹⁴ bits.
- At comparable language skill, the human is about **10⁴ times more information-efficient**.
- Caveat: the genome is a compressed summary of far more evolutionary "experience" than its own size.

### Pitfalls the definition must handle

1. **Doing nothing.** Zero bits used would mean infinite η. Fix: use the marginal form, or require a minimum level of achievement.
2. **Hidden priors.** A lookup table with hard-coded answers looks brilliant. Fix: always count I\_prior.
3. **Narrowness.** A thermostat is efficient at one trivial task. Fix: weight G by how varied and novel the tasks are.
4. **Intensity.** η alone does not rank how much a system can do. Fix: always report capacity alongside η.

## Physical bounds

The goal is a "Carnot limit for cognition": an absolute ceiling on intelligent output for given size, wiring and energy. Five known limits feed into it.

| Limit | Statement | What it bounds | Binding for brains? |
| --- | --- | --- | --- |
| Landauer (1961) | Erasing 1 bit costs ≥ kT ln 2 (≈ 3×10⁻²¹ J at 310 K) | Irreversible bit operations per joule | No: the brain runs \~10⁷ above it |
| Touchette–Lloyd (2000) | Extra entropy a feedback controller removes ≤ the information it acquires | Achievement per bit (option B): η ≤ 1 | Unknown, to be measured |
| Signal speed | τ\_cross ≥ R / v, and v ≤ c | Size of a coherent self for a given τ\_env | Yes, at the \~10–100 ms scale |
| Wiring volume | N·k·ℓ·(cross-section of a link) must fit in the volume | Bisection bandwidth and topology | Yes: white matter takes up a large share of the brain |
| Bekenstein | Information in a region ≤ 2πRE / (ħc ln 2) | Total memory | No: \~10⁴² bits for a brain |

### Integration radius

A collective can act as one self only on timescales longer than its crossing time. So for a task with timescale τ\_env, the largest coherent self is R\_max ≈ v · τ\_env.

| System | Signal speed | Size | Minimum crossing time |
| --- | --- | --- | --- |
| Human brain | \~1–100 m/s | \~0.15 m | \~10–50 ms, including synaptic delays |
| Planet-sized mind | c | 1.3×10⁷ m (Earth's diameter) | \~0.04 s |
| Galaxy-sized mind | c | \~10⁵ light-years | \~10⁵ years per "thought" |

The brain's crossing time is close to the \~100–300 ms windows of conscious perception. **\[Hypothesis\]**

### Roofline form of the bound

Borrowing the roofline model from computer architecture, intelligent output is capped by whichever bottleneck binds first: **\[Hypothesis\]**

```math
\dot{G} \;\le\; \eta \cdot \min\!\left( N r,\;\; \tfrac{1}{2} N k C,\;\; \frac{P}{kT \ln 2} \right), \qquad \eta \le 1, \quad \Pi_1 \ge 1
```

When Π₁ < 1 the collective splits into parts that each satisfy the bound on their own. For any system you can then ask which term binds. A first guess: bee swarms are bandwidth-bound (a waggle dance carries only a few bits), and brains are bound by energy and wiring.

## Consequences and predictions

The framework already makes eight predictions, each tied to a known fact that a test can confirm or break. All are **\[Hypothesis\]** until tested.

| # | Prediction | Follows from | Evidence so far | How to test |
| --- | --- | --- | --- | --- |
| P1 | A coherent self cannot be larger than about v·τ\_env. | Π₁, signal speed | The brain's crossing time (\~10–50 ms) is just below conscious perception windows (\~100–300 ms). | Compare crossing times with decision times across species and collectives. |
| P2 | A self's boundary lies where outer bandwidth falls well below internal bandwidth. | Π₄ | Split-brain patients show two partly separate streams. Craniopagus twins with a thalamic bridge share some perceptions. Speech between people runs at only \~39 bit/s ([Coupé et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970)). | Compute Π₄ for systems with known or disputed unity. |
| P3 | Large intelligent collectives must be sparse, modular and hierarchical. | Wiring volume, B\_bis scaling | Human brains and the *C. elegans* nervous system obey Rent's rule and show hierarchical modularity, like efficient chips ([Bassett et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671)). | Measure Rent exponents in ant colonies, organizations and AI clusters. |
| P4 | Intelligence scales as a power law in N, with exponents set by the Π groups. | Dimensional form | Cortical neuron count predicts cognition better than brain mass. City output scales as \~N^1.15. ML loss falls as a power law in parameters. Hopfield networks store \~0.14·N patterns. | Fit exponents across systems and derive them from the Π groups. |
| P5 | Intelligence and consciousness are lost at both extremes of coupling. | A10, A13 | Seizures (hypersynchrony) and anesthesia or deep sleep (fragmentation) both abolish consciousness. The perturbational complexity index tracks this ([Casali et al. 2013](https://orbi.uliege.be/handle/2268/171542)). | Map coupling strength against PCI. |
| P6 | Density matters independently of size. | Intensive vs. extensive | Parrot and songbird brains hold about twice as many neurons as primate brains of the same mass, and corvids and parrots reach ape-like cognition ([Olkowicz et al. 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4932926)). | Regress η on N and neuron density separately. |
| P7 | Long-term memory must compress its input at least \~25-fold. | Π₃ (lifetime form) | Consolidation, forgetting, and plasticity far slower than signaling. | Compare stored bits with input bits in learning systems. |
| P8 | Intelligence is nested: each level of a collective has its own integration radius. | A4, Π₁ | Cells and tissues show goal-directed problem-solving (Levin). | Measure Π₁ and η at the cell, organism and group levels. |

## Hierarchy of intelligence

Intelligence nests: neurons form a bee, and bees form a swarm. Each step up trades bandwidth, speed and unity for reach, robustness and longevity. The algorithms repeat across levels, but the self does not. **\[Hypothesis\]**

### Two levels, measured

- **Level 1, neurons → bee.** A honeybee brain has about 960,000 neurons in roughly 1 mm³ ([BioNumbers, after Menzel & Giurfa 2001](https://bionumbers.hms.harvard.edu/bionumber.aspx?id=109328)).
- **Level 2, bees → swarm.** A swarm of up to 10,000 bees chooses its new nest site collectively ([Cornell, Seeley et al.](https://news.cornell.edu/node/276432)).
- **Messages between bees are tiny.** A waggle dance carries about 2.9 bits of direction and 4.5 bits of distance ([Schürch & Ratnieks 2015](https://www.frontiersin.org/articles/10.3389/fevo.2015.00022)), so roughly 7 bits per location.
- **The swarm is a thinner mind than any of its members.** A bee brain's internal traffic is perhaps 10⁸–10⁹ bit/s, while the swarm deliberates at tens of bits per second. **\[Estimate\]** Yet the swarm solves a problem no single bee can: it trades capacity for reach.

```
neurons  ──▶  bee  ──▶  swarm

about 960,000 neurons          up to 10,000 bees
in about 1 mm³                 spread over kilometres
10⁸–10⁹ bit/s inside           tens of bit/s between bees
```

Each arrow is a funnel: what passes up is a compressed summary of the level below.

### The cross-level relation

Every agent is an information funnel: it takes in a lot and emits little. Humans are the best-measured case: senses gather about 10⁹ bit/s, while behaviour runs at about 10 bit/s ([Zheng & Meister 2024](https://arxiv.org/abs/2408.10234)).

At the level above, an agent's whole internal capacity plays the role of its processing rate r, and its output plays the role of the channel capacity C. So the talk-to-compute ratio of a collective equals the compression ratio of its members: **\[Hypothesis\]**

```math
\Pi_2^{(n+1)} = \frac{r^{(n+1)}}{k\,C^{(n+1)}} \approx \frac{\text{internal capacity of a level-}n\text{ agent}}{\text{output bandwidth of that agent}}
```

The timescales are linked too. A message at level n+1 passes through an agent's whole perceive–decide–act cycle, so the higher level is slower by at least the number of hops D and the number of rounds needed:

```math
\tau^{(n+1)} \;\ge\; D^{(n+1)} \cdot \tau^{(n)} \cdot (\text{rounds})
```

### Two types of intelligence

The cross-level relation splits collectives into two types. A brain has thin agents and thick wires (Π₂ ≈ 1). A swarm or a society has thick agents and thin wires (Π₂ ≈ 10⁶–10⁸).

| Quality | Integrated type (Π₂ ≈ 1) | Federated type (Π₂ ≫ 1) |
| --- | --- | --- |
| Examples | brains | bee swarms, ant colonies, human societies |
| Speed | milliseconds to seconds | hours to days |
| Collective state | high-dimensional (a whole scene) | low-dimensional (which option wins) |
| Strength | fast, flexible, rich perception | parallel search over a large area, pooling independent evidence |
| Robustness to losing agents | high | very high |
| Unified self (Π₄ < \~0.1) | yes | no |
| Where memory lives | inside, in synapses | outside: structures, chemical marks, genome, writing |

### Predictions H1–H8

All are **\[Hypothesis\]** until tested.

| # | Prediction | Evidence so far | How to test |
| --- | --- | --- | --- |
| H1 | Each level is slower than the one below by orders of magnitude, and handles only features of the world that change slower than it does. | Neurons work in milliseconds; swarm scouts can debate for about two days ([Fordham, Seeley](https://now.fordham.edu/?p=15796)). | Compare decision times level by level with the τ relation above. |
| H2 | Higher levels work with abstractions: messages carry compressed summaries, not raw data. | A whole flight is compressed into a \~7-bit dance. | Measure bits per message against the sender's input rate. |
| H3 | The same decision algorithms reappear at every level (universality). | Swarms and brains both accumulate noisy evidence in competing populations, choose at a threshold and use cross-inhibition ([Seeley et al. 2012](https://news.cornell.edu/node/271186); [Marshall et al. 2009](https://ora.ox.ac.uk/objects/uuid:e1bddf33-2467-4a42-846c-0ba4a556b138)). | Look for thresholds, cross-inhibition and criticality in immune systems, ant colonies, markets and science. |
| H4 | Every level fails the same way: too much coupling destroys intelligence. Working collectives protect agents' independence. | Seizures in brains; mild social influence undermines the wisdom of crowds ([Lorenz et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299)). Recruited bee scouts inspect a site themselves before dancing for it. | Vary coupling in a collective task and measure η. |
| H5 | A bit costs more at each level up, so higher levels favour bit-efficient algorithms such as a quorum instead of full consensus. | A buildup of 10–15 or more bees at one site triggers the swarm's take-off signal ([Seeley & Visscher 2004](https://www.doi.org/10.1007/S00265-003-0664-6)). | Compare energy per bit and bits per decision across levels. |
| H6 | Agents get simpler as the level above gets stronger. | Social wasps invest less in mushroom bodies than solitary wasps ([O'Donnell et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4590486)). Neurons are cells that gave up independent life. | Regress agent brain investment on colony-level capability across species. |
| H7 | Memory moves outward as you go up, whenever agents live shorter than the collective must remember. | Worker bees live weeks while colonies last years, so colony memory sits in comb, chemical marks and the genome. Neurons last as long as the brain and keep memory inside. | Compare agent lifespan with where memory is stored, across collectives. |
| H8 | A unified self exists at only one level. A swarm is intelligent but not a self, because its sensory inflow far exceeds its internal dance traffic (Π₄ ≫ 1). | Without cross-inhibition a swarm risks deadlock: stop signals help break ties between equally good sites ([Seeley et al. 2012](https://news.cornell.edu/node/271186)). | Look for split or deadlocked decisions as cross-inhibition is reduced. |

## Scale: fractal structure and its breaks

Within a level, a collective is fractal; between levels, the scaling breaks. The breaks are where agents begin and end, and they may be the most useful thing fractal analysis gives the theory. **\[Hypothesis\]**

### Fractal dimension of the wiring

One number replaces the three wiring cases in the dimensional framework: the **topological dimension D\_T** of the communication network. A network that behaves like a D\_T-dimensional lattice obeys Rent's rule with exponent p = 1 − 1/D\_T, so:

```math
B_{bis} \propto N^{\,p} = N^{\,1 - 1/D_T}
```

Local wiring in 3D is the case D\_T = 3 (p = 2/3). Full-bisection networks are the limit D\_T → ∞ (p → 1).

Brains have measured values:

- In human brains, *C. elegans* and computer chips, the topological dimension of the wiring exceeds the 2 or 3 dimensions of the space it is embedded in ([Bassett et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671)). The same fractal properties explain how grey and white matter volumes scale across mammals.
- Large human connectomes give D < 4, so long-range links add only a small correction to 3D ([Gastner & Ódor 2016](https://link.springer.com/content/pdf/10.1038/srep27249.pdf)). So D\_T ≈ 3–4 and p ≈ 0.67–0.75. **\[Estimate\]**
- Functional brain modules are self-similar (fractal), and weak long-range ties join them into a small world ([Gallos et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3286928)).

**Why levels exist.** Each agent's share of the bisection bandwidth falls as N grows, and the crossing time rises with physical size:

```math
\frac{B_{bis}}{N} \propto N^{-1/D_T}, \qquad \tau_{cross} \propto \frac{N^{1/3}}{v}
```

Both degrade integration, so an integrated level has a maximum size. Past it, it is cheaper to bundle agents into units that talk through a thin channel, and a new level forms. **\[Hypothesis\]**

### Deriving exponents from fractal networks

Fractal networks are the most successful route in biology from structure to scaling exponents. They are a template for deriving, not just fitting, prediction P4.

- **Metabolism.** West, Brown and Enquist derived the 3/4 power law for metabolic rate from space-filling fractal networks of branching tubes ([West et al. 1997](https://experts.arizona.edu/en/publications/a-general-model-for-the-origin-of-allometric-scaling-laws-in-biol/)). Critics showed the model gives exactly 3/4 only for infinitely large organisms ([Savage et al. 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC2518954)), so finite-size corrections matter.
- **Cities.** Socioeconomic output grows as N^(1+δ), where δ depends on the fractal dimension of people's paths through the city, typically δ = 1/6 ([Barthelemy 2019, reviewing Bettencourt 2013](https://arxiv.org/pdf/1905.01953)). That is the \~1.15 exponent cited in P4.

The programme for this theory is an **information metabolism**: derive how capacity and intelligent output scale with N from D\_T and from the fractal dimension of agents' interaction paths.

### Scale-free dynamics and the correlation ratio

Fractal structure in activity, not only in wiring, is the signature of a system near a critical point (A13).

- **Neurons.** Activity spreads in avalanches whose sizes follow a power law with exponent −3/2, with a branching parameter close to 1 ([Beggs & Plenz 2003](https://pmc.ncbi.nlm.nih.gov/articles/PMC6741045)).
- **Starling flocks.** Each bird interacts with about seven neighbours ([Cavagna et al., arXiv](https://arxiv.org/abs/0911.4393)), yet the range of behavioural correlation grows in proportion to the flock's size, so every bird effectively senses the whole flock ([Cavagna et al. 2010](https://pmc.ncbi.nlm.nih.gov/articles/PMC2900681)).

This gives a sixth dimensionless group, the **correlation ratio Π₆ = ξ / R**, where ξ is the correlation length and R the size of the collective. A collective acts as one only if Π₆ ≳ 1, which refines the coherence number Π₁. Near criticality ξ ∝ R, so coherence does not fade as N grows. **\[Hypothesis\]**

Prediction for bees: swarm recruitment should show avalanche-like cascades with power-law sizes, and correlations in scout activity that grow with swarm size. Both can be tested on tracked swarm video.

### Scaling breaks locate agents

Within a level, quantities follow clean power laws: Rent's rule, avalanche sizes, correlations. At a level boundary the power law breaks. Inside a skull, the information crossing a region's boundary grows as n^p with region size. At the skull itself, it collapses to about 10 bit/s of behaviour.

This gives an operational answer to the open question of what counts as an agent:

1. Take nested regions, or groups of nodes, of growing size.
2. Plot the information flux across each region's boundary against its size, on log–log axes.
3. Straight segments lie within a level. Kinks and sudden drops are agent boundaries, and the size of the drop is Π₄.

An agent is whatever lies between two scaling breaks, and the number of straight segments is the number of levels.

### Self-similar rules, not self-similar numbers

The hierarchy is not a pure fractal. Its algorithms repeat across levels, but its parameters jump: Π₂ goes from about 1 to about 10⁸, and timescales stretch by orders of magnitude per level.

The physics of "same rules, different numbers" is the **renormalization group** (RG); fractals are its geometric shadow. In RG terms:

- each level is one coarse-graining step;
- the algorithms that survive across levels are the "relevant" features, which is why they recur (H3);
- a critical point is where the system becomes scale-free (Π₆).

RG is the framework to aim for. Fractal dimensions and scaling breaks are the measurable quantities that feed it.

## Extrapolating the hierarchy: humanity and beyond

If neurons make a human and humans are agents, the hierarchy should continue upward. The framework predicts what the higher levels can and cannot be. Humanity is a federated collective intelligence whose modules are set by shared language and culture. Any larger mind, up to galactic scale, must be slower, more abstract and less unified at each step. **\[Hypothesis\]**, raised while reading the book draft.

### Humanity as a collective intelligence

| Quantity | Value | Basis |
| --- | --- | --- |
| Agents | about 8.2 billion people (2024) | [UN World Population Prospects 2024](https://www.un.org/development/desa/pd/world-population-prospects-2024) |
| Output per agent | \~10 bit/s of behaviour; \~39 bit/s of speech | [Zheng & Meister 2024](https://arxiv.org/abs/2408.10234); [Coupé et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970) |
| Funnel ratio, which is Π₂ of humanity | \~10⁸ | Derived: \~10⁹ bit/s in, \~10 bit/s out |
| Shared protocols (languages) | 7,164 in use; 23 of them cover more than half the world's population | [Ethnologue](https://ethnologue.com/insights/how-many-languages) |
| Time for a global decision | years to decades | **\[Estimate\]** |

Humanity is therefore of the federated type: slow, broad, robust, and without a unified self, since each person's sensory inflow dwarfs what passes between people (Π₄ ≫ 1). Science is the clearest working example of humanity-level intelligence: a shared protocol (mathematics, a common language, peer review), an external memory (the literature) and decisions by accumulated consensus rather than unanimity.

### Modules: languages and cultural circles

Shared context (Π₇) is highest within a language and a culture, so these should form the modules of the collective, as cortical areas do in a brain.

- **Language splits communication networks.** In a Belgian mobile phone network of about 2 million customers, the communities found by a standard algorithm separate by main language, French or Dutch, with a small mixed community in between ([Blondel et al. 2008](https://arxiv.org/pdf/0803.0476)).
- **Languages form a hub structure.** Networks of multilingual speakers and translations are centred on English as a global hub, with intermediate hubs including Spanish, German, French, Russian, Portuguese and Chinese ([Ronen et al. 2014](https://pmc.ncbi.nlm.nih.gov/articles/PMC4284551)).
- **Society has discrete levels.** Human groups form a discrete hierarchy of preferred sizes with a scaling ratio close to three: about 3–5, 9–15, 30–45 and so on ([Zhou et al. 2005](https://pmc.ncbi.nlm.nih.gov/articles/PMC1634986/)). These are scaling breaks inside society itself.

### Nations: agents or modules?

By the theory's criteria, nations are modules, not selves:

1. **Shared context:** high inside a national language and media space, which favours nations as modules.
2. **Decision protocols:** elections and institutions act like the swarm's quorum, a way for the module to reach decisions.
3. **Unity:** nations exchange heavily across borders through trade, migration, the internet and science, so Π₄ is not small. They are not sealed selves.

The strongest module boundaries should follow language rather than borders. Belgium already shows a communication split inside one country along its language line.

### Two forces the framework predicts

- **Integration through translation.** Machine translation and AI mediation raise κ between language modules. This should make humanity more integrated as a collective.
- **A civilisational seizure.** The same coupling can make beliefs uniform. Loss of independence is the failure mode at every level (H4): too much coupling in a brain is a seizure, in a crowd it is an echo. A healthy collective needs shared code with diverse beliefs.

### Beyond Earth: the light-speed ceiling

A mind can act as one only on timescales longer than the time a signal needs to cross it. With signals at the speed of light, the largest unified mind for a given thought time τ is about c·τ:

| Thought time τ | Largest unified mind | Comparison |
| --- | --- | --- |
| 1 ms (fast machine) | \~300 km | a region of data centres |
| 0.3 s (human perception) | \~90,000 km | \~7 Earth diameters |
| 1 day | \~2.6 × 10¹³ m (\~170 AU) | beyond the planets of the Solar System |
| 1 year | 1 light-year | less than the distance to the nearest star (\~4.2 light-years) |
| 100,000 years | \~100,000 light-years | the Milky Way: one galactic "thought" |

- **Earth and Mars are already a federation.** A signal between them takes about 3 to 22 minutes one way, depending on the planets' positions ([NASA figures, summarised](https://spacedaily.com/t-earth-mars-radio-delay-44-minutes-solar-conjunction/)). A two-planet civilisation must let each planet act on its own for anything faster than about an hour.
- **A galactic mind could only be federated.** Its thoughts would take at least 100,000 years. Its nodes, star systems, would be almost fully autonomous (Π₂ astronomically large). Its messages would be extreme abstractions, pointers into an enormous shared context built once and reused (Π₇). Facts would become actual across it no faster than light.
- **Cold computing is cheaper.** Landauer's cost per bit is proportional to temperature, so computation in deep space near 2.7 K costs about a hundred times less per bit than at room temperature. The aestivation hypothesis goes further and suggests advanced civilisations might wait for the universe to cool, gaining up to a factor of 10³⁰ ([Sandberg, Armstrong & Ćirković 2017](https://arxiv.org/abs/1705.03394)). Its thermodynamic argument is disputed ([Bennett, Hanson & Riedel 2019](https://www.arxiv.org/abs/1902.06730)).

**Can humanity form a galactic superintelligence?** Physics allows a galactic intelligence of the federated type: vast in reach, memory and robustness, but slower than anything we know and without a unified self. A fast, unified superintelligence is capped in size at about c·τ. For thoughts at human speed, that means no larger than a few Earth diameters.

### Predictions X1–X6

All are **\[Hypothesis\]**.

| # | Prediction | Evidence so far | How to test |
| --- | --- | --- | --- |
| X1 | Humanity is a federated collective intelligence, with Π₂ around 10⁸. | The human funnel: \~10⁹ bit/s in, \~10 bit/s out. | Compare humanity's problem-solving timescales with Π₁. |
| X2 | Humanity's modules follow shared context (language, culture) more than borders. | Belgian phone network; global language network. | Look for scaling breaks in communication flux in multilingual countries. |
| X3 | Nations are modules, not selves. | Heavy cross-border exchange. | Compute Π₄ for nations using effective bandwidth κC. |
| X4 | Lowering translation cost integrates humanity but threatens independence of beliefs. | Social influence reduces crowd accuracy ([Lorenz et al. 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299)). | Track belief diversity against connectivity over time. |
| X5 | No unified mind can be larger than about c·τ. | Follows from relativity and Π₁. | Latency limits on distributed computing; any future multi-planet coordination. |
| X6 | Each level up is slower by orders of magnitude: milliseconds (neurons), seconds (people), years (humanity), 100,000+ years (a galaxy). | Extends H1. | Measure decision times level by level. |

## Similarity: the same thought at different scales

Two agents of very different size can think the same thought at different speeds, when the dimensionless groups that govern them match. Time and distance trade through signal speed, so a mind's natural clock is its own crossing time. **\[Hypothesis\]**, raised while reading the book draft.

### The principle

In fluid mechanics, a scale model in a wind tunnel behaves like the full-size aircraft when its Reynolds number matches: the two flows are *dynamically similar*. The proposal is that minds obey the same rule. Two collectives think the same thought when their Π groups match, even if their sizes and speeds differ by orders of magnitude.

Measure time in each mind's own crossing times, its **cognitive time** θ:

```math
\theta = \frac{t}{\tau_{cross}}, \qquad \tau_{cross} \approx \frac{R}{v}
```

Minds A and B think the same thought if, plotted against θ, their information states follow the same trajectory, which requires matching Π groups. Their clock times then differ only by the ratio of their crossing times:

```math
\frac{t_B}{t_A} = \frac{\tau_{cross}^{B}}{\tau_{cross}^{A}} = \frac{R_B \, v_A}{R_A \, v_B}
```

### A first check: deciding in tens of steps

- **A monkey's brain** makes a perceptual choice in roughly half a second. With each neural hop taking about 5–10 ms, that is about 50–100 hops. **\[Estimate\]**
- **A bee swarm** in one documented case needed about 16 hours of dancing. A scout's cycle (fly to the site, inspect it, return, dance) takes on the order of tens of minutes, so the decision took roughly 20–50 cycles. **\[Estimate\]**
- Both systems decide in tens of their own steps, although their clock times differ by about a hundred thousand times. That is what the principle predicts if they run the same algorithm (H3) at different speeds.

### Why the match is usually partial

1. **The environment does not rescale.** A thought is only useful if Π₁ = τ\_env / τ\_cross is also similar. A slow mind can think fast thoughts only about a slow world.
2. **Not every group can be matched at once.** Ship-model tests cannot match the Froude and Reynolds numbers at the same time, so engineers accept partial similarity. Minds face the same problem: the speed of light, temperature and Landauer's cost are fixed, so a larger mind cannot keep Π₂, Π₄ and Π₅ all equal. Most cross-scale thoughts will be similar rather than identical.
3. **Capacity must suffice.** The same thought needs the same information. A collective with less memory or narrower channels can think only a compressed version of it.

### Consequences

- **The Π groups classify thoughts, not just minds.** Minds with equal groups form one similarity class; within a class, thoughts are scaled copies.
- **Universality is similarity seen from outside.** The same decision algorithm in swarms and brains (H3) is what similarity looks like in data.
- **Subjective time may be measured in θ.** A galactic mind's 100,000-year thought could be a single moment for it. **\[Speculation\]**

### Predictions S1–S3

| # | Prediction | How to test |
| --- | --- | --- |
| S1 | Decisions of the same type take a similar number of crossing times in every system, whatever the absolute speed. | Measure decision time divided by τ\_cross for brains, swarms, ant colonies and committees. |
| S2 | When two systems share their Π groups, their speed–accuracy curves fall onto one curve when time is plotted as θ. | A data-collapse test, as used for critical phenomena in physics. |
| S3 | Where groups cannot all be matched, the scaled version of a thought differs in a predictable direction set by the mismatched group. | Compare swarms and brains on tasks sensitive to Π₂ or Π₄. |

## Quantum foundations: relative actuality

Collapse is relative. An event becomes actual for an agent when that agent extracts useful information from it, and it stays in superposition for agents who have not. Actuality is graded, measured in bits, and spreads up the levels of the hierarchy at finite speed. **\[Hypothesis\]**

### The claim

Take Schrödinger's cat: an atom that may decay, a trap that kills the cat if it does, and an outside observer.

- Once information about the decay reaches the cat's integrated state, the outcome is actual for the cat.
- For the outside observer, who has received nothing, the atom, the trap and the cat together remain in superposition.
- Only extracted information counts. Light reaching an eye is not an observation unless the agent pulls useful information out of the signal.

This replaces the stronger idea that intelligence physically collapses the wave function for everyone. That idea is kept only as a rival hypothesis for the test below.

### Where it sits

- **Relational quantum mechanics** (Rovelli 1996) holds that different observers can give different accounts of the same events, and that the actualisation of an event is relative to a system. In the Wigner's-friend case, the interference Wigner observes is compatible with the friend's definite observation ([Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/Entries/qm-relational/)).
- **QBism** holds that a measurement is an agent's action on its world, and that its outcome is personal to that agent ([Fuchs 2023](https://arxiv.org/pdf/2303.01446)).
- **The gap this theory fills.** Relational QM lets any physical system be an observer, so every electron counts. QBism requires an agent but gives no physical definition of one. Here an observer is an agent as defined by the scaling-break method, and an observation is the extraction of information into that agent's integrated state.

### Relative actuality, in bits

How far an event E is actual for agent A is the fraction of the event's uncertainty that has entered A's integrated state:

```math
\sigma_A(E) = \frac{I(A;E)}{H(E)}, \qquad 0 \le \sigma_A(E) \le 1
```

I(A;E) is the mutual information between the event and the agent's integrated state, not its sensors. H(E) is the event's entropy. Light that hits the retina but is never extracted gives σ ≈ 0 for the person, even though the photons carry the information. Collapse stops being yes-or-no and becomes a quantity, per agent.

### Facts are relative to levels

An event can be actual for a bee and not yet for the swarm. It becomes actual for level n+1 only after the information crosses the agent boundary and spreads through that level:

```math
t_{actual}^{(n+1)} \;\approx\; t_{actual}^{(n)} + \tau_{cross}^{(n+1)}
```

Special relativity made simultaneity relative because the speed of light is finite. This theory makes actuality relative because bandwidth is finite and agents compress what they pass on. The hierarchy is a naturally nested Wigner's-friend setup: the bee is the friend, the swarm is Wigner.

### Stable facts are shared, classical facts

- Di Biagio and Rovelli distinguish relative facts, which hold for the systems that interacted, from stable facts, whose relativity can effectively be ignored; decoherence is what makes facts stable ([Di Biagio & Rovelli 2021](https://philsci-archive.pitt.edu/18763)). In this theory, a fact is stable when σ ≈ 1 for many agents at once.
- **Shared facts must be classical.** A set of quantum states can be broadcast (copied to several recipients) only if the states commute ([Barnum et al. 1996](https://arxiv.org/abs/quant-ph/9511010)). Agents communicate (A3), so whatever several agents share must be classical information. This is derived, not assumed.
- **Agreement comes from redundancy.** Quantum Darwinism shows how the environment stores many copies of certain states, which lets many observers reach consensus ([Zurek 2009](https://www.arxiv.org/abs/0903.5082)).
- **Brains work on classical information.** Neural decoherence takes about 10⁻¹³–10⁻²⁰ s, far shorter than neural dynamics at 0.001–0.1 s ([Tegmark 2000](https://arxiv.org/abs/quant-ph/9907009)).

### The constraint: records decide what outsiders can see

"For us it is still quantum" is formally correct. But an outsider can demonstrate the superposition, by seeing interference, only by reversing every record of the event: the cat, its breathing, the trap, every scattered photon. Records destroy that ability whether or not anyone extracted useful information from them.

So σ governs what is actual for an agent, not what outsiders can see. For a real cat, "quantum but unknown" and "collapsed but unknown" make no observable difference. The idea is testable only with agents whose entire state can be kept coherent and run backwards.

### The test: an intelligent Schrödinger's cat

Wiseman, Cavalcanti and Rieffel propose a Wigner's-friend experiment in which the friend is a human-level AI running on a large quantum computer, whose observation can then be reversed ([Wiseman et al. 2023](https://quantum-journal.org/papers/q-2023-09-14-1112/)). This theory adds a dial: vary how much useful information the AI friend extracts, from σ = 0 to σ = 1, then reverse its lab and check whether the outsider still sees interference.

| Outcome | What it would mean |
| --- | --- |
| Interference survives at every σ | Standard quantum mechanics and relative actuality hold. Only reversibility matters. |
| Interference depends on σ beyond what record-keeping explains | Intelligence-relative collapse with observable consequences: new physics. |
| No interference, even after reversal | Objective collapse triggered by the agent, as in integration-based collapse models ([Chalmers & McQueen 2021](https://arxiv.org/abs/2105.02314)). |

A small version could be built much sooner, with few-qubit "agents" on today's quantum processors: compare a register that merely copies a qubit with a circuit that extracts the information and acts on it.

## Stress tests and counterexamples

The bare premise, "many agents + processing + communication = intelligence", fails on obvious cases. Each failure forces a specific refinement, and those refinements are where the theory gains content.

| Case | Why it challenges the premise | What it forces into the theory |
| --- | --- | --- |
| A gas | \~10²³ molecules exchange information through collisions, yet nothing is intelligent. | Persistent memory, selective communication and a far-from-equilibrium energy flow (A10). |
| A crystal | Highly correlated, yet not intelligent. | Too much order is as bad as too little. This motivates the criticality hypothesis (A13). |
| Epileptic seizure | Coupling rises, and intelligence and consciousness vanish. | More communication is not always better. Agents must stay independent enough to differ. |
| Anesthesia, deep sleep | Integration falls, and consciousness vanishes. | Integration is necessary. This is measurable with the perturbational complexity index. |
| A thermostat | High η on one trivial task. | Weight achievement by how varied and novel the tasks are. |
| A lookup table | Perfect answers using no experience bits. | Count prior bits in η's denominator. |
| A CPU or GPU cluster | Billions of communicating units. | Either the theory grants some intelligence, or the agent definition must exclude units without persistent, plastic memory. **\[Open\]** |
| A language model | Intelligent behavior from a monolithic trained network. | Decide whether its units count as "independent agents", or whether the training data plays the role of the collective. **\[Open\]** |
| The internet, a market, a society | Huge collectives of intelligent agents. | The theory must give a criterion: Π₄ for unity and Π₁ for coherence. It predicts low unity because speech is \~39 bit/s against \~10⁸ bit/s inside a brain. |
| A single bacterium | Shows adaptive, quasi-intelligent behavior. | Nesting (A4): the cell is itself a collective of molecular agents. |

## Consciousness as a separate layer

Consciousness is treated as a further layer on top of intelligence, not as the same thing. The theory is built for intelligence first, and then asks which extra conditions separate a conscious collective from a merely intelligent one.

Candidate conditions, all **\[Hypothesis\]**:

1. **Integration.** The collective acts as one: Π₄ is small and Π₁ ≥ 1 on the timescale of experience.
2. **Differentiation.** It can be in a very large number of distinguishable states, so its activity is information-rich rather than uniform.
3. **Self-model.** Possibly, the collective carries a model of itself among the things it predicts. **\[Open\]**

The first two conditions already have a clinical measure. The perturbational complexity index scores the brain's response to a magnetic pulse by how integrated and differentiated it is. It separates wakefulness from deep sleep, anesthesia and coma ([Casali et al. 2013](https://orbi.uliege.be/handle/2268/171542)).

Two cautions:

- **The IIT pitfall.** Integrated Information Theory's measure Φ can rate a simple, regular grid of logic gates above a brain. Any measure this theory proposes must be checked against that kind of counterexample.
- **Scope (A15).** The framework can explain the functional signatures of consciousness: when it appears, how it fragments, and where a self ends. It does not, so far, explain why any of this is experienced. That limit is stated, not hidden.

## Relation to existing work

The core intuition is well established. What is new here is the attempt to make it a quantitative physics, with bits and agent count as state variables, dimensionless groups and hard bounds.

| Work | What it contributes | What this theory adds or does differently |
| --- | --- | --- |
| Minsky, *The Society of Mind* (1986) | The mind as a society of simple agents | Physical units, scaling and bounds |
| Hopfield (1982); statistical physics of neural networks | Collective memory as a physical system; capacity \~0.14·N | Extends it from memory to intelligence as a whole, with space and latency included |
| Landauer (1961); Szilard (1929) | Information has an energy cost; information can be turned into work | Used as the energy roof and as numerator option C |
| [Touchette & Lloyd (2000)](https://arxiv.org/abs/chao-dyn/9905039) | Each bit gathered by a feedback controller can reduce entropy by at most one extra bit | The ceiling η ≤ 1 for numerator option B |
| Chollet, *On the Measure of Intelligence* (2019) | Intelligence as skill-acquisition efficiency relative to priors and experience | Adds communication bits; puts η next to physical capacity |
| Legg & Hutter (2007) | Intelligence as goal achievement across environments | An alternative numerator |
| Yao (1979), communication complexity | The minimum bits parties must exchange to compute a function | The lower limit for I\_comm |
| Integrated Information Theory (Tononi) | Consciousness as integrated information Φ | Integration enters through Π₄ and Π₁, but must avoid the grid counterexample |
| Free Energy Principle (Friston) | Agents as Markov-blanketed systems that minimize surprise | The agent boundary definition; prediction as achievement |
| [Bassett et al. (2010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2858671) | Brains obey Rent's rule like efficient chips | Evidence for P3 |
| Bettencourt et al. (2007), urban scaling | Superlinear scaling of output with city size | Evidence for P4 |
| Herculano-Houzel; [Olkowicz et al. (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4932926) | Neuron counts and densities predict cognition | Evidence for P4 and P6 |
| Beggs & Plenz (2003), neuronal avalanches | Cortex operates near criticality | Evidence for A13 |
| [Casali et al. (2013)](https://orbi.uliege.be/handle/2268/171542), PCI | A clinical index of integration × differentiation | The measurement tool for the consciousness layer |
| Seeley, honeybee swarm decisions | A swarm chooses nest sites by distributed signaling | A reference collective with measurable bits |
| Levin, multiscale competency | Goal-directed behavior at the cell and tissue levels | Evidence for nesting (P8) |
| Seeley et al. (2012); Marshall et al. (2009) | Swarms and primate brains decide by the same algorithm: competing evidence accumulation, a threshold, cross-inhibition | Evidence for universality across levels (H3) |
| O'Donnell et al. (2015) | Social wasps invest less in mushroom bodies than solitary wasps | Evidence that agents simplify as the collective strengthens (H6) |
| Zheng & Meister (2024) | Human behaviour runs at \~10 bit/s against \~10⁹ bit/s of sensory input | Measures the agent funnel that sets Π₂ of the level above |
| Lorenz et al. (2011) | Mild social influence undermines the wisdom of crowds | Evidence that over-coupling fails at the social level too (H4) |
| Cavagna et al. (2010) | Scale-free correlations in starling flocks; flocks behave as critical systems | Basis for the correlation ratio Π₆ |
| West, Brown & Enquist (1997); Bettencourt (2013) | Scaling exponents derived from fractal networks (metabolism, cities) | Template for deriving the exponents in P4 |
| Rovelli (1996); Di Biagio & Rovelli (2021), relational quantum mechanics | Facts are relative to the system that interacts; stable facts arise through decoherence | The relational core of A16; this theory adds a physical definition of the observer and graded actuality σ |
| Fuchs, Schack et al., QBism | Measurement is an agent's action; outcomes are personal to the agent | Agent-centred view; this theory defines the agent physically |
| Barnum et al. (1996); Zurek (2009), quantum Darwinism | Only commuting states can be broadcast; redundant records create objectivity | Shared facts between agents must be classical (A17) |
| Tegmark (2000) | Brain decoherence is many orders of magnitude faster than neural dynamics | Brains operate on classical information |
| Wiseman, Cavalcanti & Rieffel (2023) | A Wigner's-friend experiment with a human-level AI friend on a quantum computer | The test for relative actuality, extended here with the σ dial |
| Chalmers & McQueen (2021) | Objective collapse triggered by integrated information | The rival hypothesis A18, decided by the same experiment |
| Shannon (1948); Weaver (1949) | Information theory deliberately excludes meaning; three levels of communication: technical, semantic, effectiveness | The theory now reaches the semantic and effectiveness levels through κ |
| Slepian & Wolf (1973) | With side information at the receiver, a source can be sent at rate H(X\|Y) | Formal basis of context amplification κ (A19) |
| Wegner, Erber & Raymond (1991) | Close couples form a transactive memory greater than either partner's | Evidence that shared context integrates agents beyond raw bandwidth |
| Woolley et al. (2010); Huckman, Staats & Upton (2009) | Group intelligence tracks social sensitivity and turn-taking; team performance tracks prior shared work | Evidence that shared context, not individual ability or bandwidth, drives group performance |
| Blondel et al. (2008); Ronen et al. (2014) | A national phone network splits into language communities; the global language network has English as hub with a few intermediate hubs | Evidence that humanity's modules follow shared language (X2) |
| Zhou, Sornette, Hill & Dunbar (2005) | Human group sizes form a discrete hierarchy with a scaling ratio near three | Scaling breaks inside human society |
| Sandberg, Armstrong & Ćirković (2017); Bennett, Hanson & Riedel (2019) | Aestivation hypothesis: cooler environments make computation cheaper; disputed | Energy side of galactic-scale intelligence |
| Dynamical similarity (Reynolds; Buckingham 1914) | Systems at different scales behave identically when their dimensionless groups match; scale models in wind tunnels and ship tanks | Basis of the similarity principle for minds (A21) and of partial similarity |

The 2024 Nobel Prize in Physics, awarded to Hopfield and Hinton, recognized the statistical physics of collective neural computation as physics.

## Open questions and uncertainty register

Twenty-nine questions stand between this draft and a testable theory. Tick each one off once it is settled, and record the decision in the relevant section.

- [ ] **Numerator of η (A11).** Option A (count per bit), B (bits removed per bit) or C (work per bit)?
- [ ] **Graded or threshold (A8).** Does intelligence grow smoothly with N, or switch on at a phase transition?
- [ ] **What counts as an agent.** Is a transistor an agent? An artificial neuron? Is persistent, plastic memory required?
- [ ] **Which communication bits count.** Raw channel bits, or only the mutual information that actually changes the receiver's state?
- [ ] **Weighting by generality.** How should G be weighted so that narrow, trivial tasks do not score high?
- [ ] **The Biot threshold.** Derive the unity threshold for Π₄ instead of borrowing 0.1 from heat transfer.
- [ ] **Units.** Should η be bit⁻¹ or dimensionless? This follows from the numerator choice.
- [ ] **Conserved quantities.** Is anything conserved, as energy is in mechanics, or does the theory only have bounds?
- [ ] **Equations of motion.** Beyond bounds, what laws govern how η and capacity change over time (learning, growth)?
- [ ] **Self-model.** Is a self-model required for consciousness, or are integration and differentiation enough?
- [ ] **Verify estimates.** Check every \[Estimate\] against primary sources, starting with the appendix.
- [ ] **Complete references.** Add links for the references in the previous section that still lack them.

* [ ] **D\_T beyond brains.** Does the topological dimension of the wiring differ between integrated and federated collectives?
* [ ] **Maximum size of an integrated level.** Derive it from D\_T, signal speed and Π₁.
* [ ] **Test the scaling-break method.** Run it on a simulation with known agent boundaries before using it on real data.
* [ ] **Bees near criticality?** Measure Π₆ and avalanche statistics in tracked swarms.
* [ ] **From fractals to RG.** Formalize levels as coarse-graining steps and identify which features are "relevant".

- [ ] **What counts as "useful".** Should σ use mutual information with the agent's integrated state, or with its decisions and actions?
- [ ] **Measuring σ in real agents.** Can σ be estimated from behaviour in brains or bee swarms?
- [ ] **A few-qubit σ-dial experiment.** Design a copy-only agent and an extract-and-act agent on a small quantum processor.
- [ ] **Actuality and consciousness.** How does relative actuality relate to the consciousness layer and to Π₄?

* [ ] **Measuring κ.** How can shared context H(X|S) be estimated for real pairs of agents: couples, teams, bees?
* [ ] **Protocol versus content.** Can shared code be separated empirically from shared beliefs, and is it only the second that harms independence?
* [ ] **Shared context and the self.** Can deep shared context make two people partly one system, when Π₄ is computed with κC?

- [ ] **The top of the hierarchy.** Is humanity the highest current level, or is humanity together with its machines already a level above it?
- [ ] **Nations and languages measured.** Compute Π₄ and κ for nations and for language communities, and compare the two boundaries.
- [ ] **Translation without uniformity.** Can AI mediation raise κ between modules without collapsing the diversity of beliefs?

* [ ] **What is "the same thought"?** Define precisely which correspondence between two minds' information trajectories counts as identity.
* [ ] **A data-collapse test.** Gather decision-time and accuracy data for brains, swarms, ant colonies and committees, and test whether they fall onto one curve in cognitive time θ.

## Research program and next steps

The program runs in six steps, from fixing definitions to testing predictions. Each step's result feeds a new version of this document.

1. **Fix the definitions.** Choose the numerator of η and a precise agent boundary. This settles A8, A11 and the agent question.
2. **Build a cross-system table.** Fill in N, k, m, r, C, ℓ, v, P and the Π groups for very different systems: a human brain, a crow brain, a honeybee colony, an ant colony, a GPU cluster and a company. The test is whether the Π groups sort them in a way that matches what we already know about their intelligence.
3. **Simulate a minimal model.** Agents with small memories on a graph perform a collective prediction or foraging task. Vary N, k, C and coupling strength, measure η, and look for phase transitions and scaling exponents.
4. **Derive and check the bounds.** Compute the roofline bound for each system in step 2 and identify which term binds.
5. **Compare with scaling data.** Neuron counts across species, colony size versus task repertoire in social insects, urban scaling, ML scaling laws.
6. **Test the consciousness layer.** Check the Π₄ and Π₁ predictions against split-brain cases, anesthesia and PCI data.

Steps 2 and 3 can start right away and do not depend on each other.

## Appendix: reference values for the human brain

The human brain is the reference collective. Sourced values link to the paper. "Derived" values are computed from the rows above them. "Approximate" values are textbook orders of magnitude still to be checked.

| Quantity | Value | Basis |
| --- | --- | --- |
| Neurons, N | 86.1 ± 8.1 × 10⁹ (19% in the cerebral cortex) | [Azevedo et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19226510/) |
| Synapses per neuron, k | \~10³–10⁴ | Approximate |
| Total synapses | \~10¹⁴–10¹⁵ | Approximate |
| Storage per synapse | \~4.7 bits (26 distinguishable strengths, rat hippocampus) | [Bartol et al. 2015](https://elifesciences.org/articles/10778v1) |
| Total memory, N·m | \~10¹⁵ bits | Derived |
| Brain volume | \~1.2 L | Approximate |
| Mean spacing between neurons, d | \~25 μm | Derived: (volume / N)^(1/3) |
| Signal speed, v | \~0.5–100 m/s (unmyelinated to myelinated) | Approximate |
| Size, R | \~0.15 m | Approximate |
| Crossing time, τ\_cross | \~10–50 ms, including synaptic delays | Derived |
| Power, P | \~20 W | Approximate |
| Synaptic events | \~10¹⁴–10¹⁵ per second | Approximate |
| Energy per synaptic event, ε | \~10⁻¹⁴ J | Derived |
| Landauer limit at 310 K | 2.97 × 10⁻²¹ J per bit | Derived: kT ln 2 |
| Landauer efficiency, Π₅ | \~10⁻⁷ | Derived |
| Retina to brain | \~10⁶ ganglion cells, \~10⁷ bit/s (extrapolated from guinea pig) | [Koch et al. 2006](https://pmc.ncbi.nlm.nih.gov/articles/PMC1564115) |
| Corpus callosum | \~2 × 10⁸ axons | Approximate |
| Speech between people | \~39 bit/s, similar across 17 languages | [Coupé et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970) |
| Genome as priors | \~6 × 10⁹ bits (3.1 × 10⁹ base pairs × 2 bits) | Derived |
