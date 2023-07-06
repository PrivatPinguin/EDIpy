# 3155  Communication channel qualifier

__description_name_code = (
    
"""
Circuit switching
A process that, on demand, connects two or more data
terminal equipments and permits the exclusive use of a
data circuit between them until the connection is
released (ISO).
"""
,
"""
SITA
Communications number assigned by Societe Internationale
de Telecommunications Aeronautiques (SITA).
"""
,
"""
ARINC
Communications number assigned by Aeronautical Radio Inc.
"""
,
"""
AT&T mailbox
AT&T mailbox identifier.
"""
,
"""
Peripheral device
Peripheral device identification.
"""
,
"""
Cable address
Self explanatory.
"""
,
"""
EDI transmission
Number identifying the service and service user.
"""
,
"""
Electronic mail
Creating/sending/receiving of unstructured free text
messages or documents using computer network, a mini-
computer or an attached modem and regular telephone line
or other electronic transmission media.
"""
,
"""
Extension
Telephone extension.
"""
,
"""
File transfer access method
According to ISO.
"""
,
"""
Telefax
Device used for transmitting and reproducing fixed
graphic material (as printing) by means of signals over
telephone lines or other electronic transmission media.
"""
,
"""
GEIS (General Electric Information Service) mailbox
Self explanatory.
"""
,
"""
IBM information exchange
Self explanatory.
"""
,
"""
Internal mail
Internal mail address/number.
"""
,
"""
Mail
Postal service document delivery.
"""
,
"""
Postbox number
Self explanatory.
"""
,
"""
Packet switching
The process of routing and transferring data by means of
addressed packets so that a channel is occupied only
during the transmission; upon completion of the
transmission the channel is made available for the
transfer of other packets (ISO).
"""
,
"""
S.W.I.F.T.
Communications address assigned by Society for Worldwide
Interbank Financial Telecommunications s.c.
"""
,
"""
Telephone
Voice/data transmission by telephone.
"""
,
"""
Telegraph
Text transmission via telegraph.
"""
,
"""
Telex
Transmission of text/data via telex.
"""
,
"""
Telemail
Transmission of text/data via telemail.
"""
,
"""
Teletext
Transmission of text/data via teletext.
"""
,
"""
TWX
Communication service involving Teletypewriter machines
connected by wire or electronic transmission media.
Teletypewriter machines are the devices used to send and
receive signals and produce hardcopy from them.
"""
,
"""
X.400
CCITT Message handling system.
"""
)

id_3155 = ('AA','AB','AC','AD','AE','CA','EI','EM','EX','FT','FX','GM','IE','IM','MA','PB','PS','SW','TE','TG','TL','TM','TT','TX','XF')

def get_description(id_text):
    id_text = id_text.upper()
    position = -1
    for pos, id in enumerate(id_3155):
        if id == id_text:
            position = pos
            break

    return __description_name_code[position] # -1 is Custom MSG

# Test
# print(get_description('AA'))