
## **Assessing patient details for covid19 Risk Report Generation**


### **List of Contents:**

- [Development tools used to build the project](#_d8dspgaklr31)
- [APIs used in the project](#_laqae3p2frex)
- [Assets used in the project](#_sqf6ukdt94ti)
- [Libraries used in the project](#_k8z6wjhs6y1b)
- [Branches](#_6rbw8tw9lsc9)
- [Code Execution](#_xweuuftv0qie)


### **Development tools used to build the project**

**For Application Development:**

- SwiftUI
- Swift 5

**For Website Development:**

- Visual Studio Code
- Jupyter Notebook

### **APIs used in the project**

- Python
- HTML5

### **Assets used in the project (****Assets = media such as pictures, videos, etc - along with frontend bootstraps (premade styles)****)**

- Plotly
- Vector image designed by rawpixel.com
- Freepik, Vector image designed by pikisuperstar
- Freepik, Vector image designed by pch.vector / Freepik

### **Libraries used in the project**

**For Application Development:**

- SwiftLocation (4.2.0)
- HealthKit
- UserNotifications
- SwiftUI

**For Website Development:**

- Python Flask Framework
- JavaScript Plotly
- JSON
- Werkzeug
- Math
- ibm\_db


### **Branches:**

- UI: Code for Web Application
- Master: Code for iOS application

### **Code Execution:**

- **Mobile Application:**
  - Clone master branch
  - Open COVIDRiskAssessment.xworkspace
  - Add Code Signing from xcode
  - Run it on emulator / device using the play button

- **Covid19 Risk Assessment Website**

The Website UI codings are uploaded as [ResultsUI2.zip]

Contents of ResultsUI2 ZIP folder:

- application.py

- templates folder

- dashboard.html

- login.html

- Patient details.html

- Register.html

- static folder

- style.css

- To execute the Results UI, run the application.py file.
- Paste the displayed URL into a browser.
- Login using any credentials to see the Dashboard.

Website GUI: It reads the JSON file from the iOS application and inserts the data in IBM DB2 database. DB2 database is then used to show Patient status&#39; and details to the Healthcare Providers.

To execute the website GUI, run the **application.py** file. Login using any credentials to see the Dashboard. The Patient data corresponding to the logged in user would be displayed on the screen classified into High, Low and Medium risk. In the List of Patients, click on the names to see the detailed Patient data.
