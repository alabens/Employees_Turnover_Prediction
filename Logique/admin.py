import sqlite3

class Admin:
    def __init__(self,entreprise,username,email,password):
        self.entreprise=entreprise
        self.username=username
        self.email=email
        self.password=password

    def Add_Admin (entreprise,username,password,email):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("""insert into Admins (CompanyName,UserName,Passwd_Admin,Mail_Admin) values (?,?,?,?)""",
                  (entreprise, username, password,email))
        c.execute("""CREATE TABLE """ + str(entreprise) + """(
                                              Id integer primary key ,
                                              First_Name text NOT NULL,
                                              Last_Name text NOT NULL,
                                              Sexe text NOT NULL,
                                              BirthDay date NOT NULL,
                                              Status text NOT NULL,
                                              occupation text NOT NULL,
                                              Departement text NOT NULL,
                                              years_of_employement text NOT NULL,
                                              Total_Experience text NOT NULL,
                                              Companies_Worked text NOT NULL,
                                              Over_Time text NOT NULL,
                                              Distance_from_home text NOT NULL,
                                              Motoriezed text NOT NULL,
                                              salary text NOT NULL,
                                              Job_Level text NOT NULL,
                                              Missions text NOT NULL)""")

        c.execute("""CREATE TABLE """ + str(entreprise) +"""_Users(
                                                username text Primary Key NOT NULL,
                                                password text NOT NULL,
                                                email text UNIQUE NOT NULL)""")
        conn.commit()
        c.close()
        conn.close()
    Add_Admin = staticmethod(Add_Admin)

    def Delete_Admin (entreprise):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("""Delete from Admins where CompanyName= """+"'"+str(entreprise)+"'")
        c.execute("drop table "+str(entreprise))
        c.execute("drop table "+str(entreprise)+"_Users")
        conn.commit()
        c.close()
        conn.close()
    Delete_Admin = staticmethod(Delete_Admin)

    def Edit_Admin (entreprise,username,password,email):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("""Update Admins set UserName=?,Passwd_Admin=?,Mail_Admin=? where CompanyName=? """, (username, password, email,entreprise))
        conn.commit()
        c.close()
        conn.close()
    Edit_Admin = staticmethod(Edit_Admin)





if __name__ == "__main__":
    """
    conn = sqlite3.connect('Attrition.db')
    c = conn.cursor()
    c.execute("drop table Admins")
    c.execute("CREATE TABLE  Admins(CompanyName text primary key NOT NULL,UserName text NOT NULL,Passwd_Admin text NOT NULL,Mail_Admin text UNIQUE NOT NULL )")
    
    """
    #Admin.Add_Admin("sofrecom","sofrecom","sofrecom@sofrecom.tn","1234")

    #Admin.Edit_Admin("ala","sofrecom","sofrecom@sofrecom.tn","0000")
    #Admin.Delete_Admin("fis")
    #Admin.Add_Admin("fis","fis","1234","fis@global.tn")
    #Admin.Delete_Admin("fis")










