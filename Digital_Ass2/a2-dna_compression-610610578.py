#!/usr/bin/env python
# coding: utf-8

# **1.  610610578 ชุติพนธ์ วิมลกาญจนา

# ให้ นศ. สร้าง Python notebook ที่แสดงการบีบอัดข้อมูล DNA sequence โดยใช้ Lossless coding อัลกอริธึมใดก็ได้ที่ นศ.สนใจ
# 
# การทำงานต้องเป็นไปตามข้อกำหนดต่อไปนี้
# 
#  1.ตั้งชื่อไฟล์ในรูปแบบ "a2-dna_compression-รหัสนักศึกษา.ipynb" และระบุ ชื่อ-สกุล และรหัสนักศึกษาไว้ใน Python notebook ด้วย
#  2.ผู้ใช้ต้องสามารถพิมพ์/ป้อนข้อมูล sequence ที่ต้องการเข้ารหัสด้วยคีย์บอร์ดได้
#  3.ส่วนเข้ารหัส (Encoder) - มีความสามารถต่อไปนี้
#     
#     3.1คำนวณ Entropy ของ sequence ได้ (2 pts.)
#     3.2แสดงข้อมูลที่บีบอัดแล้ว (binary หรือ text) ได้ (8 pts.)
#     3.3แสดงข้อมูลอื่น ๆ ที่จำเป็นต่อการบีบอัดข้อมูล (huffman table, dictionary, ...) ได้ (6 pts.)
#     3.4คำนวณ Compression Ratio ได้ (2 pts)
#     3.5คำนวณ Bitrate ได้ (bps: bits per symbol) (2 pts)
#  4.ส่วนถอดรหัส (Decoder) - มีความสามารถต่อไปนี้
#     
#     4.1แสดงข้อมูลที่ถอดรหัสออกมาได้ (8 pts.)
#     4.2แสดง error rate (%) ได้ (2 pts.)
#  
#  5.มีคำอธิบายหลักการ ขั้นตอนการทำงาน ผลการทำงานในแต่ละขั้นตอน รวมถึงข้อสรุปด้านต่าง ๆ แทรกอยู่ภายใน Python notebook
#  6.ห้ามใช้ไลบรารีสำเร็จรูปสำหรับการบีบอัดข้อมูลในการพัฒนา

# **2.  พิมพ์/ป้อนข้อมูล sequence ที่ต้องการเข้ารหัสด้วยคีย์บอร์ดด้วย input
#     เก็บข้อมูล sequence

# In[218]:


x=input('Input DNA Sequences: ')
dna_seq=x


# **3.1  คํานวณหาความยาวของ sequence
#      คํานวณหาความน่าจะเป็นของ sequence
#      คำนวณ Entropy ของ sequence

# In[219]:


from math import log2

Length=len(dna_seq)

str_countA = dna_seq.count('A')
str_countT = dna_seq.count('T')
str_countC = dna_seq.count('C')
str_countG = dna_seq.count('G')

PA = str_countA/Length
PT = str_countT/Length
PC = str_countC/Length
PG = str_countG/Length


x=[PA,PT,PC,PG]
sum=0

for i in range (0,len(x)):
    sum += (x[i]*(log2(x[i])))
    
En = -sum


print('Length DNA sequence = ',Length)
print("The count of 'A' is", str_countA)
print("The count of 'T' is", str_countT)
print("The count of 'C' is", str_countC)
print("The count of 'G' is", str_countG)


print("Probability A =",PA )
print("Probability T =",PT )
print("Probability C =",PC)
print("Probability G =",PG)


print("Entropy =",En)


# **3.2  แสดงข้อมูลที่บีบอัดแล้วเเบบ text โดยจัดเก็บข้อมูลของ sequence ด้วย function RLE(seq) เเละเเสดงผล encoding sequence ด้วยการทํา for loop(เนื่องจากมีการเก็บไว้ใน list ซ้อน list จึงต้องวน for loop 2ชั้น)
# *RLE(seq) เก็บข้อมูลเเบบ list ซ้อน list
# 

# In[220]:




