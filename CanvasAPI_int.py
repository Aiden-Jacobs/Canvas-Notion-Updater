from canvasapi import Canvas
import OptionsGUI

class CanvasTool:
    """
    This module contains the CanvasTool class that interacts with the Canvas API.

    CanvasTool:
    A class that allows for interaction with the Canvas API.

    Methods:
    - init(self, url, key): Initializes a new Canvas object.
    - get_user_selections(self): Gets the current courses from a user.
    - get_course(self, CourseID): Gets the course with the given CourseID.
    - get_course_name(self, CourseID): Gets the name of the course with the given CourseID.
    - get_assignments_for_course(self, CourseID): Gets the assignments for the course with the given CourseID.
    """
    def __init__(self, url, key):
        # Initialize a new Canvas object
        self.canvas = Canvas(url, key)

    def get_user_selections(self):
        """
        Retrieves a list of the user's currently active Canvas courses.
        
        Returns:
        - list: a list of tuples containing course name, course code, and course ID for each selected course
        """
        c = self.canvas.get_courses(enrollment_state='active')
        listOfCurrentCourses = []
        gui = OptionsGUI.OptionsGUI(c,"current courses")
        for course in gui.selected:
            listOfCurrentCourses.append([course.name, course.course_code,course.id])
        return(listOfCurrentCourses)
    
    def get_course(self, CourseID):
        """
        Args:
        - CourseCode (str): the course code for the desired Canvas course
        
        Returns:
        - object: a Canvas course object
        """
        return(self.canvas.get_course(CourseID))
    
    def get_course_name(self, CourseID):
        return self.get_course(CourseID).name
    
    def get_assignments_for_course(self,CourseID):
        """       
        Args:
        - CourseCode (str): the course code for the desired Canvas course
        
        Returns:
        - list: a list of Canvas assignment objects for the specified course
        """
        return self.get_course(CourseID).get_assignments()