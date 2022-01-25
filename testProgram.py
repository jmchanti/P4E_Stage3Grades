import io
from random import randint
import random
from unittest.mock import Mock
import gradeCalculator

def test_gradeCalculator_prints_Bad_score_with_nonNumeric(capfd, monkeypatch):
    score = 'knjgjkkjn'
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('Bad score')
    assert out == expected
def test_gradeCalculator_prints_Bad_score_with_low_score(capfd, monkeypatch):
    score = -.02
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('Bad score')
    assert out == expected
def test_gradeCalculator_prints_Bad_score_with_high_score(capfd, monkeypatch):
    score = randint(101, 1000)/100
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('Bad score')
    assert out == expected
 
def test_gradeCalculator_prints_A_score_with_above_9(capfd, monkeypatch):
    score = randint(900, 1000)/1000
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('A')
    assert out == expected
 
def test_gradeCalculator_prints_B_score_with_above_8(capfd, monkeypatch):
    score = randint(8000, 8999)/10000
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('B')
    assert out == expected
def test_gradeCalculator_prints_C_score_with_above_7(capfd, monkeypatch):
    score = randint(7000, 7999)/10000
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('C')
    assert out == expected
def test_gradeCalculator_prints_D_score_with_above_6(capfd, monkeypatch):
    score = randint(6000, 6999)/10000
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('D')
    assert out == expected
def test_gradeCalculator_prints_F_score_with_below_6(capfd, monkeypatch):
    score = randint(0, 5999)/10000
    input = [score]
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    gradeCalculator.calculateGrade()

    out, err = capfd.readouterr()
    expected = 'Calculating Grade\n{}\n'.format('F')
    assert out == expected