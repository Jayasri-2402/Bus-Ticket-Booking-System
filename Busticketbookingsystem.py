import os
import platform
import mysql.connector
import datetime

#mydb=mysql.connecter.connect(host="localhost",user="root",password="1111",database="bus",charset="utf8")
def mysqlconnection():
    global mySqlDb
    mySqlDb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1111",
    port="3306",
    database="bus_ticket_booking",
    # auth_plugin="mysql_native_password"
    )
#print(mySqldb)
    mycursor1= mySqlDb.cursor()
    return mycursor1
def registercustomerdetails():
    try:
        mycursor =mysqlconnection()

        buscustlist = []

        customer_id = int(input("Enter customer ID="))
        buscustlist.append(customer_id)

        customer_name = input("Enter customer name=")
        buscustlist.append(customer_name)

        contact_no = int(input("Enter contact no="))
        buscustlist.append(contact_no)

        age = int(input("enter customer age="))
        buscustlist.append(age)

        gender = input("Enter customer gender=")
        buscustlist.append(gender)

        journey_date = input("Enter journey date (yyyy-mm-dd):")
        buscustlist.append(journey_date)

        customer = buscustlist

        sql = "insert into customer(customer_id,customer_name,contact_no,age,gender,journey_date) values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql, customer)
        mySqlDb.commit()
        mycursor.close()

    except Exception as e:
        print(e)

    finally:
        mySqlDb.close()
def registerbusdetails():
    try:
        mycursor = mysqlconnection()

        busdetaillist = []

        customer_id = int(input("Enter customer ID="))
        busdetaillist.append(customer_id)

        bus_id = int(input("Enter bus ID="))
        busdetaillist.append(bus_id)

        bus_name = input("Enter bus name=")
        busdetaillist.append(bus_name)

        destination = input("Enter destination=")
        busdetaillist.append(destination)

        booking_id = int(input("Enter booking ID="))
        busdetaillist.append(booking_id)

        departure_time = input("Enter departure time (HH:MM)=")
        busdetaillist.append(departure_time)

        Bus = busdetaillist

        sql = "insert into busdetails(customer_id,bus_id,bus_name,destination,booking_id,departure_time) values(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql, Bus)
        mySqlDb.commit()
        mycursor.close()

    except Exception as e:
        print(e)

    finally:
        mySqlDb.close()

def registerbookingdetails():
    try:
        mycursor = mysqlconnection()

        bookingcostlist = []

        c_id = int(input("Enter customer ID: "))
        bookingcostlist.append(c_id)

        #Select destination
        print("\nSelect destination")
        print("1.type destination Chennai cost around--->Rs.800")
        print("2.type destination Trichy cost around--->Rs.600")
        print("3.type destination Coimbatore cost around--->Rs.900")
        print("4.type destination Madurai cost around--->Rs.700")

        choice = int(input("Enter your choice="))

        #Bus type selection
        print("\nSelect bus type")
        print("1.type AC Seater Cost (+200)")
        print("2.type AC Sleeper Cost (+500)")
        print("3.type Non/AC Seater Cost (+0)")
        print("4.type Non/AC Sleeper Cost (+300)")

        n = int(input("Enter your choice:"))

        #Bus type Extra cost
        if n == 1:
            extra_cost = 200
        elif n == 2:
            extra_cost = 500
        elif n == 3:
            extra_cost = 0
        elif n == 4:
            extra_cost = 300
        else:
            print("Invalid Bus Type")
            return

        #destination cost
        if choice == 1:
            print("If you go to Chennai.")
            s= 800+extra_cost
        elif choice == 2:
            print("If you go to Trichi.")
            s= 1200+extra_cost
        elif choice == 3:
            print("If you go to Coimbatore.")
            s= 600+extra_cost
        elif choice == 4:
            print("If you go to Madurai.")
            s= 1000+extra_cost
        else:
            print("please enter your type seat")
            return

        ticket_count = int(input("Enter ticket count="))
        bookingcostlist.append(ticket_count)

        total_amount = s*ticket_count
        bookingcostlist.append(total_amount)

        bookingcostlist.append(extra_cost)

        book = bookingcostlist

        sql = "insert into booking(customer_id,ticket_count,total_amount,ext_cost) values(%s,%s,%s,%s)"
        mycursor.execute(sql, book)
        mySqlDb.commit()
        mycursor.close()

        print("\nBooking Added Successfully!")
        print("Total Amount=", total_amount)

    except Exception as e:
        print(e)

    finally:
        mySqlDb.close()

def dispcustdetails():
    try:
        mycursor = mysqlconnection()
        customer_id = int(input("Enter the customer ID whose bill to be view:"))
        sql = "select c.customer_name,c.journey_date,b.bus_id,b.bus_name,b.destination,b.booking_id,b.departure_time,bk.ticket_count,bk.total_amount,bk.ext_cost FROM customer as c INNER JOIN busdetails as b ON c.customer_id=b.customer_id INNER JOIN booking as bk ON c.customer_id=bk.customer_id WHERE c.customer_id=%s"
        r1 = (customer_id,)

        mycursor.execute(sql, r1)
        res = mycursor.fetchall()

        for x in res:
            print(x)
        mycursor.close()

    except Exception as e:
        print(e)

    finally:
        mycursor.close()

def displayallcustomerdetails():
    try:
        mycursor = mysqlconnection()
        sql = "select c.customer_id,c.customer_name,c.contact_no,c.age,c.gender,c.journey_date,b.bus_id,b.bus_name,b.destination,b.booking_id,b.departure_time,bk.ticket_count,bk.total_amount,bk.ext_cost FROM customer as c INNER JOIN busdetails as b ON c.customer_id=b.customer_id INNER JOIN booking as bk ON c.customer_id=bk.customer_id"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        print("Tha customer details are as follows:")

        for x in res:
            print(x)
            mycursor.close()

    except Exception as e:
        print(e)

    finally:
        mycursor.close()

def menuset():

    print("Enter 1: To Enter customer data.")
    print("enter 2: For busdetails.")
    print("Enter 3: Display bookingdetails.")
    print("Enter 4: Display customerwise dtails")
    print("Enter 5: Display All Details.")
    print("enter 6: Exit")

    userinput = int(input("Enter your choice:"))
    if userinput == 1:
        registercustomerdetails()
    elif userinput == 2:
        registerbusdetails()
    elif userinput == 3:
        registerbookingdetails()
    elif userinput == 4:
        dispcustdetails()
    elif userinput == 5:
        displayallcustomerdetails()
    elif userinput == 6:
        quit()
    else:
        print("Sorry! ,invalid option! >> Enter correct choice.")

menuset()

def runagain():
    runagn = input("\nwant to runagain? y/n:")
    while runagn.lower() == "y":

            menuset()
            runagn = input("\nwant to runagain? y/n:")
runagain()

























