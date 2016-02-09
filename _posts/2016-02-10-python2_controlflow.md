---
layout: post
title: "Python II: Control Flow"
instructor: Becca
permalink: /python2_controlflow/
materials: files/python2.zip
---

UNDER CONSTRUCTION

# Python 2: Loops!!



First, more useful functions


- using `%` notation in print statements makes for better output

	%d: insert number here <br>
	%f: insert float here <br>
	%s: insert string here <br>

{% highlight python %}
>>> name="Rebecca"
>>> print "My name is %s." % (name)
My name is Rebecca.

>>> print "Two divided by 5 is %f" %(2.0/5)
Two divided by 5 is 0.400000
>>> print "Two divided by 5 is %0.1f" %(2.0/5)
Two divided by 5 is 0.4
>>> print "Two divided by 5 is %d" %(2.0/5)
Two divided by 5 is 0

{% endhighlight %}

- `random` module is useful for generating fake data

{% highlight python %}
>>> import random
>>> dna = ["A","C","T","G"]
>>> genome=dna*250
>>> random.shuffle(genome)
>>> genome
['A', 'A', 'A', 'A', 'T', 'C', 'T', 'A', 'T', 'G', 'G', 'C', 'A', 'C', 'C', 'G', 'C', 'A', 'C', 'T', 'A', 'A', 'T', 'G', 'C', 'G', 'A', 'etc']
>>> "".join(dna) # method to convert list to string
'AAAATCTATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCTGCTTTTAAGGCGCGAACATACGCTGGTGCTAAGCCCGCTAGTTCAGCACCAATCGACTGTTGCAGATAAGTTCATCTGGTCAAAGATCATTCACACAGTAAGATATTGACCGGGAGCCTAGATCTCCAGATGAACGCTGTGGCGCACCCTCGATTCGCGGGGCGATCCAGAAGCCATGAGGAATATAGTTATCTCGTCTGCCCGTATACCGCGCTCCGTACCAATGCACCTTAATATCGAGGCCGGACACGAGACGTACTTCATTTGACCACGCGGTAGCAGGTTCGTGGCATATGAGCCAGATAGGAGTGTGGCTATCCCCAAGGTCCTACAGGTCACTAGACTTAGCTAGTGTTGCAGTTGGGTGGGCACAATGACACCCGGCAGGAGAGCATTTGGCCGCGTGTTTCGACATTCCCTTTAATGAAAGACTCGCCAGCTCTAATACCACTCAACTTTTACCTCTTTGGAAGACTATTATTAAAGATGCCTACTCAAGGTGGATTTCGACACGGTGCGGTCATGTAATCTCGACACCATGGGTTGCAGTTGCGTTCAGTAACTCAAGACTCTGCCATTCGACTGGACACAGATAAGATGGTCATACGCTCGGTACCGATGAGTTCCTAATCTATCGGAACTAAAGCTCGAACGTATCGCATACCACCATGCCGTTGGTGCTAACGAACTTCTCGGCGCCTGATAGACAGGTTGGAATACTGCTCGGCGAATATCATCAATACAATAAACCGTGCGTTC'
>>> 
{% endhighlight %}


# Decisions and conditions: For, If, While


## For loops

A for loop is a way to iterate through a list, range, dictionary, string, etc. Use it for whenever you are repeating something.

{% highlight python %}
for item in thing: #line leading to an indented block ends with a colon
	do this command #indenting blocks of code indicates how the program flows
	do that command
	#return to for statement and move to next item
continue with main commands
{% endhighlight %}

Ok, let's test this out with the print statement. Use this statement in for loops often to check for errors and make sure that everything is working as you would expect.

{% highlight python %}
>>> dna='AGCT'
>>> for item in dna:
...     print item  # here the word "item" is completely arbitrary. 
... 
A
G
C
T

{% endhighlight %}

Let's try something a bit more complicated. Here we can do a repeat of a mathematical operation on items in a list. Note that the `x` `in for x in thing` can be whatever you want, you just have to be consistent within the loop.

