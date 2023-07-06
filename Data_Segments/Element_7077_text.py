# 7077  Description format code                                 [B]

#      Desc: Code specifying the format of a description.
#      Repr: an..3
#      Code Values: 

__description_name_code = (
# A
"""
Free-form long description
Long description of an item in free form.
"""
,
# B
"""
Code and text
Description of an item in coded and free form text.
"""
,
# C
"""
Code (from industry code list)
Description of an item in coded format.
"""
,
# D
"""
Free-form price look up
Price look-up description of a product for point of sale
        receipts.
"""
,
# E
"""
Free-form short description
Short description of an item in free form.
"""
,
# F
"""
Free-form
Description of an item in free form text.
"""
,
# S
"""
Structured (from industry code list)
Description of an item in a structured format.
"""
,
# X
"""
Semi-structured (code + text)
Description of an item in a coded and free text format.
"""
)

def get_description(char):
    char = char.lower()
    if char == 'a':
        return __description_name_code[0]
    elif char == 'b':
        return __description_name_code[1]
    elif char == 'c':
        return __description_name_code[2]
    elif char == 'd':
        return __description_name_code[3]
    elif char == 'e':
        return __description_name_code[4]
    elif char == 'f':
        return __description_name_code[5]
    elif char == 's':
        return __description_name_code[6]
    elif char == 'x':
        return __description_name_code[7]
    else:
        return ''
