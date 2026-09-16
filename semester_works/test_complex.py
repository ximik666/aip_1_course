import copy
import math
import random
import unittest
import semestr_task as c

class ComplexTests(unittest.TestCase):
    def test_add(self): self.assertEqual(c.summa([5,3,6,9]),[11,12])
    def test_subtract(self): self.assertEqual(c.raznost([1,2,3,4]),[-2,-2])
    def test_multiply(self): self.assertEqual(c.multi([1,2,3,4]),[-5,10])
    def test_divide(self):
        for actual,expected in zip(c.divide([1,2,3,4]),[.44,.08]):
            self.assertAlmostEqual(actual,expected)
    def test_invalid(self):
        for value in (None,(),[],[1],[1,2,3,4,5],[True,0,0,0],['1',0,0,0],
                      [float('nan'),0,0,0],[float('inf'),0,0,0],[10**1000,0,0,0]):
            for fn in (c.summa,c.raznost,c.multi,c.divide):
                with self.subTest(value=value,operation=fn.__name__):
                    self.assertEqual(fn(value),'error')
    def test_zero_divisor(self): self.assertEqual(c.divide([1,2,0,0]),'error')
    def test_near_zero_limit(self): self.assertEqual(c.divide([1,2,1e-7,0]),'error')
    def test_inputs_unchanged(self):
        a=[1,2,3,4]
        for fn in (c.summa,c.raznost,c.multi,c.divide):
            fn(a);self.assertEqual(a,[1,2,3,4])
    def test_independent_builtin_oracle(self):
        rng=random.Random(12)
        for _ in range(50):
            a,b,cc,d=[rng.randint(-20,20) for _ in range(4)]
            z,w=complex(a,b),complex(cc,d)
            for fn,expected in ((c.summa,z+w),(c.raznost,z-w),(c.multi,z*w)):
                result=fn([a,b,cc,d])
                self.assertAlmostEqual(result[0],expected.real)
                self.assertAlmostEqual(result[1],expected.imag)
            if w:
                result=c.divide([a,b,cc,d]);expected=z/w
                self.assertAlmostEqual(result[0],expected.real)
                self.assertAlmostEqual(result[1],expected.imag)


if __name__ == "__main__": unittest.main()
