---
layout: post
title: "Python IV: File Input/Output and Parsing"
instructor: Becca
permalink: /python4_fileio/
materials: files/python4.zip
---

~~~~ Under Construction ~~~~


Now that you can make functions, it's time to learn how to use them to manipulate other files.

## Today's Goals ##
1. Read files line by line in python 
2. Write output from python to a file
3. Use the `sys` module to take arguments from the command line 
4. Set up multi-parameter analyses using for loops in bash over python scripts



## Opening and closing files ##
To interact with files in python, you must open the file and assign it to a variable - this is now a python file object. All operations on the contents of a file must be done using this variable (not the file name itself!). Once all operations are finished, the file must be closed. Importantly, your computer's operating system limits the number of files which can be open at once (type the command `ulimit -n` to the command line to see how many), so it is very important to always close files when you are finished.

There are two basic ways to open and close files. Note that these two chunks of code are equivalent in their output.

Open and close with open() and close()
{% highlight python %}
file_handle = open("important_file.txt", "r") # Open as read-only
contents = file_handle.readlines() # Read contents of file and save as a list
file_handle.close() # Close file when finished (important!!)
{% endhighlight %}

Open with the *with* control flow command. The file automatically closes outside the scope of the with. This is what I prefer to use.
{% highlight python %}
with open("important_file.txt", "r") as file_handle:
  contents = file_handle.readlines()
{% endhighlight %}

The `open()` function takes two arguments: i) the *name* (including full or relative path!) of the file to open, and ii) the *mode* in which the file should be read. Modes include read-only (`"r"`), write-only (`"w"`), append (`"a"`), or read+write (`"rw"` for PCs and `"r+"` for Mac/Linux). Writing and appending are similar to the bash operators `>` and `>>`; write will overwrite the file, but append will add to the bottom of an existing file. Note that if you open a file for writing (or appending), that file doesn't need to exist already, and a new file will be created with the specified name. Alternatively, if you attempt to open a file that does not exist for reading, you'll receive an error message.

{% highlight python %}
# Open a file for writing, and write to it
file_handle = open("file_to_fill.txt", "w") # Open file for writing
file_handle.write("I'm writing a sentence to this file!")
file_handle.close()
{% endhighlight %}

Open a file for appending, and append text to it
{% highlight python %}
file_handle = open("file_to_fill.txt", "a")
file_handle.write("I'm writing another line to this existing file!")
file_handle.close()
{% endhighlight %}


## Looping over file contents ##

When interacting with files, we usually want to examine and perform computations with the file content. To do this, we need to read in the file contents after opening the file. There are two basic file methods, `.readlines()` and `.read()`, that exist in native Python for this purpose. Both of these read in the entire file and save it either as a list (using newline characters to separate lines) or as a long string. If you have a large file you may just want to loop through it line by line without using either of these methods.

{% highlight python %}
# Read file line-by-line with .readlines() [Note that this is slow for *MASSIVE* files because it reads in and stores the whole file as a list]
with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print line
    # To loop another time, you must direct the readlines iterator to start from the top! The same would go for .read().
    f.seek(0)
    for line in lines:
        print line
        
# Read file as one line, and then break into separate lines using the newline character
with open("file.txt", "r") as f:
    contents = f.read()
    contents_list = contents.split("\n") # Split file contents on newline character
    for line in contents_list:
        print line
        
# To go line by line, you could also use a simple for loop. This avoids saving the whole file as a list.
with open("file.txt", "r") as f:
    for line in f:
        print line
        
{% endhighlight %}

## The csv module

The **csv module** is a useful python module for parsing comma-separated files, tab-delimited files, or any files with delimited *fields*. The csv module provides functions for parsing a file which has already been opened using `open()`. Note that the `.reader()` method returns an *iterator* object, which is faster than .readlines(), but similar to for-looping over file contents.

{% highlight python %}
import csv

# Read a standard csv file.
with open("file.csv", "r") as f:
	reader = csv.reader(f)
	for row in reader:
 		print row

# Read a file with a different delimiter (e.g. tab)
with open("file.txt", "r") as f:
	reader = csv.reader(f, delimiter = '\t') # Specify the delimiter if it is not a comma!!
	for row in reader:
		print row
		
{% endhighlight %}

## File parsing

Several examples of file parsing are available in [python4_files](python4_files/). Please go ahead and download these files. 
<br>
The file `parse_delimited.py` contains examples for parsing and extracting information from csv and tab-delimited files (AbilAhuG_uniprot_blastx.txt and AbilAhuG_uniprot_blastx.csv). Note that these are the same file, except one is tab-delimited and one is comma-delimited.
<br>
The `hyphy.py` file has three versions of a script that custom parses an output file from the program Hyphy. This is so you can see how writing a script progresses before it is refined.
<br>
An integral aspect of this file parsing is the **re module**. This python module provides functions for using **regular expressions**. Regular expressions are essentially flexible pattern-matching symbols (see the lesson [cheatsheet](../../Cheatsheets/Cheatsheet_Python4.md) for some commonly-used regex's. The re module, and indeed regular expressions in general, are extremely powerful and endlessly useful. Note that the re module has many, many more available functions associated with it (see the [re module documentation](https://docs.python.org/2/library/re.html)) beyond what is discussed here!!

Several examples of `re` functions used to parse the file [mammal\_dat.nex](python4_files/mammal_dat.nex) are shown in the file [parse\_mammals.py](python4_files/parse_mammals.py) .




