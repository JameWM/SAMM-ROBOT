import numpy as np
import pandas as pd
# Hi My name is Jame WM :
# I love Code


"""LI1 = ['เคยไปสถานที่ที่มีผู้ติดเชื้อหรือไม่0 : 2', 'เป็นไข้ในช่วง 7 วันนี้หรือไม่1 : 1', 'มีอาการจามบ้างไหม2 : 1', 'มีอาการ คันหรือคัดจมูก บ้างไหม3 : 1',
       'มีอาการน้ำมูกไหลบ้างไหม4 : 1', 'มีผื่นขึ้นตามตัวหรือขึ้นบริเวณไหนบ้างไหม5 : 1', 'มีอาการไอแห้งบ้างไหม6 : 5', 'มีอาการไอแบบมีเสมหะบ้างไหม7 : 2',
       'มีอาการหอบ แน่นหน้าอก หายใจไม่คล่อง บ้างไหม8 : 5', 'มีอาการเจ็บคอบ้างไหม9 : 3', 'เสียงแหบไหม10  : 3', 'ล่าสุดตอนนี้ยังมีไข้อ่อนๆหรือมีไข้สูงอยู่ไหม11 : 5',
       'มีอาการปวดศีรษะบ้างไหม12 : 2', 'มีอาการปวดเมื่อยกล้ามเนื้อบ้างไหม13 : 1', 'มีอาการรู้สึกเมื่อยล้าบ้างไหม14 : 4', 'มีความรู้สึกหายใจลำบากไหม15 : 6']

LI2 = ['อายุ : None', 'มีโรคประจำตัวหรือไม่ : None', 'ได้ฉีดวัคซีนหรือไม่ : ไม่ได้ฉีดวัคซีน']

Q1 = ['ww', 'ไม่เป็น', 'ไม่มี', 'ไม่มีครับ', 'มี', 'ไม่มีครับ', 'มี', 'ไม่มี', 'มี', 'มี', 'มี', 'มีไข้สูง', 'มี', 'มี', 'มี', 'มี']
#TT = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]#, 6, 7, 8, 9, 10, 11, 12, 14, 15]
Q2 = ['None', 'None', 'ไม่ได้ฉีดวัคซีน']

Set = []

number = 0
Score = 0
Error = 0

Q1 = np.array(Q1)
for i in Q1:
       if "None" in Q1[number]:
              Error += 1
              Set.append(number)
       if "เคย" in Q1[number] and "ไม่" not in Q1[number]:
              Score += 2
              Set.append(number)
       if "เคย" in Q1[number] and "ไม่" in Q1[number]:
              Score -= 0
              Set.append(number)
       if "เป็น" in Q1[number] and "ไม่" not in Q1[number]:
              Score += 1
              Set.append(number)
       if "เป็น" in Q1[number] and "ไม่" in Q1[number]:
              Score -= 0
              Set.append(number)
       if "มี" in Q1[number] and "ไม่" not in Q1[number]:
              Score += 1
              Set.append(number)
       if "มี" in Q1[number] and "ไม่" in Q1[number]:
              Score -= 0
              Set.append(number)
       if Q1[number] == "ไม่":
              Score -= 0
              Set.append(number)
       number += 1


if "มี" in Q1[6] and "ไม่" not in Q1[6]:
       Score += 4
       Set.append(6)
if "มี" in Q1[6] and "ไม่" in Q1[6]:
       Score -= 0
       Set.append(6)
if "มี" in Q1[7] and "ไม่" not in Q1[7]:
       Score += 1
       Set.append(7)
if "มี" in Q1[7] and "ไม่" in Q1[7]:
       Score -= 0
       Set.append(7)
if "มี" in Q1[8] and "ไม่" not in Q1[8]:
       Score += 4
       Set.append(8)
if "มี" in Q1[8] and "ไม่" in Q1[8]:
       Score -= 0
       Set.append(8)
if "มี" in Q1[9] and "ไม่" not in Q1[9]:
       Score += 2
       Set.append(9)
if "มี" in Q1[9] and "ไม่" in Q1[9]:
       Score -= 0
       Set.append(9)
if "มี" in Q1[10] and "ไม่" not in Q1[10]:
       Score += 2
       Set.append(10)
if "มี" in Q1[10] and "ไม่" in Q1[10]:
       Score -= 0
       Set.append(10)
if "อ่อน" in Q1[11] and "ไม่" not in Q1[11]:
       Score += 2
       Set.append(11)
if "สูง" in Q1[11] and "ไม่" not in Q1[11]:
       Score += 4
       Set.append(11)
if "มี" in Q1[11] and "ไม่" in Q1[11]:
       Score -= 0
       Set.append(11)
if "มี" in Q1[12] and "ไม่" not in Q1[12]:
       Score += 1
       Set.append(12)
if "มี" in Q1[12] and "ไม่" in Q1[12]:
       Score -= 0
       Set.append(12)
if "มี" in Q1[14] and "ไม่" not in Q1[14]:
       Score += 3
       Set.append(14)
if "มี" in Q1[14] and "ไม่" in Q1[14]:
       Score -= 0
       Set.append(14)
if "มี" in Q1[15] and "ไม่" not in Q1[15]:
       Score += 5
       Set.append(15)
if "มี" in Q1[15] and "ไม่" in Q1[15]:
       Score -= 0
       Set.append(15)
I = 0
Num = []
for i in Q1:
       Num.append(I)
       I += 1
if 6 in Num and 7 in Num and 8 in Num and 9 in Num and 10 in Num and 11 in Num and 12 in Num and 14 in Num and 15 in Num:
       Num.append(6)
       Num.append(7)
       Num.append(8)
       Num.append(9)
       Num.append(10)
       Num.append(11)
       Num.append(12)
       Num.append(14)
       Num.append(15)
print(Num == Set)
if Num != Set:
       Error+=1
if Error > 0:
       print("ข้อมูลที่คุณให้มามีข้อผิดพลาดจึงทำให้การทำนายผลไม่มีความแม่นยำ จำนวน ค่า ERROR : "+ str(Error))
if Score > 6 and Score < 10:
       print("โรคภูมิแพ้")
if Score > 12 and Score < 17:
       print("โรคไข้หวัด")
if Score > 16 and Score < 21:
       print("โรคไข้หวัดใหญ่")
if Score > 25 and Score < 40:
       print("โรคโควิด-19")

for i in Q1:
       if "None" in Q1[number]:
              Error+=1
       if "have been to" in Q1[number] or "ever" in Q1[number] or "yes" in Q1[number] and "never" not in Q1[number] and "no" not in Q1[number]:
              Score += 2
       if "have been to" in Q1[number] or "ever" in Q1[number] or "yes" in Q1[number] or "never" in Q1[number] or "no" in Q1[number]:
              Score -= 0
       if "is" in Q1[number] or "yes" in Q1[number] and "no" not in Q1[number]:
              Score += 1
       if "is" in Q1[number] or "yes" in Q1[number] and "no" in Q1[number]:
              Score -= 0
       if "have" in Q1[number] and "no" not in Q1[number] and "do not " not in Q1[number] and "without" not in Q1[number]:
              Score += 1
       if "have" in Q1[number] or "no" in Q1[number] or "do not " in Q1[number] or "without" in Q1[number]:
              Score -= 0

       number += 1


if "have" in Q1[6] and "no" not in Q1[6] and "do not " not in Q1[6] and "without" not in Q1[6]:
       Score += 4
if "have" in Q1[6] or "no" in Q1[6]  or "do not " in Q1[6] or "without" in Q1[6]:
       Score -= 0

if "have" in Q1[7] and "no" not in Q1[7] and "do not " not in Q1[7] and "without" not in Q1[7]:
       Score += 1
if "have" in Q1[7] or "no" in Q1[7] or "do not " in Q1[7] or "without" in Q1[7]:
       Score -= 0

if "have" in Q1[8] and "no" not in Q1[8] and "do not " not in Q1[8] and "without" not in Q1[8]:
       Score += 4
if "have" in Q1[8] or "no" in Q1[8] or "do not " in Q1[8] or "without" in Q1[8]:
       Score -= 0

if "have" in Q1[9] and "no" not in Q1[9] and "do not " not in Q1[9] and "without" not in Q1[9]:
       Score += 2
if "have" in Q1[9] or "no" in Q1[9] or "do not " in Q1[9] or "without" in Q1[9]:
       Score -= 0

if "have" in Q1[10] and "no" not in Q1[10] and "do not " not in Q1[10] and "without" not in Q1[10]:
       Score += 2
if "have" in Q1[10] or "no" in Q1[10] or "do not " in Q1[10] or "without" in Q1[10]:
       Score -= 0

if "a mild fever" in Q1[11] or "have" in Q1[11] and "no" not in Q1[11] and "do not " not in Q1[11] and "without" not in Q1[11]:
       Score += 2
if "high fever" in Q1[11] or "have" in Q1[11] and "no" not in Q1[11] and "do not " not in Q1[11] and "without" not in Q1[11]:
       Score += 4
if "have" in Q1[11] or "no" in Q1[11] or "do not " in Q1[11] or "without" in Q1[11]:
       Score -= 0

if "have" in Q1[12] and "no" not in Q1[12] and "do not " not in Q1[12] and "without" not in Q1[12]:
       Score += 1
if "have" in Q1[12] or "no" in Q1[12] or "do not " in Q1[12] or "without" in Q1[12]:
       Score -= 0

if "have" in Q1[14] and "no" not in Q1[14] and "do not " not in Q1[14] and "without" not in Q1[14]:
       Score += 3
if "have" in Q1[14] or "no" in Q1[14] or "do not " in Q1[14] or "without" in Q1[14]:
       Score -= 0

if "have" in Q1[15] and "no" not in Q1[15] and "do not " not in Q1[15] and "without" not in Q1[15]:
       Score += 5
if "have" in Q1[15] or "no" in Q1[15] or "do not " in Q1[15] or "without" in Q1[15]:
       Score -= 0

print(Score)
print("There are errors in the data you provided and therefore the prediction is inaccurate | ERROR : ",Error)

if Score > 6 and Score < 10:
       print("allergy")
if Score > 12 and Score < 17:
       print("common cold")
if Score > 16 and Score < 21:
       print("influenza")
if Score > 25 and Score < 40:
       print("COVID-19")"""


