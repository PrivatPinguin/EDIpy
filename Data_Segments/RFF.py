import Element_1153_text  

    #    RFF  REFERENCE
    #    Function: To specify a reference.


class data:
    def __init__(self):
        # 000
        self.rName = -1
        # 010    
        #   C506 REFERENCE                                  M    1 
        self.r1153 = -1  # Reference code qualifier                  M      an..3
        self.r1153_text = ''
        self.r1154 = ''  # Reference identifier                      C      an..70
        self.r1156 = ''  # Document line identifier                  C      an..6
        self.r1056 = ''  # Version identifier                        C      an..9
        self.r1060 = ''  # Revision identifier                       C      an..6

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sC506(dataset.data)

    class sName:
        def __init__(self,  *dataset):
            global data
            dataset = dataset[0]
            data.rName = dataset[0]

    #010    
    class sC506:    # DATE/TIME/PERIOD                          M    1
        def __init__(self, dataset):
            if len(dataset)>0:
                data.r1153 = dataset[0].data    # Reference code qualifier                  M      an..3
                data.r1153_text = Element_1153_text.get_description(data.r1153)
            if len(dataset)>1:
                data.r1154 = dataset[1].data    # Reference identifier                      C      an..70
            if len(dataset)>2:
                data.r1156 = dataset[2].data    # Document line identifier                  C      an..6
            if len(dataset)>2:
                data.r1056 = dataset[2].data    # Version identifier                        C      an..9
            if len(dataset)>2:
                data.r1060 = dataset[2].data    # Revision identifier                       C      an..6

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data