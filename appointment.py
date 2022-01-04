class Appointment:

    """
    Monitar the information about an appointment. 
    
    Class methods:
    __init__: initialize class variables 
    overlap: Check if two appoitments overlaps or not
    """
    
    def __init__(self, name, start, end):

        """
        Define a __init__() with self, name, start, end parameter. 
        Install the class variable to store information in the variables. 

        name(string): name of the appointmnet 
        start(tuple): start (time) of the appoinment 
        end(tuple): end (time) of the appointment 
    
        """
        self.name = name
        self.start = start
        self.end = end

    def overlaps(self, other):

        """
       Check if two appointment overlaps or not
       other(appointmnet class): The second appointment class instance 

       Return:
       True if both appointments overlap
       False if both appointment does not overlap. 

        """
        return (self.start <= other.start < self.end) or (self.start < other.end <= self.end)
        
