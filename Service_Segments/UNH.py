# Segment Notes :

# This segment is used to head and uniquely identify a message in an interchange.

# DE 0062: It is good practice to have the message reference number both 
# unique and incremental.

# S009: Identification of an EANCOM® message.

# The content of data elements 0065, 0052, 0054 and 0051 must be taken from 
# the related UN/EDIFACT standard message.  

# The content of data element 0057 is assigned by GS1 as part of the EANCOM® 
# maintenance process.

# DE 0065: Data element 0065 identifies a UN/EDIFACT message whereas the exact 
# usage of the message is specified in BGM data element 1001. E.g. UN/EDIFACT 
# invoice message serving as a credit note: UNH DE 0065 = INVOIC, BGM DE 1001 = 381.

# DE 0110: This data element can be used by the trading partners to identify an 
# EANCOM® code list, different from the code list published as an integral part 
# of EANCOM® syntax version 4, 2002 release, they have mutually agreed to use 
# when interchanging a message.

# The combination of the values carried in the data elements 0062 and S009 shall 
# be used to uniquely identify the message within the interchange for the purpose 
# of acknowledgement (ref. UNB – data element 0031).

# Example :

# UNH+1+INVOIC:D:01B:UN:EAN010'


rName = -1
r0062 = -1 # Message reference number M an..14 M
# S010  STATUS OF THE TRANSFER C N
r0070 = '' # Sequence of transfers M n..2
r0073 = '' # First and last transfer C a1 
#Unique reference number assigned to a message within an interchange by the sender. Same reference number as in DE 0062 of the UNT segment of the message.
# S009 MESSAGE IDENTIFIER M M
r0065 = -1 # Message type M an..6 M * Identification of a message.
r0052 = -1 # Message version number M an..3 M * D = UN/EDIFACT Directory
r0054 = -1 # Message release number M an..3 M * 01B = Release 2001 - B
r0051 = -1 # Controlling agency M an..2 M * UN = UN/CEFACT
r0057 = '' # Association assigned code C an..6 R * EANnnn = EANCOM® subset version.  EAN represents GS1. ‘nnn’ is the subset version number of the EANCOM® message.

class sName:
    def __init__(self,  *dataset):
        global rName
        dataset = dataset[0]
        rName = dataset[0]

class h0062: #MESSAGE REFERENCE NUMBER
    def __init__ (self, *dataset):
        global r0062
        dataset = dataset[0]
        r0062 = dataset[0] # Message reference number

class s009:
    def __init__(self, *dataset):
        global r0065
        global r0052
        global r0054
        global r0051
        global r0057
        dataset = dataset[0]
        r0065 = dataset[0] # M Message type
        r0054 = dataset[1] # M Message version number
        r0051 = dataset[2] # M Message release number
        r0052 = dataset[3] # M Controlling agency
        if len(dataset)>4:
            r0057 = dataset[4]  # C Association assigned code

        
class r0068:
    def __init__ (self,common_acces_refferende = ''):
        self.r0068  = common_acces_refferende # C

class s010:
    def __init__ (self, sequence_of_transver, first_and_last_transfer=''):
        if not sequence_of_transver:
            sequence_of_transver = 'ERROR:\tNot an EDIFACT message name.'
            print('UNH:s010') # not EDIFACT format (e.g. ORDERS, INVOIC,...)
        self.r0070 = sequence_of_transver
        self.r0073 =first_and_last_transfer


def Set(segmentlist):
    segments = []
    for cnt, element in enumerate(segmentlist):
        parts = ()
        
        for elementPart in element.data:
            parts += (elementPart.data,)

        if cnt == 0:
            segments.append(sName(parts))
        elif cnt == 1:
            segments.append(h0062(parts))
        elif cnt == 2:
            segments.append(s009(parts))
        # elif cnt == 3:
        #     segments.append(r0068(parts[0]))
        # elif cnt == 4:
        #     segments.append(s010(parts[0],parts[1]))
    return segments
        