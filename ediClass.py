segment_list = []
element_list = []
elementPart_list = []

class Position:
    def __init__(self, line=-1, segment=-1, part=-1):
        self.pos_line=line
        self.pos_segment= segment
        self.pos_part=part

    def get_pos(self):
        return ('{}.{}.{}'.format(self.pos_line,self.pos_segment,self.pos_part))

class Element_Part:
    def __init__(self, element_postion, element_data):
        self.position = element_postion
        self.data = element_data

    def append(self):
        global elementPart_list
        elementPart_list.append(self)

    def get_elementPart_list():
        return elementPart_list
    
    def clear():
        global elementPart_list
        elementPart_list = []

class Element:
    def __init__(self, elements_postion, elements_data):
        self.position = elements_postion
        self.data = elements_data

    def clear():
        global element_list
        element_list = []

    def append(self):
        global element_list
        element_list.append(self)
    
    def get_element_list():
        return element_list

class Segment:
    def __init__(self,segment_position=-1, segment_name='', element_list=[]):
            if len(element_list) > 0:
                self.position = segment_position
                self.name = segment_name
                self.data = element_list
            else:
                self.name = -1
                self.data = ''
    
    def appendElement(self):
        global element_list
        self.data = element_list

    def append(self):
        global segment_list
        segment_list.append(self)
    
    def get_segment_list():
        return segment_list