# ChatGP

The emotional effect of receiving devastating news from the doctor could be detrimental, leading to the feeling of loneliness and isolation. To combat this, we created a platform that transforms the daunting experience of receiving life-altering medical news into a journey of shared support and understanding. It connects individuals facing similar health challenges within dedicated forums, fostering a community where advice and empathy flow freely. To enhance personal connections, our system also pairs users with peers who share their background, including ethnicity and language, promoting deeper, more meaningful support. This innovative approach not only streamlines the search for compassionate guidance but also enriches the emotional and practical support network for those navigating tough times. By uniting patients in a space of mutual experiences, our platform offers comfort, understanding, and actionable advice, making the path through adversity less isolating and more navigable with personalised, empathetic companionship.

## Installation

### Running the frontend

Begin by installing all dependencies:

```bash
cd chat-gp-frontend
npm install
```

To run the frontend code:

```bash
npm run dev
```

The website should be hosted on `localhost:3000`.

### Running the backend

You **must** have python 3.11 installed.

First navigate into the `django_server` directory and remove the `bin` folder.

```bash
cd backend
cd django_server
rmdir /s /q bin # ON WINDOWS POWERSHELL
rm -rf bin # ON UNIX
```

Now initialise a new python venv in the current directory:

```bash
py -m venv . # ON WINDOWS POWERSHELL
python3 -m venv . # ON UNIX
```

Now activate the environment:

```bash
Scripts\activate.bat # ON WINDOWS POWERSHELL
source bin/activate  # ON UNIX
```

If all is good, you should be able to run the code now.

```bash
cd chat_gp_backend
python manage.py runserver
```
