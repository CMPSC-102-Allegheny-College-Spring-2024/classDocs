#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_quad_eqn_roots(
a: float, b: float, c: float) -> float:
    """Calculate roots of quadratic equation."""
    D = (b * b - 4 * a * c) ** 0.5
    x_one = (-b + D) / (2 * a)
    x_two = (-b - D) / (2 * a)
    return x_one, x_two

print(f"{calc_quad_eqn_roots(1,2,1)}")
