import Element_5283_text, Element_5153_text, Element_3055_text, Element_5273_text, Element_5305_text, Element_1227_text, Element_5307_text

    #    TAX  DUTY/TAX/FEE DETAILS
    #    Function: To specify relevant duty/tax/fee information.

class data:
    def __init__(self):
        # 000
        self.rName = -1
        # 010    
        self.r5283 = -1  # DUTY OR TAX OR FEE FUNCTION CODE QUALIFIER M    1 an..3
        self.r5283_text = ''

        # 020    C241 DUTY/TAX/FEE TYPE                          C    1
        self.r5153 = ''   # Duty or tax or fee type name code         C      an..3
        self.r5153_text = ''
        self.r1131 = ''   # Code list identification code             C      an..17
        self.r3055 = ''   # Code list responsible agency code         C      an..3
        self.r3055_text = ''
        self.r5152 = ''   # Duty or tax or fee type name              C      an..35

        # 030    C533 DUTY/TAX/FEE ACCOUNT DETAIL                C    1
        self.r5289 = -1   # Duty or tax or fee account code           M      an..6
        # self.r1131 = ''   # Code list identification code             C      an..17
        # self.r3055 = ''   # Code list responsible agency code         C      an..3

        # 040    
        self.r5286 = ''  # DUTY OR TAX OR FEE ASSESSMENT BASIS QUANTITY                                   C    1 an..15

        # 050    C243 DUTY/TAX/FEE DETAIL                        C    1
        self.r5279 = ''   # Duty or tax or fee rate code              C      an..7
        # self.r1131 = ''   # Code list identification code             C      an..17
        # self.r3055 = ''   # Code list responsible agency code         C      an..3
        self.r5278 = ''   # Duty or tax or fee rate                   C      an..17
        self.r5273 = ''   # Duty or tax or fee rate basis code        C      an..12
        self.r5273_text = ''
        # self.r1131 = ''   # Code list identification code             C      an..17
        # self.r3055 = ''   # Code list responsible agency code         C      an..3

        # 060    
        self.r5305 = ''  # DUTY OR TAX OR FEE CATEGORY CODE           C    1 an..3
        self.r5305_text = ''

        # 070    
        self.r3446 = ''  # PARTY TAX IDENTIFIER                       C    1 an..20

        # 080    
        self.r1227 = ''  # CALCULATION SEQUENCE CODE                  C    1 an..3
        self.r1227_text = ''

        # 090    
        self.r5307 = ''  # TAX OR DUTY OR FEE PAYMENT DUE DATE CODE   C    1 an..3
        self.r5307_text = ''

    def Element_init(dataset):
        data_position = dataset.position
        if data_position == 0:
            data.sName(dataset.data)
        elif data_position == 1:
            data.sr5283(dataset.data)
        elif data_position == 2:
            data.sC241(dataset.data)
        elif data_position == 3:
            data.sC533(dataset.data)
        elif data_position == 4:
            data.sr5286(dataset.data)
        elif data_position == 5:
            data.sC243(dataset.data)
        elif data_position == 6:
            data.sr5305(dataset.data)
        elif data_position == 7:
            data.sr3446(dataset.data)
        elif data_position == 8:
            data.sr1227(dataset.data)
        elif data_position == 9:
            data.sr5307(dataset.data)

    # 000
    class sName:
        def __init__(self,  dataset):
            data.rName = dataset[0].data

    # 010    
    class sr5283:    # DUTY OR TAX OR FEE FUNCTION CODE QUALIFIER M    1 an..3
        def __init__ (self, dataset):
            data.r5283 = dataset[0].data
            data.r5283_text = Element_5283_text.get_description(data.r5283)

    # 020    
    class sC241:    #DUTY/TAX/FEE TYPE                                                C    1
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5153 = dataset[0].data  # Duty or tax or fee type name code         C      an..3
                data.r5153_text = Element_5153_text.get_description(data.r5153)
            if len(dataset)>1:
                data.r1131 = dataset[1].data  # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r5152 = dataset[3].data  # Duty or tax or fee type name              C      an..35

    # 030    
    class sC533:    # DUTY/TAX/FEE ACCOUNT DETAIL                                     C    1
        def __init__ (self, dataset):
            data.r5289 = dataset[0].data  # Duty or tax or fee account code           M      an..6
            if len(dataset)>0:
                data.r1131 = dataset[0].data  # Code list identification code             C      an..17
            if len(dataset)>1:
                data.r3055 = dataset[1].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)

    # 040    
    class sr5286:    # DUTY OR TAX OR FEE ASSESSMENT BASIS QUANTITY                    C    1 an..15
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5286 = dataset[0].data

    # 050    
    class sC243:    # DUTY/TAX/FEE DETAIL                                             C    1
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5279 = dataset[0].data  # Duty or tax or fee rate code              C      an..7
            if len(dataset)>1:
                data.r1131 = dataset[1].data  # Code list identification code             C      an..17
            if len(dataset)>2:
                data.r3055 = dataset[2].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)
            if len(dataset)>3:
                data.r5278 = dataset[3].data  # Duty or tax or fee rate                   C      an..17
            if len(dataset)>4:
                data.r5273 = dataset[4].data  # Duty or tax or fee rate basis code        C      an..12
                data.r5273_text = Element_5273_text.get_description(data.r5273)
            if len(dataset)>5:
                data.r1131 = dataset[5].data  # Code list identification code             C      an..17
            if len(dataset)>6:
                data.r3055 = dataset[6].data  # Code list responsible agency code         C      an..3
                data.r3055_text = Element_3055_text.get_description(data.r3055)

    # 060    
    class sr5305:    # DUTY OR TAX OR FEE CATEGORY CODE           C    1 an..3
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5305 = dataset[0].data
    # 070    
    class sr3446:    # PARTY TAX IDENTIFIER                       C    1 an..20
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r3446 = dataset[0].data

    # 080    
    class sr1227:    # CALCULATION SEQUENCE CODE                  C    1 an..3
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r1227 = dataset[0].data

    # 090    
    class sr5307:    # TAX OR DUTY OR FEE PAYMENT DUE DATE CODE   C    1 an..3
        def __init__ (self, dataset):
            if len(dataset)>0:
                data.r5307 = dataset[0].data

def Set(segmentlist):
    data.__init__(data)
    for element in segmentlist:
        data.Element_init(element)
    return data
