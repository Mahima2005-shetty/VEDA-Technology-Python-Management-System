\# VEDA Technology Python Management System



A Python and Flask-based management system developed for a technology and digital-services organization. The application manages services, training programs, customers, service inquiries, search and filtering, and basic business reports.



\## Project Objective



The objective of this project is to apply Python programming concepts to a realistic technology-business scenario while implementing:



\* Functions and modules

\* Classes and structured records

\* Lists and dictionaries

\* File handling

\* JSON data storage

\* Input validation

\* Search and filtering

\* Exception handling

\* Basic business reporting

\* Git and GitHub

\* Flask web application development



\## Features



\### Service Management



\* Add services

\* View all services

\* Search services

\* Update service status

\* Store service information in JSON



\### Program Management



\* Add training and internship programs

\* View programs

\* Search programs

\* Update program status

\* Store program information in JSON



\### Customer Management



\* Add customer records

\* View customer records

\* Search customers

\* Manage customer information



\### Service Inquiry Management



\* Create service inquiries

\* View inquiries

\* Search inquiries

\* Update inquiry status



\### Search \& Filtering



\* Search services

\* Search programs

\* Search customers

\* Search inquiries

\* Filter records by relevant fields and status



\### Business Reports



\* View management statistics

\* Display service information

\* Display program information

\* Display customer and inquiry summaries



\### Web Application



A Flask-based web interface is included for accessing the management system through a browser.



\## Technologies Used



\* Python

\* Flask

\* HTML

\* CSS

\* JSON

\* Git

\* GitHub

\* VS Code / PyCharm



\## Project Structure



```text

VEDA-Technology-Python-Management-System/

│

├── data/

│   ├── services.json

│   ├── programs.json

│   ├── customers.json

│   └── inquiries.json

│

├── webapp/

│   ├── app.py

│   ├── templates/

│   └── static/

│

├── customers.py

├── data\_manager.py

├── inquiries.py

├── main.py

├── programs.py

├── reports.py

├── services.py

├── utils.py

├── requirements.txt

├── README.md

└── .gitignore

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/Mahima2005-shetty/VEDA-Technology-Python-Management-System.git

```



Move into the project directory:



```bash

cd VEDA-Technology-Python-Management-System

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the virtual environment on Windows:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install the required packages:



```bash

pip install -r requirements.txt

```



\## Run the Python Management System



From the project directory:



```bash

python main.py

```



The command-line application provides options for:



1\. Service Management

2\. Program Management

3\. Customer Management

4\. Service Inquiry Management

5\. Search \& Filtering

6\. Business Reports



\## Run the Web Application



Move into the web application directory:



```powershell

cd webapp

```



Start Flask:



```powershell

python app.py

```



Open the application in a browser:



```text

http://127.0.0.1:5000

```



\## Data Storage



The application uses JSON files for persistent data storage. This allows service, program, customer, and inquiry records to be stored and retrieved without requiring a separate database server.



\## Validation and Error Handling



The application includes validation for user input and handles invalid values such as incorrect numeric input and missing records.



\## Learning Outcomes



This project demonstrates practical implementation of:



\* Python programming

\* Modular programming

\* Data structures

\* File handling

\* JSON processing

\* Validation

\* Exception handling

\* Flask web development

\* Git version control

\* GitHub project management



\## Internship Task Deliverables



\* Python management application

\* Service management module

\* Program management module

\* Customer management module

\* Service inquiry management

\* Search and filtering functionality

\* Business reports

\* JSON data storage

\* Flask web application

\* README documentation

\* GitHub repository



\## Author



\*\*Mahima\*\*



GitHub:

https://github.com/Mahima2005-shetty



\## Repository



https://github.com/Mahima2005-shetty/VEDA-Technology-Python-Management-System



