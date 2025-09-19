import pluggy

hookspec = pluggy.HookspecMarker('projeto')


@hookspec
def parse_data(data: str) -> str: ...
