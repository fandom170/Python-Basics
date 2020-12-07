from Homework_8.lesson8_task4_wh import Warehouse
from Homework_8.lesson8_task4_of import Scanner, Copier, Printer

wh1 = Warehouse()
Warehouse.warehouse_info(wh1)

# cp1 = Copier.set_item()
# pr1 = Printer.set_item()
# sc1 = Scanner.set_item()
#
#
# wh1.add_item(cp1, 1)
# wh1.add_item(pr1, 2)
# wh1.add_item(sc1, 3)
# wh1.add_item(pr1, 4)

Warehouse.warehouse_info(wh1)

cp2 = Copier.set_item()
print(cp2)
wh1.add_item(cp2, 'a')
# Warehouse.warehouse_info(wh1)
# wh1.remove_item(cp2, 10)
Warehouse.warehouse_info(wh1)
