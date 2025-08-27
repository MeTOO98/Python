
class person :
    """
    This is a person Class and every person(object) has a name ,an amount of money,a mood with a default value empty string and healthrate with a default value empty string 
    and The class also has methods such as sleep ,eat and buy  
    """
    def __init__(self,name,money=0) :
        self.name=name
        self.money=money
        self.mood=""
        self.healthrate=""

    def sleep(self,hours) :
        if hours ==7 :
            self.mood="happy"
        elif hours <7 :
            self.mood="Tired"
        else:
            self.mood="Lazy"
    
    def eat(self,meals) :
        if meals == 3:
            self.healthrate="100%"
        elif meals ==2 :
            self.healthrate="75%"
        elif meals==1:
            self.healthrate="50%"
        else:
            self.healthrate="UnKnown"

    def buy(self,items) :
        if self.money > items :
            self.money-=10*items 



class Employee(person) :
    """
    This is an Employee Class which is a child class of person and each Employee(object) has an id,a car (default value = None), an email (default value is empty string), 
    a salary (default value = 1000),a distancetowork(deault value =0) , 
    and serval attributes inherited from the parent class such as a name,an amount of money
    ,a mood with a default value empty string and healthrate with a default value empty string 
    and The class also has methods such as work ,drive and refuel.  
    and Note the car must be a car object.
    """
    def __init__(self,id,name,car=None,email="",salary=1000,distancetowork=0):
        super().__init__(name) 
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distancetowork=distancetowork
        


    def work(self,hours):
        if hours ==8 :
            self.mood="happy"
        elif hours >8 :
            self.mood="Tired"
        else :
            self.mood="Lazy"
    
        
    def drive(self,distance):  
        if self.car == None :
            print(f"{self.name} has no car")
            return ""
        else: 
            return self.car.run(distance,60)

    
    def refuel (self,gasAmount) :
      if self.car == None:
          print(f"{self.name} has not a car") 
          return ""
      else :
            if self.car.fuelrate + gasAmount >100 :
                self.car.fuelrate =100 
                return ""
            else :
                if self.car.fuelrate+gasAmount < 0 :
                    self.car.fuelrate =0 
                    return ""
                else:
                    self.car.fuelrate = self.car.fuelrate +gasAmount
                    print(f"car is fuelled with {self.car.fuelrate}")
                    return ""
 
 



class Office :
    """
    This is a office Class and every office(object) has a name and set of employees
    and The class also has methods such as get_all_employees,get_employee,hire_employee,fire_employee,deduct,reward,check lateness,calculate lateness and change_employees_number.
    """
    Countemp=0
    def __init__(self,name):
        self.name=name 
        self.employees=[]        
    
    def get_all_employees(self) :
             return self.employees
    
    def get_employee(self,empid):
       for emp in self.employees :
           if emp.id == empid :
               return emp 
           
    def hire_employee(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)
            Office.Countemp+=1
            print(f"{emp.name} is hired in {self.name}")
            return ""
        else :
            return f"{emp.name} is already hired in {self.name}"


    def fire_employee(self,emp_id) :
        for emp in self.employees :
            if emp.id == emp_id :
                self.employees.remove(emp)
                Office.Countemp-=1
                return f"{emp.id} has been fired from {self.name}"
        else:
            return f"{emp.id} not found in {self.name}"
        

        
    def deduct(self,emp_id,deduction) :
        for emp in self.employees :
            if emp.id == emp_id :
                emp.salary-=deduction
                return f"deducted {deduction} from {emp.id}'s salary"
        return f"{emp.id} is not found"
    
    def reward(self,emp_id,reward) :
        for emp in self.employees :
            if emp.id == emp_id :
                emp.salary+=reward
                return f"rewarded {reward} to {emp.id}'s salary"
        return f"{emp.id} is not found"



    def check_lateness(self,emp_id,move_hour):
        emp =self.get_employee(emp_id)
        if not emp :
            return f"{emp.id} is not found"
        is_late = Office.calculate_lateness(9,move_hour,emp.distancetowork,emp.car.velocity if emp.car != None else 0)
        if is_late == "late" :
            self.deduct(emp_id,10)
        else:
            self.reward(emp_id,10)


    @staticmethod
    def calculate_lateness (target_hour,move_hour,distance,velocity) :
        if velocity <=0 :
            return "late"
        Time=distance/velocity
        if (move_hour+Time) > target_hour :
            return "late"
        else:
            return "Not late"
        
    @classmethod 
    def change_emps_num(cls,num):
        cls.Countemp=num
                


class car :
    """
    This is a Car class and each car(object) has a name , velocity and a fuelrate and The class also has methods such as Run and Stop.
    """
    def __init__(self,velocity,name="",fuelrate=0) :
        self.name =name 
        self.fuelrate=min(max(fuelrate,0),100)
        self.velocity=min(max(velocity,0),200)

    def run(self,distance,velocity) :
        self.velocity=min(max(velocity,0),200)
        while (self.fuelrate) >0 and distance > 0:
            distance-=10
            self.fuelrate-=(self.fuelrate)*0.1
        return self.stop(distance)
        
    def stop(self,distance) :
        self.velocity=0
        if distance == 0 :
            return "you arrive the destintation"
        else:
            return f"you don't have fuel and the remaining distance is {distance}"
        
            



c1=car(20,"fiat",70)
c2=car(40,"toyota",71)
c3=car(80,"hounda",47)
c4=car(44,"ch",77)
c5=car(77,"bmw",80)
e1=Employee(10,"ahmed",c1,"ahmed@yahoo.com",4000,distancetowork=50)
e2=Employee(20,"ali",c2,"ali@yahoo.com",300,distancetowork=70)
e3=Employee(30,"eman",c3,"eman@yahoo.com",4500,distancetowork=100)
e4=Employee(40,"sara",c4,"sara@yahoo.com",6000,distancetowork=24)
e5=Employee(50,"salma",c5,"salma@yahoo.com",6000,distancetowork=24)


of1=Office('hr')
of1.employees.append(e1)
of1.employees.append(e2)
of1.employees.append(e3)
of1.employees.append(e4)

of1.change_emps_num(800)

print(Office.Countemp)



