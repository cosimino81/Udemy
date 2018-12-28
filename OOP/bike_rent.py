

class BikeStore:
    """docstring for ."""
    def __init__(self, listOfBike):
        self.availableBikes = listOfBike

    def AvailableBikes(self):
        print " "
        print "Available bikes are: "
        for bike in self.availableBikes:
            print bike
        print " "

    def AddBike(self, returnedBike):
        if returnedBike not in self.availableBikes:
            self.availableBikes.append(str(returnedBike))
            print "The bike " +str(returnedBike)+ " was returned, thanks!"
            print " "
        else:
            print "The bike "+str(returnedBike)+" already exist!"

    def RentBike(self, requestedBike):
        if requestedBike in self.availableBikes:
            print "You have borrowed the bike " + requestedBike
            self.availableBikes.remove(requestedBike)
            print " "
        else:
            print "The bike " +str(requestedBike)+ " is not available."


class Customer:
    def RequestBike(self):
        print "Type the name of the bike you want to rent:"
        self.bike = input()
        return self.bike

    def ReturnBike(self):
        print "Type the name of the bike you want to return:"
        self.bike = input()
        return self.bike

store = BikeStore(['Gina', 'Rosa', 'Nina'])
customer = Customer()

while True:
    print " "
    print "Press 1 to know the available bikes"
    print "Press 2 to rent a bike"
    print "Press 3 to return a bike"
    print "Press 4 to quit"
    print " "

    inputNumber = int(input())

    if inputNumber is 1:
        store.AvailableBikes()

    elif inputNumber is 2:
        requested_bike = customer.RequestBike()
        store.RentBike(requested_bike)

    elif inputNumber is 3:
        returned_bike = customer.ReturnBike()
        store.AddBike(returned_bike)

    elif inputNumber is 4:
        quit()
