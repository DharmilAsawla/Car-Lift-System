###################################################################
#                                                                 #
#           GROUP 1 - CIS20-1 Group Project                       #
#                                                                 #
###################################################################


######################################
#Importing
######################################
from collections import OrderedDict
import datetime
import pickle




#######################################
#Variables
#######################################
i = 0
PassengerTime = 0

########################################
#Login Data
########################################
DriverData = "DriverUserData.txt"
PassengerData = "PassengerUserData.txt"
CarTimesData = "CarTimesData.txt"


########################################
#Dictionaries
########################################
DriverDict = {"driver1" : "abc" , "driver2" : "def" }
PassengerDict = {"alan" : "sephiroth" , "dharmil" : "spheron"}
CarTimes = {}




def JourneyAnnounce():
    carCount = i + 1
    
    #listNameCounter = "Car" + str(carCount)
    destination = input("Destination : ")
    numberOfSeats = int(input("Number Of Seats in your car : "))
    timeOfJourney = float(input("Time of Journey : "))
    journeyPrice = input("Price To Charge : ")
    carPlate = input("Car Plate : ")
    colour = input("Car Colour : ")
    
    DriverCar = (destination, numberOfSeats,timeOfJourney,journeyPrice,carPlate, colour)
    
    print ("\n \n" + "This is Car No : " + str(carCount) +
           "\n" + "Destination : " + str(DriverCar[0]) +
           "\n" + "Number Of Seats : "  + str(DriverCar[1]) +
           "\n" + "Time Of Journey : " + str(DriverCar[2]) +
           "\n" + "Price To Charge : " + str(DriverCar[3]) + "£" +
           "\n" + "Car Plate : " + str(DriverCar[4]) +
           "\n" + "Car Colour : " + str(DriverCar[5])  ) 

    
    CarTimes.update({timeOfJourney:DriverCar})

    SaveStuff(CarTimesData,CarTimes)
    
    print ( "\nThe CarTimes Dictionary :" + str(CarTimes))

    

    Startup()
    



def JourneyRequest():    
    PassengerDestination = input("Where Do you Want to Travel? : ")
    PassengerTime = float(input ("When Do you want to Travel? : "))
    print ("I want to Travel At : " + str(PassengerTime))

    Sorted_CarTimes = OrderedDict(sorted(CarTimes.items(), key=lambda x: x[1]))
    
    for key,value in Sorted_CarTimes.items():
        if PassengerDestination == value[0]:
            if  key >= PassengerTime:

                NumofSeats = value[1] - 1
                print ( "\n" + "Your Journey Details are: " +
                        "\n" +
                        "\n" + "Destination : " + str(value[0]) +
                        "\n" + "Number Of Seats : "  + str(NumofSeats) +
                        "\n" + "Time Of Journey : " + str(value[2]) +
                        "\n" + "Price : " + "£" + str(value[3]) +
                        "\n" + "Car Plate : " + str(value[4]) +
                        "\n" + "Car Colour : " + str(value[5]) +
                        "\n" )

                
                Sorted_CarTimes[value[1]] = NumofSeats

                print("Thank you for using the Lift Server System")

                Exit()
                                
                
                break

            else:
                print("Error Somewhere!")
                print()
                Startup()
                
        else:
            print("No one Travels there :P ")
            print()
            Startup()


  
def SaveStuff(filename,dictname):    
    with open(filename, 'wb') as handle:
      pickle.dump(dictname, handle)
    print("Data Saved!")


def LoadStuff(filename,dictname):
    with open(filename, 'rb') as handle:
      dictname = pickle.loads(handle.read())
    return dictname
    print(dictname) 

def Login(Dict):
    
    username = input("Username : ")
    password = input("Password : ")

    for key,value in Dict.items():
        if username == key: #fix login, CreateAccount driver,customers,12-24hr conversion,
            print("Username Found : " + key)
            if password == Dict[key]:
                print("Password Found : " + Dict[key])
                return("True")
            
        
            else:
            
                print("The Username / Password did not Match , Please Try Again")
                   
        else:
            print("Searching...")

def CreateDriver():
    username = input("Please Enter A username : ")
    password = input("Please Enter A password : ")
    passwordvalidate = input("Please Enter Your Password Again : ")
    print()

    if password == passwordvalidate:
        DriverDict.update({username:password})
        SaveStuff(DriverData,DriverDict)
        print(DriverDict)
        Driver()
    else:
        print("Your Password did not match!")
        Driver()

def CreatePassenger():
    username = input("Please Enter A username : ")
    password = input("Please Enter A password : ")
    passwordvalidate = input("Please Enter Your Password Again : ")
    print()

    if password == passwordvalidate:
        PassengerDict.update({username:password})
        SaveStuff(PassengerData,PassengerDict)
        print(PassengerDict)        
        Passenger()
    else:
        print("Your Password did not match!")
        Passenger()
    

def Driver():
    print("Driver Menu")
    print()
    print("1) Login Driver")
    print("2) Create Driver Account")
    print("3) Exit")

    choice = int(input("Enter Your Choice : "))
    if choice <= 3:
        
        if choice == 1:
            print("You selected Login Driver")
            validate = Login(DriverDict)
            if validate == "True":
                JourneyAnnounce()

        elif choice == 2:
            print("You selected Create Driver")
            CreateDriver()
            
        elif choice == 3:
            Startup()
    
    else:
        print("Please Choose A number From 1 to 3")
        Startup()


def Passenger():
    print("Passenger Menu")
    print()
    print("1) Login Passenger")
    print("2) Create Passenger Account")
    print("3) Exit")
    

    choice = int(input("Enter Your Choice : "))
    if choice <= 3:
        
        if choice == 1:
            print("You selected Login Passenger")
            print()
            validate = Login(PassengerDict)
            if validate == "True":
                JourneyRequest()

        elif choice == 2:
            print("You selected Create Passenger")
            print()
            CreatePassenger()
            
        elif choice == 3:
            print()
            Startup()
    
    else:
        print("Please Choose A number From 1 to 3")
        Startup()
    


def Exit():
    exitprompt = input("Are you Sure you want to Exit? :")
    exitprompt = exitprompt.lower()
    if exitprompt == "y" or exitprompt == "yes":
        print("Thank You for using the System")
        exit()
    else:
        print("Ok")
        Startup()



        
#########################################

#####  Text Based Menu  #################
def Startup():
    #print()
    #print("Car Times = " + str(CarTimes))
    #print("Driver Dict = " + str(DriverDict))
    #print("Passenger Dict = " + str(PassengerDict))

    print()      
    print("Welcome To The Lift Server System")
    print("Please Choose Your Options using corresponding Numbers")
    print()
    print("1) Driver")
    print("2) Passenger")
    print("3) Exit")
    print()


        
    choice = int(input("Enter Your Choice : "))

    

    

    
    if choice <= 3:
        
        if choice == 1:
            print("You selected Login Driver")
            print()
            Driver()

        elif choice == 2:
            print("You selected Login Passenger")
            print()
            Passenger()
            
         
        elif choice == 3:
            print()
            Exit()
                

    else:
        print("Please Choose A number From 1 to 3")
        Startup()
        
    



DriverDict = LoadStuff(DriverData,DriverDict)
PassengerDict = LoadStuff(PassengerData,PassengerDict)
CarTimes = LoadStuff(CarTimesData,CarTimes)
    
Startup() 
        
