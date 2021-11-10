# Comments about the implemented solution

### To build the app
- To run the app, execute the `main.py` file
- To implement unit testing, execute the `testing.py` file


### Assumptions
- There is capital and lowercase sensitivity. For example the string `Hello` is different than
the string `hello`.
  
- Both numbers and letters can be included in a word. For example, `helloworld2` is considered valid.

### Design choices
I implemented the functions as static in order to simplify the testing process.
  
### Algorithm

1. Creation a dictionary of the target string where the keys are the characters of the strings and the values are the frequency of each character.
   For example the string `"seo"` yields `{'s':1, 'e':1, 'o':1}`
1. We sort this dictionary based on ascending order based on the characters. For example, `{'s':1, 'e':1, 'o':1}` becomes  `{'e':1, 'o':1, 's':1}`.
1. We traverse through the pool of given strings and for each string we follow the above process. At every iteration we check whether the dictionary from teh current string matches the dictionary of the target string. If it does, we append the original string to the answer that is going to be returned.


### Time Complexity
Since our algorithm has to check all of the values of the give strings, our implementation
has a time complexity of `O(n)` where `n` is the number of the given strings

### Space Complexity
Since we create and store one dictionary entry per word, we will have a space complexity of `O(n)` for a list of n strings.
### If the size of the initial string list is very large:
Due to the time complexity of `O(n)` this implementation would be slower. 

### If the number of *find* requests gets extremely large:
We could scale our implementation horizontally by adding more computing nodes and by distributing our traffic with an efficient load balancer.