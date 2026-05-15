import re
from collections import Counter

text = """
Artificial Intelligence is transforming the world. It helps computers perform tasks
that normally require human intelligence. AI is used in healthcare, education,
transportation, banking, and entertainment. Text summarization is one important
application of AI. It reduces long text into short and meaningful summaries.
"""

sentences = re.split(r'(?<=[.!?]) +', text.strip())
words = re.findall(r'\w+', text.lower())

stopwords = {"is", "the", "and", "in", "it", "that", "to", "of", "a", "into"}
freq = Counter(word for word in words if word not in stopwords)

scores = {}
for sentence in sentences:
    sentence_words = re.findall(r'\w+', sentence.lower())
    scores[sentence] = sum(freq.get(word, 0) for word in sentence_words)

summary = sorted(scores, key=scores.get, reverse=True)[:2]

print("Original Text:")
print(text.strip())

print("\nSummary:")
print(" ".join(summary))
