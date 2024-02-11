str = input("Enter the Message: ")
nstr = str.split()
coding = input("For coding 1 and for Decoding 0: ")
coding = True if (coding == "1") else False
if (coding):
    nwords = []
    for word in nstr:
      if(len(word)>=3):
        r1 = "dsf"
        r2 = "zvq"
        strnew = r1 + word[1:] + word[0] + r2
        nwords.append(strnew)
    #print(" ".join(nwords))
      else:
         #if(len(word)<3):
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
   nwords = []
   for word in nstr:
      if(len(word)>=3):
         stnew = word[3:-3]
         stnew = stnew[-1] + stnew[:-1]
         nwords.append(stnew)
      else:
         nwords.append(word[::-1])
   print(" ".join(nwords))