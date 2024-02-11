questions = [
             ["The International Literacy Day is observed on","A. Sep 8","B. Nov 28","C. May 2","D. Sep 22",1],
             ["The language of Lakshadweep. a Union Territory of India, is","A. Tamil","B. Hindi","C. Malayalam","D. Telugu",3],
             ["In which group of places the Kumbha Mela is held every twelve years?","A. Ujjain. Purl; Prayag. Haridwar","B. Prayag. Haridwar, Ujjain,. Nasik","C. Rameshwaram. Purl, Badrinath. Dwarika","D. Chittakoot, Ujjain, Prayag,'Haridwar",2],
             ["Bahubali festival is related to","A. Islam","B. Hinduism","C. Buddhism","D. Jainism",4],
             ["Which day is observed as the World Standards  Day?","A. June 26","B. Oct 14","C. Nov 15","D. Dec 2",2],
             ["Which of the following was the theme of the World Red Cross and Red Crescent Day?","A. Dignity for all - focus on women","B. Dignity for all - focus on Children","C. Focus on health for all","D. Nourishment for all-focus on children",2],
             ["September 27 is celebrated every year as","A. Teachers Day","B. National Integration Day","C. World Tourism Day","D.	International Literacy Day",3],
             ["Who is the author of 'Manas Ka-Hans' ?","A. Khushwant Singh","B. Prem Chand","C. Jayashankar Prasad","D.	Amrit Lal Nagar",4],
             ["The death anniversary of which of the following leaders is observed as Martyrs' Day?","A.Smt. Indira Gandhi","B.PI. Jawaharlal Nehru","C.Mahatma Oandhi","D.Lal Bahadur Shastri",3],
             ["Who is the author of the epic 'Meghdoot","A.Vishakadatta","B.Valmiki","C.Banabhatta","D.Kalidas",4],
             ["Good Friday' is observed to commemorate the event of","A.birth of Jesus Christ","B.birth of' St. Peter","C.crucification 'of Jesus Christ","D.rebirth of Jesus Christ",3],
             ["Who is the author of the book 'Amrit Ki Ore'?","A.Mukesh Kumar","B. Narendra Mohan","C. Upendra Nath","D. Nirad C. Choudhary",2],
             ["Which of the following is observed as Sports Day every year?","A.22nd April","B.26th  july","C.29th August","D.2nd October",3],
             ["World Health Day is observed on","A.Apr 7","B.Mar 6","C.Mat I5","D.Apr 28",1],
             ["Pongal is a popular festival of which state?","A.	Karnataka","B. Kerala","C.	Tamil Nadu","D.Andhra Pradesh",3]
             ]
list = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1240000,2500000,5000000,10000000]
#print(len(list))
print("Lets Play Kon banyega Crorepati")
print()
for i in range(0,len(questions)):
 #question = questions[i]
  print(f"Question for Rs. {list[i]} is")
  print()
  print(f"Q.{i+1} {questions[i][0]}")
  print(f" {questions[i][1]}                {questions[i][2]}")
  print(f" {questions[i][3]}                {questions[i][4]}")
  reply = int(input("Your Option is: "))
  if (reply == questions[i][-1]):
    print(f"Correct answer Rs. {list[i]}")
  else:
    print("Wrong answer")
    #print(f"Correct answer is option {questions[i][-1]} ")
    if (i ==4):
      print(f"Total Cash Won is = Rs 0")
    if (i ==9):
      print(f"Total Cash Won is = Rs. 10,1000")
    break