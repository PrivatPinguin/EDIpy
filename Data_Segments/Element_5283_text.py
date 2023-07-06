    #  5283  Duty or tax or fee function code qualifier              [B]

    #  Desc: Code qualifying the function of a duty or tax or fee.
    #  Repr: an..3
    #  Code Values: 

__description_name_code = ("""
Individual duty, tax or fee (Customs item)
Individual duty, tax or fee charged on a single Customs
item line of the goods declaration (CCC).
"""
,
"""
Total of all duties, taxes and fees (Customs item)
Total of all duties, taxes and fees charged on a single
Customs item line of the goods declaration (CCC).
"""
,
"""
Total of each duty, tax or fee type (Customs declaration)
Total of each duty, tax or fee charged on the goods
declaration (CCC).
"""
,
"""
Total of all duties, taxes and fee types (Customs
declaration)
Total of all duties, taxes and fees charged on the goods
declaration (CCC).
"""
,
"""
Customs duty
Duties laid down in the Customs tariff to which goods
are liable on entering or leaving the Customs territory
(CCC).
"""
,
"""
Fee
Charge for services rendered.
"""
,
"""
Tax
Contribution levied by an authority.
"""
,
"""
Tax related information
Code specifying information related to tax.
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

# print(get_description(3))
