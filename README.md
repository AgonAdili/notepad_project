# notepad_project
This is a simple notepad project where a user can register, login in, create, view, edit and delete notes. Users can also ask the AI chat any question and view its response.

# Setup
1. Clone this repository to your local machine:

        git clone https://github.com/AgonAdili/notepad_project.git

2. Create a virtual environment:

        python.exe -m venv env

3. Install the required Python packages:

        pip install -r requirements.txt

4. Make database migrations:
        
        python.exe manage.py makemigrations

5. Apply those database migrations:

        python.exe manage.py migrate

6. Create a superuser for admin access (optional):
        
        python.exe manage.py createsuperuser

7. Start the development server:

        python.exe manage.py runserver

8. Access the application in your web browser at 'http://localhost:8000'

# Usage and Testing

To use and test the web app after you have launched the development server, you need to add /notes/[what you want to test] to the url. 
For example, if the URL looks like this - http://localhost:8000 it needs to look like this - http://localhost:8000/notes/register OR http://localhost:8000/notes/login OR http://localhost:8000/notes/create and so on ...

URLs that should be used to test the whole app are as following:

http://localhost:8000/notes/register

http://localhost:8000/notes/login

http://localhost:8000/notes/notes   (after clicking on a note, you will also find the edit, delete and the logout options)

http://localhost:8000/notes/create

http://localhost:8000/notes/chat

http://localhost:8000/notes/logout
