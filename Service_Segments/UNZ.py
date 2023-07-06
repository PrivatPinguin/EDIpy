# Segment Notes :

# This segment is used to provide the trailer of an interchange.

# DE 0036: If functional groups are used, this is the number of functional groups within the interchange. If functional groups are not used, this is the number of messages within the interchange.

# Example :

# UNZ+5+12345555'
rName = -1
r0036 = -1 # Interchange control count M n..6 M . Number of messages or functional groups within an interchange.
r0020 = -1 # Interchange control reference M an..14 M . Identical to DE 0020 in UNB segment.

class sName:
    def __init__(self,  *dataset):
        global rName
        dataset = dataset[0]
        rName = dataset[0]

class s0036: # Interchange control count M n..6 M . Number of messages or functional groups within an interchange.
    def __init__ (self, *dataset):
        global r0036
        dataset = dataset[0]
        r0036 = dataset[0] # M Interchange control.

class s0020: # Interchange control reference M an..14 M . Identical to DE 0020 in UNB segment.
    def __init__(self, *dataset):
        global r0020
        dataset = dataset[0]
        r0020 = dataset[0] # M Interchange control reference.


def Set(segmentlist):
    segments = []
    for cnt, element in enumerate(segmentlist):
        parts = ()
        
        for elementPart in element.data:
            parts += (elementPart.data,)

        if cnt == 0:
            segments.append(sName(parts))
        elif cnt == 1:
            segments.append(s0036(parts))
        elif cnt == 2:
            segments.append(s0020(parts))
    return segments