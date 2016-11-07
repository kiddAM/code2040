# code2040
Chloe "Kidd" Matthews, Code2040 2017 Fellows Application
</br>#ballout

</br><b>Files:</b>
</br><ul><li>1_register.py
<blockquote>This program satisfies step 1 of the tech assessment. It formally connects the applicant (that's me) to the API's registration endpoint by sending an HTTP POST request including a given API token and the URL of this GitHub repository.</blockquote>

<blockquote><i>Notes:</i> This was my first time working with HTTP requests. It took me a while to understand ow to execute them and what language would be the most practical to work with. I'm used to writing in Java and JavaScript, but I realized that Python's 'requests' module makes sending requests pretty simple.</blockquote>
  
<li>2_reverse.py
<blockquote>This program satisfies step 2 of the tech assessment. It sends an HTTP POST request including the given API token to an API endpoint which, then, responds with a string. The program reverses the original string and returns that to the API's specified validation endpoint.</blockquote>

<blockquote><i>Notes:</i> In this program, I made use of one of Python's many string methods, [::-1], which takes a string and returns it exactly as it was but in reverse order. I suppose this is one of the "the easy ways" that the hint alluded to. </blockquote>

<li>3_haystack.py
<blockquote>This program satisfies step 3 of the tech assessment. It sends an HTTP POST request including the given API token to an API endpoint which, then, responds with a string signified as a "needle" and a string array signified as the "haystack." The program uses Python's index() method to locate the needle in the haystack. When it is found, the program logs its index and returns it to the API's specified validation endpoint.</blockquote>

<blockquote><i>Notes:</i> Again, Python's extensive library made completing this task fairly easy. After I created a JSON dictionary of elements grabbed from the API's response text (which is also something I hadn't done before), I was able to apply the index() method to easily return the index of the string in the array.</blockquote>

<li>4_prefix.py
<blockquote>This program satisfies step 4 of the tech assessment. It sends an HTTP POST request including the given API token to an API endpoint which, then, responds with a named "prefix" string and a string array. The program uses a 'for' loop to inspect all elements of the array, ignoring strings that begin with the prefix and appending all others to a new array. The program, then, returns the new array to the API's specified validation endpoint.</blockquote>

<blockquote><i>Notes:</i> For this program, I used a 'for' loop to iterate through all strings in the array. Then, in an imbedded 'if' statement, I used Python's find() method to look for the prefix in each element. If the prefix was not present in a particular string, the loop would append() that string to a new array.</blockquote>

<li>5_dating.py
<blockquote>This program satisfies step 5 of the tech assessment. It sends an HTTP POST request including the given API token to an API endpoint which, then, responds with an datestamp in iso1806 format and an interval of some number of seconds. Employing Python's 'datetime' module, the program converts the datestamp to a readable datetime object, adds the interval to the date, and converts the new datestamp to iso1806 format. The program returns the new datestamp to a specified validation endpoint.</blockquote>

<blockquote><i>Notes:</i> This task was definitely the most difficult. I had never worked with datestamps before, and hardly with time. After quite a bit of websurfing, I came across the documentation for Python's 'datetime' module. In this program, I used datetime.strptime() to convert the original string to a datetime object; timedelta() to translate the interval from an integer to readable time; and date.strftime to convert the new string with interval added to a datetime object of its own.</blockquote>

