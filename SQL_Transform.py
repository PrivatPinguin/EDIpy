

class Lists:
    LIN_list = []
    NAD_list = []

    class Contact:
        contact_details = -1
        contact_code = -1
        contact_id = ''
        em_com = '' # COM + E-Mail
        te_com = '' # COM + Telephone
        fx_com = '' # COM + Fax
        def __init__(self, details,) -> None:
            pass

    class DestinationObject: # NAD
        destination_segment = -1 # BY; ST; SU; ...
        reviever_GTIN = -1
        shipping_location = ''
        def __init__(self, destination, gTIN):
            self.destination_segment = destination
            self.reviever_GTIN = gTIN
            Lists.NAD_list.append(self)
        def contact_add(self, contactObject):
            pass


    class OrderObjedt: # LIN
        order_number = -1
        order_line = -1
        product_GTIN = -1
        delivery_location_GLN = -1
        def __init__(self, orderNR, lineNR, productGTIN, deliveryGLN):
            self.order_number = orderNR
            self.order_line = lineNR
            self.product_GTIN = productGTIN
            self.delivery_location_GLN = deliveryGLN
            Lists.LIN_list.append(self)
        
        def get_details(self):
            return [self.order_number, self.order_line, self.product_GTIN, self.delivery_location_GLN]

x = Lists.OrderObjedt(2,3,'2342','23423423')
y = Lists.OrderObjedt(3,4,'3453','34534534')
print(x.get_details())
for lin in Lists.LIN_list:
    print(lin.order_number, lin.order_line, lin.product_GTIN, lin.delivery_location_GLN)

#print(Lists.LIN_list[0].order_number)