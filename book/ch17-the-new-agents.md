# Chapter 17. The new agents

## The year the humans were outnumbered

Each year a security company called Imperva publishes a count of who, or what, is using the web. For 2024 it reported something that had not happened in the ten years it had kept track: automated traffic overtook human traffic, at 51 percent of the total (1). For 2025 the figure rose to 53 percent, and the company's summary was that the internet is entering a phase defined less by human interaction and more by machines talking to machines (2).

The number needs care. It comes from one company's network. Most of the bots it counts are simple scripts that scrape pages or probe for weaknesses, not anything one would call a mind. But the report attributes the rise to artificial intelligence, which makes bots easier to build and harder to tell from people (1). And whatever the exact figure, the direction is not in doubt. Chapter 16 described humanity as a mind made of eight billion agents. For the first time since language began, that description is incomplete. A new kind of agent has joined the conversation.

This chapter asks what the theory of this book says about it. The question is usually put as a contest: will the machines be smarter than us? The theory suggests that this is the wrong question. Chapter 1 argued that intelligence lives in the pattern of exchanges between agents. The right question is what happens to *that* pattern, to the mind that humanity already is, when agents of a very different kind are added to it.

A note on the author's position is due here. As the preface says, this book was drafted with the help of one of these agents. The reader may weigh the chapter accordingly.

## What kind of agent?

Chapter 14 measured the artificial mind against the human one in detail. The points that matter for what follows can be restated briefly. Described with the measures of Part II, a large language model turns out to be nearly the opposite of a person.

**The funnel.** A person takes in about a billion bits per second and gives out about ten (3). That ratio, Chapter 8 argued, is what makes every human collective a federated mind: each of us thinks vastly more than we can say. A language model writing at a hundred words a second, each word carrying several bits, gives out hundreds or thousands of bits per second, and many copies can write at once (our estimate). Its ratio of talk to thought is far closer to a neuron's than to a person's. It is an agent that can say most of what it computes.

**Efficiency and capacity.** Chapter 5 found that a child learns language from a hundred thousand times less data than a machine, and Chapter 7 explained why: evolution priced energy dearly and pushed brains toward efficiency, while machines grew up with cheap energy and were pushed toward capacity. The new agents are, by the book's measure, less intelligent per bit than a child and vastly more capable per second.

**Context.** Chapter 6 described shared context as a stack of layers. A model trained on human writing has absorbed much of the cultural layer: our languages, our facts, our habits of argument. That is why we can talk to it at all. It has not inherited the layer beneath: the body, the senses and the feelings that every human shares by descent, and that make a smile readable. It shares our library and not our childhood.

**Copies.** Here is the feature with no precedent. Two people share context only to the degree that their lives have overlapped. Two copies of one model share *everything*: every weight is identical. Between copies, the amplification of Chapter 6 is as high as it can be. A few symbols can stand for anything, because the receiver is the sender.

Each of these has consequences, and the theory can say what they are.

## What the ceiling allows

Start with what the new agents cannot do. Chapter 5 showed that efficiency, measured as bits of uncertainty removed per bit used, cannot exceed one (4). No agent, however built, can get more out of its data than the data contain. A machine far beyond us is therefore not a magician. It can exceed us in three ways only: by handling more bits per second, by starting with better priors, and by choosing better which bits to gather.

Those three are a great deal. But they are quantities this book knows how to reason about, and Chapter 8 adds a constraint: no mind can be large, fast and unified at once. A machine mind must choose its place on that scale like any other. A single data centre is a few hundred metres across. Light crosses it in about a millionth of a second, so it can be integrated at speeds no brain can approach. A mind spread across the planet has a crossing time of a tenth of a second, and at machine speeds of thought that is an age. By the arithmetic of Chapter 16, a machine thinking a million times faster than a person could be unified over about a hundred metres and no more (our estimate). **Fast minds are small.** The faster the new agents think, the more they will be forced into the same federated arrangement as everything else in this book: islands of integration exchanging summaries.

