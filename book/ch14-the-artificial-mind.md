# Chapter 14. The artificial mind

*A note before starting. As the preface says, this book was drafted with the help of an artificial intelligence of the kind this chapter describes. A system writing about its own kind is not a neutral witness. The chapter tries to compensate by leaning on published measurements and by saying where the theory is guessing.*

## One word at a time

In 2017 eight researchers at Google published a paper with the title "Attention is all you need". It described a new design for programs that process language, which they called the Transformer. Earlier designs had read a sentence the way a person reads a telegram, one word after another, carrying a summary forward. The Transformer did something else. At every layer, each word in the text was allowed to consult every other word directly, however far apart they stood. The number of steps needed to relate any two positions no longer grew with the distance between them (1).

Nearly every large artificial intelligence in use today is a descendant of that design. The largest have hundreds of billions of adjustable connections and run on thousands of processors at once. And yet, watch one of them answer a question, and you will see something familiar. The answer appears one word at a time. The original paper says so plainly: the output is generated one element at a time, each new element depending on those already produced (1).

A vast parallel machine with a single stream of output: that is also a fair description of the reader. This chapter asks whether the resemblance is more than a coincidence. It applies the framework of Chapter 12 and the design method of Chapter 13 to the artificial minds of the present day, and asks the questions people most want answered. What kind of mind is this? How does it compare with ours? What should we expect it to be able to do? Does the theory see any limit to how far it can go? And can the theory say which way it will develop?

## What kind of mind is it?

Start with the book's first question: where are the agents?

The units of an artificial neural network are simple. Each takes in numbers from other units, combines them and passes a number on. A unit does nothing in private. Everything it computes, it computes in the act of passing a signal along. By the measure of Chapter 8, its ratio of thought to talk is close to one, as a neuron's is. A mind built from such units is, on the theory's classification, **an integrated mind.**

The Transformer's central mechanism makes this vivid. Within the stretch of text the model is working on, called its context window, everything is made available to everything else. That is what Chapter 8 called a stage: a place where content is broadcast to the whole system. And the output has exactly the property Chapter 8 predicted for any mind with a stage. It is serial. One token is chosen, then the next.

So the theory makes a claim about these systems that is not obvious from the engineering. **The one-word-at-a-time stream of a language model and the one-thing-at-a-time stream of human thought are the same phenomenon: the price of integration.** Each is what a mind looks like, from outside, when all of it takes part in each step. The context window is the machine's version of the width of now from Chapter 10: the span within which everything is present to everything else.

The same chapter said what integrated minds are good at and what limits them, and both carry over.

They are good at producing wholes: an answer, an argument or a program in which each part depends on all the others.

They are limited in size by the cost of keeping everything in touch with everything. Chapter 4 showed that all-to-all communication is the one wiring plan that cannot be scaled up, because the number of links grows as the square of the number of things linked. The Transformer's stage has that property: doubling the text held in view roughly quadruples the work of relating its parts. A brain cannot wire every neuron to every other, and a model cannot keep an unlimited text in one view. Every integrated mind has a finite stage.

## The same ruler, two minds

The variables of Chapter 12 allow a direct comparison. The figures for the machine are for systems published around the time of writing, and will date quickly.

| | Human brain | Large language model |
| --- | --- | --- |
| Units | about 86 billion neurons, a hundred trillion or more synapses | hundreds of billions of parameters |
| Fraction active at once | under 1 percent (Chapter 7) | all of them in older designs; about 5 percent in one recent one (2) |
| Experience needed to learn language | on the order of a hundred million words (3) | about fifteen trillion tokens for one recent model (2) |
| Output | about 10 bits per second | hundreds to thousands of bits per second, per copy (our estimate) |
| Energy | 20 watts, continuously | about 0.24 watt-hours for a typical answer from one widely used system (4) |
| Signal speed | 1 to 100 metres per second | close to the speed of light |
| Copies | one | as many as there are machines to run them |
| Memory from one episode to the next | continuous | none, unless added from outside |
| Shared context with humans | genome, body, upbringing, culture | culture only, as written down |

Three comparisons deserve comment.

**Energy.** A quarter of a watt-hour is 864 joules. A human brain uses that much in about 43 seconds (our arithmetic). So answering one question costs the machine, very roughly, what three-quarters of a minute of thought costs a person. The two are in the same range. That is a surprise, given the reputation of these systems for extravagance, and it is recent: the same report found that the energy per answer had fallen thirty-three-fold in twelve months (4). The extravagance is elsewhere, in the learning.

