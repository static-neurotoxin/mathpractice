#!/usr/bin/env python3
# coding: utf-8

import random

def printSheet(width:int, height:int, operand1:list[int],  operand2:list[int], operator:str) -> None:
    print("\n"*4)
    print("Name:")
    print("-" * 40)
    print("\n"*4)
    print("Date:")
    print("-" * 40)
    print("\n"*4)

    for y in range(0, height):
        line1 = "    "
        line2 = "    "
        line3 = "    "
        for x in range(0, width):
            num1 = random.choice(operand1)
            num2 = random.choice(operand2)
            op = random.choice(operator)
            if op == "÷":
                a = num1 * num2
                b = num2
            else:
                a = max(num1, num2)
                b = min(num1, num2)
            line1 += f"  {a:8d}    "
            line2 += f"{op} {b:8d}    "
            line3 += f"----------    "
        print(line1)
        print(line2)
        print(line3)
        print("\n"*4)
#printSheet(5, 5, range(20,99), range(2,9), "++++++--×")
printSheet(5, 5, range(20,88), [7,9,11,13], "+-")

# printSheet(5, 5, 2, "+-×÷")
# printSheet(5, 5, 1, "++++++--×")