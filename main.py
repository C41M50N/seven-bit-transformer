
#? CONFIG
INPUT_BITS = 4
OUTPUTS = [ # 2^4 = 16 distinct outputs
#    a b c d e f g
    (1,1,1,1,1,1,0), # 0
    (0,1,1,0,0,0,0), # 1
    (1,1,0,1,1,0,1), # 2
    (1,1,1,1,0,0,1), # 3
    (0,1,1,0,0,1,1), # 4
    (1,0,1,1,0,1,1), # 5
    (1,0,1,1,1,1,1), # 6
    (1,1,1,0,0,0,0), # 7
    (1,1,1,1,1,1,1), # 8
    (1,1,1,1,0,1,1), # 9
    (1,1,1,0,1,1,1), # A
    (0,0,1,1,1,1,1), # b
    (1,0,0,1,1,1,0), # C
    (0,1,1,1,1,0,1), # d
    (1,0,0,1,1,1,1), # E
    (1,0,0,0,1,1,1), # F
]

O_a = [x[0] for x in OUTPUTS]
O_b = [x[1] for x in OUTPUTS]
O_c = [x[2] for x in OUTPUTS]
O_d = [x[3] for x in OUTPUTS]
O_e = [x[4] for x in OUTPUTS]
O_f = [x[5] for x in OUTPUTS]
O_g = [x[6] for x in OUTPUTS]

LETTERS     = ["a", "b", "c", "d", "e", "f", "g"]
OUTPUT_COLS = [O_a, O_b, O_c, O_d, O_e, O_f, O_g]

#? MAIN
from utils import generate_bit_combos, generate_SOP, generate_POS

SOP_vhdl_strings = generate_SOP(n=INPUT_BITS, bit_combos=generate_bit_combos(INPUT_BITS))
print("################################")
print("Canonical SOP (Sum of Products)")
print("################################")
for i, output_col in enumerate(OUTPUT_COLS):
    var = LETTERS[i]
    s = f"{var} <= not( "
    for j, x in enumerate(output_col):
        if x == 1:
            s += SOP_vhdl_strings[j]
            s += " OR "
    s += ")"

    if s.endswith(" OR )"):
        s = s.replace(" OR )", " )")

    if s.endswith("not( )"):
        s = s.replace("not( )", "not( '0' )")

    print(f"{s};")

print("")

POS_vhdl_strings = generate_POS(n=INPUT_BITS, bit_combos=generate_bit_combos(INPUT_BITS))
print("################################")
print("Canonical POS (Product of Sums)")
print("################################")
for i, output_col in enumerate(OUTPUT_COLS):
    var = LETTERS[i]
    s = f"{var} <= not( "
    for j, x in enumerate(output_col):
        if x == 0:
            s += POS_vhdl_strings[j]
            s += " AND "
    s += ")"
    
    if s.endswith(" AND )"):
        s = s.replace(" AND )", " )")

    if s.endswith("not( )"):
        s = s.replace("not( )", "not( '1' )")

    print(f"{s};")
