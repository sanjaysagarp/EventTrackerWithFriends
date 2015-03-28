import MySQLdb as mdb

con =  mdb.connect('localhost','sanjay','sassytaco95','friends')

with con:

    cur = con.cursor()
    statement ='''
    CREATE FUNCTION udfCalculateEventsAttended(ID INT)
    RETURNS INT
    BEGIN
        RETURN(SELECT COUNT(Attended) FROM PERSON_EVENT
        WHERE PersonID = ID AND Attended = '1');
    END;
    '''
    cur.execute(statement)
    statement = '''
    CREATE FUNCTION udfCalculateTotalEvents(ID INT)
    RETURNS INT
    BEGIN
        RETURN(SELECT COUNT(Attended) FROM PERSON_EVENT
        WHERE PersonID = ID);
    END;
    '''
    #cur.execute(statement)
             
