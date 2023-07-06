import Element_2005_text
import Element_2379_text

    #    DTM  DATE/TIME/PERIOD
    #    Function: To specify date, and/or time, or period.

class data:
    def __init__(self):
        # 000
        self.rName = -1
        # 010   
        #   C507 DATE/TIME/PERIOD                           M    1
        self.r2005 = -1 # Date or time or period function code qualifier    M      an..3
        self.r2005_text = ''
        self.r2380 = '' # Date or time or period text               C      an..35
        self.r2379 = '' # Date or time or period format code        C      an..3
        self.r2379_text = ''    

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sC507(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    #010    
    class sC507:    # DATE/TIME/PERIOD                          M    1
        def __init__(self, dataset): 
            data.r2005 = dataset[0].data   # Date or time or period function code qualifier                                 M      an..3
            data.r2005_text = Element_2005_text.get_description(data.r2005)
            if len(dataset)>1:
                data.r2380 = dataset[1].data   # Date or time or period text               C      an..35
            if len(dataset)>2:
                data.r2379 = dataset[2].data   # Date or time or period format code        C      an..3
                data.r2379_text = Element_2379_text.get_description(data.r2379)

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data
