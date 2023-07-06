import Element_3155_text

#       COM    COMMUNICATION CONTACT

#       Function: To identify a communication number of a department or
#                 a person to whom communication should be directed.


class data:
    def __init__(self):

        self.rName = -1
        # 010   C076  COMMUNICATION CONTACT                                 M  
        self.r3148 = -1 # Communication number                                 M  an..512
        self.r3155 = -1 # Communication channel qualifier                      M  an..3
        self.r3155_text = ''

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sC067(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010    
    class sC067: # PARTY FUNCTION CODE QUALIFIER              M    1 an..3
        def __init__(self, dataset):
            data.r3148 = dataset[0].data
            data.r3155 = dataset[1].data
            data.r3155_text = Element_3155_text.get_description(data.r3155)

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data