 ![](https://github.com/hishreyas/Noteasy/blob/main/notices/static/img/logo.png?raw=true)
 ***
Code Github repo :[https://github.com/hishreyas/Noteasy/](NotEasy) 
***
 **Abstract**
1. **Timely Notices:**
 Prioritizes notices based on dates for timely delivery of critical information.
2. **Classification Feature:**
Enables users to filter notices, facilitating organized information retrieval.
3. **Inclusive Lecture Links:**
Integrates lecture links directly into the system for streamlined access to instructional content.
4. **Environmental Sustainability:**
Reduces paper usage, contributing to tree conservation and waste reduction.
5. **Automatic Removal of Outdated Notices:**
Ensures a clutter-free notice board by removing outdated information automatically.

***

**Project time management:**

+ As we were working on a known tech stack i.e python django, Linux, postgreSQL. Our plan was to first outline the design of our project using figma where every team gave their inputs. After designing different screens we started programming and distributed our roles throughout the process.

***

**Roles:**

* **Shreyas Bansode - Backend and Frontend (Implementing database connection and crucial relationship between tables & display data from database to frontend).**

* **Sahil Gurav \- Documentation and functional Testing (Documenting each and every component of a project for better understanding to others and functional testing to identify bottlenecks bugs ).**

* **Sachin Sharma - Frontend -  (Implementing robust and responsive UI and reusable components).**

* **Manas Darpelli - Testing ( Manual testing. Testing required components for better user experience).**

***

**First web page:-**

* Our first page is the landing page where the user will first arrive. We have a button for getting started that will redirect to the sign-up page. And also displayed our core functionality.

![](images/image20.png)

***

**Navigational Components :-**

* We have designed our project in such a way that even a person with no background in Computer science can easily navigate through our project. On the landing page we provide three buttons: login, sign up, start for free respectively.

* After logged In you will see your username and beside it a drop-down menu in which you can change password, my account to edit profile and logout. And two buttons namely my notices and filters. Filter for searching specific notices.

* If a teacher logged In there will be an extra button named as new notice for creating new notices.

![](images/image1.png)

***

* If a user is coming for the first time on our website it has to register using sign up and then log in to their account.

* All fields are compulsory to be filled with correct information.

* User will get promoted if :
  1.  Left any field empty.
  2.  Not providing relevant information i.e requested.

 ![](images/image14.png)

***

 **Login/Signup page-**

* On the login/sign-up page on submitting the form i.e username and password it goes through validation and verification of the information that was provided by the user. If the information is correct the user will be redirected to the home page or else it will be redirected again to the login page.

***
**Creating Notices-**

* Only Teachers can create notices. For creating notice all the necessary fields should be filled with relevant information. On click of create notice if the information is correct then notice is created successfully or else an error will prompt near the field. After creating the notices it will be displayed to every student. After creating the notice teacher can edit and delete notices as per their need.


***

**Data handling:-**

* We choose postgresQL as a database to store users and notice information. Whenever a user registers on the platform immediately an entry is created in the database along with the username and is stored in the account table in the database. If the registered user is a student then it can only view and sort the notices. i.e We choose the Django-REST framework as technology for data transfer. If the registered user is a teacher or staff then they can create as well as edit and delete notices. When a notice is created by a teacher it is also stored in the notice table in the database. And this notice from the database is displayed to relevant students.

***

**Database connectivity :-**

* **Online connectivity –**

  1. We have deployed our project on heroku that means we can access it throughout the internet using just the url like any other websites. You can access our project using url: [https://noteeasyweb.herokuapp.com/](https://www.google.com/url?q=https://noteeasyweb.herokuapp.com/&sa=D&source=editors&ust=1708498853632545&usg=AOvVaw1C8OgWwFtpacVg0LQRrlo1)

  2. The benefits of deployment is that now everyone is eligible to use it.

  3. And now our project runs on cloud and every notice that is created is seamlessly computed and stored in a database and shared among relevant users.

* **Offline connectivity -**

  1. As of now we are only online functioning. We might look out for offline connectivity in the near future.

***

**Notice generation -**

* Notices can be generated by teachers and staff. Only they are eligible to do it. To create a notice you have to navigate to the navigation bar where there is a button named new notice for creating new notices. By clicking it you will be redirected to fill a form for creating a new notice. You will be required to fill all the necessary fields and after all the checks you can click a button named post to publish the notice. If you wish to edit or delete your notices then head to the home page where you can see all your notices. Select and click view on a notice to edit or delete. You will find two buttons named edit and delete. Edit lets you customize your notice. Delete lets you delete the notice from the page.

![](images/image15.png)

***

 **Module of Deployment:-**

* Root level module of our project consists of two sub modules namely accounts and notices. Root level wraps all sub modules together and creates a lightweight folder called direct. This direct folder contains optimized code and also stores all images that are used in our project.

* On deployment this direct folder with our entire project is deployed onto the cloud server.

 **(Currently not available due to heroku discontinued the free services)**
[https://noteeasyweb.herokuapp.com/](https://www.google.com/url?q=https://noteeasyweb.herokuapp.com/&sa=D&source=editors&ust=1708498853634870&usg=AOvVaw0eCiciTzUKolfH8IWNgpv6) 

***

Test cases :-

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Module | Test Case ID | Test Case Description | Pre-conditions | Test Data | Execution Stages | Expected Result | Actual Result | Status |
| Web App  | T001 | User Interface | Open Application window | -   | Click on the text boxes | UI should be Perfect and all text boxes are clickable | UI should be Perfect and all text boxes are clickable | Pass |
| Teacher | T002 | Required Fields | Open Application window | -   | Do not enter any data in text box | It show the error message | It show the error message | Pass |
| Teacher | T003 | Required Fields | Open Application window | 1.Enter user name Shreyas 2.Enter password 12345 | Enter any data in text box | Its shows next page | Its shows next page | Pass |
| Teacher | T004 | Verify username text box | Login window must be open | Enter user name sachin | 1.Click on the user box 2.Enter user name 3.Click on login button | It show the error message | It show the error message | Pass |
| Teacher | T005 | Verify Password text box | Login window must be open | Enter password 1234 | 1.Click on the password box 2.Enter password 3.Click on login button | It show the error message | It show the error message | Pass |
| Teacher | T006 | Valid username and password | Login window must be open | 3.Enter user name Shreyas 4.Enter password 12345 | 1.Click on the user box 2.Enter user name 3.Enter password 4.Click on login button | Its shows next page | Its shows next page | Pass |
| Student | T007 | Invalid username and password | Login window must be open | 1.Enter user name Sahil 2.Enter password 78654 | 3.Click on the user box 4.Enter user name 5.Enter password 6.Click on login button | Its does't show next page | Its does't show next page | Pass |

