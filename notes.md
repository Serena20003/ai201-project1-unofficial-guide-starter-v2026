# Unit 1 Milestone 3 - Chunker

## Running `python app.py index` with fallback chunker
Corpus: city_guides
  loaded   14 documents, 28,958 characters, ~2,068 characters per document
  chunked  51 chunks, 650 characters on average (shortest 24, longest 800), produced by chunker.py::fallback_split
  embedding 51 chunks (first run downloads the model)...
  stored   51 chunks in 19.5s

## problem with current chunker

It slices straight through the labelled sections. Town name the information is for is not always immediately clear

## Running `python app.py index` with modified split_documents chunker

Corpus: city_guides
  loaded   14 documents, 28,958 characters, ~2,068 characters per document
  chunked  94 chunks, 318 characters on average (shortest 173, longest 758), produced by chunker.py::split_documents
  embedding 94 chunks (first run downloads the model)...
  stored   94 chunks in 63.3s

## Assumptions
1. Title is always the first line in the guide.
2. Each subsection under the subtitles are within reasonable size (not more than the initially defined 800 chunk size).

## Design choices
1. Overlap = 0. Upon reading the guides, overlap does not seem to provide extra information.
2. Include main title in all chunks.

## Improvements
1. Average chunk size smaller.
2. More readable and reasonable full sentence chunks.

## Future ideas
1. Handle subsection exceeding maximum chunk size.
2. Handle new lines within paragraphs.

# Unit 1 Milestone 4 - Tune retrival & Ground answers

## Asking questions (in-scope & out-of-scope)

### Cutoff THRESHOLD = 0.6, TOP_K = 5.

> Which towns are the worst when it comes to getting around with limited mobility?
(best distance 0.561, cutoff 0.6)

Based on the provided documents, **Kestrelford** and **Halden Bay** are described as difficult for getting around with limited mobility (from `guide_accessibility.md`).

Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_givens_mill.md

> When is the busy season for Kestrelford?
(best distance 0.246, cutoff 0.6)

August is busy with walkers in Kestrelford (from guide_kestrelford.md).

Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_seasons.md, guide_walking.md

> Do I need to bring cash or can I pay with card mostly when I visit Givens Mill?
(best distance 0.461, cutoff 0.6)

Cards are accepted almost everywhere now, though cash is still useful at the market and in smaller places. 

Source: guide_givens_mill.md

Sources retrieved: guide_corry_vale.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md

> What is the best season to visit Brightwater?
(best distance 0.305, cutoff 0.6)

According to `guide_brightwater.md`, May and June are the best months to visit Brightwater. Additionally, `guide_seasons.md` states that late May is arguably the best week of the year in Brightwater.

Sources retrieved: guide_brightwater.md, guide_seasons.md

> Does Elder Ness have an airport?
(best distance 0.324, cutoff 0.6)

I do not have enough information to answer whether Elder Ness has an airport. 

Source: `guide_elder_ness.md`

Sources retrieved: guide_elder_ness.md

> What is the recommended month to visit the Chinese rice farms?
(best distance 0.537, cutoff 0.6)

I do not have enough information to answer this question.

Sources retrieved: guide_givens_mill.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

> What is the capital of Mongolia?
(best distance 0.803, cutoff 0.6)

I don't have enough information about that.

> How do I change the oil in a diesel engine?
(best distance 0.886, cutoff 0.6)

I don't have enough information about that.

> Who won the 1994 World Cup?
(best distance 0.975, cutoff 0.6)

I don't have enough information about that.

> How do I write a for loop in Rust?
(best distance 0.838, cutoff 0.6)

I don't have enough information about that.

### Cutoff THRESHOLD = 0.7, TOP_K = 6

> Which towns are the worst when it comes to getting around with limited mobility?
  (best distance 0.561, cutoff 0.7)

Based on the documents, the locations categorized as "Difficult" for limited mobility are Kestrelford, Halden Bay, Corry Vale, and Elder Ness. 

Source: `guide_accessibility.md`

Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_givens_mill.md, guide_kestrelford.md

**IMPROVED!!**

> When is the busy season for Kestrelford?
(best distance 0.246, cutoff 0.7)

Based on the provided documents, August is busy with walkers in Kestrelford (*guide_kestrelford.md*).

Sources retrieved: guide_eating.md, guide_kestrelford.md, guide_seasons.md, guide_walking.md

> Do I need to bring cash or can I pay with card mostly when I visit Givens Mill?
(best distance 0.461, cutoff 0.7)

Cash is still useful at the market and in smaller places, but cards are accepted almost everywhere now (guide_givens_mill.md).

Sources retrieved: guide_corry_vale.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md, guide_thornby_wells.md

> What is the best season to visit Brightwater?
(best distance 0.305, cutoff 0.7)

May and June are considered the best months to visit Brightwater because of the long days, everything being open, and the students largely being gone (guide_brightwater.md). Additionally, late May is described as arguably the best week of the year for the same reasons (guide_seasons.md). September is also noted as a "sweet spot" that is warm, quiet, and has everything still open (guide_seasons.md).

Sources retrieved: guide_brightwater.md, guide_seasons.md, guide_thornby_wells.md

**IMPROVED!!**

> Does Elder Ness have an airport?
(best distance 0.324, cutoff 0.7)

Based on the provided documents, there is no mention of an airport in Elder Ness. (Source: guide_elder_ness.md)

Sources retrieved: guide_elder_ness.md

**IMPROVED!!**

> What is the capital of Mongolia?
(best distance 0.803, cutoff 0.7)

I don't have enough information about that.

> How do I change the oil in a diesel engine?
(best distance 0.886, cutoff 0.7)

I don't have enough information about that.

> Who won the 1994 World Cup?
(best distance 0.975, cutoff 0.7)

I don't have enough information about that.

> What is the recommended month to visit the Chinese rice farms?
(best distance 0.537, cutoff 0.7)

I don't have enough information to answer your question.

Sources retrieved: guide_givens_mill.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

> How do I write a for loop in Rust?
(best distance 0.838, cutoff 0.7)

I don't have enough information about that.

### --show-prompt example

```(best distance 0.537, cutoff 0.6)

======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from guide_givens_mill.md]
# Givens Mill
When to go

The mill runs March to November and is closed entirely in winter. Late spring is the best time. Summer Saturdays are busy enough that the car park becomes the limiting factor; come on a weekday if you can.

[from guide_givens_mill.md]
# Givens Mill
Where to stay

Nothing in the village itself. The nearest rooms are in Brightwater, which is close enough that this is not really a problem — most people come for a half day.

[from guide_thornby_wells.md]
# Thornby Wells
When to go

Year-round, genuinely. The gardens are best in May and June. The concert season runs September to April, which makes this the region's most reliable winter destination after Marchwood.

[from guide_marchwood.md]
# Marchwood
When to go

Any time. This is the one place in the region that works in winter, since almost everything is indoors and nothing closes seasonally. Conference weeks in March and October fill the hotels and double the prices; check before booking.

[from guide_seasons.md]
# When to visit the region
Spring, March to May

Days lengthen quickly and businesses that closed for winter reopen through
March and April. By May everything is open and the weather is reliable enough
to plan around. Late May is arguably the best week of the year in Brightwater —
long days, everything running, and the students gone.

The Kestrelford Saturday market builds back to full size through April.

---

Question: What is the recommended month to visit the Chinese rice farms?

Answer using only the documents above, and name the file you used.
======================================================================

I do not have enough information to answer this question.

Sources retrieved: guide_givens_mill.md, guide_marchwood.md, guide_seasons.md, guide_thornby_wells.md

0 model calls this session, 1 served from cache```