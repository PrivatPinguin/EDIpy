
# import Service_Segments.UNA as UNA
import Service_Segments.UNB as UNB
import Service_Segments.UNG as UNG
import Service_Segments.UNH as UNH
import Data_Segments.BGM as BGM
import Data_Segments.DTM as DTM
import Data_Segments.NAD as NAD
import Data_Segments.IMD as IMD
import Data_Segments.LOC as LOC
import Data_Segments.NAD as NAD
import Data_Segments.RFF as RFF
import Data_Segments.TAX as TAX
import Data_Segments.CTA as CTA
import Data_Segments.COM as COM
import Data_Segments.FTX as FTX
import Service_Segments.UNT as UNT
import Service_Segments.UNE as UNE
import Service_Segments.UNZ as UNZ


class Segments:
    def __init__(self):
        pass

    def partSegment_check(segmentObject):
        pass

    def segment_check(line):
        line_name = line[0].data[0].data
        # if line_name == 'UNA':
        #     una = UNA.set_segment(line)
        if line_name == 'UNB':
            unb = UNB.Set(line)
        elif line_name == 'UNG':
            ung = UNG.Set(line)
        elif line_name == 'UNH':
            unh = UNH.Set(line)
            # unh = testUnh.set_segment(line)
        if line_name == 'BGM':
            bgm = BGM.Set(line)
        elif line_name == 'DTM':
            dtm = DTM.Set(line) # TODO
            pass
        elif line_name == 'FTX':
            ftx = FTX.Set()
        elif line_name == 'RFF':
            rff = RFF.Set(line)
            pass
        elif line_name == 'NAD':
            nad = NAD.Set(line) #TODO
            pass
        elif line_name == 'LOC':
            loc = LOC.Set(line)
        elif line_name == 'CTA':
            cta = CTA.Set(line)
            pass
        elif line_name == 'COM':
            com = COM.Set(line)
            pass
        elif line_name == 'LIN':
            # create article
            pass
        elif line_name == 'PIA':
            pass
        elif line_name == 'IMD':
            imd = IMD.Set(line) # TODO
            pass
        elif line_name == 'MEA':
            pass
        elif line_name == 'QTY':
            pass
        elif line_name == 'PRI':
            pass
        elif line_name == 'UNS':
            pass
        elif line_name == 'MOA':
            pass
        elif line_name == 'CNT':
            pass
        elif line_name == 'UNT':
            unt = UNT.Set(line)
        elif line_name == 'UNE':
            une = UNE.Set(line)
        elif line_name == 'UNZ':
            unz = UNZ.Set(line)