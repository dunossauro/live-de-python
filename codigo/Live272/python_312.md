# Interpretador adaptativo 3.12

TODO: Adicionar os diferenciais da DSL

## O que é diferente?

Na inicialização do frame `init_code` o processo de quickening já é executado.

```c
// codeobject.c
static void
init_code(PyCodeObject *co, struct _PyCodeConstructor *con)
{
// ...
    co->_co_firsttraceable = entry_point;
    _PyCode_Quicken(co);  // 449: aqui!
    notify_code_watchers(PY_CODE_EVENT_CREATE, co);
}
```

O que faz com que as super instruções já sejam criadas no início da operação. O mecanismo de cache também já é ativado nesse momento:

```python
>>> def add(x, y): return x + y
... 
>>> from dis import dis
>>> 
>>> dis(add, adaptive=True, show_caches=True)
  1           0 RESUME                   0
              2 LOAD_FAST__LOAD_FAST     0 (x)
              4 LOAD_FAST                1 (y)
              6 BINARY_OP                0 (+)
              8 CACHE                    0 (counter: 17)
             10 RETURN_VALUE
```

O contador nesse caso é referente a operação `BINARY_OP`. Que levará as chamadas de `counter` em conta para especializar a operação.

---

Os casos de `TARGET` foram movidos para `generated_cases.c.h`:

```c
        TARGET(BINARY_OP) {
            PREDICTED(BINARY_OP);
            static_assert(INLINE_CACHE_ENTRIES_BINARY_OP == 1, "incorrect cache size");
            PyObject *rhs = stack_pointer[-1];
            PyObject *lhs = stack_pointer[-2];
            PyObject *res;
			// ...
            _PyBinaryOpCache *cache = (_PyBinaryOpCache *)next_instr;
            if (ADAPTIVE_COUNTER_IS_ZERO(cache->counter)) {  // aqui!
                next_instr--;
                _Py_Specialize_BinaryOp(lhs, rhs, next_instr, oparg, &GETLOCAL(0));
                DISPATCH_SAME_OPARG();
            }
			//...
        }
```

Quando o counter decrementar o suficiente a otimização será feita!
