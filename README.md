# Codeforces Group Standings Project
## Description
This project retrieves and displays the standings for Codeforces contests for a specific group. The data is processed through a Python backend, which connects to the Codeforces API, and a frontend that displays the information interactively on a web page. The project also allows for exporting standings to a CSV file.

## Features
Fetch standings for specific Codeforces contests within a group.
Display contestant rankings, scores, and other details on a web interface.
Export contestant data to a CSV file.

## Project Structure
application.py: The main backend script in Python that interacts with the Codeforces API, processes contest data, and handles requests from the frontend.
frontend/: Contains HTML, CSS, and JavaScript files for the user interface, displaying the standings.
README.md: Documentation for the project.
requirements.txt: Lists dependencies for the Python backend.

## Prerequisites
Python 3.x
requests library (install using pip install requests)
A web server (optional, for serving the frontend files)

## Setup
Clone the repository:
```
git clone https://github.com/your-username/codeforces-group-standings.git
cd codeforces-group-standings
```

# Install dependencies:

```
pip install -r requirements.txt
Configure API parameters:
```

In application.py, set the desired Codeforces group ID and contest ID for fetching the standings. Modify any other configuration parameters if necessary.

# Usage
1. Run the backend server:
```
python application.py
```
2. Access the frontend:

    Open index.html in the frontend/ folder in a web browser, or host it locally for smoother interaction with the backend.

3. Exporting to CSV:

    Once the standings are loaded, click the "Export to CSV" button to generate a CSV file of contestants and their standings.
