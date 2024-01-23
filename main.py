import pandas as pd
print("------------WELCOME TO TRYLIFE------------")
data=pd.read_csv("medical_database_extended.csv")
class Patient:
    def __init__(self,patient_id,name,age,gender,height,weight,bmi,sex_life,STD,diabetes_history,kidney_history,liver_history,respiratory_history,pulmonary_history):
        self.patient_id = patient_id
        self.name=name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.bmi=bmi
        self.sex_life=sex_life
        self.STD=STD
        self.diabetes_history=diabetes_history
        self.kidney_history=kidney_history
        self.liver_history=liver_history
        self.respiratory_history=respiratory_history
        self.pulmonary_history=pulmonary_history

Patient = []

# for i in range(0,10):
#     Patient[i]=Patient()
l=[]
l.append(input("Enter the parameter : "))
dic={}

dic[l[0]]=input("Enter the value : ")
print(dic)
i=1
while i:
    print("Do you want to continue or exit (yes/no) :")
    cont=input("").lower()
    if cont=="yes":
        l.append(input("Enter the parameter : "))
        dic[l[i]]=input("Enter the value : ")
        i+=1
    elif cont=="no":
        break
    else:
        print("Enter the input correctly")

print(dic)
