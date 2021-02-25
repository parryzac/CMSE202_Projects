# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    year: this is the student current year as an intger
    '''
    
    def __init__(self, name='', gpa=0.0, year=0):
        self.name = name
        self.gpa = gpa
        self.year= year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    
    def enroll(self, courses=[]):
        self.courses= courses
        return
    
    def display_courses(self):
        
        print('I am enrolled in', self.courses)
    
    def years_until_graduation(self):
        self.years_until_graduation= 4 - self.year
        
        print('I have',self.years_until_graduation,'years until graduation')
        
        
class Spartan(Student):
    def __init__(self, name='', motto=''):
        
        self.name= name
        self.motto=motto
        
        return
    
    def set_motto(self, motto):
        self.motto= motto
        return motto
    
    def school_spirit(self):
        print('My name is,',self.name,'\n''I am a spartan. My motto is,', self.motto)
        
        
        
        
    
   