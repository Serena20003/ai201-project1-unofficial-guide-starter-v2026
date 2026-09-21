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