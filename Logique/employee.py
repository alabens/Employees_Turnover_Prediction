import sqlite3

class Employee:
    def __init__(self,id,first_name,last_name,sex,birth_day,status,departement,years_of_employment,experience,
                 companies_worked,over_time,distance,motorized,salary,level,missions):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.birth_day=birth_day
        self.status=status
        self.departement=departement
        self.years_of_employment=years_of_employment
        self.experience=experience
        self.companies_worked=companies_worked
        self.over_time=over_time
        self.distance=distance
        self.motorized=motorized
        self.salary=salary
        self.level=level
        self.missions=missions

    def add_Employee(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                     text13, text14, text15, text16, text17,text18):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()

        c.execute("""insert into """ + text18 + """ (id,First_Name, Last_Name,Sexe,BirthDay,Status,occupation,Departement,years_of_employement,
                Total_Experience,Companies_Worked,Over_Time,Distance_from_home,Motoriezed,salary,Job_Level,Missions) 
                values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14,
            text15, text16, text17))

        conn.commit()
        c.close()
        conn.close()
    add_Employee = staticmethod(add_Employee)


    def edit_Employee(text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12,
                      text13, text14, text15, text16,text17,text18):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("""Update """ + text18 + """ set First_Name=?, Last_Name=?,Sexe=?,BirthDay=?,Status=?,occupation=?,
                   Departement=?,years_of_employement=?,
                   Total_Experience=?,Companies_Worked=? , Over_Time=? , Distance_from_home=? , Motoriezed=? , salary=?, Job_Level=?, Missions=? where Id=? 
                   """, (
            text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15,
            text16, text17,
            text1))
        conn.commit()
        c.close()
        conn.close()
    edit_Employee = staticmethod(edit_Employee)

    def delete_Employee(text1,text2):

        A = text1
        B =str(text2)
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("delete from " + B + " where Id= " + A)
        conn.commit()
        c.close()
        conn.close()

    delete_Employee = staticmethod(delete_Employee)




