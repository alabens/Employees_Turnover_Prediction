import sqlite3

class Account() :
    def __init__(self,entreprise,username,password,email):
        self.entreprise=entreprise
        self.username=username
        self.password=password
        self.email=email

    def Add_Account(entreprise,username,email,password):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()

        c.execute("""insert into """ + str(entreprise) + """_users (username,password,email) values (?,?,?)""",
                  (username, password,email))
        conn.commit()
        c.close()
        conn.close()
    Add_Account = staticmethod(Add_Account)


    def Delete_Account(username,entreprise):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("delete from " + str(entreprise) + "_users where username= '" + str(username) + "'")
        conn.commit()
        c.close()
        conn.close()
    Delete_Account = staticmethod(Delete_Account)

    def Edit_Account(username,email,password,entreprise):
        conn = sqlite3.connect('Attrition.db')
        c = conn.cursor()
        c.execute("""Update """ + entreprise + """_users set password=?,email=?
        where username=? """, (password, email, username))
        conn.commit()
        c.close()
        conn.close()
    Edit_Account = staticmethod(Edit_Account)







""""
if __name__ == "__main__":
    Account.Add_Account("fis","alaaaaaaa","alaaaaaaa","alaaaaaa")

"""