import sys
import types
import importlib._bootstrap
# https://github.com/python/cpython/blob/3.6/Lib/importlib/_bootstrap.py#L504
# https://github.com/python/cpython/issues/79362


# O sistema de import
def _import(module_name) -> types.ModuleType | None:
    module = None
    for hook in sys.meta_path:  # Varrer os Hooks
        if spec := hook.find_spec(module_name, None):
            if spec.loader:
                module = spec.loader.create_module(spec)

            if not module:
                module = types.ModuleType(spec.name)

            importlib._bootstrap._init_module_attrs(spec, module)


            if spec.origin is None and spec.submodule_search_locations is not None:
                sys.modules[spec.name] = module

            elif not hasattr(spec.loader, 'exec_module'):
                module = spec.loader.load_module(spec.name)

            else:
                sys.modules[spec.name] = module
                try:
                    spec.loader.exec_module(module)
                except BaseException:
                    try:
                        del sys.modules[spec.name]
                    except KeyError:
                        pass
                    raise

    return module


module = _import('pacote_namespace')

print(module.__dict__)