{% highlight python %}
>>>sequences=['AGTCTA','AGTCAGTCAGTCAGT','ACTAGCTAGCTA','ACGTCAGTATCGTATTTTA','ACAGTCAGTGATCA','AGT','AGCTAGCTAGCTACGATGCTAGCTAGC'] #create our list
>>> for seq in sequences: #for each sequence in the list
...     length=len(seq) #calculate the length
...     Gcontent=seq.count('G') #count the number of Gs
...     Ccontent=seq.count('C') #count the number of Cs
...     Tcontent=seq.count('T') #count the number of Ts
...     Acontent=seq.count('A') #count the number of As
...     GCcontent=(Gcontent+Ccontent)/float(length) #calculate the GC content
...     print "GC content of %s is %f" %(seq,GCcontent) 
... 
GC content of AGTCTA is 0.333333
GC content of AGTCAGTCAGTCAGT is 0.466667
GC content of ACTAGCTAGCTA is 0.416667
GC content of ACGTCAGTATCGTATTTTA is 0.315789
GC content of ACAGTCAGTGATCA is 0.428571
GC content of AGT is 0.333333
GC content of AGCTAGCTAGCTACGATGCTAGCTAGC is 0.518519

{% endhighlight %}

But, if you see in this code, there is a calculation that is repeated four times, so we should also use a for loop in this case too.

{% highlight python %}
>>>GCdict={} #create an empty dictionary that we will fill with GCcontent values
>>>for seq in sequences:
...     seqdict={} #create another empty dictionary to *temporarily* store ACGT counts
...     length=len(seq)
...     for nuc in ['A','G','C','T']: #for each nucleotide
...             seqdict[nuc]=seq.count(nuc) #count the number of nucleotides in the sequence
...     GCcontent=(seqdict['G']+seqdict['C'])/float(length) #what happens if you don't do float()?
...		GCdict[seq]=GCcontent
...     print "GC content of %s is %f" %(seq,GCcontent)
... 
GC content of AGTCTA is 0.333333
GC content of AGTCAGTCAGTCAGT is 0.466667
GC content of ACTAGCTAGCTA is 0.416667
GC content of ACGTCAGTATCGTATTTTA is 0.315789
GC content of ACAGTCAGTGATCA is 0.428571
GC content of AGT is 0.333333
GC content of AGCTAGCTAGCTACGATGCTAGCTAGC is 0.518519

{% endhighlight %}

Now we can check what is in our dictionary.

{% highlight python %}
>>> for key in GCdict:
...     print '%s: %f' %(key,GCdict[key])
... 
ACAGTCAGTGATCA: 0.428571
ACGTCAGTATCGTATTTTA: 0.315789
ACTAGCTAGCTA: 0.416667
AGTCAGTCAGTCAGT: 0.466667
AGCTAGCTAGCTACGATGCTAGCTAGC: 0.518519
AGTCTA: 0.333333
AGT: 0.333333

{% endhighlight %}

A quick note: you can do for loops in bash too!

{% highlight bash %}
#for file in a list of text files in this directory, print filename
for i in *.txt; do echo $i; done
#for file in a list of .fasta files in this directory, cat file to end of newseqs.fasta file
for i in *.fasta; do cat $i >> newseqs.fasta; done
{% endhighlight %}

And in many many other languages: http://rosettacode.org/wiki/Foreach


## if statements

- IF

If statements are used to test if your variable is true for some logical condition in order to determine what the program should do next. These are super handy and are essentially how you get the computer to make decisions for you.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
continue with main commands
{% endhighlight %}

{% highlight python %} 
>>> numbers=range(20)
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> if sum(numbers) >= 20:
...     print "Sum is greater than 20!"
... 
Sum is greater than 20!

>>> if sum(numbers) >= 20:
...     print "%d is greater than 20!" % (sum(numbers))
... 
190 is greater than 20!
>>> 

{% endhighlight %}

- IF ELSE

Adding an else to your statement allows the computer to decide what to do based on the conditional.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
else:
	do this command
{% endhighlight %}


{% highlight python %}
>>> dna='AGTCTGTAGTCTATAGA'
>>> if (dna.count('G') + dna.count('C'))/len(dna) > 0.5:
...     print "GC content higher than 50%"
... else:
...     print "GC content lower than 50%"
... 
GC content lower than 50%

{% endhighlight %}

- IF and FOR together!

Using conditionals and for loops together makes your code very powerful. Let's take our fake genome we made in the random module example above and randomly select 100 random-length subsequences from it.

