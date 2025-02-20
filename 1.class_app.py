class App():
    def __init__(self,users,username,storage):
        self.users = users
        self.username = username
        self.storage = storage

    def login(self):
        if self.username =="owner" and self.users >= 1 :
            print("you can login: ",self.username)
            print(f"your storage is {self.storage}")
        else:
            print("login denied. ")



    def increase_capacity(self,space):
        self.storage += space
        print("increased storage:",self.storage)

    def check_upgrade(self):
        if self.users >= self.storage:
            amount_increase = int(input("enter the amount by which you want to upgrade: "))
            self.storage += amount_increase
            print(self.storage)
        else:
            print('no need to upgrade storage',self.storage - self.users)


app1 = App(34,"owner",128)
app1.login()
app1.increase_capacity(45)
app1.check_upgrade()
print()
app2 = App(50,"owner",5)
app2.login()
app2.increase_capacity(10)
app2.check_upgrade()


