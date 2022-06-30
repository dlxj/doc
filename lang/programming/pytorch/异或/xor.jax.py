

import imp
import jax
import jax.lax as lax
import jax.numpy as jnp
import jax.random as jrandom
import optax  # https://github.com/deepmind/optax

import functools

X = jnp.array([
                [0, 0],
                [0, 1],
                [1, 0],
                [1, 1]
             ], jnp.float32)

# 输入矩阵，维度4*2。

Y = jnp.array([
                [0],
                [1],
                [1],
                [0]
             ], jnp.float32)
# 4*1 输出


# (4*4) . (4*2) = (4*2)
# (4*2) . (2*1) = (4*1) 


key1, key2, key3, key4 = jrandom.split(jrandom.PRNGKey(1999), 4)

W1 = jrandom.normal(key1, (4, 4) )  # 第一层权重
W2 = jrandom.normal(key1, (2, 1))   # 第二层权重

b1 = jrandom.normal(key1, (4, 2))   # 第一层偏置
b2 = jrandom.normal(key1, (4, 1))   # 第二层偏置


# https://github.com/google/jax/pull/762

# '''
# This patch adds a function jax.value_and_jacfwd, which is the
# forward-mode version of jax.value_and_grad. It allows returning
# the value of a function in addition to its derivative, so that
# you don't need to evaluate the function twice to get both the
# value and its derivative as you would using plain jax.jacfwd.
# For example:
# >>> import jax, value_and_jacfwd
# >>> def g(x):
# >>>     return (x ** 2).sum()
# >>> dg = jax.value_and_jacfwd(g, has_aux=False)
# >>> y, dg = dg(np.arange(3) * 1.)
# >>> print(f'g(x) = {y}')
# g(x) = 5.0
# >>> print(f'dg(x) = {dg}')
# dg(x) = [0. 2. 4.]
# You can also export auxiliary values using the has_aux=True parameter,
# again by analogy to jax.value_and_grad. For example:
# >>> import jax, value_and_jacfwd
# >>> def f(x):
# >>>     return (x ** 2).sum(), x.sum()
# >>> df = jax.value_and_jacfwd(f, has_aux=True)
# >>> (y, aux), df = df(np.arange(3) * 1.)
# >>> print(f'f(x) = {y}')
# f(x) = 5.0
# >>> print(f'df(x) = {df}')
# df(x) = [0. 2. 4.]
# >>> print(f'aux = {aux}')
# aux = 3.0
# This patch addresses the following Github issue:
#   https://github.com/google/jax/pull/762
# '''

from jax._src.api_util import _argnums_partial

from jax._src.api import (
    _check_callable,
    _ensure_index,
    _check_input_dtype_jacfwd,
    _check_output_dtype_jacfwd,
    _std_basis,
    _unravel_array_into_pytree,
    _dtype
)
from jax._src.api import *


# def _jvp(fun: lu.WrappedFun, primals, tangents, has_aux=False):
#   """Variant of jvp() that takes an lu.WrappedFun."""
#   if (not isinstance(primals, (tuple, list)) or
#       not isinstance(tangents, (tuple, list))):
#     raise TypeError("primal and tangent arguments to jax.jvp must be tuples or lists; "
#                     f"found {type(primals).__name__} and {type(tangents).__name__}.")

#   ps_flat, tree_def = tree_flatten(primals)
#   ts_flat, tree_def_2 = tree_flatten(tangents)
#   if tree_def != tree_def_2:
#     raise TypeError("primal and tangent arguments to jax.jvp must have the same tree "
#                     f"structure; primals have tree structure {tree_def} whereas tangents have "
#                     f"tree structure {tree_def_2}.")
#   for p, t in safe_zip(ps_flat, ts_flat):
#     if core.primal_dtype_to_tangent_dtype(_dtype(p)) != _dtype(t):
#       raise TypeError("primal and tangent arguments to jax.jvp do not match; "
#                       "dtypes must be equal, or in case of int/bool primal dtype "
#                       "the tangent dtype must be float0."
#                       f"Got primal dtype {_dtype(p)} and so expected tangent dtype "
#                       f"{core.primal_dtype_to_tangent_dtype(_dtype(p))}, but got "
#                       f"tangent dtype {_dtype(t)} instead.")
#     if np.shape(p) != np.shape(t):
#       raise ValueError("jvp called with different primal and tangent shapes;"
#                        f"Got primal shape {np.shape(p)} and tangent shape as {np.shape(t)}")

#   if has_aux:
#     flat_fun, out_aux_trees = flatten_fun_nokwargs2(fun, tree_def)
#     main, aux = ad.jvp(flat_fun, has_aux=True)
#     out_primals, out_tangents = main.call_wrapped(ps_flat, ts_flat)
#     aux = aux()
#     out_tree, aux_tree = out_aux_trees()
#     return (tree_unflatten(out_tree, out_primals),
#             tree_unflatten(out_tree, out_tangents)), tree_unflatten(aux_tree, aux)
#   else:
#     flat_fun, out_tree = flatten_fun_nokwargs(fun, tree_def)
#     out_primals, out_tangents = ad.jvp(flat_fun).call_wrapped(ps_flat, ts_flat)
#     return (tree_unflatten(out_tree(), out_primals),
#             tree_unflatten(out_tree(), out_tangents))


