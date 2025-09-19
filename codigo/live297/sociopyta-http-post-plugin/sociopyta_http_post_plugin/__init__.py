import pluggy

hookimpl = pluggy.HookimplMarker('sociopyta')

@hookimpl
def config(config_file):
    URL = input('digite sua URL: ')

@hookimpl
def post(text: str, images, config):
    return 'post', 'URL'
