import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    if not scores:
        return []

    max_score = max(scores)
    exp_scores = [math.exp(score - max_score) for score in scores]
    denominator = sum(exp_scores)

    return [exp_score / denominator for exp_score in exp_scores]