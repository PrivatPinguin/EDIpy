#   4453  Text function, coded

#   Desc: Code specifying how to handle the text.

#   Repr: an..3
__description_name_code = (
"""
1 Text for subsequent use
The occurrence of this text does not affect message
processing.
"""
,
"""
2 Text replacing missing code
Text description of a coded data item for which there is
no currently available code.
"""
,
"""
3 Text for immediate use
Text must be read before actioning message.
"""
,
"""
4 No action required
Pass text on to later recipient.
"""
)

def get_description(id_text):
    id = int(id_text)-1
    try:
        return __description_name_code[id]
    except:
        return __description_name_code[-1]

# print(get_description('5'))