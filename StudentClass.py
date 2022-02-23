class Student:
    def __init__(self, ID, Name, DOB, Class):
        self.__StudentID = ID
        self.__Student_Name = Name
        self.__Student_DOB = DOB
        self.__Student_Class = Class

    def Calc_age(self, age):
        self.__Student_DOB = age

        #calculation
    def Reg_date(self, date):
        self.__Student_Class = date

#test