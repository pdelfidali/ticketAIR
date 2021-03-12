class Flight:
    def __init__(self):
        self.origin = ''
        self.destination = ''
        self.flightNumber = ''
        self.airplane = None

    def __int__(self, origin, destination, flightNumber, airplane):
        self.origin = origin
        self.destination = destination
        self.flightNumber = flightNumber
        self.airplane = airplane


class Plane:
    def __init__(self):
        self.yearOfProduction = 0
        self.flightMiles = 0
        self.capacity = 0

    def __init__(self, yearOfProduction, flightMiles, capacity):
        self.yearOfProduction = yearOfProduction
        self.flightMiles = flightMiles
        self.capacity = capacity

class Ticket:
    def __init__(self):
        self.flight = None
        self.day = None
        self.price = 0

    def __init__(self, flight, day, price):
        self.flight = flight
        self.day = day
        self.price = price

    def buyTicket(self, passenger):
        passenger.tickets.append(self)