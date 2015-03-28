import getpass, MySQLdb as mdb

print("\nHello! Welcome to the simple friends database!")
print("Please Log in to continue")

user = raw_input("Username: ")
pswd = getpass.getpass()
con = mdb.connect("localhost", user, pswd, 'friends')
with con:    
    cur = con.cursor()
    running = True
    while running:
        print("What would you like to do?")
        testVar = raw_input('[V]iew\t [A]dd\t [E]dit\n')
        testVar = testVar.lower()
        checkS1 = testVar not in ['v', 'a', 'e']
        while checkS1:  
            testVar = raw_input('Please Try Again. \n[V]iew\t [A]dd\t [E]dit\n')
            checkS1 = testVar not in ['v', 'a', 'e']
        #Check success rate of hangouts for each person
        if testVar == 'v':
            cur.execute('SELECT PersonFname, PersonLname, udfCalculateEventsAttended(PersonID) AS Events_Attended, udfCalculateTotalEvents(PersonID) AS Total_Events FROM PERSON')
            data = cur.fetchall()
            for row in data:
                print row[0], row[1], row[2], row[3]
            raw_input('Press Enter to Continue.')
        
        if testVar == 'a':
            print("What would you like to add? \n1: Friend \n2: Event \n3: Type of Friend \n4: Type of Event\n5: Existing Friend with Event")
            responseA = raw_input('Enter a number: ')
            responseA = int(responseA)
            checkSa = responseA not in [1,2,3,4,5]
            while checkSa:
                responseA = raw_input('Try Again. Enter another number: ')
                checkSa = responseA not in [1,2,3,4,5]
    
            #Check went through for adding. What are the requirements to add someone?
            #Options: Add persontype, eventtype, person, event
    
            if responseA == 1:
                Fname = raw_input('First Name: ')
                Lname = raw_input('Last Name: ')
                PersonType = raw_input('Type of Friend (Existing): ')
                try:
                    cur.execute('INSERT INTO PERSON(PersonFname, PersonLname, PersonTypeID) VALUES(%s, %s, (SELECT PersonTypeID FROM PERSON_TYPE WHERE PersonTypeName = %s))',(Fname, Lname, PersonType))
                    con.commit()
                    print('Success!\n')
                except:
                    print(cur._last_executed)
                    raise
            elif responseA == 2:
                eventName = raw_input('Event Name: ')
                eventType = raw_input('Event Type (Existing): ')
                try:
                    cur.execute('INSERT INTO EVENT(EventName, EventTypeID) VALUES(%s,(SELECT EventTypeID FROM EVENT_TYPE WHERE EventTypeName = %s))',(eventName, eventType))
                    con.commit()
                    print('Success!\n')
                except:
                    print(cur._last_executed)
                    raise
            elif responseA == 3:
                friendTypeName = raw_input('Friend Type Title: ')
                friendTypeDesc = raw_input('Friend Type Description: ')
                try:
                    cur.execute('INSERT INTO PERSON_TYPE(PersonTypeName, PersonTypeDesc) VALUES(%s,%s)', (friendTypeName,friendTypeDesc))
                    con.commit()
                    print('Success!\n')
                except:
                    print(cur._last_executed)
                    raise
            elif responseA == 4:
                eventTypeName = raw_input('Event Type Name: ')
                eventTypeDesc = raw_input('Event Type Desc: ')
                try:
                    cur.execute('INSERT INTO EVENT_TYPE(EventTypeName, EventTypeDesc) VALUES (%s,%s)',(eventTypeName,eventTypeDesc))
                    con.commit()
                    print('Success!\n')
                except:
                    print(cur._last_executed)
                    raise
            elif responseA == 5:
                cur.execute('SELECT PersonID, PersonFname, PersonLname FROM PERSON')
                data = cur.fetchall()
                for row in data:
                    print row[0], row[1],  row[2]
                existingFriendID = raw_input('Which Friend? (Use ID!): ')
                cur.execute('SELECT EventID, EventName FROM EVENT')
                data = cur.fetchall()
                for row in data:
                    print row[0], row[1]
                existingEventID = raw_input('Which Event? (Use ID!): ')
                date = raw_input('When? (YYYY-MM-DD): ')
                attendance = raw_input('Attended? (y/n): ')
                attendance = attendance.lower()
                if attendance == 'y':
                    attended = 1
                elif attendance == 'n':
                    attended = 0
                try:
                    cur.execute('INSERT INTO PERSON_EVENT(PersonID, EventID, EventDate, Attended) VALUES (%s, %s, %s, %s)',(int(existingFriendID), int(existingEventID), date, int(attended)))
                    con.commit()
                    print('Success!\n')
                except:
                    print(cur._last_executed)
                    raise