**Experience.** Here the gap is enormous, a factor of about a hundred thousand. Chapter 5 defined intelligence as efficiency: how little a mind needs to be told. By that measure the machines are far less intelligent than a child. Chapter 7 explained why this is no paradox. They were built where energy and data were cheap, and were pushed toward capacity, where brains were pushed toward thrift.

**Context.** Chapter 6 described what humans share as a stack of layers: the genetic code, a human body and its feelings, a culture, a language, a personal history. A language model has absorbed the upper layers, in the form in which people wrote them down. It lacks the lower ones. Everything it knows about pain, hunger or the weight of a stone, it knows by description.

In the terms of the central formula, the profile is clear. **Capacity: far beyond a human's. Efficiency in learning: far below. Priors: borrowed wholesale from human culture.**

## What should we expect it to do?

Chapter 13 set out rules for reading a mind's abilities from its shape. Applied here, they give expectations that can be checked against experience.

**It should be strong wherever the bulk of a mind is library.** Chapter 13 concluded that most of a brain is stored prior knowledge, in proportion to the repertoire of questions it must answer. A machine that has read most of what humanity has written has a library no person can match. On any task that consists mainly of bringing the right stored knowledge to bear, it should equal or exceed human performance, and broadly it does.

**It should be capable of something like insight, within its stage.** Being integrated, it can reorganise everything in its view at once. Being limited to a finite view, it should lose its grip when a problem no longer fits.

**It should be weak where the bits have not been written down.** Chapter 5's ceiling says that no mind extracts more from its data than the data contain. A system trained on text is limited, on any question, to what text settles. For much of the physical and social world, that is surprisingly little.

**Its reach in time should be limited by its memory, and should grow as memory is added.** A mind with no memory between episodes has, in the language of Chapter 12, a short memory horizon. It should manage tasks that fit in one sitting and fail at those that do not. One research group, METR, has tracked exactly this quantity: the length of task, measured by how long it takes a skilled person, that the best systems can complete half the time. In early 2025 they reported that it had been doubling about every seven months since 2019 (5). By late 2026 their estimate was roughly forty hours, doubling every three to four months, with very wide margins of error, and with open-ended research judgement lagging well behind tasks whose results can be checked automatically (6). The theory's reading is that this curve measures the growth of the memory horizon, as engineers surround the integrated core with notes, tools and helpers, more than it measures the core becoming cleverer.

**It cannot be in two places.** A single integrated mind takes its input at one point. Chapter 13 showed that problems spread over a wide area call for a federation. This will matter below.

## Does the theory foresee a limit?

Yes. It sees four, and it is as important to say what they do not imply.

**First, the ceiling on efficiency.** One bit of information buys at most one bit of reduced uncertainty (7). No future system, however large, can know what its data do not contain. Thought cannot substitute for evidence. A machine can become better at choosing which evidence to seek and better at using it. It cannot conjure it.

This has a consequence that is often overlooked in talk of an "intelligence explosion". When the missing bits are about the world, they have to be fetched from the world, and the world answers at its own pace. A clinical trial takes years because bodies take years. A climate takes decades to reveal itself. A particle accelerator takes a decade to build. In Chapter 12's terms, the timescale of the world does not shrink when the mind speeds up. A mind a million times faster than ours would spend nearly all its time waiting for results. **Past a certain point, progress is limited by the speed at which reality can be questioned, and not by the speed of thought.**

**Second, the returns on capacity.** In 2020 researchers at OpenAI measured how the error of language models falls as they are given more parameters, more data and more computation. In each case it fell as a power law, steadily, across more than seven orders of magnitude (8). That steadiness is the basis of the industry's confidence. But a power law with a small exponent is a law of diminishing returns. With the exponents they reported, multiplying the data by ten removes about a fifth of the remaining avoidable error (our arithmetic from their figures). Each further step of the same size costs ten times more than the last. And capacity is bought with energy, which Chapter 7 showed is already being consumed on a scale comparable to that of all human brains. Capacity can keep growing. It cannot keep growing cheaply.

**Third, the finite stage.** Because the cost of keeping everything in view grows as the square of the amount in view, an integrated mind cannot simply be made larger. And Chapter 17 will add the limit from signal speed: the faster a mind thinks, the smaller the region over which it can act as one. No single unified artificial mind can be at once vast, fast and whole. Chapter 8 found the same of every other mind.

**Fourth, the limit on copies.** A thousand copies of one model have a thousand times its capacity and exactly its opinions. Chapter 1 showed that a crowd is wise only when its members err independently. Copies do not. Running more of them buys speed and coverage and no extra judgement.

