import ediClass
import re
import EDIFACT as edi
from Service_Segments import UNA
filepath = 'edifactExmpl.edi'

def __get_file(filepath):
    file = open(filepath, "r")
    stringFile = file.read()
    return stringFile

def __regexReplace(regex, subst, data):
    return re.sub(regex, subst, data, 0, re.MULTILINE)

def __normalize_file(stringFile, seperator):
    stringFile = __regexReplace("{}".format(seperator), "{}\n".format(seperator), stringFile)
    return __regexReplace("{}\n+".format(seperator), "\n".format(seperator), stringFile)

def getFile(filepath):
    stringFile = __get_file(filepath)
    return stringFile

def init_seperators(una_line):
    seperatorCol = ()
    for seperator in una_line:
        seperatorCol += (seperator,)
    return seperatorCol

# File to ediClass.py Object
def objectify_file(path):
    edifact_file = getFile(path)
    
    UNA.get_UNA(edifact_file)
    edifact_file = __normalize_file(edifact_file, UNA.data.get_Segment_terminator())
    for line, data in enumerate(edifact_file.splitlines()):

        # if inLine('UNH'):
        data = __regexReplace('\{}'.format(UNA.data.get_Element_Seperator()),'\n', data)
        ediClass.Element.clear()
        for pos, segements in enumerate(data.splitlines()):

            segements = __regexReplace('{}'.format(UNA.data.get_Component_Seperator()), "\n", segements)
            ediClass.Element_Part.clear()
            for partPos, elementpart in enumerate(segements.splitlines()):

                posCoord = ediClass.Position(line,pos,partPos)
                ## if not '#' print seperator ':'
                # if not elementpart:
                #     elementpart = UNA.data.get_Component_Seperator()
                ediClass.Element_Part(posCoord, elementpart).append()
            if not segements:
                # print empty space for seperator '+'
                ediClass.Element_Part(ediClass.Position(line,pos,0), '').append()

            ediClass.Element(pos,ediClass.elementPart_list).append()
        ediClass.Segment(line, data, ediClass.element_list).append()
    return ediClass.segment_list

def print_ediData(segmentlist):
    for segments in segmentlist:
        for pos, element in enumerate(segments.data):
            for posPart, elementpart in enumerate(element.data):
                tabs = '\t'
                if pos != 0:
                    tabs = '\t\t'
                    if posPart != 0:
                        tabs = '\t\t\t'
                print(elementpart.position.get_pos(), tabs, elementpart.data)


if __name__ == '__main__':
    print('init\tMain')
    ediObject = objectify_file(filepath)
    for cnt, line in enumerate(ediObject):
        edi.Segments.segment_check(line.data)
    print_ediData(ediObject)