def RLE(seq):
  comp_d = []
  dracula = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char:
      dracula +=1
    else :
      comp_d.append([char,dracula])
      char = seq[i]
      dracula = 1
  comp_d.append([char,dracula])
  return comp_d
 
 


comp_data = RLE(dna_seq)

compressed_sequences = ''
 
for i in range(0,len(comp_data)):
  for j in comp_data[i]:
    compressed_sequences += str(j)
    








print("DNA Encoding Sequences :",compressed_sequences)


# **3.3  แสดงข้อมูลอื่น ๆ ที่จำเป็นต่อการบีบอัดข้อมูลเเบบ Run-Length-Code ผ่าน RLE(seq) ท่ี่เก็บข้อมูล sequence ไว้อยู่เเล้ว(เก็บในรูปเเบบของ list[list[]])

# In[221]:


print("DNA Encoding Sequences Information :",comp_data)


# **3.4  คํานวณขนาดก่อนบีบอัดข้อมูล
#      คํานวณขนาดหลังบีบอัดข้อมูล
#      คำนวณ Compression Ratio

# In[222]:


U_S=len(dna_seq)*8
C_S=len(compressed_sequences)*8
C_R=(U_S/C_S)
print("Length Of Uncompressed :",len(dna_seq))
print("Length Of Compressed :",len(compressed_sequences))
print("Uncompressed Size :",U_S,"bits")
print("Compressed Size :",C_S,"bits")
print("Compression Ratio :",C_R)


# **3.5  คำนวณ Bitrate

# In[223]:


bR=(C_S/len(dna_seq))
print("Bitrate :",bR,"bps")


# **4.1  แสดงข้อมูลที่ถอดรหัสออกมาผ่าน function RLD(compressed_seq) 

# In[224]:


def run_length_decoding(compressed_seq):
  seq = ''
  for i in range(0,len(compressed_seq)):
    if compressed_seq[i].isalpha() == True:
      for j in range(int(compressed_seq[i+1])):
        seq += compressed_seq[i]
 
  return(seq)


decompressed_sequences=(run_length_decoding(compressed_sequences))
print("DNA Decoding Sequences :",decompressed_sequences)


def run_length_decoding(compressed_seq):
  seq = ''
  for i in range(0,len(compressed_seq)):
    if compressed_seq[i].isalpha() == True:
      for j in range(int(compressed_seq[i+1])):
        seq += compressed_seq[i]
 
  return(seq)



# **4.2  คํานวณหาค่า error rate

# In[225]:


dracula = 0
for i in range (0,len(dna_seq)):
    if(dna_seq[i]!=decompressed_sequences[i]):
        dracula+=1

print("Error Count :",dracula)
eR = (dracula/len(dna_seq))*100
print("Error Rate :",eR,"%")


# ******เหตุผล เเละ ข้อสรุปของงานชิ้นนี้******
# การบีบอัดข้อมูลที่ผมเลือกใช้เป็นเเบบ Run-length encoding เนื่องจากเป็นการบีบอัดที่สามารถตรวจสอบความถูกต้องได้ง่าย(คนตรวจสอบว่าเขียน code 
# ถูกไหม) ถ้าเปรียบเทียบกับวิธีการ encode อื่นๆที่จะมีรายละเอียดต่างๆในการบีบอัดที่ยากกว่าทําให้ผมตรวจสอบความถูกต้องได้ยาก อีกทั้งตัวผมยังมั่นใจเเละ
# ถนัดในวิธี้ที่สุดจึงตัดสินใจเลือกวิธีนี้
# 
# จากผลลัพธ์ของการใช้วิธีนี้เเสดงให้เห็นถึงความเเม่นยําในการ encode และ decode ข้อมูลไม่มีความผิดพลาดในขั้นตอนใดๆ เเต่ก็มีข้อจํากัดด้านประสิทธิภาพ
# การบีบอัดข้อมูลให้เห็นเช่น ในตัวอย่าง dna sequence ที่ผมเลือกมาเเสดงนี้จะเห็นได้ชัดว่าข้อมูลไม่ได้มีการบีบอัดลงเลยทําให้เห็นกรณีข้อจํากัดของ 
# Run-length ที่ผมเลือกใช้อย่างชัดเจน
