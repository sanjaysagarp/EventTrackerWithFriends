import MySQLdb as mdb

con = mdb.connect('localhost','sanjay','sassytaco95','friends')

with con:

    cur = con.cursor()

    cur.execute("CREATE TABLE PERSON_TYPE\
            (\
            PersonTypeID INT PRIMARY KEY AUTO_INCREMENT,\
            PersonTypeName VARCHAR(40) NOT NULL,\
            PersonTypeDesc VARCHAR(140))")

    cur.execute("CREATE TABLE PERSON\
            (\
            PersonID INT PRIMARY KEY AUTO_INCREMENT,\
            PersonFname VARCHAR(20) NOT NULL,\
            PersonLname VARCHAR(20) NOT NULL,\
            PersonTypeID INT NOT NULL)")

    cur.execute("CREATE TABLE EVENT_TYPE\
            (\
            EventTypeID INT PRIMARY KEY AUTO_INCREMENT,\
            EventTypeName VARCHAR(50) NOT NULL,\
            EventTypeDesc VARCHAR(120))")
    
    cur.execute("CREATE TABLE EVENT\
            (\
            EventID INT PRIMARY KEY AUTO_INCREMENT,\
            EventName VARCHAR(250) NOT NULL,\
            EventTypeID INT NOT NULL)")

    cur.execute("CREATE TABLE PERSON_EVENT \
            (\
            PersonEventID INT PRIMARY KEY AUTO_INCREMENT,\
            PersonID INT NOT NULL,\
            EventID INT NOT NULL,\
            EventDate DATE NOT NULL,\
            Attended BIT NOT NULL)")
    # BIT - (0 for False, 1 for True)
    
    cur.execute("ALTER TABLE PERSON_EVENT \
            ADD CONSTRAINT Person_Event_PersonID_FK FOREIGN KEY (PersonID) REFERENCES PERSON(PersonID)")

    cur.execute("ALTER TABLE PERSON_EVENT \
            ADD CONSTRAINT Person_Event_EventID_FK FOREIGN KEY (EventID) REFERENCES EVENT(EventID)")

    cur.execute("ALTER TABLE EVENT \
            ADD CONSTRAINT Event_EventTypeID_FK FOREIGN KEY (EventTypeID) REFERENCES EVENT_TYPE(EventTypeID)")

    cur.execute("ALTER TABLE PERSON \
            ADD CONSTRAINT Person_PersonTypeID_FK FOREIGN KEY (PersonTypeID) REFERENCES PERSON_TYPE(PersonTypeID)")
