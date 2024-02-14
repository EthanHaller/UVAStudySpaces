# UVA Study Spaces

## Project Description

UVA Study Spaces is web application built in Django using Python, HTML, CSS, and JavaScript. UVA Study Spaces is a catalog of different buildings to study in at the University of Virginia. This project was created for CS 3240: Advanced Software Development at the University of Virginia.

## Table of Contents

1. [Website Access](#website-access)
2. [Functions](#functions)
3. [Technologies Used](#technologies-used)
4. [Credits](#credits)

## Website Access

The web application can be found at the following link: https://project-a-06-99a4abdf2d2b.herokuapp.com. JavaScript must be enabled in the browser. Loading the website for the first time might take some time.

Additionally, the project can be opened locally. To open the project locally, run the command `pip install requirements.txt`. Then, run the command `python manage.py collectstatic` and `python manage.py runserver`.

## Functions

- A Google account is required to login
- All users can browse different study spaces and view them on a map or in a list of cards on the homepage.
- All users can find the closest study spaces to a given address from the Get Directions tab.
- All users can view their own profile containing their name and email
- Regular users can submit new study spaces with associated information and view past submissions.
- Admin users can view pending submissions and accept or deny them
- Admin users can edit or delete study spaces

## Technologies Used

The following technologies are listed in requirements.txt and were used throughout the project. Additionally, the website has been deployed on Heroku and is connected to a Heroky Postgres database.

- Django
- gunicorn
- django-allauth
- python-dotenv
- whitenoise
- django-bootstrap-v5
- django-bootstrap-icons
- postgres
- googlemaps

## License
This project is licensed under the MIT License - see the 
[LICENSE](https://github.com/EthanHaller/UVAStudySpaces/blob/main/LICENSE) file for details

## Credits

This project was successfully implemented thanks to the commitment and dedication of:

- Luke Creech [GitHub](https://github.com/LukeCreech)
- Grace Flynn [GitHub](https://github.com/grace-flynn)
- Ethan Haller [GitHub](https://github.com/EthanHaller)
- Siddharth Premjith [GitHub](https://github.com/rqf8pe)
- Kate Van-Meter [GitHub](https://github.com/kate-van-meter)
