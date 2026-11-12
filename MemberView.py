from mysql import connector
from datetime import datetime

class GymManager:
    def __init__(self):
        self.connection = connector.connect(
            user = "root",
            database = "gym_db",
            host = 'localhost'
        )
        print("Connected Successfully...")

    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from Member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = """ insert into member( name,place,mobile,plan,fee,joined_date) values (%s,%s,%s,%s,%s,%s)
            """
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Data Inserted Successfully...")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from member"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            for i in records:
                print(i)
        except Exception as e:
            print(e)

member = GymManager()
member.post(name= "Ahana",place = "Kochi",mobile = 8570165438,plan = "Diet",fee = 5000,joined_date = datetime.today())
member.get()
