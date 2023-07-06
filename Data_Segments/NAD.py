import Element_3035_text
import Element_3045_text
import Element_3055_text
 
# United Nations Directories
# for Electronic Data Interchange for
# Administration, Commerce and Transport
#  UN/EDIFACT
#       Change indicators

#         a plus sign (+)    for an addition
#         an asterisk (*)    for an amendment to structure
#         a hash sign (#)    for changes to names
#         a vertical bar (|) for changes to text for descriptions,
#                            notes and functions
#         a minus sign (-)   for a deletion
#         an X sign (X)      for marked for deletion

#        NAD  NAME AND ADDRESS
#        Function: To specify the name/address and their related
#                  function, either by C082 only and/or
#                  unstructured by C058 or structured by C080 thru
#                  3207.

class data:
    def __init__(self):

        self.rName = -1
        # 010    
        self.r3035 = -1 # PARTY FUNCTION CODE QUALIFIER              M    1 an..3
        self.r3035_text = ''

        # 020   
        #   C082 PARTY IDENTIFICATION DETAILS               C    1
        self.r3039 = -1 # Party identifier                          M      an..35
        self.r1131 = '' # Code list identification code             C      an..17
        self.r3055 = '' # Code list responsible agency code         C      an..3
        self.r3055_text = ''

        # 030    
        #   C058 NAME AND ADDRESS                           C    1
        self.r3124 = -1 # Name and address description              M      an..35
        self.r3124a = '' # Name and address description              C      an..35
        self.r3124b = '' # Name and address description              C      an..35
        self.r3124c = '' # Name and address description              C      an..35
        self.r3124d = '' # Name and address description              C      an..35

        # 040    
        #   C080 PARTY NAME                                 C    1
        self.r3036 = -1 # Party name                                M      an..70
        self.r3036a = '' # Party name                                C      an..70
        self.r3036b = '' # Party name                                C      an..70
        self.r3036c = '' # Party name                                C      an..70
        self.r3036d = '' # Party name                                C      an..70
        self.r3045 = '' # Party name format code                    C      an..3
        self.r3045_text = ''

        # 050    
        #   C059 STREET                                     C    1
        self.r3042 = '' # Street and number or post office box identifier   M      an..256
        self.r3042a = '' # Street and number or post office box identifier C      an..256
        self.r3042b = '' # Street and number or post office box identifier C      an..256
        self.r3042c = '' # Street and number or post office box identifier C      an..256

        # 060    
        self.r3164 = '' # CITY NAME                                  C    1 an..35

        # 070    C819 COUNTRY SUBDIVISION DETAILS                C    1
        self.r3229 = '' # Country subdivision identifier            C      an..9
        # self.r1131 = '' # Code list identification code             C      an..17
        # self.r3055 = '' # Code list responsible agency code         C      an..3
        self.r3228 = '' # Country subdivision name                  C      an..70

        # 080    
        self.r3251 = '' #POSTAL IDENTIFICATION CODE                 C    1 an..17

        # 090    
        self.r3207 = '' #COUNTRY IDENTIFIER                         C    1 an..3

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.s3035(dataset.data)
        elif data_position == 2:
            data.sC082(dataset.data)
        elif data_position == 3:
            data.sC058(dataset.data)
        elif data_position == 4:
            data.sC080(dataset.data)
        elif data_position == 5:
            data.sC059(dataset.data)
        elif data_position == 6:
            data.s3164(dataset.data)
        elif data_position == 7:
            data.sC819(dataset.data)
        elif data_position == 8:
            data.s3251(dataset.data)
        elif data_position == 9:
            data.s3207(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010    
    class s3035: # PARTY FUNCTION CODE QUALIFIER              M    1 an..3
        def __init__(self, dataset):
            data.r3035 = dataset[0].data
            data.r3035_text = Element_3035_text.get_description(data.r3035)

    # 020   
    class sC082: # PARTY IDENTIFICATION DETAILS               C    1
        def __init__(self, dataset):
            data.r3039 = dataset[0].data # Party identifier                          M      an..35
            if len(dataset)>1:
                data.r1131 = dataset[1].data # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)

    # 030    
    class sC058: # NAME AND ADDRESS                           C    1
        def __init__(self, dataset):
            data.r3124 = dataset[0].data # Name and address description              M      an..35
            if len(dataset)>1:
                data.r3124a = dataset[1].data # Name and address description              C      an..35
            if len(dataset)>2:
                data.r3124b = dataset[2].data # Name and address description              C      an..35
            if len(dataset)>3:
                data.r3124c = dataset[3].data # Name and address description              C      an..35
            if len(dataset)>4:
                data.r3124d = dataset[4].data # Name and address description              C      an..35

        def form_string(self):
            return (data.r3124, data.r3124a, data.r3124b, data.r3124c, data.r3124d)

    # 040    
    class sC080: # PARTY NAME                                 C    1
        def __init__(self, dataset):
            data.r3036 = dataset[0] # Name and address description              M      an..35
            data.r3036a = dataset[1].data # Party name                                M      an..70
            if len(dataset)>1:
                data.r3036b = dataset[2].data # Party name                                C      an..70
            if len(dataset)>2:
                data.r3036c = dataset[3].data # Party name                                C      an..70
            if len(dataset)>3:
                data.r3036d = dataset[3].data # Party name                                C      an..70
            if len(dataset)>4:                   
                data.r3045 = dataset[4].data # Party name format code                    C      an..3
                data.r3045_text = (Element_3045_text.get_description(data.r3045))
        
        def form_string(self):
            return (data.r3036, data.r3036a, data.r3036b, data.r3036c, data.r3036d)

    # 050    
    class sC059: # STREET                                     C    1
        def __init__(self, dataset):
            data.r3042 = dataset[0].data # Street and number or post office box identifier                                M      an..256
            if len(dataset)>1:
                data.r3042a = dataset[1].data # Street and number or post office box identifier                                C      an..256
            if len(dataset)>2:
                data.r3042b = dataset[2].data # Street and number or post office box identifier                                C      an..256
            if len(dataset)>3:
                data.r3042c = dataset[3].data # Street and number or post office box identifier                                C      an..2562
            
        def form_string(self):
            return (data.r3042, data.r3042a, data.r3042b, data.r3042c)
    # 060   
    class s3164: # CITY NAME                                  C    1 an..35
        def __init__(self, dataset):
            data.r3164 = dataset[0].data

    # 070    
    class sC819: # COUNTRY SUBDIVISION DETAILS                C    1
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r3229 = dataset[0].data # Country subdivision identifier            C      an..9
            if len(dataset)>1:
                data.r1131 = dataset[1].data # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r3228 = dataset[3].data # Country subdivision name                  C      an..70

    # 080    
    class s3251: # POSTAL IDENTIFICATION CODE                 C    1 an..17
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r3251 = dataset[0].data
            

    # 090    
    class s3207: # COUNTRY IDENTIFIER                         C    1 an..3
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r3207 = dataset[0].data

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data

