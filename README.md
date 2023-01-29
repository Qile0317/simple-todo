unfinished

notes for contributors:
- data/todo.txt is the file where todo strings are stored
- each line in data/todo.txt should be in the format of:
x (A) YYYY-mm-dd HH:MM:SS YYYY-mm-dd HH:MM:SS task +project @context =2+2

see http://epsilonexpert.com/e/info/todotxt.php for more info

- data/settings.txt first line tells whether its fullscreen(2) or miniview(1)

- requirements.txt has all the dependencies and shouldn't be modified manually. 

- items folder is for the ```item``` class

- tests folder are the scripts that uses unittest to test every testable function and maybe GUIs in the future
- please write testcases for any new feature if they are testable

- miniview and fullscreen folders are for the 

before dependency stuff gets sorted, you need:
- tkinter
- datetime
- screeninfo
- Piprecs (for modifying requirements.txt) just literally type ```piprecs --force``` in the terminal if you have any new dependencies loaded. however piprecs isnt working properly atm
- unittest

Also, there should in general be more handling of invalid imputs.