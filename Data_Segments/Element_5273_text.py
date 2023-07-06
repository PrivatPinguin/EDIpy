    #  5273  Duty or tax or fee rate basis code                      [B]

    #  Desc: Code specifying the basis for a duty or tax or fee rate.
    #  Repr: an..12
    #  Code Values: 

__description_name_code = (
"""
Value
(5316) To specify that the applicable rate of duty, tax
or fee is based on the Customs value (CCC).

"""
,
"""     
Weight
To specify that the applicable rate of duty, tax or fee
is based on the weight of the item (CCC).

"""
,
"""    
Quantity
(6060) To specify that the applicable rate of duty, tax
or fee is based on the quantity of the item (CCC).
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