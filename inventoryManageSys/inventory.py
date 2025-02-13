from .item import Item
class Inventory:
    '''
    This class manages the collection of items.
    Available Attributes:
    A. Class Level Atributes - N/A
    B. Object Level Attributes - N/A
    Available Methods:
    A. Class Level Methods - N/A
    B. Object Level Methods:
    1. add_to_inventory() -- to add an item or multiple items at once in inventory
    2. get_inventory_details() -- to get the full details of all available items in the inventory
    3. update_item() -- to change the item quantity by giving positive or negative integer value. The first argument is item id and second argument is quantity you want to add or reduce.
    4. delete_from_inv() -- to delete specific item from the inventory. It takes one argument which is the item instance
    5. total_inv() -- to see the total number of items available in the inventory
    '''
    
    def __init__(self): 
        self.__items_list = list() 
        self.__items_detail = []
        
    def __update_details(self):
        self.__items_detail = [[x.item_id,x.item_name,x.item_quantity,x.item_price] for x in self.__items_list if not x._Item__is_deleted]
    
    def get_inventory_details(self):
        self.__items_detail = [[x.item_id,x.item_name,x.item_quantity,x.item_price] for x in self.__items_list if not x._Item__is_deleted]
        return_val = self.__items_detail
        if return_val == list():
            print("No items in the inventory to show details.")
        else:
            print(return_val)
        
    def add_to_inventory(self, *items):
        # check if no argument is passed
        if items == tuple():
            print("please specify the items you want to add")
            return
        for i in items:
            if not isinstance(i, Item):
                raise ValueError("Please enter a valid instance of Item class")
        tempval = []
        for i in items:
            if i not in self.__items_list:
                if i._Item__is_deleted:
                    raise Exception("Can't add item thats already deleted.")
                self.__items_list.append(i)
                tempval.append((i.item_name).title())
                self.__update_details()
            else:
                position = self.__items_list.index(i)
                print(f"{self.__items_list[position].item_name} is already in inventory. Not added again.")
        if tempval:
            v = ', '.join(tempval)
            print(f'{v} added successfully to inventory!!!')
        
    def update_item(self, *items):
        '''Add or Reduce the item quantity by giving positive or negative integer value. The first argument is item id and second argument is quantity you want to add or reduce.'''
        if len(items)!=2:
            raise Exception("update_item method must take only two arguments: item_id and quantity")
        if not isinstance(items[0], int) or not isinstance(items[1], int):
            raise ValueError("Please give a valid whole number as arguments")

        if self.__items_detail == list():
            print("no items in inventory to update. Add some items first")
            return
        else:
            for h, i in enumerate(self.__items_detail):
                if items[0] in i:
                    for i in self.__items_list:
                        if i.item_id == items[0]:
                            i.item_quantity = items[1]
                            print(f"{i.item_name} data has been updated")
                            return
            else:
                print(f"No item found with id({items[0]})")
        
    def delete_from_inv(self, item):
        if item in self.__items_list:
            if item._Item__is_deleted:
                print(f"The item you are trying to delete is already deleted or doesn't exist.")
                return
            self.__items_list.remove(item)
            self.__update_details()
            print(f'{item.item_name} deleted successfully from inventory')
        
    def total_inv(self):
        print(f'Total items in Inventory: {len(self.__items_detail)}')