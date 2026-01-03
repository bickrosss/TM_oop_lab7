#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from threading import Thread
import math

class Series:
    """
    Класс для вычисления суммы ряда:
    S = Σ [x^(2n+1) / (2n+1)], n = 0 .. ∞
    Контрольное значение: y = 0.5 * ln((1+x)/(1-x))
    """

    def __init__(self, x: float = 0.35, eps: float = 1e-7) -> None:
        self.x = x
        self.eps = eps

    def _term(self, n: int) -> float:
        """
        Вычисление члена ряда для заданного n.
        """
        return (self.x ** (2 * n + 1)) / (2 * n + 1)

    def _worker(self, start: int, step: int, result_list: list, index: int) -> None:
        """
        Потоковая функция для вычисления частичной суммы.
        """
        sum_local = 0.0
        n = start
        a_n = self._term(n)
        count = 0
        
        while abs(a_n) >= self.eps:
            sum_local += a_n
            n += step
            a_n = self._term(n)
            count += 1
            
        result_list[index] = sum_local
        # Для отладки можно раскомментировать:
        # print(f"[Thread {index}] Завершил. Посчитано членов ряда: {count}")

    def calculate(self, num_threads: int = 4) -> float:
        """
        Вычисление суммы ряда с использованием многопоточности.
        """
        threads = []
        results = [0.0] * num_threads
        
        # Создание и запуск потоков
        for i in range(num_threads):
            thread = Thread(target=self._worker, args=(i, num_threads, results, i))
            threads.append(thread)
            thread.start()

        # Ожидание завершения всех потоков
        for thread in threads:
            thread.join()

        # Суммирование результатов всех потоков
        return sum(results)

    def __str__(self) -> str:
        """
        Строковое представление ряда и параметров.
        """
        return (
            "Исходный ряд:\n"
            "S = Σ [x^(2n+1) / (2n+1)],  n = 0 .. ∞\n\n"
            f"Параметры:\n"
            f"x = {self.x}\n"
            f"epsilon = {self.eps}\n\n"
            "Аналитическое выражение суммы:\n"
            "y = 0.5 * ln((1+x)/(1-x))"
        )

    def ex_value(self) -> float:
        """
        Вычисление контрольного значения функции.
        """
        return 0.5 * math.log((1 + self.x) / (1 - self.x))
