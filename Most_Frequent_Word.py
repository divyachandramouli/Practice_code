#Most_Frequent_Word.py
	'''
	Programming is an essential part of this Nanodegree program.
Complete the most_frequent() function below so that it returns the most frequently occurring word in a given string.
For example, if the input s is s = 'I scream you scream we all scream for ice cream', the result should be scream as it is the most frequent word in this sentence.
If there is a tie for the most common word, return only one result, the first (tied) word in alphabetical order.
NOTE: This quiz will be evaluated in Python 2.7.
	'''
#from collections import OrderedDict
def most_frequent(s):
    """Return the most frequently occuring word in s."""
    words=[]
    words=s.split(" ")
    words=sorted(words)
    word_count={}
    counts=[]
    for word in words:
        counts.append(words.count(word))
    m=counts.index(max(counts))
    return (words[m])
    
    # USING OrderedDict
    '''
    for word in words:
        word_count[word]=words.count(word)
    max_count=max(word_count.values())
    for word in OrderedDict(sorted(word_count.items(), key=lambda t:t[0])):
        if word_count[word]==ma
        x_count:
            return ("Using OrderedDict:", word)
    '''
            
            
        
    # HINT: Use the built-in split() function to transform the string s into an
    #       array
    
    # HINT: Sort the new array by using the built-in sorted() function or
    #       .sort() list method
    
    # HINT: Iterate through the array and count each occurance of every word
    #       using the .count() list method
    
    # HINT: Find the number of times the most common word appears using max()
    
    # HINT: Locate the index of the most frequently seen word
    
    # HINT: Return the most frequent word. Remember that if there is a tie,
    #       return the first (tied) word in alphabetical order.
    
 
 


def test_run():
    """Test most_frequent() with some inputs."""
    print most_frequent("cat bat mat cat bat cat") # output: 'cat'
    print most_frequent("betty bought a bit of butter but the butter was bitter") # output: 'butter'

    print most_frequent ("in in of aaa act act act is quiet aaa aaa")

if __name__ == '__main__':
    test_run()
