# Segment Notes :

# This segment is used to end and provide information for checking 
# the completeness of a message.

# The segment number shows the position of the segment in a message. 
# It must always be the last segment in a message.

# DE 0074: Count of all segments in a message, UNH and UNT included.

# Example :

# UNT+103+1'


rName = -1
r0074 = -1 # Segments in the message M n..10 M . Total number of segments in a message.
r0061 = -1 # Message_reference M an..14 M . Same reference number as in DE 0062 of the UNH segment of the message.


class sName:
    def __init__(self,  *dataset):
        global rName
        dataset = dataset[0]
        rName = dataset[0]

class s0074: # Segments in the message M n..10 M . Total number of segments in a message.
    def __init__ (self, *dataset):
        global r0074
        dataset = dataset[0]
        r0074 = dataset[0] # M Total number of segments in a message.

class s0061: # Message_reference style='color:white'>_number M an..14 M . Same reference number as in DE 0062 of the UNH segment of the message.
    def __init__(self, *dataset):
        global r0061
        dataset = dataset[0]
        r0061 = dataset[0] # M Same reference number as in DE 0062 of the UNH segment of the message.


def Set(segmentlist):
    segments = []
    for cnt, element in enumerate(segmentlist):
        parts = ()
        
        for elementPart in element.data:
            parts += (elementPart.data,)

        if cnt == 0:
            segments.append(sName(parts))
        elif cnt == 1:
            segments.append(s0074(parts))
        elif cnt == 2:
            segments.append(s0061(parts))
    return segments
        