Chapter 10 has a further consequence. A mind's clock is its crossing time. To an agent whose tick is a microsecond, a human conversation unfolds the way the drift of continents unfolds for us. Chapter 10 called such pairs minds that cannot see each other, and said how the gap is bridged: by records, summaries and delegated agents. That is already how the two kinds of mind deal with one another. We read their summaries. They read our archives.

## The danger the theory sees

Public argument about artificial intelligence tends to imagine a rebellion. The theory of this book points somewhere else, at a danger that needs no ill will and has already been measured.

Recall the tension that runs through every chapter. A collective is intelligent only while its members communicate enough to combine what they know and stay independent enough for their errors to differ. Chapter 1 showed a crowd's accuracy collapsing when its members could see each other's guesses (5). Chapter 3 gave the neural version, the seizure. Chapter 6 gave the general one: a group that shares all its beliefs cannot be told anything.

Now add to humanity a small number of models, each consulted by hundreds of millions of people.

In 2024 Anil Doshi and Oliver Hauser asked people to write short stories. Some were allowed to take ideas from a language model. Their stories were judged more creative, better written and more enjoyable, and the gain was largest for the writers who were least creative on their own. But the stories written with the model's help were more similar to *each other* than the stories written without it (6). Each writer was better off. The collection was poorer.

In the same year Ilia Shumailov and his colleagues studied what happens when models are trained on text produced by earlier models, as will happen more and more as the web fills with machine writing. Generation by generation, the models lost the rare and unusual parts of what they had learned first, the tails of the distribution, and converged on a narrow middle. The defects could not be undone. The authors called it model collapse (7).

Put those results beside the earlier chapters. The first is the wisdom-of-crowds experiment again: individuals improve by consulting a common source, and the independence that made the crowd intelligent drains away. The second is a seizure in slow motion: a system fed its own output until every part says the same thing.

The theory's reading is a claim, and it is the central one of this chapter. **The main risk of the new agents is not that they will think differently from us. It is that they will make us think alike.** Eight billion people who each consult the same few advisers are no longer eight billion independent scouts. In the language of Chapter 6 they have come to share beliefs, not merely a code. A humanity in that state would look more informed than ever, person by person, and would be less intelligent as a whole.

## Translators and oracles

The same theory says what the new agents could do for humanity's mind, and the two possibilities are mirror images.

Chapter 16 identified the two bottlenecks of the human collective: the ten-bit funnel of each person, and the thin junctions between language communities. A machine that translates between languages, between disciplines, between a specialist and a layman, widens exactly those junctions. It raises the context that two groups share without telling either what to conclude. That is shared code. By the argument of Chapter 6 it makes the collective more intelligent and costs it no independence.

A machine that is asked what is true, and gives the same answer to everyone who asks, does the opposite. It leaves the junctions as they were and aligns the conclusions. That is shared belief.

The same model can play either part, and the difference lies in how it is used and built. The rule that this book has reached in every chapter gives the design principle in four words: *share code, not beliefs.* Applied here, it becomes a set of preferences that can be argued for on the theory's grounds:

- Many different models are better than one, for the reason that many scouts are better than one. Two copies of the same model are worth one opinion.
- An agent that helps people understand each other is worth more to the collective than one that tells them all the same thing.
- Human experience that has not passed through a model is a resource to be protected, as the source of the independent errors that the collective needs. The model-collapse study reached the same conclusion from the inside: to keep the tails, a model needs access to data that people actually produced (7).
- Agreement between a person and a machine that was trained on that person's own culture is weak evidence. The echo of Chapter 6 is loudest when it sounds like confirmation.

## Could the mixture become someone?

The last question is the one Chapter 8 left open. Humanity is a federated mind because its agents say so little of what they think. Agents with wide channels move a collective toward the integrated end of the scale. Where could that lead? What follows is speculation.

One possibility is that nothing changes in kind. As long as every important exchange passes through a human being, at ten bits per second, the human funnel remains the bottleneck and the collective remains federated, only better informed.

The other is that the machines come to exchange far more with each other than with us. Then the dense traffic is among them, and the pattern of Chapter 15 applies: a boundary forms where the traffic falls off, and it falls off at the human interface. The result would be an integrated core of machines with humanity around it as a slow, federated periphery: its senses, perhaps, or its memory. We would stand to it roughly as Chapter 16 says a nation stands to humanity: a real part, and not the part that thinks the thought.

