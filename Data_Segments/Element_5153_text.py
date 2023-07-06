
    #  5153  Duty or tax or fee type name code                       [C]

    #  Desc: Code specifying a type of duty, tax or fee.
    #  Repr: an..3
    #  Code Values: 

__code_id = ('AAA', 'AAB', 'AAC', 'AAD', 'AAE', 'AAF', 'AAG', 'AAH', 'AAI', 'AAJ', 'AAK', 'AAL', 'AAM', 'ADD', 'BOL', 'CAP', 'CAR', 'COC', 'CST', 'CUD', 'CVD', 'ENV', 'EXC', 'EXP', 'FET', 'FRE', 'GCN', 'GST', 'ILL', 'IMP', 'IND', 'LAC', 'LCN', 'LDP', 'LOC', 'LST', 'MCA', 'MCD', 'OTH', 'PDB', 'PDC', 'PRF', 'SCN', 'SSS', 'STT', 'SUP', 'SUR', 'SWT', 'TAC', 'TOT', 'TOX', 'TTA', 'VAD', 'VAT')
__description_name_code = ("""
Petroleum tax
A tax levied on the volume of petroleum being
transacted.
"""
,
"""
Provisional countervailing duty cash
Countervailing duty paid in cash prior to a formal
finding of subsidization by Customs.
"""
,
"""
Provisional countervailing duty bond
Countervailing duty paid by posting a bond during an
investigation period prior to a formal decision on
subsidization by Customs.
"""
,
"""
Tobacco tax
A tax levied on tobacco products.
"""
,
"""
Energy fee
General fee or tax for the use of energy.
"""
,
"""
Coffee tax
A tax levied specifically on coffee products.
"""
,
"""
Harmonised sales tax, Canadian
A harmonized sales tax consisting of a goods and service
tax, a Canadian provincial sales tax and, as applicable,
a Quebec sales tax which is recoverable.
"""
,
"""
Quebec sales tax
A sales tax charged within the Canadian province of
Quebec which is recoverable.
"""
,
"""
Canadian provincial sales tax
A sales tax charged within Canadian provinces which is
non-recoverable.
"""
,
"""
Tax on replacement part
A tax levied on a replacement part, where the original
part is returned.
"""
,
"""
Mineral oil tax
Tax that is levied specifically on products containing
mineral oil.
"""
,
"""
Special tax
To indicate a special type of tax.
"""
,
"""
Insurance tax
A tax levied specifically on insurances.
"""
,
"""
Anti-dumping duty
Duty applied to goods ruled to have been dumped in an
import market at a price lower than that in the
exporter's domestic market.
"""
,
"""
Stamp duty (Imposta di Bollo)
Tax required in Italy, which may be fixed or graduated
in various circumstances (e.g. VAT exempt documents or
bank receipts).
"""
,
"""
Agricultural levy
Levy imposed on agricultural products where there is a
difference between the selling price between trading
countries.
"""
,
"""
Car tax
A tax that is levied on the value of the automobile.
"""
,
"""
Paper consortium tax (Italy)
Italian Paper consortium tax.
"""
,
"""
Commodity specific tax
Tax related to a specified commodity, e.g. illuminants,
salts.
"""
,
"""
Customs duty
Duties laid down in the Customs tariff, to which goods
are liable on entering or leaving the Customs territory
(CCC).
"""
,
"""
Countervailing duty
A duty on imported goods applied for compensate for
subsidies granted to those goods in the exporting
country.
"""
,
"""
Environmental tax
Tax assessed for funding or assuring environmental
protection or clean-up.
"""
,
"""
Excise duty
Customs or fiscal authorities code to identify a
specific or ad valorem levy on a specific commodity,
applied either domestically or at time of importation.
"""
,
"""
Agricultural export rebate
Monetary rebate given to the seller in certain
circumstances when agricultural products are exported.
"""
,
"""
Federal excise tax
Tax levied by the federal government on the manufacture
of specific items.
"""
,
"""
Free
No tax levied.
"""
,
"""
General construction tax
General tax for construction.
"""
,
"""
Goods and services tax
Tax levied on the final consumption of goods and
services throughout the production and distribution
chain.
"""
,
"""
Illuminants tax
Tax of illuminants.
"""
,
"""
Import tax
Tax assessed on imports.
"""
,
"""
Individual tax
A tax levied based on an individual's ability to pay.
"""
,
"""
Business license fee
Government assessed charge for permit to do business.
"""
,
"""
Local construction tax
Local tax for construction.
"""
,
"""
Light dues payable
Fee levied on a vessel to pay for port navigation
lights.
"""
,
"""
Local sales tax
Assessment charges on sale of goods or services by city,
borough country or other taxing authorities below state
or provincial level.
"""
,
"""
Lust tax
Tax imposed for clean-up of leaky underground storage
tanks.
"""
,
"""
Monetary compensatory amount
Levy on Common Agricultural Policy (European Union)
goods used to compensate for fluctuating currencies
between member states.
"""
,
"""
Miscellaneous cash deposit
Duty paid and held on deposit, by Customs, during an
investigation period prior to a final decision being
made on any aspect related to imported goods (except
valuation) by Customs.
"""
,
"""
Other taxes
Unspecified, miscellaneous tax charges.
"""
,
"""
Provisional duty bond
Anti-dumping duty paid by posting a bond during an
investigation period prior to a formal decision on
dumping by Customs.
"""
,
"""
Provisional duty cash
Anti-dumping duty paid in cash prior to a formal finding
of dumping by Customs.
"""
,
"""
Preference duty
Duties laid down in the Customs tariff, to which goods
are liable on entering or leaving the Customs territory
falling under a preferential regime such as Generalised
System of Preferences (GSP).
"""
,
"""
Special construction tax
Special tax for construction.
"""
,
"""
Shifted social securities
Social securities share of the invoice amount to be paid
directly to the social securities collector.
"""
,
"""
State/provincial sales tax
All applicable sale taxes by authorities at the state or
provincial level, below national level.
"""
,
"""
Suspended duty
Duty suspended or deferred from payment.
"""
,
"""
Surtax
A tax or duty applied on and in addition to existing
duties and taxes.
"""
,
"""
Shifted wage tax
Wage tax share of the invoice amount to be paid directly
to the tax collector(s office).
"""
,
"""
Alcohol mark tax
A tax levied based on the type of alcohol being
obtained.
"""
,
"""
Total
The summary amount of all taxes.
"""
,
"""
Turnover tax
Tax levied on the total sales/turnover of a corporation.
"""
,
"""
Tonnage taxes
Tax levied based on the vessel's net tonnage.
"""
,
"""
Valuation deposit
Duty paid and held on deposit, by Customs, during an
investigation period prior to a formal decision on
valuation of the goods being made.
"""
,
"""
Value added tax
A tax on domestic or imported goods applied to the value
added at each stage in the production/distribution
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
