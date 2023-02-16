# Canvas-Notion-Updater

**Canvas Notion Updater**

This is a python program that retrieves upcoming assignments from a Canvas account and adds them to a specified Notion database. It uses the Canvas API, and the Notion API.

**Libraries Required:**

- CanvasAPI
- NotionAPI
- tkinter
- requests
- datetime

## How to use

To use this program, follow these steps:

1. Clone this repository and install the required libraries.

2. Set up an integration in your Canvas account to generate a developer key, and add it to the `API_KEY` variable in the script.

3. Set up an integration in your Notion account
    1. Generate an integration key [here](https://www.notion.so/my-integrations), and add it to the `token` variable in the script . 
    2. Add the integration to your database as a conection
    3. You will also need to add the database ID for the database that you want to use. 
    >![picture alt](https://files.readme.io/62e5027-notion_database_id.png "Title is optional")

4. Run the script, and follow the prompts to select the courses and tags that you want to include.

5. The script will then retrieve the assignments from Canvas and add them to the specified Notion database.

## Files:

* `CanvasAPI_int.py`: Contains the class definition for the `CanvasTool` object which holds functions to interact with the CanvasAPI.
* `NotionAPI_Int.py`: Contains the class definition for the `NotionTool` object which holds functions to interact with the NotionAPI.
* `assignment_class.py`: Contains the class definition for the `assignment` object.
* `CtoN.py`: This file is the main file that runs the entire code.

### Classes:

* `CanvasTool`: This object interacts with the CanvasAPI to get the current courses and assignments for a user. It takes in a URL and key to access the CanvasAPI.
* `NotionTool`: This object interacts with the NotionAPI to get and add data from and to a specific Notion Database. It takes in a database ID and header information to access the NotionAPI.
* `assignment`: The class definition for the `assignment` object. This object contains the information for a single assignment (name, due date, start date, tags, and link). 

### Additional Information

- All code is written in Python 3.
- This script is not officially associated with Canvas or Notion.
- For more information on the CanvasAPI library, see [here](https://github.com/ucfopen/canvasapi).
- For more information on the NotionAPI library, see [here](https://developers.notion.com/docs/getting-started). 
