# Background

For this exercise, you will write an Appointment class that tracks information about an appointment such as the start and end times and a name for the appointment. Your Appointment class will also have  an  overlaps()  method  that  takes  another  Appointment  object  as  an  argument  and  determines whether the two appointments overlap.


# Instructions

Write a script named a**ppointment.py** containing a class called Appointment with methods as
described below:
- self
- name, a string indicating the name of the appointment (for example, "Sales brunch").
- start, a tuple consisting of two integers representing the start time of the appointment. The first integer represents an hour in 24-hour time; the second integer represents a number of minutes. For example, the tuple (10, 30) would represent 10:30 am.
- end, a tuple similar to start representing the end time of the appointment.

The  __init__()  method  should  create  attributes  name,  start,  and  end,  and  use  them  to  store  the information from the parameters.

**overlaps() method**

Define an overlaps() method with two parameters, self and other, where other is another Appointment object.

This method should return True if self and other overlap and False if they do not. Be sure to return a boolean value rather than a string.

Note that two appointments overlap if
- The  start  time  of  one  appointment  occurs  between  the  start  and  end  times  of  the  other appointment (including if the start times are equal), OR
- The end time of one appointment occurs between the start and end times of the other appointment (including if the end times are equal)

# Docstrings

- Write a docstring for your class that documents the purpose of the class as well as the purpose and expected data type of each attribute.
- For each of the methods you wrote, write a docstring that documents the purpose of the method as well  as  the  purpose  and  expected  data  type  of  each  parameter  other  than  self  (you  never  need  to document self in a docstring). If your document returns a value, document that. If your document has side effects, such as modifying attributes or writing to standard output, document those as well.
- Be  sure  your  docstrings  are  the  first  statement  in  the  class  or  method  they  document.  Improperly
positioned docstrings are not recognized as docstrings by Python.
