"""
Basta Fazoolin'

You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. 
The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

"""

class menu:
    
  def __init__(self, name, items, start_time, end_time):
    self.name=name
    self.items=items
    self.start_time=start_time
    self.end_time=end_time
  
  def __repr__(self):
    strin=self.name+" menu available from "+str(self.start_time)+" to "+str(self.end_time)
    return strin
  
  def calculate_bill(self,purchased_items):
    total_bill=0
    for name in purchased_items:
      total_bill+=self.items[name]
    return total_bill
  
class Franchise:
  def __init__(self,address,menus):
    self.address=address
    self.menus=menus
  
  def __repr__(self):
    strin="the restaurant is located in "+self.address
    return strin
  
  def available_menus(self,time):
    ans=[]
    for menu in self.menus:
      if time >= menu.start_time and time <=menu.end_time:
        ans.append(menu)
    return ans    

class Business:
  def __init__(self,name,franchises):
    self.name=name
    self.franchises=franchises
    
    
    
brunch=menu("brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
},11,16)

early_bird=menu("early_bird",{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
},15,18)   

dinner=menu("dinner",{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
},17,23)

kids=menu("kids",{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
},11,21)

arepas_menu=menu("Take a’ Arepa",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
},10,20)

menus=[brunch,early_bird,dinner,kids]
flagship_store=Franchise("1232 West End Road",menus)
new_installment=Franchise("12 East Mulberry Street",menus)
arepas_place=Franchise("189 Fitzgerald Avenue",arepas_menu)

arepa=Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])

print(brunch)
order=('pancakes','home fries','coffee')
print(brunch.calculate_bill(order))
order=('salumeria plate','mushroom ravioli (vegan)')
print(early_bird.calculate_bill(order))

print(flagship_store.available_menus(12))
print(new_installment.available_menus(17))
