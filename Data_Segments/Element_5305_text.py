#   Change indicators

#     a plus sign (+)    for an addition
#     an asterisk (*)    for an amendment to structure
#     a hash sign (#)    for changes to names
#     a vertical bar (|) for changes to text for descriptions and notes
#     a minus sign (-)   for marked for deletion (within either batch and interactive messages)
#     a X sign (X)       for marked for deletion (within both batch and interactive messages)

#  5305  Duty or tax or fee category code                        [B]

#  Desc: Code specifying a duty or tax or fee category.
#  Repr: an..3
#  Code Values: 

__code_id = ('A','AA','AB','AC','AE','B','C','D','E','F','G','H','I','J','L','M','O','S','Z')
__description_name_code = (
"""
Mixed tax rate
Code specifying that the rate is based on mixed tax.
"""
,
"""
Lower rate
Tax rate is lower than standard rate.
"""
,
"""
Exempt for resale
A tax category code indicating the item is tax exempt
when the item is bought for future resale.
"""
,
"""
Value Added Tax (VAT) not now due for payment
A code to indicate that the Value Added Tax (VAT) amount
which is due on the current invoice is to be paid on
receipt of a separate VAT payment request.
"""
,
"""
Value Added Tax (VAT) due from a previous invoice
A code to indicate that the Value Added Tax (VAT) amount
of a previous invoice is to be paid.
"""
,
"""
VAT Reverse Charge
Code specifying that the standard VAT rate is levied
from the invoicee.
"""
,
"""
Transferred (VAT)
VAT not to be paid to the issuer of the invoice but
directly to relevant tax authority.
"""
,
"""
Duty paid by supplier
Duty associated with shipment of goods is paid by the
supplier; customer receives goods with duty paid.

Value Added Tax (VAT) margin scheme - travel agents
Indication that the VAT margin scheme for travel agents
is applied.
"""
,
"""
Exempt from tax
Code specifying that taxes are not applicable.
"""
,
"""
Value Added Tax (VAT) margin scheme - second-hand goods
Indication that the VAT margin scheme for second-hand
goods is applied.
"""
,
"""
Free export item, tax not charged
Code specifying that the item is free export and taxes
are not charged.
"""
,
"""
Higher rate
Code specifying a higher rate of duty or tax or fee.
"""
,
"""
Value Added Tax (VAT) margin scheme - works of art
Margin scheme � Works of art
Indication that the VAT margin scheme for works of art
is applied.
"""
,
"""
Value Added Tax (VAT) margin scheme - collector�s items and
antiques
Indication that the VAT margin scheme for collector�s
items and antiques is applied.
"""
,
"""
VAT exempt for EEA intra-community supply of goods and
services
A tax category code indicating the item is VAT exempt
due to an intra-community supply in the European
Economic Area.
"""
,
"""
Canary Islands general indirect tax
Impuesto General Indirecto Canario (IGIC) is an indirect
tax levied on goods and services supplied in the Canary
Islands (Spain) by traders and professionals, as well as
on import of goods.
"""
,
"""
Tax for production, services and importation in Ceuta and
Melilla
Impuesto sobre la Producci�n, los Servicios y la
Importaci�n (IPSI) is an indirect municipal tax, levied
on the production, processing and import of all kinds of
movable tangible property, the supply of services and
the transfer of immovable property located in the cities
of Ceuta and Melilla.
"""
,
"""
Services outside scope of tax
Code specifying that taxes are not applicable to the
services.
"""
,
"""
Standard rate
Code specifying the standard rate.
"""
,
"""
Zero rated goods
Code specifying that the goods are at a zero rate.
""")

def get_description(id_text):
    id_text = id_text.upper()
    position = -1;
    for pos, id in enumerate(__code_id):
        if id == id_text:
            position = pos
            break

    #global description_name_code
    try:
        return __description_name_code[position]
    except:
        return ''

# print(get_description('C'))
