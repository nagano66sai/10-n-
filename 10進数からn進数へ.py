#基数変換　　10進数-------->n進数へ
print("変換したい10進数を入力してください")
x=int(input())　　#変換したい10進数を入力
for  n  in    range(2,10): #2進数から9進数までに直す
        amari=[]
  
  
        target=x
    
        while  target!=0:
            amari.append(target%n) #あまり
            target=target//n#商
        amari.reverse()
        e=len(amari)#リストamariの長さ
        s=""
        for  i  in  range(0,e): #リスト形式を普通の数字に直す
              s=s+str(amari[i])


    
       
        print(f"{x}は{n}進数では{s}です.")
