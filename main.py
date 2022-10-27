
# 4 variable input = 2^4 = 16
INPUTS = {
    0:  [ (0,0,0,0), "(NOT(S3) AND NOT(S2) AND NOT(S1) AND NOT(S0))", "(S3 AND S2 AND S1 AND S0)" ],
    1:  [ (0,0,0,1), "(NOT(S3) AND NOT(S2) AND NOT(S1) AND S0)", "(S3 AND S2 AND S1 AND NOT(S0))" ],
    2:  [ (0,0,1,0), "(NOT(S3) AND NOT(S2) AND S1 AND NOT(S0))", "(S3 AND S2 AND NOT(S1) AND S0)" ],
    3:  [ (0,0,1,1), "(NOT(S3) AND NOT(S2) AND S1 AND S0)", "(S3 AND S2 AND NOT(S1) AND NOT(S0))" ],
    4:  [ (0,1,0,0), "(NOT(S3) AND S2 AND NOT(S1) AND NOT(S0))", "(S3 AND NOT(S2) AND S1 AND S0)" ],
    5:  [ (0,1,0,1), "(NOT(S3) AND S2 AND NOT(S1) AND S0)", "(S3 AND NOT(S2) AND S1 AND NOT(S0))" ],
    6:  [ (0,1,1,0), "(NOT(S3) AND S2 AND S1 AND NOT(S0))", "(S3 AND NOT(S2) AND NOT(S1) AND S0)" ],
    7:  [ (0,1,1,1), "(NOT(S3) AND S2 AND S1 AND S0)", "(S3 AND NOT(S2) AND NOT(S1) AND NOT(S0))" ],
    8:  [ (1,0,0,0), "(S3 AND NOT(S2) AND NOT(S1) AND NOT(S0))", "(NOT(S3) AND S2 AND S1 AND S0)" ],
    9:  [ (1,0,0,1), "(S3 AND NOT(S2) AND NOT(S1) AND S0)", "(NOT(S3) AND S2 AND S1 AND NOT(S0))" ],
    10: [ (1,0,1,0), "(S3 AND NOT(S2) AND S1 AND NOT(S0))", "(NOT(S3) AND S2 AND NOT(S1) AND S0)" ],
    11: [ (1,0,1,1), "(S3 AND NOT(S2) AND S1 AND S0)", "(NOT(S3) AND S2 AND NOT(S1) AND NOT(S0))" ],
    12: [ (1,1,0,0), "(S3 AND S2 AND NOT(S1) AND NOT(S0))", "(NOT(S3) AND NOT(S2) AND S1 AND S0)" ],
    13: [ (1,1,0,1), "(S3 AND S2 AND NOT(S1) AND S0)", "(NOT(S3) AND NOT(S2) AND S1 AND NOT(S0))" ],
    14: [ (1,1,1,0), "(S3 AND S2 AND S1 AND NOT(S0))", "(NOT(S3) AND NOT(S2) AND NOT(S1) AND S0)" ],
    15: [ (1,1,1,1), "(S3 AND S2 AND S1 AND S0)", "(NOT(S3) AND NOT(S2) AND NOT(S1) AND NOT(S0))" ],
}

OUTPUTS = [
    #a b c d e f g
    (1,1,1,1,1,1,0),
    (0,1,1,0,0,0,0),
    (1,1,0,1,1,0,1),
    (1,1,1,1,0,0,1),
    (0,1,1,0,0,1,1),
    (1,0,1,1,0,1,1),
    (1,0,1,1,1,1,1),
    (1,1,1,0,0,0,0),
    (1,1,1,1,1,1,1),
    (1,1,1,1,0,1,1),
    (1,1,1,0,1,1,1),
    (0,0,1,1,1,1,1),
    (1,0,0,1,1,1,0),
    (0,1,1,1,1,0,1),
    (1,0,0,1,1,1,1),
    (1,0,0,0,1,1,1),
]

O_a = [x[0] for x in OUTPUTS]
O_b = [x[1] for x in OUTPUTS]
O_c = [x[2] for x in OUTPUTS]
O_d = [x[3] for x in OUTPUTS]
O_e = [x[4] for x in OUTPUTS]
O_f = [x[5] for x in OUTPUTS]
O_g = [x[6] for x in OUTPUTS]

LETTERS = ["a", "b", "c", "d", "e", "f", "g"]
OUTS = [O_a, O_b, O_c, O_d, O_e, O_f, O_g]

print("################################")
print("Canonical SOP (Sum of Products)")
print("################################")
for i, out in enumerate(OUTS):
    var = LETTERS[i]
    s = f"{var} <= not( "
    for j, x in enumerate(out):
        if x == 1:
            s += INPUTS[j][1]
            s += " OR "
    s += ")"
    print(f"{s};")

print("")

print("################################")
print("Canonical POS (Product of Sums)")
print("################################")
for i, out in enumerate(OUTS):
    var = LETTERS[i]
    s = f"{var} <= not( "
    for j, x in enumerate(out):
        if x == 0:
            s += str(INPUTS[j][2]).replace("AND", "OR")
            s += " AND "
    s += ")"
    print(f"{s};")
