from sqlalchemy import create_engine

db = create_engine('postgres://oetowqpnbuonwk:b58854c08f68596f8ca36436e93fc3e2ae5e91a77d99f054d1f27bb26e651ba8@ec2-3-216-129-140.compute-1.amazonaws.com:5432/dbhb351ushkvo3')

def fill_string(records):
    string = str(records)
    string = string.replace ("[", "")
    string = string.replace ("]", "")
    string = string.replace (",),", "\n")
    string = string.replace (")", "\n")
    string = string.replace (",)", "")
    string = string.replace ("\'", "")
    string = string.replace ("\\\\r\\", "")
    i = 1
    for char in string:
        if char == "(":
            N = string.index("(")
            string = string[ : N] + str(i)+ "- " + string[N : ]
            if i>=10:
                string = string[ : N+3] + str(i)+ "- " + string[N+5 : ]
            string = string[:N+2] + string[N+4:]
            i = i + 1
    return string
   
def getLocations(num):
    query = "SELECT location FROM company WHERE name IN(Select cname FROM offer WHERE intern_ID IN(SELECT ID FROM internselection))"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
        return "Choose one of the available locations:\n" + string
    if num != -1:
        query3 = "SELECT * FROM internselection WHERE ID IN (SELECT intern_ID From offer WHERE  cname in (SELECT name FROM company where location = %s))" 
        r = db.execute(query3,records[num-1])
        records1 = r.fetchall()
        string = fill_string(records1)
        query2 = "DELETE FROM internSelection"
        db.execute(query2)
        return string

def getDuration(num):
    query = "SELECT duration FROM internselection GROUP BY duration"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
       return "Choose one of the available Durations:\n"+ string
    if num != -1:
        query1 = "SELECT * FROM internselection WHERE  duration = %s " 
        r = db.execute(query1,records[num-1])
        records1 = r.fetchall()
        string = fill_string(records1)
        query2 = "DELETE FROM internSelection"
        db.execute(query2)
        return string

def getField(num):
   query = "SELECT Field FROM internship GROUP BY Field"
   r = db.execute(query)
   records = r.fetchall()
   string = fill_string(records)
   if num == -1:
       return "Choose one of the available Fields:\n" + string
  
   if num != -1:
       query1 = "INSERT INTO internselection SELECT * FROM internship WHERE field = %s "
       r = db.execute(query1,records[num-1])
       query2 = " SELECT internshipTitle FROM internselection WHERE field= %s "
       r = db.execute(query2,records[num-1])
       records1 = r.fetchall()
       string = fill_string(records1)
       return string


def getAllInternships():
    query = "SELECT * FROM internselection"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    query2 = "DELETE FROM internSelection"
    db.execute(query2)
    return "Suitable Internship(/s):\n" + string



#Job functions:
def getMajor(num):
    query = "SELECT Field FROM job GROUP BY Field"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
        return "Choose Your major from the list below\n" + string
    if num != -1:
       
        query1 = "INSERT INTO jobselection SELECT * FROM job WHERE field = %s "
        r = db.execute(query1,records[num-1])
        query2 = " SELECT title FROM jobselection WHERE field= %s"
        r = db.execute(query2,records[num-1])
        records1 = r.fetchall()
        string = fill_string(records1)
        return "The available options:\n" + string 

def getRequiredSkills():
    query1 = "Select skills from jobselection "
    r = db.execute(query1)
    records1 = r.fetchall()
    string = fill_string(records1)
    return "The job offers we have require the following:\n" + string +"\nDo u meet the requirments ?\n" + "1- Yes\n" + "2- No"
            
def getJobLocations(num):
    query = "SELECT location FROM company WHERE name IN(Select c_name FROM has WHERE J_ID IN(SELECT J_ID FROM jobselection))"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
        return "Here is what matches your selection... So glad to help you\n" + string
    if num != -1:
        query3 = "SELECT * FROM jobselection WHERE J_ID IN (SELECT J_ID From has WHERE  c_name in (SELECT name FROM company where location = %s))" 
        #query1 = "SELECT location FROM company WHERE name IN (Select c_name FROM has WHERE J_ID =%s)  "
        r = db.execute(query3,records[num-1])
        records1 = r.fetchall()
        string = fill_string(records1)
        query2 = "DELETE FROM jobselection"
        db.execute(query2)
        return string

def getJobType(num):
    query = "SELECT type FROM jobselection GROUP BY type"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
        return string
    if num != -1:
        query1 = "SELECT * FROM jobselection WHERE  type = %s "
        
        r = db.execute(query1,records[num-1])
        records1 = r.fetchall()
        string = fill_string(records1)
        query2 = "DELETE FROM jobselection"
        db.execute(query2)
        return string

def getExperince(num):
    query = "SELECT experience FROM jobselection GROUP BY experience"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    if num == -1:
        return "Do you have any of the following experiences ?\n" + string
    if num != -1:

        query1 = "Delete FROM jobselection WHERE experience > %s "
        r = db.execute(query1,records[num-1])
        query2 = "SELECT title from jobselection"
        r = db.execute(query2)
        records1 = r.fetchall()
        string = fill_string(records1)
        return string

def getAllJobs():
    query = "SELECT * FROM jobselection"
    r = db.execute(query)
    records = r.fetchall()
    string = fill_string(records)
    query2 = "DELETE FROM jobSelection"
    db.execute(query2)
    return string