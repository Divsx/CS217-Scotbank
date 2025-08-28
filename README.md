# 🏦 ScotBank – Full-Stack Banking Web App

**ScotBank** is a full-stack web app simulating core online banking features such as account access, transaction history and balance tracking. Originally developed as part of an Agile group project in collaboration with **JPMorgan**, this application models production-style fintech systems using RESTful APIs, modular architecture and continued integration workflows.

After project completion, I independently extended the system by developing a **custom Python-based mock API server**, restoring functionality following the shutdown of the original API service.

---

## 🛠️ How to Run ScotBank

Follow these steps to get ScotBank up and running locally:

1. **Install Python**

  Download and install Python. I used 3.11 for this project but any version higher than 3.11 should work as well: [python.org](https://www.python.org/downloads/release/python-3110/)
  > *Make sure to add Python to your system PATH during installation*

2. **Install Project Dependencies**
  
  Navigate to the project directory and run:
  
  ```bash
  pip install -r requirements.txt
  ```

  This will install all necessary Python packages, including Flask.

3. **Install Java**
  
  If you don't have Java already, download and install it. I used Java 21 for this, follow this tutorial and it should help you set it up. [youtube.com](https://www.youtube.com/watch?v=-hxCPXjYWJU)

4. **Download The Latest Release**
  
  Download and unzip the latest ZIP file from the releases section on the GitHub Repo.

5. **Run the Local API Server**

  Inside the ZIP folder will be 2 folders. Inside of the PyAPI folder, run the `app.py` file with the command
  `flask run` or `python app.py` in a command line window. It should run as long as you have all the modules required.

6. **Run the JAR App**

  Inside the second folder will be a `Scotbank-1.0.0.jar` file, run that with the command `java -jar scotbank-1.0.0.jar`
  or `C:\Users\{user}\.jdks\{java_version}\bin\java.exe -jar scotbank-1.0.0.jar` and it should boot up a terminal window without any failures.

7. **Open Browser and Test**

  If you open up your browser and go to `127.0.0.1:8080`, it should open up the login screen for the bank!

8. **Logging In**

  Logging into the bank app requires a username and password. There is a user and admin account already set up.
  `username` and `admin` usernames both use `password1` as their password. If you want to sign up a new account,
  you need to get a UUID from the `accounts.json` file and use that as the Bank ID.

---

## 🧩 System Architecture

The ScotBank system follows a RESTful client-server model. The original version utilised a Java based backend (Jooby framework), with a browser-based UI powered by server side templating.

Following the module's conclusion and API decommissioning, I engineered a drop in Python-based API server that replicates the original service’s JSON structure and behavior, using reverse engineered request/response patterns derived from legacy code and limited documentation.

---

## ⚙️ Technology Stack

| Layer           | Tools Frameworks                            |
|-----------------|---------------------------------------------|
| Frontend        | HTML5, CSS3, JavaScript, Handlebars.js      |
| Original Backend| Java (Jooby Framework), REST APIs           |
| Custom API Mock | Python (Flask), JSON, CSV                   |
| DevOps          | GitLab CI/CD Pipelines                      |
| Version Control | Git, GitLab                                 |
| Project Mgmt    | GitLab Issues, Merge Requests, Scrum Boards |

---

## ✨ Core Features

- **User Authentication**: Session-based login system
- **Account Dashboard**: Displays balances and recent transactions
- **Admin Dashboard**: Dedicated administrative interface providing access to system wide account overviews, user lists, and operational controls
- **Admin Summary Views**: Aggregated visual summaries of total balances, number of active users, and recent transaction activity for monitoring system performance
- **Frontend–Backend Integration**: API-driven interaction using HTTP requests and JSON
- **Templating System**: Dynamic rendering via Handlebars.js
- **Custom Mock API**:
  - Built in **Python + Flask**
  - Emulates endpoints of the original banking API
  - Parses and serves static datasets in **JSON/CSV** formats
  - Designed to plug into the original frontend with minimal changes required

---

## 🔄 Agile Development Workflow

This application was developed in a Scrum-based environment with the following practices:

- **Sprint Planning & Retrospectives**: Regular planning and review meetings
- **Backlog Management**: GitLab Issues and Scrum boards used for task tracking
- **Daily Standups**: Ensured team alignment and incremental progress
- **Code Reviews**: Merge requests and peer feedback enforced code quality
- **Continuous Integration**: GitLab pipelines automated builds and testing

---

## 🔧 Independent Post-Project Work

After the project concluded and the API endpoints were deactivated, I:

- **Reverse engineered** the API contract using legacy code and partial documentation
- **Rebuilt** the core endpoints using **Flask**, matching expected routes and payload formats
- **Recreated** data outputs using Python scripts to generate local **CSV/JSON datasets**, simulating backend persistence and supporting consistent API responses
- Ensured full compatibility with the existing frontend, allowing continued development and testing if required

This initiative not only restored broken functionality but also demonstrated backend integration skills and a deeper understanding of API lifecycle management.

---

## 📌 Notes

This project reflects both collaborative software engineering practices in a structured Agile environment and individual technical problem solving through system level reverse engineering.

While this repository is a personal version, it is based on group work and extended beyond its original scope to support additional learning and functionality.

---

## 🙏 Thank You

Special thanks to the team at **JPMorgan** for their partnership and industry guidance throughout the module, and to my teammates for their contributions, collaboration and shared commitment to delivering a high quality solution.
