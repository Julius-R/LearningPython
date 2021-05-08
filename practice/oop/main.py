import uuid
import fridge

idGen = lambda :  uuid.uuid1()

f = fridge.Fridge('Peppinos', idGen())

f.add_item('Cheese')
f.display_items()

f.show_fridge_details()
