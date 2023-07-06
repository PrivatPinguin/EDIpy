import Element_1131_text, Element_4453_text, Element_3055_text
    #   FTX    FREE TEXT
    #   Function: To provide free form or coded text information.

class data:
    def __init__(self):
        # 000
        self.rName = -1
        # 010   
        self.r4451 = '' # EXT SUBJECT QUALIFIER                                M  an..3
        # 020   
        self.r4453 = '' # EXT FUNCTION, CODED                                  C  an..3
        self.r4453_text = ''
        # 030   C107  TEXT REFERENCE                                        C  
        self.r4441 = -1 # Free text, coded                                     M  an..3
        self.r1131 = '' # Code list qualifier                                  C  an..3
        self.r1131_text = ''
        self.r3055 = '' # Code list responsible agency, coded                  C  an..3
        self.r3055_text = ''
        # 040   C108  TEXT LITERAL                                          C  
        self.r4440 = -1 # Free text                                            M  an..70
        self.r4440a = '' # Free text                                            C  an..70
        self.r4440b= '' # Free text                                            C  an..70
        self.r4440c = '' # Free text                                            C  an..70
        self.r4440d = '' # Free text                                            C  an..70
        # 050   
        self.r3453 = '' # ANGUAGE, CODED                                       C  an..3

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sr4451(dataset.data)
        elif data_position == 2:
            data.sr4453(dataset.data)
        elif data_position == 3:
            data.sC107(dataset.data)
        elif data_position == 4:
            data.sC108(dataset.data)
        elif data_position == 5:
            data.sr3453(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010    
    class sr4451:    # TEXT SUBJECT QUALIFIER   M    an..3
        def __init__ (self, dataset):
            data.r4451 = dataset[0].data

    # 020    
    class sr4453:    # TEXT FUNCTION, CODED C
        def __init__ (self, dataset):
            data.r4453 = dataset[0].data
            data.r4453_text = Element_4453_text.get_description(data.r4453)  

    # 030    
    class sC107:    # TEXT REFERENCE   C    1
        def __init__ (self, dataset):
            self.r4441 = dataset[0].data # Free text, coded                                     M  an..3
            if len(dataset)>1:
                self.r1131 = dataset[1].data # Code list qualifier                                  C  an..3
                data.r1131_text = Element_1131_text.get_description(data.r1131)
            if len(dataset)>2:
                self.r3055 = dataset[2].data # Code list responsible agency, coded                  C  an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)

    # 040    
    class sC108:    # TEXT LITERAL C   
        def __init__ (self, dataset):
            self.r4440 = dataset[0].data
            if len(dataset)>1:
                data.r4440a = dataset[1].data
            if len(dataset)>2:
                data.r4440b = dataset[2].data
            if len(dataset)>3:
                data.r4440c = dataset[3].data
            if len(dataset)>4:
                data.r4440d = dataset[4].data

    # 050    
    class sr3453:    # LANGUAGE, CODED  C    an..3
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r3453 = dataset[0].data

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data
