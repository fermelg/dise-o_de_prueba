"""calculator.py
Módulo simple para demostrar pruebas unitarias.
"""
from typing import List, Optional

def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide a entre b y levanta ZeroDivisionError si b == 0."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

def mean(values: List[float]) -> Optional[float]:
    """Promedio de una lista. Devuelve None si está vacía."""
    if not values:
        return None
    return sum(values) / len(values)