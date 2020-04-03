import time
question_list = [
  "How many continents are there?",       # pehla question
  "What is the capital of India?",      # doosra question
  "NG mei kaun se course padhaya jaata hai?"  # teesra question
]

options_list = [
  #pehle question ke liye options
  "(1) Four\t(2) Nine\n(3) Seven\t(4)Eight\n*50-50 life line*",
  #second question ke liye options
  "(1) Chandigarh\t(2) Bhopal\n(3) Chennai\t(4) Delhi\n*50-50 life line*",
  #third question ke liye options
  "(1) Software Engineering\t(2) Counseling\n(3) Tourism\t(4) Agriculture\n*50-50 life line*",

]


options_50_50 = [
  #pehle question ke liye options
  "(1) Four\t(2) Seven",
  #second question ke liye options
  "(1) Chandigarh\t(2) Delhi",
  #third question ke liye options
  "(1) Software Engineering\t(2) Tourism",

]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
solution_list1=[2,2,1]
counter=0


for i in range(len(question_list)):
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<*KBC*>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print("Aapka {}st sawal hai....".format(i+1))
  time.sleep(3)
  print(question_list[i])
  input()
  print(options_list[i])
  k=int(input("your answer_"))
  if k==5050:
    counter+=1
    if counter>1:
      print("SORRY..!!u already used once")
      k=int(input())
      if k==solution_list[i]:
        print("Checkin...plz wait...")
        time.sleep(2)
        print("Congrats...!!!\nAapka jawab bilkul sahi H")
        input()
      else:
        print("Checkin...plz wait...")
        time.sleep(2)
        print("SORRY..!! aapka javab galat hai.\n@@@GAME OVER@@@")
        break
    else:
      print("Plz_wait...Prepairing...")
      time.sleep(3)
      print(options_50_50[i])
      k1=int(input("your answer_"))
      if k1==solution_list1[i]:
        print("Checkin...plz wait...")
        time.sleep(2)
        print("Congrats...!!!\nAapka jawab bilkul sahi H")
        input()
      else:
        print("Checkin...plz wait...")
        time.sleep(2)
        print("SORRY..!! aapka javab galat hai.\n@@@GAME OVER@@@")
        break
  else:
    if k==solution_list[i]:
      print("Checkin...plz wait...")
      time.sleep(2)
      print("Congrats...!!!\nAapka jawab bilkul sahi H")
      input()
    else:
      print("Checkin...plz wait...")
      time.sleep(2)
      print("SORRY..!! aapka javab galat hai.\n@@@GAME OVER@@@")
      break
