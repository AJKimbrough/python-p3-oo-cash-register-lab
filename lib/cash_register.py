#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total
    self._items = []
    self.void_item = 0
    
  def add_item(self, title, price, quantity = 1):
    
    self.total = ((price * quantity)+ self.total)
    #self.items.extend([title] * quantity)
      #self.void_item = price
    trans = Transaction(title,price,quantity)
    self._items.append(trans)
      
  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total - round((self.discount/100) * self.total)
      print(f"After the discount, the total comes to ${self.total}.")
    else: 
      print("There is no discount to apply.")

  def get_items(self):
    flat_list = []
    for transaction in self._items:
      x = [transaction.item] * transaction.quantity
      flat_list.extend(x)
    return flat_list

    #return print([[transaction.item] * transaction.quantity for transaction in self._items])
    
  
  def void_last_transaction(self):
    if self._items:
      #self.total = self.total - self.void_item
      print(self.total)
      last_trans = self._items.pop()
      self.total -= last_trans.quantity * last_trans.price
      
    elif self._items == []:
      self.total == 0.0
    

  def total(self):
    return self.total
  
  items = property(get_items)

class Transaction():
  def __init__(self, item, price, quantity):
    self.item = item
    self.price = price
    self.quantity = quantity
  

  
  
cash = CashRegister()
cash.add_item("apple", 0.99,10)
cash.add_item("tomato", 1.76)
print(cash.items)
cash.void_last_transaction()
cash.void_last_transaction()
