***
  - SCRIPT: **Facebom**
  -    JOB: **Brute Force Attack On Facebook Accounts**
***

- **SCRIPT ScreeenShot**:

    - **Usage**:
    
      ![options](https://user-images.githubusercontent.com/29546157/88081778-90e36080-cb89-11ea-85f5-325bede38878.PNG)


    - **Brute Force On Facebook Account Without proxy**:
     
     * **Command**: python facebom.py -t Oseid@gmail.com -w wlist.txt
     
     ![withoutProxy](https://user-images.githubusercontent.com/29546157/88081833-a22c6d00-cb89-11ea-84c6-50ab34fb62a3.PNG)
   
   - **Brute Force On Facebook Account With Proxy(HTTP)**:
   
    * **Command**: python facebom.py -t Oseid@gmail.com -w wlist.txt -p 35.236.37.121
    
    ![withProxy](https://user-images.githubusercontent.com/29546157/88081886-b83a2d80-cb89-11ea-893e-0fb77059fe83.PNG)

   - **Get Target Facebook Profile ID**:
   
    * **Command**: python facebom.py -g https://www.facebook.com/zuck
    
    ![getID](https://user-images.githubusercontent.com/29546157/88082079-f9cad880-cb89-11ea-894b-801e8c4fe369.PNG)

***

# For Install:

 - git clone https://github.com/Oseid/Facebom.git
 - cd Facebom/
 - pip install requests
 - pip install mechanize
***

# Supported Platforms:
- [x] Windows
- [x] Linux
- [x] Android~**Termux**
- [x] MacOs
- [x] **any Os has python(2.x, 3.x) with required modules**


# Protection yourself from this attack:
  * Use Strong Password which contains {letters(lower,upper),tokens,numbers} make it longest as possible, at least 10 letters
  * don't use your basic information in the password for example don't use your name or birthday\
        because the hacker can do a information gathering attack and get this information easily\
        then he will generate a wordlist based on this info.
  * Use 2F Authentication.
  
# Warning:
  * this script is only for educational purposes
  * i am not responsible for your actions.

# That's All :)
   * This Script Coded By Oseid Aldary
   * Thanks For Usage
   * Have A Nice Day...GoodBye :)
