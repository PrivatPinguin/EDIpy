

    # UNG - C 1 - Functional Group Header
    # Function : To start, identify and specify a functional group.

    # Segment notes :

    # Within EANCOM® the use of the UNG..UNE segments should not be used for 
    # grouping of multiple message types in the same interchange as this is not 
    # considered good practice. However, they can be used by organisations to 
    # create their own identifiable application level envelopes, which can be 
    # addressed from the originating department to a department in the recipient's 
    # system, e.g. to group multiple issuers in one transmission file with invoices.

    # Example :

    # UNG+INVOIC+5412345678908:14+8798765432106:14+020102:1000+471123+UN+D:01B:EAN010'

class data:
    def __init__(self):
        # 000
        self.rName = -1

        # 010
        self.r0038 = -1 # FUNCTIONAL GROUP IDENTIFICATION M an..6 M Identification of a message contained in the functional group, e.g. INVOIC.

        # 020
        #   S006 APPLICATION SENDER’S IDENTIFICATION M M 
        self.r0040 = -1 # Sender identification M an..35 M GLN (n13)
        self.r0007 = '' # Identification code qualifier C an..4 R * 14 = GS1

        # 030
        #   S007 INTERCHANGE RECIPIENT M M 
        self.r0044 = -1 # Recipient identification M an..35 M GLN (n13)
        self.r0007 = '' # Identification code qualifier C an..4 R * 14 = GS1

        # 040
        #   S004 DATE / TIME OF PREPARATION M M
        self.r0017 = -1 # Date M n6 M YYMMDD
        self.r0019 = -1 # Time M n4 M HHMM
        self.r0048 = -1 # Functional group reference number M an..14 M Unique reference identifying the functional group. Created by the interchange sender.
        self.r0051 = -1 # Controlling agency M an..2 M * UN = UN/CEFACT

        # 050
        #   S008 MESSAGE VERSION M M 
        self.r0052 = -1 # Message type version number M an..3 M * D = UN/EDIFACT directory
        self.r0054 = -1 # Message type release number M an..3 M The value of this data element depends on the message type.
        self.r0057 = '' # Association assigned code C an..6 R The value of this data element depends on the message type.
        self.r0058 = '' # Application password C an..14 D The use of this data element depends on agreements between the trading partners.

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sr0038(dataset.data)
        elif data_position == 2:
            data.s006(dataset.data)
        elif data_position == 3:
            data.s007(dataset.data)
        elif data_position == 4:
            data.s004(dataset.data)
        elif data_position == 5:
            data.s0048(dataset.data)
        elif data_position == 6:
            data.s0051(dataset.data)
        elif data_position == 7:
            data.s008(dataset.data)

    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0]

    class sr0038: #MESSAGE REFERENCE NUMBER
        def __init__ (self, dataset):
            data.r0038 = dataset[0] # Message reference number

    class s006:
        def __init__(self, dataset):
            data.r0040 = dataset[0] # M 
            if len(dataset)>1:
                data.r0007 = dataset[1]  # C 

    class s007:
        def __init__(self, dataset):
            data.r0044 = dataset[0] # M 
            if len(dataset)>1:
                data.r0007 = dataset[1]  # C 

    class s004:
        def __init__(self, dataset):
            data.r0017 = dataset[0] # M 
            data.r0019 = dataset[1] # M 

    class s0048:
        def __init__(self, dataset):
            data.r0048 = dataset[0] # M 

    class s0051:
        def __init__(self, dataset):
            data.r0051 = dataset[0] # M 

    class s008:
        def __init__(self, dataset):
            data.r0052 = dataset[0] # M 
            data.r0054 = dataset[1] # M 
            if len(dataset)>2:
                data.r0057 = dataset[2]  # C 
            if len(dataset)>3:
                data.r0058 = dataset[3]  # C 

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data
