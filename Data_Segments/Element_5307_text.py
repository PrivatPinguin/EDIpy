    #  5307  Tax or duty or fee payment due date code                [B]

    #  Desc: A code indicating when the duty, tax, or fee payment will be due.
    #  Repr: an..3
    #  Code Values: 




__description_name_code = (
"""
Duty, tax or fee payment due on invoice payment date
Duty, tax or fee payment is due on the date when the
invoice is paid.
"""
,
"""
Duty, tax or fee payment due on invoice issue date
Duty, tax or fee payment is due on the date when the
invoice is issued.
"""
)

def get_description(position):
    position = int(position)
    position -= 1
    #global description_name_code
    try:
        return __description_name_code[position]
    except:
        return ''