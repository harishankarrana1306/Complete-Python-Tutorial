code=input("Enter the Code language \n")
words=code.split(" ")
# print(words)   -->('harry','is','good')

coding = False  #if coding = False -- it will decode 
if(coding):
    nwords=[]
    for i in words:
        if(len(i)>=3):
          r1="srn"
          r2="sff"
          codenew= r1 + i[1:] + i[0] + r2
        #   print(codenew)
          nwords.append(codenew)
        else:
            nwords.append(i[::-1])  # reverse the string
    print(" ".join(nwords))


 # # for decoding 
 #  print(words)   -->('harry','is','good')

else:
    nwords=[]
    for i in words:
        if(len(i)>=3):
          r1="srn"
          r2="sff"
          codenew=i[3:-3]
          codenew=codenew[-1]+codenew[:-1]
        #   print(codenew)
          nwords.append(codenew)

        else:
            nwords.append(i[::-1])  # reverse the string
    print(" ".join(nwords))