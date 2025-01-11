import BerryField
import json
import Bear
import Tourist
#opens file
def createFieldFromFile(f):
     return json.loads(open(f).read())
if __name__ == "__main__":
    #gets file with all information
    fName = input('Enter the json file name for the simulation => ').strip()
    print(fName)
    field = createFieldFromFile(fName)
    #creates bear
    b= Bear.Bear(field['active_bears'],field['reserve_bears'])
    #creates tourist
    t= Tourist.Tourist(field['active_tourists'],field['reserve_tourists'])
    #creates berryField
    bF = BerryField.BerryField(field['berry_field'],t.tour,b.bs,t.res,b.res,b,t)
    print()
    print('Starting Configuration')
    print(bF)
    print()
    print(b)
    print()
    print(t)
    i = 1
    #runs simulation until end
    #uses methods from berryfield to run simulation
    #prints out stats every 5 turns
    #prints out if a tourists or bear leaves or enters
    while bF.checkToEnd() == False:
          print()
          print('Turn: {}'.format(i))
          bF.growField() 
          bF.bearMoves()
          bOut = bF.bearOut()
          if len(bOut)>0:
             print(bOut)
          bearC = bF.bearCheck()
          if len(bearC)>0:
             print(bearC)
          bF.NoExtras()
          bF.importBears()
          bF.importTourists()
          if i % 5 ==0 and bF.checkToEnd()==False:
               print(bF)
               print()
               print(b)
               print()
               print(t)
          print()
          i+=1
    print(bF)
    print()
    print(b)
    print()
    print(t)