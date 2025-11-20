from app.core.ref import ref_with_steps
from fractions import Fraction
def test_ref_simple():
    A = [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]]
    R, steps = ref_with_steps(A)
    assert R[0][0] == 1
