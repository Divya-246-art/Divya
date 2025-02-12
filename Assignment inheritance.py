class university():
    def College(self,a,b):
        print("City name:",a)
        print("No of departments:",b)
class fees():
    def details(self,c,d,e):
        print("Hostel fee:",c)
        print("Transportation fee:",d)
        print("Tution fee:",e)
class students():
    def info(self,f,g):
        print("No of students placed:",f)
        print("No of companies:",g)
class final(university,fees,students):
    pass
SRM=final()
SRM.College("Chennai",20)
SRM.details(20000,6500,50000)
SRM.info(1000,150)
RVS=final()
RVS.College("Sulur",35)
RVS.details(15000,7500,60000)
RVS.info(1200,250)
