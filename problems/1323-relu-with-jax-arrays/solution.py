import jax
import jax.numpy as jnp

def relu(x):
    """Return x with negative entries replaced by 0 (same shape as x)."""

    return jnp.where(x < 0, 0, x)
