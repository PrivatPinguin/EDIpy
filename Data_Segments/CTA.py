import Element_3139_text

    #   CTA    CONTACT INFORMATION

class data:
    def __init__(self):
        # 000
        self.rName = -1
        
        # 010    
        self.r3139 = '' # CONTACT FUNCTION, CODED                               C  an..3
        self.r3139_text = ''

        # 020 DEPARTMENT OR EMPLOYEE DETAILS Desc: Code and/or name of a department or employee. Code preferred.
        self.r3413 = '' # Department or employee identificat                        Cion                C  an..17
        self.r3412 = '' # Department or employee                               C  an..35
   

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.s3139(dataset.data)
        elif data_position == 2:
            data.sC056(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010
    class s3139:
        def __init__(self, dataset):
            data.r3139 = dataset[0].data
            data.r3139_text = Element_3139_text.get_description(data.r3139)

    # 020    
    class sC056:    # DATE/TIME/PERIOD                          M    1
        def __init__(self, dataset): 
            if len(dataset)>0:
                data.r3413 = dataset[0].data # Department or employee identification                C  an..17
            if len(dataset)>1:
                data.r3412 = dataset[1].data # Department or employee                               C  an..35

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data