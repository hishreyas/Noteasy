# NoteEasy

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
<p class="c72 c30"><span class="c7"></span></p><p class="c72"><span class="c65 c33 c87">Test cases :-</span></p><p class="c2"><span class="c1"></span></p><a id="t.c0a62d7c6db454808005321bb4ddad70fbe3faeb"></a><a id="t.1"></a><table class="c39"><tr class="c86"><td class="c43" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Module</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Test Case ID</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Test Case Description</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Pre-conditions</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c29"><span class="c11 c17">Test Data</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Execution Stages</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Expected Result</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Actual Result</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c11">Status</span></p></td></tr><tr class="c99"><td class="c43" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">-</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T001</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">User Interface</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Open Application window</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">-</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Click on the text boxes</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">UI should be Perfect and all text boxes are clickable</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">UI should be Perfect and all text boxes are clickable</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c96"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Teacher</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T002</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Required Fields</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Open Application window</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">-</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Do not enter any data in text box</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c106"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Teacher</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T003</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Required Fields</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Open Application window</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">1.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name Shreyas</span></p><p class="c25 c37"><span class="c9">2.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password 12345</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Enter any data in text box</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its shows next page</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its shows next page</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c63"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Teacher</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T004</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Verify username text</span></p><p class="c25"><span class="c17 c18">box</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Login window must be open</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Enter user name sachin</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">1.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on the user box</span></p><p class="c25 c37"><span class="c9">2.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name</span></p><p class="c25 c37"><span class="c9">3.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on login button</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c111"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Teacher</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T005</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Verify Password text box</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Login window must be open</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Enter password 1234</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c6 c60 c44"><span class="c9">1.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on the password box</span></p><p class="c6 c60 c44"><span class="c9">2.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password</span></p><p class="c6 c44 c60"><span class="c9">3.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on login button</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">It show the error message</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c84"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Teacher</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T006</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Valid username and password</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Login window must be open</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">3.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name Shreyas</span></p><p class="c25 c37"><span class="c9">4.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password 12345</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">1.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on the user box</span></p><p class="c25 c37"><span class="c9">2.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name</span></p><p class="c25 c37"><span class="c9">3.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password</span></p><p class="c25 c37"><span class="c9">4.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on login button</span></p><p class="c25"><span class="c17 c18">&nbsp;</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its shows next page</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its shows next page</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr><tr class="c84"><td class="c43" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Student</span></p></td><td class="c82" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">T007</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Invalid username and password</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Login window must be open</span></p></td><td class="c45" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">1.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name Sahil</span></p><p class="c25 c37"><span class="c9">2.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password 78654</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25 c37"><span class="c9">3.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on the user box</span></p><p class="c25 c37"><span class="c9">4.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter user name</span></p><p class="c25 c37"><span class="c9">5.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Enter password</span></p><p class="c25 c37"><span class="c9">6.</span><span class="c13">&nbsp; &nbsp;</span><span class="c17 c18">Click on login button</span></p><p class="c25"><span class="c17 c18">&nbsp;</span></p></td><td class="c46" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its does&#39;t show next page</span></p></td><td class="c52" colspan="1" rowspan="1"><p class="c25"><span class="c17 c18">Its does&#39;t show next page</span></p></td><td class="c67" colspan="1" rowspan="1"><p class="c29"><span class="c17 c18">Pass</span></p></td></tr></table><p class="c2"><span class="c1"></span></p><p class="c2"><span class="c1"></span></p><p class="c2"><span class="c23 c24"></span></p><div><p class="c78"><span class="c23 c53">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span><span class="c23 c24">&nbsp;| </span><span class="c24 c77">Page</span></p><p class="c2"><span class="c23 c53"></span></p></div></body></html>