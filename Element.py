

element_list = []

class Element:
    def __init__(self, element_postion, element_data):
            self.postion = element_postion
            self.data = element_data

    def append(self):
        element_list.append(self)

################## Testumgebung der Klasse ##################
consoleTest = False
if consoleTest:
    x = Element(1234, 'Adress:details')
    y = Element(1235, '')
    x.append()
    y.append()
    # print(x.postion, x.data)