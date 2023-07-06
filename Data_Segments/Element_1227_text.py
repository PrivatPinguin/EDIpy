    #  1227  Calculation sequence code                               [B]

    #  Desc: Code specifying a calculation sequence.
    #  Repr: an..3
    #  Code Values: 


__description_name_code = (
"""
First step of calculation
Code specifying the first step of a calculation.
"""
,
"""
Second step of calculation
Code specifying the second step of a calculation.
"""
,
"""
Third step of calculation
Code specifying the third step of a calculation.
"""
,
"""
Fourth step of calculation
Code specifying the fourth step of a calculation.
"""
,
"""
Fifth step of calculation
Code specifying the fifth step of a calculation.
"""
,
"""
Sixth step of calculation
Code specifying the sixth step of a calculation.
"""
,
"""
Seventh step of calculation
Code specifying the seventh step of a calculation.
"""
,
"""
Eighth step of calculation
Code specifying the eighth step of a calculation.
"""
,
"""
Ninth step of calculation
Code specifying the ninth step of a calculation.
""")

def get_description(position):
    position = int(position)
    position -= 1
    #global description_name_code
    try:
        return __description_name_code[position]
    except:
        return ''