# def value_and_jacfwd(fun: Callable, argnums: Union[int, Sequence[int]] = 0,
#            holomorphic: bool = False, has_aux: bool = False) -> Callable:
#   """
#   [Constructed by analogy to value_and_grad -- see help(value_and_grad) for more.]
#   """
#   _check_callable(fun)
#   argnums = _ensure_index(argnums)

#   def jacfun(*args, **kwargs):
#     f = lu.wrap_init(fun, kwargs)
#     f_partial, dyn_args = argnums_partial(f, argnums, args, require_static_args_hashable=False) #require_static_args_hashable=False)  lambda z: f(z, alpha, T)
#     tree_map(partial(_check_input_dtype_jacfwd, holomorphic), dyn_args)
#     if has_aux:
#         pushfwd = partial(_jvp, f_partial, dyn_args, has_aux=True)
#         (y, jac), aux = vmap(pushfwd, out_axes=((None, -1), None))(_std_basis(dyn_args))
#     else:
#         pushfwd = partial(_jvp, f_partial, dyn_args)
#         (y, jac) = vmap(pushfwd, out_axes=(None, -1))(_std_basis(dyn_args))
#     tree_map(partial(_check_output_dtype_jacfwd, holomorphic), y)
#     example_args = dyn_args[0] if isinstance(argnums, int) else dyn_args
#     if has_aux:
#         return (y, aux), tree_map(partial(_unravel_array_into_pytree, example_args, -1), jac)
#     else:
#         return y, tree_map(partial(_unravel_array_into_pytree, example_args, -1), jac)

#   return jacfun
# jax.value_and_jacfwd = value_and_jacfwd  # !!


# def _jacfwd(fun, argnums=0, holomorphic=False, return_value=False):

#   def jacfun(*args, **kwargs):
#     f = lu.wrap_init(fun, kwargs)
#     a = _argnums_partial(f, argnums, args)
#     f_partial, dyn_args = _argnums_partial(f, argnums, args)
#     # holomorphic or tree_map(_check_real_input_jacfwd, dyn_args)
#     pushfwd = partial(jvp, f_partial, dyn_args)
#     y, jac = vmap(pushfwd, out_axes=(None, batching.last))(_std_basis(dyn_args))
#     example_args = dyn_args[0] if isinstance(argnums, int) else dyn_args
#     jac = tree_map(partial(_unravel_array_into_pytree, example_args, -1), jac)
#     if return_value:
#         return jac, y
#     else:
#         return jac

#   return jacfun

# def jacfwd(fun, argnums=0, holomorphic=False):
#   return _jacfwd(fun, argnums, holomorphic, return_value=False)


# def value_and_jacfwd(fun, argnums=0, holomorphic=False):
 
#   jacfun = _jacfwd(fun, argnums, holomorphic, return_value=True)

#   def value_and_jacobian_func(*args, **kwargs):
#       jacobian, value = jacfun(*args, **kwargs)
#       return value, jacobian

#   return value_and_jacobian_func



# def value_and_jacfwd(f, x):
#   pushfwd = functools.partial(jax.jvp, f, (x,))
#   basis = jnp.eye(x.size, dtype=x.dtype)
#   y, jac = jax.vmap(pushfwd, out_axes=(None, 1))((basis,))
#   return y, jac

# def value_and_jacrev(f, x):
#   y, pullback = jax.vjp(f, x)
#   basis = jnp.eye(y.size, dtype=y.dtype)
#   jac = jax.vmap(pullback)(basis)
#   return y, jac

# [ A1, grads1 ] = value_and_jacfwd (jnp.dot, argnums=0)(W1, X) # 同时返回函数值和梯度

f1 = lambda W1, b1, X : jax.nn.sigmoid( jnp.dot(W1, X) + b1 )  # 前向传播

A1 =f1(W1, b1, X)
grads10, grads11 = jax.jacfwd(f1, argnums=(0,1))(W1, b1, X) # 梯度


f2 = lambda W2, b2, A1 : jax.nn.sigmoid( jnp.dot(A1, W2) + b2 )  # 前向传播

A2 =f2(W2, b2, A1)
grads20, grads21 = jax.jacfwd(f2, argnums=(0, 1))(W2, b2, A1)# 梯度


loss = lambda A2, Y : jnp.sum( jnp.abs( A2 - Y ) ** 2, axis=0 )[0]

lss = loss(  A2, Y )
grad_lss = jax.jacfwd(loss, argnums=(0, ))(A2, Y )


# f11 = lambda A1, b1 : A1 + b1

# A11 = f11(A1, b1)
# grads11 = jax.jacfwd(f11, argnums=(0,))(A1, b1)

print( A1 )
print( grads11 )
