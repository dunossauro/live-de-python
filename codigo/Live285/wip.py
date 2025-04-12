from hypothesis import given
from hypothesis import strategies as st


def add(x, y):
    return x + y
    

@given(
    x=st.integers(
        min_value=-100, max_value=573
    ).filter(lambda x: x % 2 == 1),
    y=st.integers(min_value=379).map(lambda y: y ** 3)
)
def test_add_comutativo(x, y):
    print(x, y)
    assert add(x, y) == add(y, x)