Print 25-bp kmers from a randomly generated sequence
{% highlight python %} 
import random
>>> dna='AGCT'
>>> random.choice(dna)
'G'
>>> seq=[random.choice(dna) for letter in range(100)]
>>> seq="".join(seq)
>>> seq
'CGCGCAAAGACCGTTTTTGGCTGCCCAGGATCTCCCGGCTAGGGTATGAGGCCACCAAAAACAGACGGTTCGGCCCGGTATTATAAGAATATCCTAGGAA'
>>> for i in range(0,len(seq)):
...     print seq[i:i+25]
... 
CGCGCAAAGACCGTTTTTGGCTGCC
GCGCAAAGACCGTTTTTGGCTGCCC
CGCAAAGACCGTTTTTGGCTGCCCA
GCAAAGACCGTTTTTGGCTGCCCAG
CAAAGACCGTTTTTGGCTGCCCAGG
AAAGACCGTTTTTGGCTGCCCAGGA
AAGACCGTTTTTGGCTGCCCAGGAT
AGACCGTTTTTGGCTGCCCAGGATC
GACCGTTTTTGGCTGCCCAGGATCT
ACCGTTTTTGGCTGCCCAGGATCTC
CCGTTTTTGGCTGCCCAGGATCTCC
CGTTTTTGGCTGCCCAGGATCTCCC
GTTTTTGGCTGCCCAGGATCTCCCG
TTTTTGGCTGCCCAGGATCTCCCGG
TTTTGGCTGCCCAGGATCTCCCGGC
...
ATTATAAGAATATCCTAGGAA
TTATAAGAATATCCTAGGAA
TATAAGAATATCCTAGGAA
ATAAGAATATCCTAGGAA
TAAGAATATCCTAGGAA
AAGAATATCCTAGGAA
AGAATATCCTAGGAA
GAATATCCTAGGAA
AATATCCTAGGAA
ATATCCTAGGAA
TATCCTAGGAA
ATCCTAGGAA
TCCTAGGAA
CCTAGGAA
CTAGGAA
TAGGAA
AGGAA
GGAA
GAA
AA
A
# but we don't want kmers that are less than 25bp!

>>> for i in range(len(seq)):
...     if len(seq[i:i+25]) < 25:
...             break  # if it does not meet this condition, for loop ends.
...     else:
...             print seq[i:i+25]
... 
CGCGCAAAGACCGTTTTTGGCTGCC
GCGCAAAGACCGTTTTTGGCTGCCC
CGCAAAGACCGTTTTTGGCTGCCCA
GCAAAGACCGTTTTTGGCTGCCCAG
CAAAGACCGTTTTTGGCTGCCCAGG
AAAGACCGTTTTTGGCTGCCCAGGA
AAGACCGTTTTTGGCTGCCCAGGAT
AGACCGTTTTTGGCTGCCCAGGATC
GACCGTTTTTGGCTGCCCAGGATCT
ACCGTTTTTGGCTGCCCAGGATCTC
...
TCGGCCCGGTATTATAAGAATATCC
CGGCCCGGTATTATAAGAATATCCT
GGCCCGGTATTATAAGAATATCCTA
GCCCGGTATTATAAGAATATCCTAG
CCCGGTATTATAAGAATATCCTAGG
CCGGTATTATAAGAATATCCTAGGA
CGGTATTATAAGAATATCCTAGGAA

>>> for i in range(len(seq)):
...     if len(seq[i:i+25]) < 25:
...             print 'too short! continuing'
...             continue
...     else:
...             print seq[i:i+25]
... 

{% endhighlight %}


You can do nested if/else statements.

