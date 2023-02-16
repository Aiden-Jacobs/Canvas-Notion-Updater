import datetime

import assignment_class
import NotionAPI_Int
import OptionsGUI
import CanvasAPI_int


def parseDate(TextDate):
    #TIME ZONE SET TO GMT/UTC/Z
    """
    Parameters:
    TextDate (str): A string representing a date and time in ISO 8601 format.

    Returns:
    (datetime.datetime): A datetime object representing the parsed date and time, in the UTC time zone.
    If the TextDate is "None", returns None.
    """
    if TextDate == "None":
        return None
    tempDateTime = TextDate.split("T")
    tempDate = tempDateTime[0].split("-")
    tempTime = tempDateTime[1].split(":")
    year = int(tempDate[0]) #TextDate[0:4]
    month = int(tempDate[1])
    day = int(tempDate[2])
    hour = int(tempTime[0])
    minute = int(tempTime[1])
    second = int(tempTime[2].replace("Z", ""))
    DTFinal = datetime.datetime(year, month, day, hour, minute,second, tzinfo=datetime.timezone.utc)
    return(DTFinal)


def tagsToAdd(AllTags, courseName):
    gui = OptionsGUI.OptionsGUI(AllTags,"Tag options for "+str(courseName),"name")
    return (gui.selected)


def main():
    # API keys and headers
    # Notion API key
    token = ''
    # Notion database ID
    databaseID = ""
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
        }
    # Canvas API URL
    API_URL = "https://canvas.calpoly.edu/" # EXAMPLE
    # Canvas API key
    API_KEY = "" 

    # Initialize a new Canvas tool
    CanvasWorkspace = CanvasAPI_int.CanvasTool(API_URL,API_KEY)
    # Initialize a new Notion tool
    Ndb = NotionAPI_Int.NotionTool(databaseID, headers)

    AllTags = Ndb.getTagsFromDatabase()
    assignmentList = []
    for c in CanvasWorkspace.get_user_selections():
        assignments = CanvasWorkspace.get_assignments_for_course(c[2])
        tagsToAddToAssignment = tagsToAdd(AllTags,CanvasWorkspace.get_course_name(c[2]))

        for i in assignments:
            date_due = str(i.due_at)
            date_start = str(i.unlock_at)
            link = i.html_url
            #TODO Comment out print 
            print(i.name)
            assignmentToAdd = assignment_class.assignment(i,parseDate(date_due),parseDate(date_start),link)
            assignmentToAdd.setTags(tagsToAddToAssignment)
            assignmentList.append(assignmentToAdd)
    Ndb.addAssignments(assignmentList,token)


if __name__ == '__main__':
    main()