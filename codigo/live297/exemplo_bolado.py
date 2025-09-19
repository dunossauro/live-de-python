import pluggy


# === Spec
hookspec = pluggy.HookspecMarker('app_bolado')

class BoladoSpec:
    @hookspec
    def validate(self, data): ...


# === Plugins
hookimpl = pluggy.HookimplMarker('app_bolado')

class PluginBolado:
    @hookimpl(trylast=True)
    def validate(self, data):
        print(f'Bolado - {data}')
        return data


class PluginMaisBolado:
    @hookimpl(wrapper=True, specname='validate')
    def validate_wrap(self, data):
        print('Antes')
        yield data
        print('Depois')

    @hookimpl(specname='validate')
    def outro_nome(self, data):
        print(f'MaisBolado - {data}')
        return data


# === Manager

# Manager
pm = pluggy.PluginManager('app_bolado')

# Aplica spec
pm.add_hookspecs(BoladoSpec)

# Regista os plguins
pm.register(PluginBolado())
pm.register(PluginMaisBolado())

# pm.hook.validate.call_historic(kwargs={'data': 'a'})

def before_hook(hook_name, hook_impls, kwargs):
    print(f'Antes do hook "{hook_name}". Argumentos: {kwargs}')


def after_hook(result, hook_name, hook_impls, kwargs):
    print(f'Depois do hook "{hook_name}". Resultado: {result}')


pm.add_hookcall_monitoring(before_hook, after_hook)

# Proxeia as chamadas
pm.hook.validate(data='Live de Python')



def test_hook_validate():
    plugin = PluginBolado()
    result = plugin.validate(data='test')

    assert result == 'test'
