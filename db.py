import matplotlib.pyplot as plt 
import mysql.connector as mysql

mydb = mysql.connect(
  host="localhost",
  user='root',
  passwd="{sudha}",
  #after creating the database
  database='student'
)

mycursor=mydb.cursor()
#we can execute mysql commands using my cursor.execute()

#creating database and table -run it only for first time
#mycursor.execute("create database student;use student;")
#mycursor.execute("create table marks(students varchar(20),rollno integer(15), mark integer(3));")

students_passed=[]
students_failed=[]

#function to fetch records from the db
def fetch():
    mycursor.execute("SELECT mark FROM marks ")
    myresult = mycursor.fetchall()
    for i in myresult:
        i=i[0]
        if i>40:
            students_passed.append(i)
        else:
            students_failed.append(i)
        
#function to update records
def update():
    print('-----------------------------------------------------------------')
    print("Enter entries seperated by space as displayed, to update database")
    print("Student-name Roll-no Marks\n")
    #mycursor.execute('SHOW COLUMNS FROM marks')
    #result=mycursor.fetchall()
    #1print(result)
    print('Enter "c" to exit updating')
    while(True):
        data=list(input().split(" "))
        if data[0]=='c':
            start()
            break
        data[1]=int(data[1])
        data[2]=int(data[2])
        data=tuple(data)
        print(data)
        mycursor.execute("INSERT INTO marks (students, rollno, mark) VALUES ('{:s}',{:d},{:d})".format(*data))
        mydb.commit()
        print("1 record inserted")

def grap():
    # plotting a histogram 
    rang = (0, 100) 
    bins = 10
    plt.hist([students_passed,students_failed], bins,rang, color = ['green','red'], 
            histtype = 'bar', rwidth = 0.8) 
    # x-axis label 
    plt.xlabel('marks') 
    # frequency label 
    plt.ylabel('No. of students') 
    # plot title 
    plt.title('students_passed: '+str(len(students_passed))+" students_failed: "+str(len(students_failed))) 
    # function to show the plot 
    plt.show() 

def show():
    mycursor.execute('select students from marks where mark>=40;')
    myresult = mycursor.fetchall()
    print("-------------DETAILED REPORT-------------")
    print("PASSED STUDENTS: ")
    for i in myresult:
        print(i[0])
    print('\n')
    mycursor.execute('select students from marks where mark<40;')
    myresult = mycursor.fetchall()
    print("FAILED STUDENTS: ")
    for i in myresult:
        print(i[0])
    


def start():
    print("--------------STUDENT DATABASE-------------")
    print("STUDENT-NAME STUDENT-ROLLNO STUDENT-MARKS")
    mycursor.execute("select * from marks")
    results=mycursor.fetchall()
    for i in results:
        print(i)
    print('1-update database\n2-show graph')
    n=int(input("Enter your choice:"))
    if n==1:
        update()
    if n==2:
        fetch()
        show()
        grap()
start()





'''
# frequencies 
marks = [2,5,70,40,30,45,50,45,43,40,44, 
		60,7,13,57,18,90,77,32,21,20,40] 
students_passed=[]
students_failed=[]
for mark in marks:
    if mark>35:
        students_passed.append(mark)
    else:
        students_failed.append(mark)


# setting the ranges and no. of intervals 
rang = (0, 100) 
bins = 10

plt.hist([students_passed,students_failed], bins,rang, color = ['green','red'], 
		histtype = 'bar', rwidth = 0.8) 

plt.xlabel('marks') 
# frequency label 
plt.ylabel('No. of students') 
# plot title 
plt.title('students_passed: '+str(len(students_passed))+" students_failed: "+str(len(students_failed))) 
plt.show() 
'''


