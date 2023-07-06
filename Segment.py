
segment_list = []

class Segment:
    def __init__(self, segment_name, element):
        self.name = segment_name
        self.data = element
    
    def append(self):
        segment_list.append(self)
    
    def get_segment_list():
        return segment_list

