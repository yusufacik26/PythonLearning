class Spaceship:
   # Class attribute
   tractor_beam = 'off'

   # Instance attributes
   def __init__(self, name, kind):
      self.name = name
      self.kind = kind
      self.speed = None


   def warp(self,warp):
      self.speed = warp
      print(f'Warp{warp},engage!')
   
   def tractor(self):
      if self.tractor_beam == 'off':
         self.tractor.beam = 'on'
         print('Tractor beam on.')
      else:
         self.tractor_beam = 'off'
         print('tractor beam off')     

 
ship = Spaceship('Işıkyılı','starfighter') 

print(ship.name)
print(ship.tractor_beam)
ship.warp(7)

ship.speed