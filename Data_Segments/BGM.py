
import Element_1001_text as e1001_text
import Element_1225_text as d1225_text

# BGM - M 1 - Beginning of message
# Function:
# To indicate the type and function of a message and to transmit the identifying number.

class data:
    def __init__(self):
        self.rName = ''
        # 010 
        #   C002 DOCUMENT/MESSAGE NAME C R
        self.r1001 = '' # Document name code C an..3 R * 67 = Commercial dispute
        self.r1001_text = ''
        self.r1131 = '' # Code list identification code C an..17 N
        self.r3055 = '' # Code list responsible agency code C an..3 N
        self.r1000 = '' # Document name C an..35 O C106 DOCUMENT/MESSAGE IDENTIFICATION C R

        # 020 
        #   C106 DOCUMENT/MESSAGE IDENTIFICATION C R
        self.r1004 = '' # Document identifier C an..35 R Invoice Number assigned by document sender. For global unique identification of documents Global Document Type Identifier (GDTI) is available.
        self.r1056 = '' # Version identifier C an..9 N
        self.r1060 = '' # Revision identifier C an..6 O

        # 030
        self.r1225 = '' # Message function code C an..3 R * 1 = Cancellation
        self.r1225_text = ''

        #   C106 DOCUMENT/MESSAGE IDENTIFICATION C R
        self.r1004 = '' # Document identifier C an..35 R Invoice Number assigned by document sender. For global unique identification of documents Global Document Type Identifier (GDTI) is available.
        self.r1056 = '' # Version identifier C an..9 N
        self.r1060 = '' # Revision identifier C an..6 O

        # 030
        self.r1225 = '' # Message function code C an..3 R * 1 = Cancellation
        self.r1225_text = ''

        # 040    
        self.r4343 = '' # RESPONSE TYPE CODE                         C    1 an..3

        # 050    
        self.r1373 = '' # DOCUMENT STATUS CODE                       C    1 an..3

        # 060    
        self.r3453 = '' # LANGUAGE NAME CODE                         C    1 an..3

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sC002(dataset.data)
        elif data_position == 2:
            data.sC106(dataset.data)
        elif data_position == 3:
            data.sr1225(dataset.data)
        elif data_position == 4:
            data.sr4343(dataset.data)
        elif data_position == 5:
            data.sr1373(dataset.data)
        elif data_position == 6:
            data.sr3453(dataset.data)

    # 000
    class sName:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.rName = dataset[0].data
    # 010
    class sC002: # DOCUMENT/MESSAGE NAME                      C    1
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r1001 = dataset[0].data # Document name code                        C      an..3
                data.r1001_text = e1001_text.get_description(data.r1001) # watch ./Elements_1001_text
            if len(dataset)>1:
                data.r1131 = dataset[1].data # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data # Code list responsible agency code         C      an..3
            if len(dataset)>3:
                data.r1000 = dataset[3].data # Document name                             C      an..35
    # It is of critical importance to use the appropriate
    # document name qualifier relevant to the message.
    # Code value 325 may be used to provide valued
    # despatch information. Before using code value '384', it
    # is advised to check with the local tax authorities the
    # legality of using corrected invoices, as some countries
    # may not allow their use.
            
    # 020 
    class sC106:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r1004 = dataset[0].data
            if len(dataset)>1:
                data.r1056 = dataset[1].data
            if len(dataset)>2:
                data.r1060 = dataset[2].data

    # 030
    class sr1225:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r1225 = dataset[0].data
                data.r1225_text = d1225_text.get_description(data.r1225)
    
    # 040
    class sr4343:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r4343 = dataset[0].data

    # 060
    class sr1373:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r1373 = dataset[0].data

    # 060
    class sr3453:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r3453 = dataset[0].data

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data
