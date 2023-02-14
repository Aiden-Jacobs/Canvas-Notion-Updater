import datetime

class assignment:
    """
    A class representing a student assignment.

    Attributes:
    - DaysToWorkOnAssignment (int): The number of days a student has to work on the assignment.
    - name (str): The name of the assignment.
    - StartDate (datetime.datetime): The start date of the assignment.
    - DueDate (datetime.datetime): The due date of the assignment.
    - link (str): The link to the assignment.
    - Tags (list of str): The list of tags associated with the assignment.

    Methods:
    - setDaysToWorkOnAssignment(days): Sets the number of days a student has to work on the assignment.
    - setTags(TagList): Sets the tags associated with the assignment.
    - addTag(tag): Adds a tag to the list of tags associated with the assignment.
    - getTags(): Returns the list of tags associated with the assignment.
    - get_name(): Returns the name of the assignment.
    - get_due_date(): Returns the due date of the assignment.
    - get_start_date(): Returns the start date of the assignment.
    - get_link(): Returns the link to the assignment.
    - __repr__(): Returns a string representation of the assignment.

    """    

    def __init__(self, name, DueDate,StartDate, link):
        """
        Initializes an instance of the assignment class.

        Parameters:
        - name (str): The name of the assignment.
        - DueDate (datetime.datetime): The due date of the assignment.
        - StartDate (datetime.datetime): The start date of the assignment.
        - link (str): The link to the assignment.

        """
        self.DaysToWorkOnAssignment = 4
        self.name = name
        if  DueDate != None: #StartDate == None and
            self.StartDate = DueDate + datetime.timedelta(days = -self.DaysToWorkOnAssignment)
        else:
            self.StartDate = StartDate
        self.DueDate = DueDate
        self.link = link
        self.Tags = []

    def setDaysToWorkOnAssignment(self, days):
        """
        Sets the number of days a student has to work on the assignment.

        Parameters:
        - days (int): The number of days a student has to work on the assignment.

        """
        self.DaysToWorkOnAssignment = days

    def setTags(self, TagList):
        """
        Sets the tags associated with the assignment.

        Parameters:
        - TagList (list of str): The list of tags associated with the assignment.

        """
        self.Tags = TagList

    def addTag(self, tag):
        """
        Adds a tag to the list of tags associated with the assignment.

        Parameters:
        - tag (str): The tag to be added to the list of tags associated with the assignment.

        """
        self.Tags.append(tag)

    def getTags(self):
        """
        Returns the list of tags associated with the assignment.

        Returns:
        - The list of tags associated with the assignment.

        """
        return self.Tags

    def get_name(self):
        """
        Returns the name of the assignment.

        Returns:
        - The name of the assignment.

        """
        return str(self.name)

    def get_due_date(self):
        """
        Returns the due date of the assignment.

        Returns:
        - The due date of the assignment.

        """
        return self.DueDate

    def get_start_date(self):
        """
        Returns the start date of the assignment.

        Returns:
        - The start date of the assignment.

        """
        return self.StartDate
    
    def get_link(self):
        """
        Returns the link to the assignment.

        Returns:
        - The link to the assignment.

        """
        return(self.link)

    def __repr__(self):
        return(str(self.name)+" Due Date: "+str(self.DueDate))