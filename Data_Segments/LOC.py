import Element_3227_text, Element_3055_text
 
    #    LOC  PLACE/LOCATION IDENTIFICATION

    #    Function: To identify a place or a location and/or related locations.


class data:
    def __init__(self):

        self.rName = -1
        # 010    
        self.r3227 = -1 # LOCATION FUNCTION CODE QUALIFIER           M      1 an..3
        self.r3227_text = ''

        # 020    C517 LOCATION IDENTIFICATION                        C      1
        self.r3225 = ''  # Location identifier                       C      an..35
        self.r1131 = ''  # Code list identification code             C      an..17
        self.r3055 = ''  # Code list responsible agency code         C      an..3
        self.r3055_text = ''
        self.r3224 = ''  # Location name                             C      an..256

        # 030    C519 RELATED LOCATION ONE IDENTIFICATION            C      1
        self.r3223 = ''  # First related location identifier         C      an..35
        # self.r1131 = ''  # Code list identification code             C      an..17
        # self.r3055 = ''  # Code list responsible agency code         C      an..3
        self.r3222 = ''  # First related location name               C      an..70

        # 040    C553 RELATED LOCATION TWO IDENTIFICATION            C      1
        self.r3233 = ''  # Second related location identifier        C      an..35
        # self.r1131 = ''  # Code list identification code             C      an..17
        # self.r3055 = ''  # Code list responsible agency code         C      an..3
        self.r3232 = ''  # Second related location name              C      an..70

        # 050    
        self.r5479 = '' # RELATION CODE                              C      1 an..3

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.s3227(dataset.data)
        elif data_position == 2:
            data.sC517(dataset.data)
        elif data_position == 3:
            data.sC519(dataset.data)
        elif data_position == 4:
            data.sC553(dataset.data)
        elif data_position == 5:
            data.s5479(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010
    class s3227:    # LOCATION FUNCTION CODE QUALIFIER           M    1 an..3
        def __init__ (self, dataset):
            data.r3227 = dataset[0].data
            data.r3227_text = Element_3227_text.get_description(data.r3227)
            

    # 020
    class sC517:    # LOCATION IDENTIFICATION                    C    1
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r3225 = dataset[0].data  # Location identifier                       C      an..35
            if len(dataset)>1:
                data.r1131 = dataset[1].data  # Code list identification code             C      an..17
            if len(dataset)>2:                
                data.r3055 = dataset[2].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r3224 = dataset[3].data  # Location name                             C      an..256

    # 030
    class sC519:    # RELATED LOCATION ONE IDENTIFICATION        C    1
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r3223 = dataset[0].data  # First related location identifier         C      an..35
            if len(dataset)>1:
                data.r1131 = dataset[1].data  # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r3222 = dataset[3].data  # First related location name               C      an..70

    # 040
    class sC553:    # RELATED LOCATION TWO IDENTIFICATION        C    1
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r3233 = dataset[0].data  # Second related location identifier        C      an..35
            if len(dataset)>1:
                data.r1131 = dataset[1].data  # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r3232 = dataset[3].data  # Second related location name              C      an..70

    # 050
    class s5479:    # RELATION CODE                              C    1 an..3
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5479 = dataset[0].data

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data

