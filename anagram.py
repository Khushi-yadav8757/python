def angrams(str1,str2)
    if len[str1]!=len[str2]
        return False
        freq1 ={}
        freq2 ={}
   for char in str1:
     freq1[char]=freq1.get(char,0)+1
   for char in str2:
     fre2[char]=freq2.get(char,0)+1
  return freq1==freq2
print(argrams("listen","silent"))
