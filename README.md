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

3. Set up an integration in your Notion account to generate an integration key, and add it to the `token` variable in the script. You will also need to add the database ID for the database that you want to use.

4. Run the script, and follow the prompts to select the courses and tags that you want to include.

5. The script will then retrieve the assignments from Canvas and add them to the specified Notion database.

### Files

- `assignment_class.py`: Contains the class definition for the assignment object.
- `NotionAPI_Int.py`: Contains the NotionTool class, which provides the methods for interacting with the Notion API.
- `OptionsGUI.py`: Contains the OptionsGUI class, which provides a simple GUI for selecting multiple options from a list.
- `canvas_notion.py`: Contains the main script.

### Functions

- `parseDate(TextDate)`: This function takes a string in the format "yyyy-mm-ddThh:mm:ssZ" and converts it to a datetime object.
- `tagsToAdd(AllTags, courseName)`: This function takes a list of all tags in the Notion database and the name of the current course, and opens a GUI to allow the user to select the tags to add to the current course's assignments.
- `main()`: The main function of the script, which retrieves the user's Canvas courses and tags, retrieves the assignments for each course, and adds them to the Notion database.

### Classes

- `assignment_class.assignment`: The class definition for the assignment object. This object contains the information for a single assignment (name, due date, start date, tags, and link).
- `NotionAPI_Int.NotionTool`: The class definition for the NotionTool object. This object provides the methods for interacting with the Notion API, and contains the information for a single Notion database (database ID, headers, schema, and items).
- `OptionsGUI.OptionsGUI`: The class definition for the OptionsGUI object. This object provides a simple GUI for selecting multiple options from a list.

### Additional Information

- All code is written in Python 3.
- This script is not officially associated with Canvas or Notion.
- For more information on the CanvasAPI library, see [here](https://github.com/ucfopen/canvasapi).
- For more information on the NotionAPI library, see [here](https://developers.notion.com/docs/getting-started). 
