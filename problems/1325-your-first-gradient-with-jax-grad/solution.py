import jax
import jax.numpy as jnp

def f(x):
    return x**3 + 2*x

def df_dx(x):
    """Derivative of f(x) = x**3 + 2x at float x, via jax.grad. Returns float."""
    grad_f = jax.grad(f)
    return float(grad_f(x))
