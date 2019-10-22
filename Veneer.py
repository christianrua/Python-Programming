"""
Veneer

Here at Veneer we strive to provide the best marketplace experience to connect vetted art dealers with premium galleries. Create a 
marketplace for people and organizations to buy and sell pieces of art!

In this project we’ll be developing classes and objects that represent the various responsibilities of art dealership software.
"""
class Art:
  
  def __init__(self,artist,title,medium,year,owner):
    self.artist=artist
    self.title=title
    self.medium=medium
    self.year=year
    self.owner=owner
    
  def __repr__(self):
    return '{artist}."{title}". {medium}. {year}.{name},{location}.'.format(artist=self.artist,title=self.title,medium=self.medium,year=self.year,name=self.owner.name,location=self.owner.location)

class Marketplace:
  
  def __init__(self):
    self.listings=[]
  
  def add_listing(self,new_listing):
      self.listings.append(new_listing)
  
  def remove_listing(self,old_listing):
    self.listings.remove(old_listing)
  
  def show_listings(self):
    for lists in self.listings:
      print(lists)

class Client:
  
  def __init__(self,name,location,is_museum):
    self.name=name
    self.is_museum=is_museum
    if is_museum:
      self.location=location
    else:
      self.location='Private Collection'
    
  
  def sell_artwork(self,artwork,price):
    if self==artwork.owner:
      new_listing=Listing(artwork,price,self)
      veneer.add_listing(new_listing)
   
  def buy_artwork(self,artwork):
    if self!=artwork.owner:
      art_listing=None
      for listings in veneer.listings:
        if listings.art==artwork:
          art_listing=listings
          break
      
      if art_listing!=None: 
        art_listing.art.owner=self
        veneer.remove_listing(art_listing)
          
      
      
class Listing:
  
  def __init__(self,art,price,seller):
    self.art=art
    self.price=price
    self.seller=seller
    
  def __repr__(self):  
    return '{name},{price}'.format(name=self.art.title,price=self.price)
    
edytta=Client('Edytta Halpirt','Private Collection',False)

moma=Client('The MOMA','New York',True)

girl_with_mandolin=Art('Picasso, Pablo','Girl with a Mandolin (Fanny Tellier)','oil on canvas',1910,edytta)  

print(girl_with_mandolin)

veneer=Marketplace()
veneer.show_listings()

edytta.sell_artwork(girl_with_mandolin,'$6M (USD)')
print('\n')
veneer.show_listings()

moma.buy_artwork(girl_with_mandolin)
print('\n')
print(girl_with_mandolin)
veneer.show_listings()
