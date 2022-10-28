
#? CONFIG
INPUT_BITS = 5
OUTPUTS = [ # 2^5 = 32 distinct outputs
#    a1 b1 c1 d1 e1 f1 g1 h1 a2 b2 c2 d2 e2 f2 g2 
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0), # 1.0
    (0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0), # 1.1
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1), # 1.2
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1), # 1.3
    (0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1), # 1.4
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1), # 1.5
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1), # 1.6
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0), # 1.7
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1), # 1.8
    (0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1), # 1.9
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0), # 2.0
    (1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0), # 2.1
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1), # 2.2
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1), # 2.3
    (1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1), # 2.4
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1), # 2.5
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1), # 2.6
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0), # 2.7
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 2.8
    (1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1), # 2.9
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0), # 3.0
    (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0), # 3.1
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1), # 3.2
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1), # 3.3
    (1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1), # 3.4
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1), # 3.5
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1), # 3.6
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0), # 3.7
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 3.8
    (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1), # 3.9
    (0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0), # 4.0
    (0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0), # 4.1
]

O_a1 = [x[0] for x in OUTPUTS]
O_b1 = [x[1] for x in OUTPUTS]
O_c1 = [x[2] for x in OUTPUTS]
O_d1 = [x[3] for x in OUTPUTS]
O_e1 = [x[4] for x in OUTPUTS]
O_f1 = [x[5] for x in OUTPUTS]
O_g1 = [x[6] for x in OUTPUTS]
O_h1 = [x[7] for x in OUTPUTS]
O_a2 = [x[8] for x in OUTPUTS]
O_b2 = [x[9] for x in OUTPUTS]
O_c2 = [x[10] for x in OUTPUTS]
O_d2 = [x[11] for x in OUTPUTS]
O_e2 = [x[12] for x in OUTPUTS]
O_f2 = [x[13] for x in OUTPUTS]
O_g2 = [x[14] for x in OUTPUTS]

LETTERS     = ["a1","b1","c1","d1","e1","f1","g1","h1","a2","b2","c2","d2","e2","f2","g2"]
OUTPUT_COLS = [O_a1,O_b1,O_c1,O_d1,O_e1,O_f1,O_g1,O_h1,O_a2,O_b2,O_c2,O_d2,O_e2,O_f2,O_g2]

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
