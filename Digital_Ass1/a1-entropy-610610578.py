#!/usr/bin/env python
# coding: utf-8

# In[2]:


from math import log

x = open(r'/Users/hok191/Digital_Ass1/s1.fasta','r')
a = x.read()
x.close()

b=a[29:]
DNA= b.replace("\n","")
Length=len(DNA)

str_countA = DNA.count('A')
str_countT = DNA.count('T')
str_countC = DNA.count('C')
str_countG = DNA.count('G')

PA = str_countA/Length
PT = str_countT/Length
PC = str_countC/Length
PG = str_countG/Length

EA = -1*PA*log(PA,2)
ET = -1*PT*log(PT,2)
EC =  -1*PC*log(PC,2)
EG = -1*PG*log(PG,2)

En =EA+ET+EC+EG

print("====================FROM s1.fasta====================")
print('Length DNA sequence = ',Length)
print("The count of 'A' is", str_countA)
print("The count of 'T' is", str_countT)
print("The count of 'C' is", str_countC)
print("The count of 'G' is", str_countG)


print("Probability A ",PA )
print("Probability T ",PT )
print("Probability C ",PC)
print("Probability G ",PG)


print("Entropy ",En)
print("=====================================================")


# In[ ]:


from math import log

x = open(r'/Users/hok191/Digital_Ass1/s2.fasta','r')
a = x.read()
x.close()

b=a[29:]
DNA= b.replace("\n","")
Length=len(DNA)

str_countA = DNA.count('A')
str_countT = DNA.count('T')
str_countC = DNA.count('C')
str_countG = DNA.count('G')

PA = str_countA/Length
PT = str_countT/Length
PC = str_countC/Length
PG = str_countG/Length

EA = -1*PA*log(PA,2)
ET = -1*PT*log(PT,2)
EC =  -1*PC*log(PC,2)
EG = -1*PG*log(PG,2)

En =EA+ET+EC+EG

print("====================FROM s2.fasta====================")
print('Length DNA sequence = ',Length)
print("The count of 'A' is", str_countA)
print("The count of 'T' is", str_countT)
print("The count of 'C' is", str_countC)
print("The count of 'G' is", str_countG)


print("Probability A ",PA )
print("Probability T ",PT )
print("Probability C ",PC)
print("Probability G ",PG)


print("Entropy ",En)
print("=====================================================")


# In[1]:


from math import log

x = open(r'/Users/hok191/Digital_Ass1/s3.fasta','r')
a = x.read()
x.close()

b=a[29:]
DNA= b.replace("\n","")
Length=len(DNA)

str_countA = DNA.count('A')
str_countT = DNA.count('T')
str_countC = DNA.count('C')
str_countG = DNA.count('G')

PA = str_countA/Length
PT = str_countT/Length
PC = str_countC/Length
PG = str_countG/Length

EA = -1*PA*log(PA,2)
ET = -1*PT*log(PT,2)
EC =  -1*PC*log(PC,2)
EG = -1*PG*log(PG,2)

En =EA+ET+EC+EG

print("====================FROM s3.fasta====================")
print('Length DNA sequence = ',Length)
print("The count of 'A' is", str_countA)
print("The count of 'T' is", str_countT)
print("The count of 'C' is", str_countC)
print("The count of 'G' is", str_countG)


print("Probability A ",PA )
print("Probability T ",PT )
print("Probability C ",PC)
print("Probability G ",PG)


print("Entropy ",En)
print("=====================================================")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




