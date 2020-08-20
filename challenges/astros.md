# Morning Challenge: ASTRONAUT TRACKER!

![Image description](https://media1.tenor.com/images/c2e16afc6bff5a5ec0f027f1cc209649/tenor.gif?itemid=15935992)

There has been a lot of activity with astronauts going up and down due to SpaceX! There is a public API that records all current people in space and what vessel they are on. Check it out at http://api.open-notify.org/astros.json

**Your challenge this morning is to do the following:**

0. Access the API from the link above, pull/translate the JSON!

0. This API changes EVERY SINGLE TIME astronauts leave/arrive in space! Write a script that would give the following output:
    
    ```
    People in space: 3
    Chris Cassidy on the ISS
    Anatoly Ivanishin on the ISS
    Ivan Vagner on the ISS
    ```
0. HOWEVER, you should be able to run this exact same script a year from now and that inevitably updated list of astronauts would still display correctly! How? That's the challenge!

0. Do not hard-code "ISS" into your output... who's to say what other spacecraft our astronauts may fly in someday?