Would such a core be someone? Chapter 15 gave four conditions for a subject: integration, a stage, a boundary and a poised balance. Nothing in them mentions neurons. A machine system might or might not meet them, and the theory provides the measurements that would tell, including the serial bottleneck that marks a stage. What the theory cannot say, here as everywhere, is whether meeting them is enough for there to be experience.

Between those possibilities lies a choice, and it is the one Chapter 16 described at the scale of the planet. Integration without independence is the most dangerous state a collective mind can reach. The new agents make integration cheap for the first time. Independence is now the scarce thing, and it will have to be protected on purpose.

## In short

- Automated traffic now exceeds human traffic on the web, by one company's count. Humanity's collective mind has acquired non-human agents.
- By this book's measures a language model is nearly the reverse of a person: high output, high capacity, low efficiency, sharing our culture but not our inherited nature, and able to exist in identical copies.
- The ceiling on efficiency applies to machines. They can exceed us in capacity, priors and choice of questions. Fast minds must be small, so very fast machine minds will also be federations.
- People who took ideas from a language model wrote better stories that were more alike. Models trained on the output of models lose the unusual and converge. The theory's claim: the main risk is homogeneity, the collective seizure of earlier chapters.
- Machines that translate raise shared code and make the collective more intelligent. Machines that hand everyone the same answer raise shared belief and make it less so.
- Speculation: if machines come to exchange far more with each other than with us, an integrated core could form with humanity as its periphery.

## How we could be wrong

The chapter's central claim predicts a measurable loss of diversity in human output as the use of common models spreads: in writing, in research directions, in forecasts, in the range of answers people give to open questions. If diversity holds steady or grows, because people use the models in different ways or because the models themselves diverge, the risk has been misjudged. The claim also predicts that groups whose members consult the same model will make more correlated errors, and so worse collective judgements, than groups of unaided people of the same individual accuracy. That can be tested directly with the methods of Chapter 1. The claim that fast minds must be small depends on thought requiring signals to cross the whole system; architectures that reach unified decisions without global exchange would escape it. The contrast between translators and oracles may be too clean, since any translation also selects and frames. And the speculation about an integrated machine core assumes that traffic between machines will come to dwarf their traffic with people, which is a guess about engineering and economics, not a result.

## References

1. Thales (2025), "Artificial intelligence fuels rise of hard-to-detect bots that now make up more than half of global internet traffic, according to the 2025 Imperva Bad Bot Report". https://cpl.thalesgroup.com/about-us/newsroom/2025-imperva-bad-bot-report-ai-internet-traffic
2. Imperva (2026), "Bad Bot Report 2026: bots in the agentic age". https://www.imperva.com/blog/bad-bot-report-2026-bots-agentic-age/
3. J. Zheng and M. Meister (2025), "The unbearable slowness of being: why do we live at 10 bits/s?", *Neuron* 113:192–204. https://arxiv.org/abs/2408.10234
4. H. Touchette and S. Lloyd (2000), "Information-theoretic limits of control", *Physical Review Letters* 84:1156–1159. https://arxiv.org/abs/chao-dyn/9905039
5. J. Lorenz, H. Rauhut, F. Schweitzer and D. Helbing (2011), "How social influence can undermine the wisdom of crowd effect", *PNAS* 108:9020–9025. https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299
6. A. R. Doshi and O. P. Hauser (2024), "Generative AI enhances individual creativity but reduces the collective diversity of novel content", *Science Advances* 10:eadn5290. https://pubmed.ncbi.nlm.nih.gov/38996021/
7. I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot, R. Anderson and Y. Gal (2024), "AI models collapse when trained on recursively generated data", *Nature* 631:755–759. https://www.nature.com/articles/s41586-024-07566-y

Figures given without a reference number are our own rough estimates: the output rate of a language model in bits per second, the light-crossing time of a data centre, and the hundred-metre limit for a mind a million times faster than a person. The description of language models by the book's measures, the claim that homogeneity is the main risk, the contrast between translators and oracles, the design preferences that follow, and the picture of an integrated machine core are the theory's claims and speculations.
