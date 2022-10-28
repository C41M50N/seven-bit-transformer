
import itertools
from typing import List, Tuple

def generate_bit_combos (n: int) -> List[Tuple[int]]:
    return [tuple(x) for x in itertools.product((0,1), repeat=n)]

def generate_SOP (n: int, bit_combos: List[Tuple[int]]) -> List[str]:
    SOP = []
    for bits in bit_combos:
        s = "("
        for i, bit in enumerate(bits):
            var = f"S{n-(i+1)}"
            if bit == 0:
                s += f"NOT({var})"
            elif bit == 1:
                s += var

            if i != n-1:
                s += " AND "
                
        s += ")"
        SOP.append(s)

    return SOP

def generate_POS (n: int, bit_combos: List[Tuple[int]]) -> List[str]:
    POS = []
    for bits in bit_combos:
        s = "("
        for i, bit in enumerate(bits):
            var = f"S{n-(i+1)}"
            if bit == 0:
                s += var
            elif bit == 1:
                s += f"NOT({var})"

            if i != n-1:
                s += " OR "
        
        s += ")"
        POS.append(s)

    return POS


if __name__ == '__main__':
    print(generate_bit_combos(4))
    print(generate_SOP(4, generate_bit_combos(4)))
    print(generate_POS(4, generate_bit_combos(4)))
