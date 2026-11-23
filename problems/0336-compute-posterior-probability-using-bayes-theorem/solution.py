def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
    """
    Calculate posterior probabilities using Bayes' Theorem.
    
    Args:
        priors: Prior probabilities P(H_i) for each hypothesis
        likelihoods: Likelihoods P(E|H_i) for each hypothesis
        
    Returns:
        Posterior probabilities P(H_i|E) for each hypothesis
    """
    posteriors = []
    denominator = sum(likelihood * prior for prior, likelihood in zip(priors, likelihoods))

    for prior, likelihood in zip(priors, likelihoods):
        posteriors.append(prior * likelihood / denominator)
    
    return posteriors
