# Segment Notes :

# Within EANCOM® the use of the UNG..UNE segments should not be used for 
# grouping of multiple message types in the same interchange as this is 
# not considered good practice. However, they can be used by organisations 
# to create their own identifiable application level envelopes, which can 
# be addressed from the originating department to a department in the 
# recipient's system, e.g. to group multiple issuers in one transmission 
# file with invoices.

# Example :

# UNE+25+471123'

rName = -1
r0060 = -1 # Number of messages M n..6 M Number of messages in the group.
r0048 = -1 # Functional group reference number M an..14 M Identical to DE 0048 in UNG segment.


class sName:
    def __init__(self,  *dataset):
        global rName
        dataset = dataset[0]
        rName = dataset[0]

class s0060: # Segments in the message M n..10 M . Total number of segments in a message.
    def __init__ (self, *dataset):
        global r0060
        dataset = dataset[0]
        r0060 = dataset[0] # M Total number of segments in a message.

class s0048: # Message_reference style='color:white'>_number M an..14 M . Same reference number as in DE 0062 of the UNH segment of the message.
    def __init__(self, *dataset):
        global r0048
        dataset = dataset[0]
        r0048 = dataset[0] # M Same reference number as in DE 0062 of the UNH segment of the message.


def Set(segmentlist):
    segments = []
    for cnt, element in enumerate(segmentlist):
        parts = ()
        
        for elementPart in element.data:
            parts += (elementPart.data,)

        if cnt == 0:
            segments.append(sName(parts))
        elif cnt == 1:
            segments.append(s0060(parts))
        elif cnt == 2:
            segments.append(s0048(parts))
    return segments
        