AA = 1;OTP = 0;R = 0;RT = 0
LI2 = ['อายุ : None', 'มีโรคประจำตัวหรือไม่ : None', 'ได้ฉีดวัคซีนหรือไม่ : ไม่ได้ฉีดวัคซีน']
#Q2 = ['None', 'None', 'ไม่ได้ฉีดวัคซีน']
Q2 = ['อายุ 19 ครับ', 'None', 'ไม่ได้ฉีดวัคซีน'] #AA แทนได้

if AA == 2:
       for i in range(0, 100):
              R += 1
              if str(R) in Q2[0]:
                     RT = R
       print("เราจะแนะนำวัคซีนที่คุณควรฉีด ขอตรวจสอบข้อมูลเบื้องต้นก่อนนะครับ")
       if Q2[0] == 'None' or Q2[1] == 'None' or Q2[2] == 'None':
              print("ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลมีข้อผิดพลาด")
              OTP = 0
       if Q2[0] != 'None' and Q2[1] != 'None' and Q2[2] != 'None':
              if OTP == 0:
                     if "เคย" in Q2[1] and "ไม่" not in Q2[1]:
                            OTP = 1
                     if "เคย" in Q2[1] and "ไม่" in Q2[1]:
                            OTP = 2
                     if "เป็น" in Q2[1] and "ไม่" not in Q2[1]:
                            OTP = 1
                     if "เป็น" in Q2[1] and "ไม่" in Q2[1]:
                            OTP = 2
                     if "มี" in Q2[1] and "ไม่" not in Q2[1]:
                            OTP = 1
                     if "มี" in Q2[1] and "ไม่" in Q2[1]:
                            OTP = 2
                     if Q2[1] == "ไม่":
                            OTP = 2
                     else:
                            print("ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลมีข้อผิดพลาด")
                            OTP = 0
if OTP == 1 :
       print("ไม่สามารถแนะนำวัคซีนได้เนื่องจากข้อมูลที่ให้มาไม่เหมาะสมกับการที่จะได้รับวัคซีน")
if OTP == 2:
       print("เราจะแนะนำวัคซีนเป็น")
       if  RT > 17 and RT < 60:
              print("ซินโนเวต หรือ โคโรนาแวค หรือ ซิโนฟาร์ม")
       if  RT > 18 :
              print("โมเดอร์นา หรือ แอสตร้าเซนเนก้า")
       print("ก่อนจะฉีดควรเช็ครายละเอียดวัคซีนก่อนนะครับ")







