###################################################################
#                                                                 #
#                    Car Lift Booking System                      #
#                                                                 #
###################################################################

from collections import OrderedDict # Save to a dictionary with a list format which is later stored
import datetime    # import time functions to help store user inputs and record real time
import pickle       # Load the dictionary back from the pickle file.
import sys          


#######################################

#Variables

i = 0 #Used as an incrementer later on
CarTimes = {} #libary variable

PassengerTime = 0 #variable to set when the passenger wants to leave for the next ride

########################################
#Login Data

DriverData = "DriverUserData.txt" # text file for driveruserdata
PassengerData = "PassengerUserData.txt"  # text file for passenger user data


DriverDict = {"user1" : "abc" , "user2" : "def"} #the driver Libary for the logins(more can be added)
PassengerDict = {"user3" : "abc" , "user4" : "def", "user5" : "ghi"} #The passenger libary for the logins(more can be added)









def JourneyAnnounce():
    carCount = i + 1
    
    #listNameCounter = "Car" + str(carCount)
    destination = input("Destination : ")
    numberOfSeats = int(input("Number Of Seats in your car : "))
    timeOfJourney = float(input("Time of Journey (Input in decimal e.g 10:30 is 10.5) : "))
    journeyPrice = input("Price To Charge : ")
    carPlate = input("Car Plate : ")
    colour = input("Car Colour : ")
    
    DriverCar = (destination, numberOfSeats,timeOfJourney,journeyPrice,carPlate, colour)

    print("\n__________________SUMMARY__________________")
    
    print ("\n" + "This is Car No : " + str(carCount) +
           "\n" + "Destination : " + str(DriverCar[0]) +
           "\n" + "Number Of Seats : "  + str(DriverCar[1]) +
           "\n" + "Time Of Journey : " + str(DriverCar[2]) +
           "\n" + "Price To Charge : " + str(DriverCar[3]) + "£" +
           "\n" + "Car Plate : " + str(DriverCar[4]) +
           "\n" + "Car Colour : " + str(DriverCar[5])  ) 

    print("\n__________________END__________________\n")

    
    prompt = input("Are the details correct? (Yes/No) :")#Receive an input 
    prompt.lower()#Lower cap all the letters
    if prompt == "y" or prompt == "yes":#if statemnt which detects string
        CarTimes.update({timeOfJourney:DriverCar})
        print("Your details have been saved!")
        print ( "\n The CarTimes Dictionary :" + str(CarTimes))
        Startup()
    
    else:
        print("Please Re-enter Your details")#goes back to main menu
        JourneyAnnounce();
    
    
  



def JourneyRequest():    
    PassengerDestination = input("Where Do you Want to Travel? : ")
    PassengerTime = float(input ("When Do you want to Travel? (Input in decimal e.g 10:30 is 10.5) : "))
    print ("I want to Travel At : " + str(PassengerTime))

    Sorted_CarTimes = OrderedDict(sorted(CarTimes.items(), key=lambda x: x[1]))
    
    
    for key,value in Sorted_CarTimes.items():
        if PassengerDestination == value[0]:
            if  key >= PassengerTime:

                NumofSeats = value[1] - 1
                print (
                        "\n" + "Destination : " + str(value[0]) +
                        "\n" + "Number Of Seats : "  + str(NumofSeats) +
                        "\n" + "Time Of Journey : " + str(value[2]) +
                        "\n" + "Price : " + str(value[3]) + "£" +
                        "\n" + "Car Plate : " + str(value[4]) +
                        "\n" + "Car Colour : " + str(value[5])  )
                Sorted_CarTimes[value[1]] = NumofSeats

                print (value[1])

                Startup()
                                
                
                break

            else:
                print("Error Somewhere!")
        else:
            print("No one Travels there. ")
        


def Time12To24Converter():
    m2 = "11:30"
    currenttime = datetime.datetime.now().time().strftime("%H:%M")
    if currenttime >= "10:00" and currenttime <= "13:00":
        if m2 >= "10:00" and m2 >= "12:00":
            
            m2 = ("""%s%s""" % (m2, " AM"))
        else:
            m2 = ("""%s%s""" % (m2, " PM"))
    else:
            m2 = ("""%s%s""" % (m2, " PM"))
            m2 = datetime.datetime.strptime(m2, '%I:%M %p')
            m2 = m2.strftime("%H:%M %p")
            m2 = m2[:-3]
            print (m2)
    



def SaveStuff(filename,dictname):    
    with open(filename, 'wb') as handle:
      pickle.dump(dictname, handle)


def LoadStuff(filename,dictname):
    with open(filename, 'rb') as handle:
      dictname = pickle.loads(handle.read())
    print (dictname) 

def Login(Dict):
    username = input("Username : ")
    password = input("Password : ")

    for key,value in Dict.items():
        if username == key: #fix login, CreateAccount driver,customers,12-24hr conversion,
            print(key)
            if password == Dict[key]:
                print(password)
                return("True")
            
        
            else:
            
                print("The Username / Password did not Match , Please Try Again")
                   
        else:
            print("Searching...")

def CreateDriver():
    username = input("Please Enter A username : ")
    password = input("Please Enter A password : ")
    passwordvalidate = input("Please Enter Your Password Again :")
    print()

    if password == passwordvalidate:
        DriverDict.update({username:password})
        print(DriverDict)
        Driver()
    else:
        print("Your Password did not match!")
        Driver()
    

def Driver():#driver branches
    print("Driver Menu")
    print()
    print("1) Login Driver")
    print("2) Create Driver Account")
    print("3) Exit")

    choice = int(input("Enter Your Choice : "))
    if choice <= 3 and choice >= 0:
        
        if choice == 1:
            print("You selected Login Driver")
            validate = Login(DriverDict)
            if validate == "True":
                JourneyAnnounce()

        elif choice == 2:
            print("You selected Create Driver")
            CreateDriver()
            
            
            
                

        elif choice == 3:
            Exit()#Goes to the function.
                

    else:
        print("Please Choose A number From 1 to 3")#ensures number is 1-3 if not it loops back and reruns program
        Startup()


def Exit():#proc to leave program
    exitprompt = input("Are you Sure you want to Exit? :")#Receive an input 
    exitprompt.lower()#Lowwer cap all the letters
    if exitprompt == "y" or exitprompt == "yes":#if statemnt which detects string
        print("Thank You for using the System")#goodbye message
        exit() #actually terminates program, no need for sys.
    else:
        print("Ok")#goes back to main menu
#########################################

#####  Text Based Menu  #################
def Startup():#Main Method

      
    print("Welcome To The Lift Server System")
    print("Please Choose Your Options using corresponding Numbers")#number of differnt options
    print()
    print("1) Driver")
    print("2) Passenger")
    print("3) Exit")
    print()


    choice = int(input("Enter Your Choice : "))
    if choice <= 3:
        
        if choice == 1:
            print("You selected Login Driver")
            Driver()

        elif choice == 2:
            print("You selected Login Passenger")
            validate = Login(PassengerDict)
            if validate == "True":
                JourneyRequest()
            
                

        elif choice == 3:
            exit()
                

    else:
        print("Please Choose A number From 1 to 3")
        Startup()
#all the three options all lead to different parts of the program. the options 1 and 2 lead to their seperate branches
#Which allows you to create drivers or passengers. the third option allows you to exit the program. 
    


Startup()        
#Initialisation
