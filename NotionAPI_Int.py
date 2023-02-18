import requests, json
import assignment_class

class NotionTool:
    """
    A class representing a tool to interact with Notion API for managing a database of assignments.

    Attributes:
    - databaseID (str): ID of the database in Notion.
    - headers (dict): Headers for the API requests.
    - DatabaseSchema (dict): Schema of the Notion database.
    - DatabaseItems (list): List of items (assignments) in the database.

    Methods:
    - readDatabase: Retrieve the list of items in the database and return it.
    - API_Get_Database_Schema: Retrieve the schema of the database and return it.
    - Update_Database_Schema: Update the DatabaseSchema attribute with the latest database schema.
    - getDatabaseSchema: Return the current DatabaseSchema attribute.
    - getTagsFromDatabase: Retrieve the list of tags (multi-select options) from the database schema and return it.
    - CreateJsonForItem: Create a JSON object for an assignment to be added to the database, based on the current database schema.
    - AddItem: Add a new assignment to the database.
    - addAssignments: Add multiple assignments to the database.
    """
    def __init__(self, databaseID,headers):
        """
        Initialize the NotionTool instance.

        Parameters:
        - databaseID (str): ID of the database in Notion.
        - headers (dict): Headers for the API requests.
        """
        self.databaseID = databaseID
        self.headers = headers
        self.DatabaseSchema = self.API_Get_Database_Schema()
        self.DatabaseItems = self.readDatabase()

    def readDatabase(self):
        """
        Retrieve the list of items in the database and return it.
        """
        readUrl = f"https://api.notion.com/v1/databases/{self.databaseID}/query"
        res = requests.request("POST", readUrl, headers=self.headers)
        data = res.json()
        print(res.status_code)
        with open('./full-properties.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)
        return data['results']
    
    def API_Get_Database_Schema(self):
        """
        Retrieve the schema of the database and return it.
        """
        url = F"https://api.notion.com/v1/databases/{self.databaseID}"
        response = requests.get(url, headers=self.headers)
        data = response.json()
        #print(response.status_code)
        return(data)
    
    def Update_Database_Schema(self):
        """
        Update the DatabaseSchema attribute with the latest database schema.
        """
        self.DatabaseSchema = self.API_Get_Database_Schema()

    def getDatabaseSchema(self):
        """
        Return the current DatabaseSchema attribute.
        """
        return(self.DatabaseSchema)


    def getTagsFromDatabase(self):
        """
        Retrieve the list of tags (multi-select options) from the database schema and return it.
        """
        return(self.DatabaseSchema['properties']['Tags']['multi_select']['options'])

    def getPropertiesType(self, prop):
        return self.DatabaseSchema['properties'][prop]['type']
    
    def getProperty(self, prop):
        pass
    
    def CreateJsonForItem(self,Assignment : assignment_class.assignment):
        """
        Create a JSON object for an assignment to be added to the database, based on the current database schema.

        Parameters:
        - Assignment (assignment_class.assignment): Assignment object to be added.

        Returns:
        - propertiesJson2 (dict): JSON object for the assignment to be added to the database.
        """
        propertiesJson2 = {}
        for prop in self.DatabaseSchema['properties']:
            try:
                del self.DatabaseSchema['properties'][prop]['name']
            except:
                pass
            temp = self.DatabaseSchema['properties'][prop]
            if self.getPropertiesType(prop) == "date" :        
                
                if Assignment.get_due_date() != None:
                    temp[self.DatabaseSchema['properties'][prop]['type']] = {'start': Assignment.get_start_date().astimezone().isoformat(), 'end': Assignment.get_due_date().astimezone().isoformat(), 'time_zone': None}
                else:
                    temp[self.DatabaseSchema['properties'][prop]['type']] = {'start': None, 'end': None, 'time_zone': None}
                propertiesJson2[prop] = temp

            if self.getPropertiesType(prop) == "email" :
                temp[self.DatabaseSchema['properties'][prop]['type']] = {}        
                propertiesJson2[prop] = temp

            if self.getPropertiesType(prop) == "files" :
                temp[self.DatabaseSchema['properties'][prop]['type']] = {}        
                propertiesJson2[prop] = temp

            if self.getPropertiesType(prop) == "multi_select" :
                temp[self.DatabaseSchema['properties'][prop]['type']] = Assignment.getTags()      
                propertiesJson2[prop] = temp

            if self.getPropertiesType(prop) == "title" :
                temp[self.DatabaseSchema['properties'][prop]['type']] = [{'type': 'text',
                            'text': {'content': Assignment.get_name(), 'link': {'url': Assignment.get_link()}},
                            'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'},
                            'plain_text': Assignment.get_name(), 'href': Assignment.get_link()}]        
                propertiesJson2[prop] = temp

            if self.getPropertiesType(prop) == "url" :        
                temp[self.DatabaseSchema['properties'][prop]['type']] = {}        
                propertiesJson2[prop] = temp

        return(propertiesJson2)
    
    def AddItem(self, Assignment,token, completed=False):
        """
        This method adds a new assignment to the database.
        Args:
            Assignment (assignment_class.assignment): an instance of the assignment_class.assignment
            token (str): the authentication token for Notion API
            completed (bool, optional): a boolean value that represents if the assignment is completed or not. Defaults to False.
        """
        url = f'https://api.notion.com/v1/pages'
        payload = {
        "parent": {
            "database_id": self.databaseID
        }, "properties" :
        self.CreateJsonForItem(Assignment)}
        r = requests.post(url, headers={
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json"
        }, data=json.dumps(payload))


    def addAssignments(self,list,token):
        """
        This method adds multiple assignments to the database.
            Args:
        list (list): a list of instances of the assignment_class.assignment
        token (str): the authentication token for Notion API
        """
        TasksINDB = []
        for task in self.DatabaseItems:
            for prop in task['properties']:
                if (task['properties'][prop]['type']) == "title":
                    try:
                        TasksINDB.append(task['properties'][prop]['title'][0]["text"]["content"])
                    except:
                        pass
        for i in list:
            if i.get_name() not in TasksINDB:
                print(i,i.get_name(),i.get_due_date())
                self.AddItem(i,token,False)