{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
else:
	if logical condition == True: 
		do this command  
		do this command
	else:
		do this command
{% endhighlight %}



{% highlight python %}


{% endhighlight %}

But, wait, wasn't that a terribly long way to do something? Yes it was! Here is a better way:

- IF ELIF

The if/elif statement can be used when you would otherwise use multiple nested if/else statements. They are performed *in order* and will not go through all of the options if one before the end is True.


{% highlight python %}
if logical condition == True: 
	do this command  
	do this command
elif other logical condition == True:
	do this command
elif other logical condition == True:
	do this command
else:
	do this command
{% endhighlight %}



{% highlight python %}


{% endhighlight %}

- Important tip: You can make a dictionary without knowing/defining a priori what they keys are

{% highlight python %}
>>> dictionary={}
>>> seq='AGTAGTATTTGAGAGTTTAGATATAG'
>>> for letter in seq:
...     if letter in dictionary.keys(): #if the key already exists
...             dictionary[letter]+=1 #augment the value by one
...     else:
...             dictionary[letter]=1 #or else, make the new key
... 
>>> dictionary
{'A': 9, 'T': 10, 'G': 7}

{% endhighlight %}

Another example:
{% highlight python %}
seqs=['AUUGACAUCGAUCGA','AGACTGATCGATCTAG','JIEONONE']
for seq in seqs:
	if 'U' in seq:
		print '%s is RNA' %seq
	elif 'T' in seq:
		print '%s is DNA' %seq
	else:
		print '%s might be a protein' %seq
{% endhighlight %}


## While

While loops repeat until some condition becomes False. Be careful as they are prone to infinite loops. If you get caught in one, hit Ctrl+C.

{% highlight python %}
while condition == True:
	do this command
	do that command
continue with normal commands
{% endhighlight %}

Example script with while loop:
{% highlight python %}
import time #useful module for printing timestamps and counting time units during your scripts
i = 0
while i < 5:
        time.sleep(1) #wait one second before proceeding
        i+=1
        print i
print "Time is up!"
{% endhighlight %}

outputs:
{% highlight bash %}
python timer.py
1
2
3
4
5
Time is up!
{% endhighlight %}

While loops can ensure that user input is in the right format. They are also useful when you want to manipulate part of the conditional that is being used within the loop.

Try using this program, which has a test for user input using a while loop:
{% highlight python %}
x=int(input("Give me a number from 1 to 10: ")) #accepts user input, converts to an integer
while x not in range(0,11): #if input was not number between 1 and 10
        print "That's not a number between 1 and 10 :(" #prints a complaint
        x=int(input("Give me a number from 1 to 10: ")) #asks for a new number
print "Thanks!" #thanks the user for being a nice user
{% endhighlight %}

Here we manipulate the conditional (x) within the loop. Could you do this with a for loop? Why is the last number less than 40?
{% highlight python %} 
>>> x=2000
>>> while x > 40:
...     x=x/4
...     if x%2 == 0:
...             print "%d is even!" %x
...     else:
...             print "%d is not even!" %x
...             x+=5
... 
500 is even!
125 is not even!
32 is even! 

{% endhighlight %}




## List comprehensions

List comprehensions are faster ways to execute loops that result in lists. Your typical loop structure is shown below followed by the comprehension structure.

{% highlight python %}
list1=[] #make empty list
for item in thing:
	list1.append(item)	

list1 = [item for item in thing]
{% endhighlight %}

examples:

{% highlight python %}
>>> mylist=[]
>>> for i in range(0,20):
...     mylist.append(i**3)
... 
>>> mylist
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

>>> mylist=[i**3 for i in range(0,20)]
>>> mylist
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

{% endhighlight %}

{% highlight python %}
>>> sequences=['AGTCTA','AGTCAGTCAGTCAGT','ACTAGCTAGCTA','ACGTCAGTATCGTATTTTA','ACAGTCAGTGATCA','AGT','AGCTAGCTAGCTACGATGCTAGCTAGC']
>>> mylist=[len(seq) for seq in sequences]
>>> mylist
[6, 15, 12, 19, 14, 3, 27]

>>> mylist=[(seq,len(seq)) for seq in sequences]
>>> mylist
[('AGTCTA', 6), ('AGTCAGTCAGTCAGT', 15), ('ACTAGCTAGCTA', 12), ('ACGTCAGTATCGTATTTTA', 19), ('ACAGTCAGTGATCA', 14), ('AGT', 3), ('AGCTAGCTAGCTACGATGCTAGCTAGC', 27)]

>>> dictionary=dict(mylist)
>>> dictionary
{'ACAGTCAGTGATCA': 14, 'ACGTCAGTATCGTATTTTA': 19, 'ACTAGCTAGCTA': 12, 'AGTCAGTCAGTCAGT': 15, 'AGCTAGCTAGCTACGATGCTAGCTAGC': 27, 'AGTCTA': 6, 'AGT': 3}
>>> 

{% endhighlight %}









- more examples

{% highlight python %}
>>> newseqs=[] #create an empty list
>>> for i in range(100): #do this 100 times
...     int1=random.randint(0,1000) #choose a random integer
...     int2=random.randint(0,1000) #choose another random integer
...     if int1 > int2: #if int1 is greater than int2, then select a sequence from int2 to int1
...             newseqs.append(genome[int2:int1])
...     else: #otherwise, do the opposite
...             newseqs.append(genome[int1:int2])
...	random.shuffle(genome) #this could be optional depending what your code is for
... 
>>> newseqs
['GAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGA', 'CGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGAC', 'GCACTCCGCTG', 'TGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAA', 'TGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGT', 'TAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAG', 'CCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATA', 'TGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCT', 'ACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCTGCTTTTAAG', 'CGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGT', 'TTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTG', 'TTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCC', 'AAATCTATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAAC', 'AGTAAGACTTTGGTG', 'CATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCC', 'GTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAA', 'ACTCCGCTGCTTTTAAG', 'TTTTA', 'GAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCC', 'TTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGG', 'GAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGC', 'TGGACAGAACAACACTGCTCCAGCCCCACAGATTAA', 'GCACTA', 'TTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTAC', 'GATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCC', 'GGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGAT', 'GTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGA', 'CTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCT', 'TATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGG', 'GCACTAATGCGAGGTCGACAGAGTAAGA', 'GTAGG', 'CTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGAT', 'CGCACTAATGCGA', 'ATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGG', 'CTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGA', 'GTCGTGGACT', 'GTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTAT', 'GTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTA', 'ATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACG', 'CTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCAC', 'CGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGG', 'TAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGC', 'CGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCTGCTTT', 'AGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACA', 'TGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCA', 'TCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCT', 'GCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGGCACTCCGCTGCTTTT', 'CGAGCTAGTGTGACTCTCCA', 'AAAATCTATGGC', '', 'TCTATGGCACCGCACTAATGCGAGGTCGACAGAGT', 'ACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTT', 'CCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCA', 'CTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCA', 'TGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCA', 'TGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGAT', 'AATCTAT', 'CTGGACAGAACAACACTGCTCCAGCCCCACAGAT', 'TAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACG', 'AGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTC', 'AGTAAGA', 'GTTGCTTATGGGAGA', 'CAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGA', 'TCGTTGCACGAGCTAGTGTGACTCTCCA', 'CTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGA', 'GTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGC', 'GAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGG', 'CATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGG', 'GACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCT', 'GACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCT', 'GTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGG', 'GAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAAC', 'TGGACAGAACAACACTGCTCCAGC', 'TATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAG', 'ATCTATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGA', '', 'TGCTTAGGTTGCTTATGGGAGAC', 'GGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAA', 'CTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCG', 'CGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCG', 'TTGCACGAGCTAGTGTGACTCTCCAAGGTAGT', 'GTTGACTGGACAGAACAACACTGCTCCAGCCCCAC', 'GACAGAACAACACTGC', 'CCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCC', 'CGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACG', 'TGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCG', 'CTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCT', 'GGACTTGTCCATGCTGTAGGATATGTGAT', 'AGATTAACTGATCT', 'ATCTATGGCACCGCACTAATGCGAGGTCGA', 'ATATGTGATCGTTGCACGAGCTAGTGTGACTC', 'CACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAGAACAACACTGCTCCAGCCCCACAGATTAACTGATCTGCAACGTACGTGG', 'GATTAACTGATCTGCAA', 'ATGGCACCGCACTAATGCGAGGTCGACAGAGTA', 'ACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGGCTTCCGGTCGTTTTATGGTTGACTGGACAG', 'ATGGCACCGCACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGT', 'TAGTGTGACTCTCCAAGGTAG', 'CACTAATGCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGA', 'GCGAGGTCGACAGAGTAAGACTTTGGTGTGTCGTGGACTTGTCCATGCTGTAGGATATGTGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGC', 'TGATCGTTGCACGAGCTAGTGTGACTCTCCAAGGTAGTCGAACTGCTGCTTAGGTTGCTTATGGGAGACGG']

>>> for seq in newseqs:
...     if len(seq) < 10: go through the list, find short sequences
...             print seq 
...             newseqs.remove(seq) #then remove the sequence from the list (you could add these to a new list also)
... 
TTTTA
GCACTA
GTAGG
AATCTAT
AGTAAGA
...
>>> len(newseqs)
93 #7 sequences were removed

{% endhighlight %}

