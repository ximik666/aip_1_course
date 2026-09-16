"""Публичные тесты. Для студенческой проверки замените два импорта."""
import copy
import math
import random
import unittest
from teacher import complex_reference as c
from teacher import matrix_reference as m

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

class MatrixTests(unittest.TestCase):
    def test_add(self): self.assertEqual(m.add([[1,2]],[[3,4]]),[[4,6]])
    def test_subtract(self): self.assertEqual(m.subtract([[1,2]],[[3,4]]),[[-2,-2]])
    def test_product(self): self.assertEqual(m.matmul([[1,2]],[[3],[4]]),[[11]])
    def test_rectangular_product(self):
        self.assertEqual(m.matmul([[1,2,3],[4,5,6]],[[1,0],[0,1],[1,1]]),[[4,5],[10,11]])
    def test_transpose(self): self.assertEqual(m.transpose([[1,2,3],[4,5,6]]),[[1,4],[2,5],[3,6]])
    def test_transpose_twice(self):
        a=[[1,2,3],[4,5,6]];self.assertEqual(m.transpose(m.transpose(a)),a)
    def test_det_swap(self): self.assertAlmostEqual(m.determinant([[0,2],[3,4]]),-6)
    def test_det_singular(self): self.assertAlmostEqual(m.determinant([[1,2],[2,4]]),0)
    def test_det_scalar(self): self.assertAlmostEqual(m.determinant([[7]]),7)
    def test_rank(self): self.assertEqual(m.rank([[1,2],[2,4]]),1)
    def test_rank_skipped_column(self): self.assertEqual(m.rank([[0,1,2],[0,0,3]]),2)
    def test_rank_zero(self): self.assertEqual(m.rank([[0,0],[0,0]]),0)
    def test_eps_contract(self):
        self.assertEqual(m.rank([[1,0],[0,1e-10]]),1)
        self.assertEqual(m.count_nonzero([[1e-10]]),1)
    def test_norm(self): self.assertEqual(m.norm1([[-1,2],[3,-4]]),6)
    def test_nonzero(self): self.assertEqual(m.count_nonzero([[0,2],[3,0]]),2)
    def test_invalid(self):
        for value in (None,[],[[]],[[1],[2,3]],[[True]],[['2']],[[float('nan')]],
                      [[float('inf')]],[[1001]],[[0]]*21,[[0]*21]):
            for fn in (m.transpose,m.rank,m.determinant,m.norm1,m.count_nonzero):
                with self.subTest(value=value,operation=fn.__name__):
                    with self.assertRaises(ValueError):fn(value)
    def test_incompatible(self):
        for fn in (m.add,m.subtract,m.matmul):
            with self.assertRaises(ValueError):fn([[1,2]],[[1,2,3]])
        with self.assertRaises(ValueError):m.determinant([[1,2]])
    def test_preserve_input(self):
        a=[[0,2],[3,4]];saved=copy.deepcopy(a)
        for fn in (m.transpose,m.rank,m.determinant,m.norm1,m.count_nonzero):
            fn(a);self.assertEqual(a,saved)
        for fn in (m.add,m.subtract,m.matmul):
            fn(a,a);self.assertEqual(a,saved)
    def test_identity_product(self):
        a=[[1,2],[3,4]];self.assertEqual(m.matmul(a,[[1,0],[0,1]]),a)
    def test_independent_determinants(self):
        rng=random.Random(8)
        for _ in range(50):
            a,b,c,d,e,f,g,h,i=[rng.randint(-5,5) for _ in range(9)]
            expected=a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
            self.assertTrue(math.isclose(m.determinant([[a,b,c],[d,e,f],[g,h,i]]),expected,abs_tol=1e-7))

if __name__=='__main__':unittest.main()
