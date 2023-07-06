    #   Change indicators

    #     a plus sign (+)    for an addition
    #     an asterisk (*)    for an amendment to structure
    #     a hash sign (#)    for changes to names
    #     a vertical bar (|) for changes to text for descriptions and
    #                        notes
    #     a minus sign (-)   for marked for deletion (within either
    #                        batch and interactive messages)
    #     a X sign (X)       for marked for deletion (within both batch
    #                        and interactive messages)

    #  3045  Party name format code                                  [C]

    #  Desc: Code specifying the representation of a party name.
    #  Repr: an..3
    #  Code Values: 


__description_name_code = (
"""
Name components in sequence as defined in description below
Name component:
    1: Family name. Name component 
    2: Given name or initials. Name component 
    3: Given name or initials. Name component 
    4: Maiden name. Name component
    5: Title Group of name components transmitted in
sequence with name component 1 transmitted first. 
The maiden name is the family name given at birth of a
female. Other names are self-explanatory.

"""
,
"""
Name component sequence 2, sequence as defined in
description Name component:
    1: paternal name; name component 
    2: maternal name; name component 
    3: given name or initial(s); name component 
    4: middle name or initial(s); name component 
    5: name suffix.

"""
,
"""
Name components in the sequence as defined in definition
Name component 1: Qualification
Name component 2: First part of the name
Name component 3: Second part of the name.
"""
)

def get_description(postition):
    postition = int(postition)
    postition -= 1
    #global description_name_code
    try:
        return __description_name_code[postition]
    except:
        return ''

# print(get_description(380))
