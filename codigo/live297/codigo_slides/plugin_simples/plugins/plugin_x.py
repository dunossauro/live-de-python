import pluggy

hookimpl = pluggy.HookimplMarker('projeto')

@hookimpl
def parse_data(data: str) -> str:
    print('Plugin X!')
    return 'X'
