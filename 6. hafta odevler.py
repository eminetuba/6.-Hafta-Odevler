import random
print("sayi tahmin oyunu")
tahmin=27  # bulmasini istedigim sayi

print("1-100 arasi bir sayi tahmin et\n\ntuttugun sayi buyukse -, kucukse +, dogruysa 'tammadir' yaz")
input("bir tusa basin")
sayi=random.randint(1,100)  # sayi 1 100 arasi en genis aralikta olacak
count=0  # tahmini saydiracagiz
eksi=[100]
arti=[1]
while True:
  count+=1 # tahmin sayiyisini arttir
  print(count,". tahminim: ",sayi)
  kontrol=input("Dogru mu:  ").lower()
  if kontrol=="-":
    eksi+=[sayi]
  if kontrol=='+':
    arti+=[sayi]
  if kontrol=="tamamdir":
    print("Tahmin ettigin sayi {} imis..{} tahminimde bildim..".format(sayi,count))
    break
  eksi.sort()
  arti.sort()
  sayi=random.randint(arti[-1],eksi[0])  #veya   sayi=random.randint(max(arti),min(eksi))
