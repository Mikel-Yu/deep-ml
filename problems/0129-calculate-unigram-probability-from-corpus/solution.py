def unigram_probability(corpus: str, word: str) -> float:
    # Your code here
    corpus = corpus.split()
    count = corpus.count(word)
    length = len(corpus)
    return count / length