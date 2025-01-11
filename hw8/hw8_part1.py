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
    #prints everything
    print()
    print(bF)
    print()
    print(b)
    print()
    print(t)
