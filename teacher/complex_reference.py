"""Эталон учебного контракта. Не использует встроенный complex."""
import math

def _valid(v):
    return (type(v) is list and len(v) == 4
            and all(type(x) in (int, float) and abs(x) <= 10**6
                    and math.isfinite(x) for x in v))

def summa(v):
    if not _valid(v): return 'error'
    a,b,c,d = v
    return [a+c,b+d]

def raznost(v):
    if not _valid(v): return 'error'
    a,b,c,d = v
    return [a-c,b-d]

def multi(v):
    if not _valid(v): return 'error'
    a,b,c,d = v
    return [a*c-b*d,a*d+b*c]

def divide(v):
    if not _valid(v): return 'error'
    a,b,c,d = v
    denominator = c*c+d*d
    if denominator < 1e-12: return 'error'
    return [(a*c+b*d)/denominator,(b*c-a*d)/denominator]
