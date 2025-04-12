
from hypothesis import given
from hypothesis import strategies as st


def concat(x: list[str], y: list[str]) -> list[str]:
    return x + y


@given(
    x=st.lists(st.text(max_size=10), unique=True),
    y=st.lists(st.text(min_size=1), min_size=1)
)
def test_concat_size(x, y):
    print(x, y)
    assert len(concat(x, y)) == len(x) + len(y)
