import Element_7077_text as e7077_text
    #   Change indicators

    #     a plus sign (+)    for an addition
    #     an asterisk (*)    for an amendment to structure
    #     a hash sign (#)    for changes to names
    #     a vertical bar (|) for changes to text for descriptions,
    #                        notes and functions
    #     a minus sign (-)   for a deletion
    #     an X sign (X)      for marked for deletion



    #    IMD  ITEM DESCRIPTION


    #    Function: To describe an item in either an industry or
    #              free format.
class data:
    def __init__(self):
        # 000
        self.rName = ''
        # 010
        self.r7077 = '' # DESCRIPTION FORMAT CODE                    C    1 an..3
        self.r7077_text = ''
        # 020
        #   C272 # ITEM CHARACTERISTIC
        self.r7081 = '' # Item characteristic code                  C      an..3
        self.r7081_text = ''
        self.r1131 = '' # Code list identification code             C      an..17
        self.r3055 = '' # Code list responsible agency code         C      an..3
        # 030
        #   C273 # ITEM DESCRIPTION   
        self.r7009 = '' # Item description code                     C      an..17
        self.r7008 = '' # Item description                          C      an..256
        self.r7008a = '' # Item description                          C      an..256
        self.r3453 = '' # Language name code                        C      an..3
        # 040
        self.r7383 = '' # SURFACE OR LAYER CODE                      C    1 an..3

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sr7077(dataset.data)
        elif data_position == 2:
            data.sC272(dataset.data)
        elif data_position == 3:
            data.sC273(dataset.data)
        elif data_position == 4:
            data.sr7383(dataset.data)

    # 010
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010
    class sr7077:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r7077 = dataset[0].data # DESCRIPTION FORMAT CODE                    C    1 an..3
                data.r7077_text = e7077_text.get_description(data.r7077)

    # 020
    class sC272: # ITEM CHARACTERISTIC                        C    1
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r7081 = dataset[0].data # Item characteristic code                  C      an..3
            if len(dataset)>1:
                data.r1131 = dataset[1].data # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data # Code list responsible agency code         C      an..3

    # 030
    class sC273: # ITEM DESCRIPTION                           C    1
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r7009 = dataset[0].data # Item description code                     C      an..17
            if len(dataset)>1:
                data.r1131 = dataset[1].data # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data # Code list responsible agency code         C      an..3
            if len(dataset)>3:
                data.r7008 = dataset[3].data # Item description                          C      an..256
            if len(dataset)>4:
                data.r7008a = dataset[4].data # Item description                          C      an..256
            if len(dataset)>5:
                data.r3453 = dataset[5].data # Language name code                        C      an..3

    # 040
    class sr7383:
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r7383 = dataset[0].data # SURFACE OR LAYER CODE                      C    1 an..3

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data