class Item:
    '''
    This class represents an item in an inventory system. Unique id is automatically generated when an Item instance is created. 
    Available Attributes:
    A. Class Level Atributes - N/A
    B. Object Level Attributes:
    1. item_id -- to get the id of an item
    2. item_name -- to get and set the item name
    3. item_quantity -- to get and change the item quantity. It takes only one argument which increases the quantity if given positive number and decreases the quantity if given neagtive number
    4. item_price -- to get and change the item price
    Available Methods:
    A. Class Level Methods - N/A
    B. Object Level Methods:
    1. delete_item() -- to delete an item if it exists
    2. search_item() -- to check if an item with specific id exists or not. It takes id as an argument
    3. item_details() -- to get the full detail of an item
    4. item_total_value() -- to calculate the total value of an item based on it's quantity and price
    '''
    
    __unique = 2000
    __instance_list = []
    
    def __init__(self,name,quantity,price):
            
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError("please enter a valid string")
        
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ValueError("please enter a valid whole number")
        
        if isinstance(price, (int, float)):
            self.__price = price
        else:
            raise ValueError("please enter a valid whole number")
        
        # generate unique id for each instance
        Item.__unique += 1
        self.__id = Item.__unique
        
        # append created instance to all_instance_list
        self.__instance_list.append(self)
        
        self.__is_deleted = False
    
    # getter for id
    @property
    def item_id(self):
        if not self.__is_deleted:
            return self.__id
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
        
    # getter for name
    @property
    def item_name(self):
        if not self.__is_deleted:
            return self.__name
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
    
    # setter for name
    @item_name.setter
    def item_name(self, name):
        if not self.__is_deleted:
            print("Warning!!! you can't change name once created")
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
        
    # getter for quantity
    @property
    def item_quantity(self):
        if not self.__is_deleted:
            return self.__quantity
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
    
    # setter for quantity
    @item_quantity.setter
    def item_quantity(self, qty):
        if not self.__is_deleted:
            if isinstance(qty, int):
                self.__quantity += qty
                if self.item_quantity<0:
                    raise Exception("you are trying to deduct more than the quantity you have")
                if qty > 0:
                    print("increased quantity successfully!!!")
                elif qty < 0:
                    print("quantity deducted successfully!!!")
                else:
                    print("no change in quantity")
            else:
                raise ValueError("please give valid integer")
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
        
    # getter for price
    @property
    def item_price(self):
        if not self.__is_deleted:
            return self.__price
        else:
            raise Exception("Sorry but you can't perform an operation on the instance that doesn't exist.")
    
    # setter for price
    @item_price.setter
    def item_price(self, price): 
        if not self.__is_deleted:
            if isinstance(price, (int, float)) and price > 0:
                self.__price = price
            else:
                raise ValueError('please enter a valid number and the number should be greater than zero')
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
        
    # delete an item
    def delete_item(self):
        if not self.__is_deleted:
            if self in Item.__instance_list:
                Item.__instance_list.remove(self)
                print(f'item ({self.item_name}) has been deleted successfully')
                self.__is_deleted = True
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
    
    # search if item of specific id exists or not
    def search_item(self, identity):
        if not self.__is_deleted:
            if not isinstance(identity, int):
                raise ValueError("argument passed must be a valid integer.")
            for x in Item.__instance_list:
                if identity == x.item_id:
                    print(f'Id: {x.item_id}, Name: {x.item_name}, Quantity: {x.item_quantity}, Price: {x.item_price}')
                    break
            else:
                print(f'No item with id({identity}) found.')
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
            
    # details of an item
    def item_details(self):
        if not self.__is_deleted:
            print(f'Id: {self.__id}, Name: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price}')
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
    
    # get the total value of an item
    def item_total_value(self):
        if not self.__is_deleted:
            print(self.__quantity * self.__price)
        else:
            raise Exception("Can't perform operation on the instance that doesn't exist.")
    
    # return msg for deleted instances
    def __str__(self):
        if self.__is_deleted:
            return "item doesn't exist."
        return super().__str__()