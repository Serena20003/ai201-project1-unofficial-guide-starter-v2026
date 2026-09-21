"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

  ✗ "What are good dining halls?"          — no right answer
  ✓ "What do students say about wait times at Commons during lunch?"

Fill in `QUESTIONS` below. `expects` is a word or short phrase you'd expect a
correct answer to contain — you'll use it in unit 2 when you build a scorer,
and having written it now means you decided what "correct" meant before you saw
any results.

`OUT_OF_SCOPE` holds five questions your documents clearly don't cover. You
need these in Milestone 4 to find where your relevance cutoff belongs, and
again in unit 2, where `run_eval.py` runs them through the gate and writes what
happened into your run log — that's the evidence for criterion 3.

Swap them for your own if you like. Keep five of them either way: criterion 3
names a target of "4 of 5", and four of three is not a thing.
"""

QUESTIONS = [
    # {"question": "...", "expects": "..."},
    {"question": "Which towns are the worst when it comes to getting around with limited mobility?", "expects": "Kestrelford, Halden Bay, and Corry Vale."}, # guide_accessibility.md ## Difficult
    {"question": "When is the busy season for Kestrelford?", "expects": "The months between May and September, especially August."}, # guide_kestrelford.md - ## Where to stay and ## When to go
    {"question": "Do I need to bring cash or can I pay with card mostly when I visit Givens Mill?", "expects": "Cards are accepted almost everywhere now, but cash is still useful at the market and in smaller places"}, # guide_eating.md ## Practical and guide_givens_mill.md ## Practical notes
    {"question": "What is the best season to visit Brightwater?", "expects": "Spring, especially late May."}, # guide_seasons.md ## Spring, March to May and guide_brightwater.md ## When to go
    {"question": "Does Elder Ness have an airport?", "expects": "No."}, # guide_brightwater.md ## Getting there and guide_marchwood.md ## Getting there
]

# Questions from a different world entirely. Your gate should refuse all five.
#
# There are five of these because criterion 3 in criteria.md names a target of
# "at least 4 of 5" — you need five things to try before you can report 4 of 5.
# `run_eval.py` runs these through retrieval and the gate on every eval and
# records what happened, so criterion 3 has evidence in the run log alongside
# the others. They cost no model calls: a refusal never reaches the model.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended month to visit the Chinese rice farms?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
