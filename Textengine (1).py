import time


import os


Thing = 0
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'
    os.system(command)

class Say:
  def __init__(self, text):
    self.text = text
    Scrtext = self.text
    x = 1
    counter = 0
    Thing =+ 1
    

    Length = len(Scrtext)
    for x in range(Length):
      if counter < 1: 
        print(Scrtext[counter])
        add = Scrtext[counter]
        time.sleep(0.2)
        counter += 1
  

        
      else:
          clearConsole()    
          Add2 = add + Scrtext[counter] 
          add = Add2
          print(Add2)
          counter += 1
          Thing += 1
          
          time.sleep(0.06)
          
clearConsole()        