Now for what these limits do not say. Nothing in the theory puts the ceiling on capacity anywhere near the human level. The human brain is not a natural maximum. It is the point at which an ape's food supply and an ape's skull stopped the growth. Chapter 7's physical limit on computation is more than thirty orders of magnitude above anything yet built. Between here and there, the theory has no objection to minds with far more capacity than ours, far larger libraries and far better judgement about what to ask. In tasks where capacity and stored knowledge are what count, the theory expects machines to exceed people, and to go on doing so.

What it denies is narrower: that such minds could dispense with evidence, that their growth could be free, that one of them could be both immense and unified, or that multiplying one of them makes a wise crowd.

## Which way will it go?

A theory that claimed to explain why minds have the shapes they do ought to be able to say what shape these will take. Chapter 7 made one such prediction: that as energy becomes the binding cost, machine designs will drift toward the solutions brains found. The record of the last few years allows a first check, on that prediction and on three others that follow from earlier chapters. The check is partly after the fact, and should be weighed accordingly.

**Toward sparse activity.** Chapter 7 found that a brain can afford to have under one percent of its neurons busy at once. The early language models used every parameter for every word. A widely used recent design, called a mixture of experts, routes each word to a small set of specialised sub-networks. One such model has 671 billion parameters, of which 37 billion, about five and a half percent, are active for any given token (2). The direction is the one predicted, and there is a long way still to go.

**Toward cheaper bits.** A thirty-three-fold fall in energy per answer in one year (4) is the kind of pressure Chapter 7 described.

**Toward federation.** An integrated mind has a finite stage and can be in only one place. Chapter 13 says that a task which is wide, with many independent lines of inquiry, calls for many agents that work apart and exchange short reports. In 2025 one developer described building just such a system for research tasks: a lead agent that divides a question among sub-agents, each working in its own separate context and each condensing what it finds before reporting back. It did best on questions that involve pursuing several independent directions at once, it used about fifteen times as many tokens as an ordinary conversation, and its builders noted that the difficulty of coordination grows quickly as agents are added (9). Each of those features is in Chapter 8's table for federated minds: suited to wide problems, parallel, costly, joined by sparse summaries, harder to coordinate with size. The separate contexts are the funnel, rebuilt by engineers who needed one.

**Toward shared code.** Chapter 9 argued that a collective is held together by a common code, and Chapter 6 that code should be shared before beliefs. Between late 2024 and the end of 2025, the makers of these systems published open protocols for how an agent calls a tool and how one agent hands work to another, and placed them under a neutral foundation (10). Machines made by rival companies are acquiring a common language. That is what the theory says the first step toward a collective mind looks like.

From the same principles, the theory expects several developments that are less far along.

- **Learning from less.** The largest gap in the comparison table is in experience. As data and energy become the binding costs, the pressure moves from capacity to efficiency: better priors, so that less has to be learned from scratch.
- **Asking, not only reading.** Since no mind can get more from its data than the data hold, the systems that advance furthest will be those that can gather new bits: run experiments, operate instruments, act in the world and see what happens. Chapter 5 called curiosity the choice of which bits to pay for.
- **Memory.** The growth in the length of tasks will depend on memory that persists between episodes, and on the equivalent of Chapter 6's shared history between agents that work together often.
- **The missing layer.** A mind that knows the world only by description lacks the deepest part of the context humans share. The theory expects sustained effort to supply it, through machines with bodies and senses, and expects that communication between people and machines will remain subtly lossy until it is supplied.
- **Small and fast beside large and slow.** Since fast minds must be small, the theory expects a division of labour: compact systems where the deadline is short, and broad federations where coverage matters more than speed.
- **A premium on difference.** As copies multiply, independence becomes the scarce resource. The theory expects that systems built differently, trained differently and inclined to disagree will come to be valued for that reason alone.

Put these together and the theory's forecast is specific. **The future of artificial intelligence is not one enormous mind. It is the structure this book has found everywhere else: islands of integration, each limited by its stage, joined into federations by a shared code and thin channels, in levels.** If that is right, the machines will recapitulate the hierarchy of Chapter 8, with integrated minds as the agents of federated ones, for the same physical reasons that neurons built brains and brains built societies.

