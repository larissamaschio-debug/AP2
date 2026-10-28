from unittest import result

from calculadora import calc_soma, soma, sub, votacao

def test_soma():
    result = soma(2,1)
    assert result == 3

def test_sub():
    result = sub(2,1)  
    assert result == 1
       
def test_votacao_maior_16():
    result= votacao(18)
    assert result is True

def test_votacao_menor_16():
    result = votacao(15)
    assert result is False 

def test_calc_soma():
    result1 = calc_soma(1, 2, 4)
    result2 = calc_soma(1, 2, 2)
    assert result1 == 6 and result2 == 4

