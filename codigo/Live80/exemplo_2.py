from unittest import TestCase, main
from hypothesis import given
from hypothesis import strategies as st
from typing import Union

def div(x: int, y: int) -> Union[int, float]:
    return x / y


class TestDiv(TestCase):
    @given(
        st.integers(),
        st.integers().filter(lambda val: val > 0)
    )
    def test_div_test_da_explosao(self, x, y):
        print(x, y)
        # self.assertEqual(div(x, y), 0.5)
        div(x, y)


if __name__ == '__main__':
    main()
