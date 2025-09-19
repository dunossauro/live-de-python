from pluggy import PluginManager
from plugins import plugin_x, plugin_y

pm = PluginManager('projeto')

pm.register(plugin_x)
pm.register(plugin_y)

results = pm.hook.parse_data(data='')

print(results)
