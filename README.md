Cell phones have become an essential part of modern life. In addition to making voice calls, cell phones can be used to send text messages, which areknown as SMS for short. Unlike computer keyboards, most cell phones have limited number of keys. To accommodate all alphabets, letters are compactedinto single key. Therefore, to type certain characters, a key must be repeatedly pressed until that character is shown on the display panel.In this problem we are interested in finding out the number of times keys on a cell phone must be pressed to type a particular message.
In this problem we will assume that the key pad of our cell phone is arranged as follows.
abc def
ghi jkl mno
pqrs tuv wxyz
<SP>
In the above grid each cell represents one key. Here <SP> means a space. In order to type the letter ‘a’, we must press that key once, however to type ‘b’ the same key must be repeatedly pressed twice and for ‘c’ three times. In the same manner, one key press for ‘d’, two for ‘e’ and three for ‘f’. This is also applicable for the remaining keys and letters. Note that it takes a single press to type a space.

Input
The first line of input will be a positive integer T where T denotes the number of test cases. T lines will then follow each containing only spaces and lower case letters. 
Each line will contain at least 1 and at most 100 characters.
Output
For every case of input there will be one line of output. It will first contain the case number followed by the number of key presses required to type the messageof that case.
Look at the sample output for exact formatting.

Sample input Sample output
2
welcome to ulab
good luck and have fun
Case 1 : 29
Case 2 : 41
