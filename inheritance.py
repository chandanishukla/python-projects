class SBI:  # single inheritance
    def assign(self):
        self.ifsc='SBI10023'
        self.bname='HYD'
class customer(SBI):
    def __init__(self,cid,cname):
        self.cid = cid
        self.cname = cname
    def display(self):
        print(self.ifsc)
        print(self.bname)
        print(self.cid)
        print(self.cname)
e1=customer(201,'chandani')
e1.assign()
e1.display()


class SBI: #mutiple  inheritance
    def register(self):
        print("Register in SBI bank")
class VISA:
    def login(self):
        print("login in VISA")
class customer(SBI,VISA):
    def display(self):
        print("customer information")
e1=customer()
e1.register()
e1.login()
e1.display()


class RBI: #multilevel inheritance
    def assign(self):
        self.repo=6.5
        self.revrepo=7
class SBI(RBI):
    def  register(self):
        self.cid=1001
        self.cname='chandani'
class customer(SBI):
    def display(self):
        print(self.repo)
        print(self.revrepo)
        print(self.cid)
        print(self.cname)
e1=customer()
e1.assign()
e1.register()
e1.display()



class SBI: #hierarchical inheritance
    def register(self):
        print("SBI registration")
class customer(SBI):
    def balanceEnq(self):
        print("check your balance")
class employee(SBI):
    def login(self):
        print("employee login")
e1=customer()
e2=employee()
e1.register()
e1.balanceEnq()
e2.register()
e2.login()
















