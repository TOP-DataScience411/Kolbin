def orth_triangle(*, cathetus1=0, cathetus2=0, hypotenuse=0) -> float | None:
    if hypotenuse == 0 and cathetus1 > 0 and cathetus2 > 0:
        return (cathetus1**2 + cathetus2**2) ** 0.5
    elif hypotenuse > 0 and cathetus1 > 0 and cathetus2 == 0 and cathetus1 < hypotenuse:
        return (hypotenuse**2 - cathetus1**2) ** 0.5
    elif hypotenuse > 0 and cathetus2 > 0 and cathetus1 == 0 and cathetus2 < hypotenuse:
        return (hypotenuse**2 - cathetus2**2) ** 0.5
    else:
        return None
        
        
# >>> orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# >>> orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# >>> print(orth_triangle(cathetus2=9, hypotenuse=3))
# None