"""Эталон для небольших учебных матриц. eps — абсолютный порог."""
import math
EPS = 1e-9

def shape(a):
    if type(a) is not list or not 1 <= len(a) <= 20:
        raise ValueError('ожидается 1..20 строк')
    if any(type(row) is not list for row in a):
        raise ValueError('строки должны быть списками')
    n = len(a[0])
    if not 1 <= n <= 20 or any(len(row) != n for row in a):
        raise ValueError('ожидается прямоугольная матрица с 1..20 столбцами')
    for row in a:
        for x in row:
            if type(x) not in (int,float) or abs(x) > 1000 or not math.isfinite(x):
                raise ValueError('неверный элемент')
    return len(a),n

def _same(a,b):
    m,n=shape(a)
    if shape(b)!=(m,n): raise ValueError('разные размеры')
    return m,n

def add(a,b):
    m,n=_same(a,b)
    return [[a[i][j]+b[i][j] for j in range(n)] for i in range(m)]

def subtract(a,b):
    m,n=_same(a,b)
    return [[a[i][j]-b[i][j] for j in range(n)] for i in range(m)]

def matmul(a,b):
    m,n=shape(a);q,p=shape(b)
    if n!=q: raise ValueError('несовместимые размеры')
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(p)] for i in range(m)]

def transpose(a):
    m,n=shape(a)
    return [[a[i][j] for i in range(m)] for j in range(n)]

def norm1(a):
    m,n=shape(a)
    return max(sum(abs(a[i][j]) for i in range(m)) for j in range(n))

def count_nonzero(a):
    shape(a)
    return sum(x != 0 for row in a for x in row)

def _eliminate(a):
    m,n=shape(a)
    rows=[[float(x) for x in row] for row in a]
    r=0;sign=1;pivots=[]
    for col in range(n):
        if r==m: break
        pivot=max(range(r,m), key=lambda i:abs(rows[i][col]))
        if abs(rows[pivot][col])<=EPS: continue
        if pivot!=r:
            rows[r],rows[pivot]=rows[pivot],rows[r]
            sign=-sign
        value=rows[r][col];pivots.append(value)
        for i in range(r+1,m):
            factor=rows[i][col]/value
            rows[i][col]=0.0
            for j in range(col+1,n):
                rows[i][j]-=factor*rows[r][j]
        r+=1
    return r,sign,pivots

def rank(a):
    return _eliminate(a)[0]

def determinant(a):
    m,n=shape(a)
    if m!=n: raise ValueError('нужна квадратная матрица')
    r,sign,pivots=_eliminate(a)
    return float(sign*math.prod(pivots)) if r==n else 0.0
