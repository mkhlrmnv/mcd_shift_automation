<h1>Automate getting your shifts from finnish McDonald's webstie</h1>
<br>
<br>
<br>

<h2>Update 17.08.2023 - Version 2.2</h2>
<p>Added 'Remember me' check box that if checked saves users credentials for the next time</p>

<br>
<br>
<br>

<h2>Update 14.08.2023 - Version 2.1</h2>
<p>Update to 'defs.py' that fixes problem with vocation days in your calendar and added one new function to 'UI.py'</p>

<br>
<br>
<br>

<h2>If you want to install everything by files and open it in your vs code scroll past Version 2</h2>
<br>
<br>
<br>
<h2>Update 10.08.2023 - Version 2</h2>
<p>I made .exe file for the projects so so need to install anything, just download foalder and enable API</p>
<h3>How to do it</h3>
<h4>1. Download full folder from -> https://drive.google.com/drive/folders/1aTlxDgPhOMHJniLr3Adogs91_VLEuwAC?usp=drive_link</h4>

<h4>2. Enable Google API -> https://developers.google.com/drive/api/quickstart/python</h4>

<h4>3. Rename json file and put it into main folder</h4>
<p> - While doing previous stepp you downloaded .json file from 0AUTH2.0 client and renamed it to 'credentials.json', now rename it one more time to 'automation.json'
<p> - After that open main folder that you downloaded in first step and find there 'automation.json' file and replace it with you 'automation.json' file</p>

<h4>4. Run main.exe</h4>
<p>Now you good to go, just find 'main' file in main folder and run it</p>
<p> - First time runnign will pop-up default browser, just you guide bellow for that</p>

![image](https://github.com/mkhlrmnv/mcd_shift_automation/assets/118537912/169390a8-6a97-4032-b194-e95571027068)

<p> - Then will pop up liitle window that will ask for you username, password and about what shifts do you want to upload</p>
<p> - Then give a minute to program to run and after that check you google calendar, everything should be there</p>
<br>
<br>
<br>

<h2>Part below is for understanding how program works and downloading it by files</h2>
<br>
<br>
<h2>1. Install three code files</h2>
<p> - Download 'main.py', 'defs.py' and 'UI.py'</p>

<h2>2. Install selenium</h2>
<p>https://selenium-python.readthedocs.io/installation.html</p>

<h2>3. Enable Google API</h2>
<p>https://developers.google.com/drive/api/quickstart/python</p>

<h2>4. Json file</h3>
<p>In last step you downloaded OAuth2.0 json file. Name it 'automation.json' and move to the same plase with you main.py file/p>

<h2>5. Run the code</h3>
<p>Run the code by for right clicking folder with the files and choosing "Open in the termilan" and in the terminal typing "main.py"</p>
<td> - Firstly your default browser will pop-up and google will ask you to give permision for api usage</td>
<br><tr> - Choose you google account and then clicl "continue" button</tr>
<br><td> - Then window will pop-up and will ask you for you username, password and selection</td>
<br><td> - After that you don't need to really to anything, if everything is succesfull you will see in your console "event created" textes</td>
<br><td> - More information about funktions can be found in the comments of the code</td>
