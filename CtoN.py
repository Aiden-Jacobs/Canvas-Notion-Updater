from canvasapi import Canvas
import datetime

import assignment_class
import NotionAPI_Int
import OptionsGUI


def parseDate(TextDate):
    #TIME ZONE SET TO GMT/UTC/Z
    #Returns Datetime object if Not None
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
    UserInput = ""
    tagsToAddToAssignment = []
    gui = OptionsGUI.OptionsGUI(AllTags,"Tag options for "+str(courseName),"name")
    return (gui.selected)
    # |  is used for CLI  |
    # V                   V
    """
    print(gui.selected)
    for tag in AllTags:
        while True:
            UserInput = input("Should assignments in class "+str(courseName)+" be tagged with tag "+str(tag['name'])+" ? y/n: ")
            if UserInput.lower() == "y":
                tagsToAddToAssignment.append(tag)
                break
            elif UserInput.lower() == "n":
                break
            else:
                print("Invalid input")
    return(tagsToAddToAssignment)
    """



def main():
    token = ''
    databaseID = ""
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
        }
    # Canvas API URL
    API_URL = "https://canvas.calpoly.edu/"
    # Canvas API key
    API_KEY = ""
    # Initialize a new Canvas object
    canvas = Canvas(API_URL, API_KEY)
    c = canvas.get_courses(enrollment_state='active')

    listOfCurrentCourses = []
    allCourses = {}
    # get current courses from user
    gui = OptionsGUI.OptionsGUI(c,"current courses")
    for course in gui.selected:
        listOfCurrentCourses.append([course.name, course.course_code,course.id])
    # |  is used for CLI  |
    # V                   V
    """
    for course in c:
        try:
            UInput = ""
            while True:
                UInput = input("Is "+str(course.name)+" a current course? y/n: ")
                if UInput.lower() == "y":
                    listOfCurrentCourses.append([course.name, course.course_code,course.id])#course,
                    print("Course added")
                    break
                elif UInput.lower() == "n":
                    break
                else:
                    print("Invalid input")
        except:
            pass
    """
    Ndb = NotionAPI_Int.NotionTool(databaseID, headers)
    AllTags = Ndb.getTagsFromDatabase()
    #TODO Comment out print 
    print(listOfCurrentCourses)
    assignmentList = []
    for c in listOfCurrentCourses:
        course = canvas.get_course(c[2])
        #TODO Comment out print 
        print(course.name)
        assignments = course.get_assignments()

        tagsToAddToAssignment = tagsToAdd(AllTags,course.name)

        for i in assignments:
            #print("\n----------------------------------\n")
            date_due = str(i.due_at)
            date_start = str(i.unlock_at)
            link = i.html_url
            #TODO Comment out print 
            print(i.name)
            assignmentToAdd = assignment_class.assignment(i,parseDate(date_due),parseDate(date_start),link)
            assignmentToAdd.setTags(tagsToAddToAssignment)
            assignmentList.append(assignmentToAdd)
    Ndb.addAssignments(assignmentList,token)


main()



"""
def readPage(databaseID, headers):
    readUrl = f"https://api.notion.com/v1/pages/e485dedc19ce4fb9927479ec9e0bc20c?v=55edb77ea1de4ae5a2ec99da6a8611bb"
    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    # print(res.text)

    with open('./full-properties.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)

    print("-",data['results'])
    return data['results']



    'properties': {
        #"CHECKBOX":{  "id": "BBla","name": "Task complete","type": "checkbox","checkbox": {}},  # NOT WORKING
        'DUE': {'id': '%5EnW~', 'type': 'date', 'date': {'start': startDate, 'end': endDate, 'time_zone': None}},
        'Tags': {'id': '%7BnRb', 'type': 'multi_select', 'multi_select': Assignment.getTags()}, #{'id': 'd20f854e-b264-4aef-a4f5-ad2c611453e3', 'name': 'run', 'color': 'red'}
        
        'Name': {'id': 'title', 'type': 'title',
             'title': [{'type': 'text',
                'text': {'content': Assignment.get_name(), 'link': {'url': Assignment.get_link()}},
                'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'},
                'plain_text': Assignment.get_name(), 'href': Assignment.get_link()}]}}}
    """
