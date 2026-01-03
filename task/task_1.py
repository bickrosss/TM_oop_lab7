#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import time
from sum_series import Series

if __name__ == "__main__":
    # Создание объекта ряда с параметрами варианта 18
    series = Series(x=0.35, eps=1e-7)

    # Вывод информации о ряде
    print(series)

    # Многопоточное вычисление
    start_time = time()
    s_numeric = series.calculate(num_threads=4)
    end_time = time()

    # Контрольное значение
    s_exact = series.ex_value()

    # Вывод результатов
    print("\nРезультаты вычислений:")
    print(f"Сумма ряда (численно)     = {s_numeric:.10f}")
    print(f"Контрольное значение y    = {s_exact:.10f}")
    print(f"Абсолютная погрешность    = {abs(s_numeric - s_exact):.2e}")
    print(f"Требуемая точность ε      = {series.eps:.1e}")
    print(f"Время вычисления (4 потока) = {end_time - start_time:.6f} сек")

    # Проверка точности
    if abs(s_numeric - s_exact) < series.eps:
        print("\n✓ Точность достигнута: |S - y| < ε")
    else:
        print("\n✗ Точность не достигнута: |S - y| ≥ ε")