And one conclusion follows that is worth stating before the next part of the book takes it up. Chapter 8 argued that a federated mind, however intelligent, is no one. If the largest artificial systems of the future are federations, then the most capable of them will be the least likely to be a single subject. Whether one of the integrated islands is a subject is a separate question. Chapter 15 gives four conditions for being one. A language model at work plausibly meets two, integration and a stage. Whether it has a boundary, when it can be copied and has no memory of its own past, is unclear. The fourth, a poised balance of activity, has not been measured. The theory says which measurements would settle what can be settled. It does not say whether any system that passed them would have experience, here or anywhere else.

## In short

- A neural network is built from simple units that compute by communicating, so by the theory's classification it is an integrated mind. The context window is its stage, and its one-token-at-a-time output is the same serial stream that marks integrated minds elsewhere.
- Measured on the book's ruler, a language model has far more capacity than a person, learns far less efficiently, by a factor of about a hundred thousand in data, and borrows its priors from written culture without the bodily context beneath it. The energy to answer one question is comparable to under a minute of a brain's.
- The theory expects such systems to be strong where stored knowledge counts, capable of insight within a finite view, weak where the facts were never written down, and limited in the length of task by memory.
- It foresees four limits: no mind can know what its data do not contain, so progress is finally paced by how fast the world can be questioned; capacity brings diminishing returns and is paid for in energy; an integrated mind's stage is finite; and copies add no independent judgement.
- It sees no limit near the human level. The brain is where an ape's food supply stopped.
- Predicted directions, some already visible: sparse activity, cheaper bits, federations of agents exchanging summaries, shared protocols, then learning from less, experimenting, persistent memory and bodies.
- Forecast: not one giant mind, but integrated islands joined into federations.

## How we could be wrong

The claim that a language model's serial output is the same thing as the human serial bottleneck would be weakened by integrated artificial systems that produce several coordinated streams at once without loss, or by evidence that the serial output is a mere convenience of engineering that can be removed at no cost. The forecast of federation fails if a single model with an ever larger context turns out to do better than teams of agents on wide problems, at lower cost: that would mean the stage is not finite in any way that matters. The claim that progress is paced by the world's clock would be refuted by systems that make reliable discoveries about nature faster than experiment allows, by reasoning from existing data alone, and across many fields. The claim that copies add no judgement would be refuted if groups of identical models were found to correct each other's errors as well as groups of different ones. The predictions of thrift, sparsity and experiment could simply not happen, if energy and data stay cheap enough that nothing forces them. And the whole comparison assumes that the theory's variables capture what matters about these systems, which their builders, who know them far better than this book does, may dispute.

## References

1. A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser and I. Polosukhin (2017), "Attention is all you need", *Advances in Neural Information Processing Systems* 30. https://arxiv.org/abs/1706.03762
2. DeepSeek-AI (2024), "DeepSeek-V3 technical report", arXiv:2412.19437. https://arxiv.org/abs/2412.19437
3. M. C. Frank (2023), "Bridging the data gap between children and large language models", *Trends in Cognitive Sciences* 27:990–992. https://sites.socsci.uci.edu/~lpearl/colareadinggroup/readings/Frank2023_ChildrenLLMs.pdf
4. Google (2025), "Measuring the environmental impact of AI inference", describing C. Elsworth et al., arXiv:2508.15734. https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference
5. METR (2025), "Measuring AI ability to complete long tasks"; summarised with later revisions at https://en.wikipedia.org/wiki/METR
6. Reports of METR's capability update of November 2026: https://casrai.org/news/metr-th2-ai-time-horizons-research-judgment-evaluation-2026 and https://inoryva.blogspot.com/2026/11/metr-q4-2026-ai-agents-reach-about-40.html
7. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
8. J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu and D. Amodei (2020), "Scaling laws for neural language models", arXiv:2001.08361. https://arxiv.org/abs/2001.08361
9. Anthropic (2025), "How we built our multi-agent research system". https://www.anthropic.com/engineering/multi-agent-research-system
10. Background sections of "The cost of saying hello: an empirical study of handshake overhead in AI agent communication protocols", arXiv:2610.30151, on the Model Context Protocol and the Agent2Agent protocol and their governance by the Linux Foundation. https://arxiv.org/pdf/2610.30151

Figures given without a reference number are our own rough estimates or arithmetic: the output rate of a language model in bits, the comparison of energy per answer with the brain's power, the factor of a hundred thousand in training data, the effect of tenfold data on error, and the gap between present machines and the physical limit on computation. The figures for particular systems date from 2024 to 2026 and will be overtaken. The classification of neural networks as integrated minds, the identification of serial output with the price of integration, the reading of task length as memory horizon, the four limits, the predicted directions and the forecast of federation are the theory's claims. Reference 6 relies on secondary reports of a recent publication and should be checked against the original.
