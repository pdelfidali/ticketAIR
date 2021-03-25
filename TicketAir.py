import sqlite3

class Flight:
    def __init__(self):
        self.origin = ''
        self.destination = ''
        self.flightNumber = ''
        self.airplane = None
        self.date = None
        self.price = 0
        self.time = 0

    def __init__(self, origin, destination, flightNumber, airplane, date, price, time):
        self.origin = origin
        self.destination = destination
        self.flightNumber = flightNumber
        self.airplane = airplane
        self.date = date
        self.price = price
        self.time = time

    def values(self):
        return f'("{self.origin}", "{self.destination}", "{self.flightNumber}", "{self.airplane.tailNumber}", "{self.date}", {self.price}, {self.time})'


class Plane:
    def __init__(self):
        self.yearOfProduction = 0
        self.flightMiles = 0
        self.capacity = 0
        self.tailNumber = ''

    def __init__(self, yearOfProduction, flightMiles, capacity, tailNumber):
        self.yearOfProduction = yearOfProduction
        self.flightMiles = flightMiles
        self.capacity = capacity
        self.tailNumber = tailNumber

    def values(self):
        return f'("{self.tailNumber}", "{self.yearOfProduction}", "{self.flightMiles}", "{self.capacity}")'

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

class Passenger:
    def __init__(self):
        self.name = None
        self.tickets = None
        self.address = None
        self.password = None
        self.login = None

    def __int__(self, name, tickets, address, password, login):
        self.name = name
        self.tickets = tickets
        self.address = address
        self.password = password
        self.login = login

    def values(self):
        #Trzeba dodać ID
        isAdmin = int(isinstance(self, Admin))
        return f'("ID", "{self.name}", "{self.tickets}", "{isAdmin}", "{self.password}", "{self.login}")'

class Admin (Passenger):
        def __init__(self):
            super().__init__()

        def addFlight(self, flight):
            flight.add(self)

        def addPlane(self, plane):
            plane.add(self)

        def cancelFlight(self, flight):
            flight.cancel(self)

        def removePlane(self, plane):
            plane.remove(self)

class DataBase:
    def __init__(self):
        print("Init")

    def create_tables(self):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        try:
            cur.execute('''CREATE TABLE flights
                            (origin text, destination text, flightNumber text, planeTailNumber text, date text, price real, time real)
                        ''')
        except sqlite3.OperationalError:
            pass
        try:
            cur.execute('''CREATE TABLE planes
                            (tailNumber text, year integer, flightMiles real, capacity integer)
                        ''')
        except sqlite3.OperationalError:
            pass
        try:
            cur.execute('''CREATE TABLE users
                            (userID text, name text, ticketsIDs text, isAdmin integer, password text, login text)
                        ''')
        except sqlite3.OperationalError:
            pass
        try:
            cur.execute('''CREATE TABLE tickets
                            (flightNumber text, day text, price real)
                        ''')
        except sqlite3.OperationalError:
            pass
        con.commit()
        con.close()

    def addFlight(self, flight):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute('INSERT INTO flights VALUES ' + flight.values())
        con.commit()
        con.close()

    def addPlane(self, plane):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute('INSERT INTO planes VALUES ' + plane.values())
        con.commit()
        con.close()

    def addUser(self, user):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute('INSERT INTO users VALUES ' + user.values())
        con.commit()
        con.close()

    def getPlane(self, tailNumber):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM planes WHERE tailNumber = "{tailNumber}"')
        tailNumber, year, flightMiles, capacity = cur.fetchone()
        con.close()
        return Plane(year, flightMiles, capacity, tailNumber)

    def getDestinations(self, origin):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM flights WHERE origin="{origin}"')

        rows = cur.fetchall()
        destinations = []
        for origin, destination, flightNumber, planeTailNumber in rows:
            destination.append(Flight(origin, destination, flightNumber, DataBase.getPlane(tailNumber=planeTailNumber)))
        con.close()
        return destinations

    def getOrigins(self, destination):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM flights WHERE destination="{destination}"')

        rows = cur.fetchall()
        destinations = []
        for origin, destination, flightNumber, planeTailNumber in rows:
            destination.append(Flight(origin, destination, flightNumber, DataBase.getPlane(tailNumber=planeTailNumber)))
        con.close()
        return destinations


    def login(self, login, password):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'SELECT * FROM users WHERE login="{login}"')

        userID, name, ticketsIDs, isAdmin, passwordData, loginData = cur.fetchone()
        con.close()
        if passwordData == password:
            return Passenger(name, ticketsIDs, "", password, loginData)
        else:
            return None

    def cancelFlight(self, flightNumber):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'DELETE FROM flights WHERE flightNumber="{flightNumber}"')
        con.close()

    def removePlane(self, tailNumber):
        con = sqlite3.connect('ticketair.db')
        cur = con.cursor()
        cur.execute(f'DELETE FROM planes WHERE tailNumber="{tailNumber}"')
        con.close()

if __name__ == '__main__':
    currentUser = None
    boeing737 = Plane(2000, 0, 150, 'LOTPL2115')
    KRK2WAW = Flight('Krakow', 'Warszawa', 'LOT0354', boeing737, '12/12/25', 15, 0.80)
    db = DataBase()
    plane = db.getPlane('LOTPL2115')
    print(plane.values())
    print(KRK2WAW.values())
    db.create_tables()
