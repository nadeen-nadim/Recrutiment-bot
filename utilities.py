import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    db="recruitment"
)

def getLocations(num):
    cursor = db.cursor()
    query = "SELECT location FROM company WHERE name IN(Select cname FROM offer WHERE intern_ID IN(SELECT ID FROM internselection))"
    cursor.execute(query)
    records = cursor.fetchall()
    if num == -1:
        return records
    if num != -1:
        query3 = "SELECT * FROM internselection WHERE ID IN (SELECT intern_ID From offer WHERE  cname in (SELECT name FROM company where location = %s))" 
        cursor.execute(query3, records[num-1])
        records1 = cursor.fetchall()
        query2 = "DELETE FROM internSelection"
        cursor.execute(query2)
        db.commit()
        return records1



def getDuration(num):
    cursor = db.cursor()
    query = "SELECT duration FROM internselection GROUP BY duration"
    cursor.execute(query)
    records = cursor.fetchall()
    if num == -1:
       return records
    if num != -1:
       
        query1 = "SELECT * FROM internselection WHERE  duration = %s " 
        cursor.execute(query1,records[num-1])
        records1 = cursor.fetchall()
        query2 = "DELETE FROM internSelection"
        cursor.execute(query2)
        db.commit()
        return records1
    




def getField(num):
    cursor = db.cursor()
    query = "SELECT Field FROM internship GROUP BY Field"
    cursor.execute(query)
    records = cursor.fetchall()
    
    if num == -1:
        return records
    
   
    if num != -1:
        
        query1 = "INSERT INTO internselection SELECT * FROM internship WHERE field = %s "
        cursor.execute(query1,records[num-1])
        db.commit()
        query2 = " SELECT internshipTitle FROM internselection WHERE field= %s "
        cursor.execute(query2,records[num-1])
        records1 = cursor.fetchall()
        return records1

def getAllInternships():
    cursor = db.cursor()
    query = "SELECT * FROM internselection"
    cursor.execute(query)
    records = cursor.fetchall()
    query2 = "DELETE FROM internSelection"
    cursor.execute(query2)
    db.commit()
    return records



#Job functions:
def getMajor(num):
    cursor = db.cursor()
    query = "SELECT Field FROM job GROUP BY Field"
    cursor.execute(query)
    records = cursor.fetchall()
    
    if num == -1:
        return records
    if num != -1:
       
        query1 = "INSERT INTO jobselection SELECT * FROM job WHERE field = %s "
        cursor.execute(query1,records[num-1])
        db.commit()
        query2 = " SELECT title FROM jobselection WHERE field= %s"
        cursor.execute(query2,records[num-1])
        records1 = cursor.fetchall()
        return records1

def getRequiredSkills(num):
    cursor = db.cursor()
    if num != -1:
      
        query1 = "Select skills from jobselection "
        cursor.execute(query1)
        records1 = cursor.fetchall()
        return records1
            
def getJobLocations(num):
    cursor = db.cursor()
    query = "SELECT location FROM company WHERE name IN(Select c_name FROM has WHERE J_ID IN(SELECT ID FROM jobselection))"
    cursor.execute(query)
    records = cursor.fetchall()
    if num == -1:
        return records
    if num != -1:
        query3 = "SELECT * FROM jobselection WHERE ID IN (SELECT J_ID From has WHERE  c_name in (SELECT name FROM company where location = %s))" 
        #query1 = "SELECT location FROM company WHERE name IN (Select c_name FROM has WHERE J_ID =%s)  "
        cursor.execute(query3,records[num-1])
        records1 = cursor.fetchall()
        query2 = "DELETE FROM jobselection"
        cursor.execute(query2)
        db.commit()
        return records1

def getJobType(num):
    cursor = db.cursor()
    query = "SELECT type FROM jobselection GROUP BY type"
    cursor.execute(query)
    records = cursor.fetchall()
    if num == -1:
        return records
    if num != -1:
        query1 = "SELECT * FROM jobselection WHERE  type = %s "
        
        cursor.execute(query1,records[num-1])
        records1 = cursor.fetchall()
        query2 = "DELETE FROM jobselection"
        cursor.execute(query2)
        db.commit()
        return records1

def getExperince(num):
    cursor = db.cursor()
    query = "SELECT experience FROM jobselection GROUP BY experience"
    cursor.execute(query)
    records = cursor.fetchall()
    if num == -1:
        return records
    if num != -1:

        query1 = "Delete FROM jobselection WHERE experience > %s "
        cursor.execute(query1,records[num-1])
        db.commit()
        query2 = "SELECT title from jobselection"
        cursor.execute(query2)
        records1 = cursor.fetchall()
        return records1

def getAllJobs():
    cursor = db.cursor()
    query = "SELECT * FROM jobselection"
    cursor.execute(query)
    records = cursor.fetchall()
    query2 = "DELETE FROM jobSelection"
    cursor.execute(query2)
    db.commit()
    return records