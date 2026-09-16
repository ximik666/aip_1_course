import copy
import math
import random
import unittest
import matrix_ops as m

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


if __name__ == "__main__": unittest.main()
