class Concentration:
    '''
    Represent concentrations at Babson.
    attributes: name, course_list
    '''
    def __init__(self, name, course_list = []):
        self.name = name
        self.courses = course_list
    
    def add_course(self, course):
        return self.courses.append() 
