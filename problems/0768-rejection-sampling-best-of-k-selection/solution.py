def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """

    best_candidates = []

    for candidate, score in zip(candidates, scores):
        max_cand = candidate[0]
        max_score = score[0]
        for c, s in zip(candidate, score):
            if s > max_score:
                max_cand = c
                max_score = s

        best_candidates.append(max_cand)
    return best_candidates