#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from sum_series import Series

def test_term():
    """Тест вычисления членов ряда."""
    s = Series(x=0.35)
    
    # Проверяем первые несколько членов
    assert math.isclose(s._term(0), 0.35, rel_tol=1e-9)
    assert math.isclose(s._term(1), 0.35**3 / 3, rel_tol=1e-9)
    assert math.isclose(s._term(2), 0.35**5 / 5, rel_tol=1e-9)
    print("✓ test_term пройден")

def test_ex_value():
    """Тест контрольного значения."""
    s = Series(x=0.35)
    expected = 0.5 * math.log((1 + 0.35) / (1 - 0.35))
    assert math.isclose(s.ex_value(), expected, rel_tol=1e-9)
    print("✓ test_ex_value пройден")

def test_calculate_single_thread():
    """Тест однопоточного вычисления."""
    s = Series(x=0.35, eps=1e-7)
    result = s.calculate(num_threads=1)
    expected = s.ex_value()
    assert math.isclose(result, expected, rel_tol=1e-6)
    print("✓ test_calculate_single_thread пройден")

def test_calculate_multi_thread():
    """Тест многопоточного вычисления."""
    s = Series(x=0.35, eps=1e-7)
    result = s.calculate(num_threads=4)
    expected = s.ex_value()
    assert math.isclose(result, expected, rel_tol=1e-6)
    print("✓ test_calculate_multi_thread пройден")

def test_str_method():
    """Тест строкового представления."""
    s = Series(x=0.35, eps=1e-7)
    string = str(s)
    assert "Исходный ряд" in string
    assert "x = 0.35" in string
    assert "epsilon = 1e-07" in string
    assert "0.5 * ln((1+x)/(1-x))" in string
    print("✓ test_str_method пройден")

def run_all_tests():
    """Запуск всех тестов."""
    test_term()
    test_ex_value()
    test_calculate_single_thread()
    test_calculate_multi_thread()
    test_str_method()
    print("\nВсе тесты пройдены успешно!")

if __name__ == "__main__":
    run_all_tests()
