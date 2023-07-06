
def infotext():
    pass
    """
    Segment Notes:

    This segment is used to inform the receiver of the interchange that 
    a set of service string characters which are different to the default 
    characters are being used.

    When using the default set of service characters, the UNA segment need 
    not be sent. If it is sent, it must immediately precede the UNB segment 
    and contain the four service string characters (positions UNA1, UNA2, 
    UNA4 and UNA6) selected by the interchange sender.

    Regardless of whether or not all of the service string characters are 
    being changed every data element within this segment must be filled, 
    (i.e., if some default values are being used with user defined ones, 
    both the default and user defined values must be specified).

    When expressing the service string characters in the UNA segment, it 
    is not necessary to include any element separators.

    The use of the UNA segment is required when using a character set 
    other than level A.

    Example: 

    UNA:+.? ' 
    """

class data:
    def __init__(self):
        self.rName = -1
        self.una1 = -1 # Component data element separator M an1 M Used as a separator between component data elements contained within a composite data element (default value: ":")
        self.una2 = -1 # Data element separator M an1 M * Used to separate two simple or composite data elements (default value: "+" )
        self.una3 = -1 # Decimal notation M an1 M *Used to indicate the character used for decimal notation (default value:".")
        self.una4 = -1 # Release character M an1 M *Used to restore any service character to its original specification (value: "?").
        self.una5 = -1 # Reserved for future use M an1 M *(default value: space )
        self.una6 = -1 # Segment terminator M an1 M * Used to indicate the end of segment data (default value: " ' ")
    def get_Component_Seperator():
        return data.una1
    def get_Element_Seperator():
        return data.una2
    def get_Decimal_Seperator():
        return data.una3
    def get_Service_Charakter():
        return data.una4
    def get_Space_char():
        return data.una5
    def get_Segment_terminator():
        return data.una6

    class sName:
        def __init__(self, dataset):
            # global data
            dataset = dataset[0]
            data.rName = dataset[0]

    class una_seperators: # Interchange control count M n..6 M . Number of messages or functional groups within an interchange.
        def __init__ (self, dataset):
            # global data
            data.una1 = dataset[0] # ':' M Interchange control.
            data.una2 = dataset[1] # '+'
            data.una3 = dataset[2] # '.'
            data.una4 = dataset[3] # '?'
            data.una5 = dataset[4] # ' '
            data.una6 = dataset[5] # '''
        def get_seprerator(pos):
            if pos == 0:
                return data.una1
            elif pos == 1:
                return data.una2
            elif pos == 2:
                return data.una3
            elif pos == 3:
                return data.una4
            elif pos == 4:
                return data.una5
            elif pos == 5:
                return data.una6

    class suna1: # Interchange control count M n..6 M . Number of messages or functional groups within an interchange.
        def __init__ (self, dataset):
            global data
            dataset = dataset[0]
            data.una1 = dataset[0][0] # '+' M Interchange control.
            data.una2 = dataset[0][1] # '.'
            data.una3 = dataset[0][2] # '?'
            data.una4 = dataset[0][3] # ' '
            data.una5 = dataset[0][4] # ' '
            data.una6 = dataset[0][5] # '''


    class suna2: # Interchange control reference M an..14 M . Identical to DE 0020 in UNB segment.
        def __init__(self, *dataset):
            global data
            dataset = dataset[0]
            data.una2 = dataset[0] # M Interchange control reference.


def get_UNA(file):
    data.sName(file[:3])
    data.una_seperators(file[3:9])

# def set_segment(segmentlist):
#     segments = []
#     for cnt, element in enumerate(segmentlist):
#         parts = ()
        
#         for elementPart in element.data:
#             parts += (elementPart.data,)

#         if cnt == 0:
#             segments.append(sName(parts))
#         elif cnt == 1:
#             segments.append(suna1(parts))
#     return segments