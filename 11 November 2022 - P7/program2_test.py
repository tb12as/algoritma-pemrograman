#Menghitung luas bangun ruang
pilih = "y"
while pilih != "n":
    print("Menghitung Luas Bangun Ruang")
    print("Pilih Program Bangun Ruang""\n" "1. Volume dan luas permukaan kubus ""\n" "2. Volume dan luas permukaan limas segiempat""\n" "3. Volume dan luas permukaan balok""\n" "4. Volume, luas permukaan dan luas selimut kerucut""\n" "5. Volume dan luas permukaan bola""\n" "6. Volume,luas permukaan dan luas selimut tabung""\n" "7. Luas & Keliling Segitiga""\n" "8. Program Lingkaran")
    p = int(input())
    if p == 1:
        print("Program Menghitung Volume dan Luas Permukaan Kubus")
        s=float(input("Masukkan nilai sisi kubus :"))
        volume=s*s*s
        lp=6*s*s
        print("Diketahui")
        print("Sisi :",s,"cm")
        print("Maka Volume dan Luas Permukaan Kubus adalah :")
        print("Volume           :",volume,"cm")
        print("Luas Permukaan   :",lp,"cm")
    else:
        if p == 2:
            import math
            print("Program Menghitung Volume dan Luas Permukaan Limas Segi Empat")
            s=float(input("Masukkan nilai sisi alas     : "))
            t=float(input("Masukkan nilai tinggi limas  : "))
            la=s*s #luas alas
            lsg=0.5*s*(math.sqrt((t**2)+(0.5*s))) #luas segitiga
            lp=la+(4*lsg) #luas permukaan limas segi empat
            volume=(la*t)/3
            print("Diketahui")
            print("Sisi Alas    :",s,"cm")
            print("Tinggi Limas :",t,"cm")
            print("Maka Volume dan Luas Permukaan Limas Segi Empat adalah :")
            print("Volume           :",round(volume,2),"cm")
            print("Luas Permukaan   :",round(lp,2),"cm")
        else:
            if p == 3:
                print("Program Menghitung Volume dan Luas Permukaan Balok")
                p=float(input("Masukkan nilai panjang   :"))
                l=float(input("Masukkan nilai lebar     :"))
                t=float(input("Masukkan nilai tinggi    :"))
                lp=2*((p*l)+(l*t)+(p*t))
                volume=p*l*t
                print("Diketahui")
                print("Panjang  :",p,"cm")
                print("Lebar    :",l,"cm")
                print("Tinggi   :",t,"cm")
                print("Maka Volume dan Luas Permukaan Balok adalah :")
                print("Volume           :",volume,"cm")
                print("Luas Permukaan   :",lp,"cm")
            else:
                if p == 4:
                    import math
                    print("Program Menghitung Volume dan Luas Permukaan dan Luas Selimut Kerucut")
                    r=float(input("Masukkan nilai jari jari         : "))
                    t=float(input("Masukkan nilai tinggi            : "))
                    s=float(input("Masukkan nilai  garis pelukis    : "))
                    if r%7==0:
                        la=(22/7)*r*r #luas alas
                        ls=(22/7)*r*s #luas selimut
                        lp=la+ls #luas permukaan kerucut
                        volume=((22/7)*r*r*t)/3
                    else:
                        la=3.14*r*r #luas alas 
                        ls=3.14*r*s #luas selimut
                        lp=la+ls #luas permukaan kerucut
                        volume=(3.14*r*r*t)/3
                    print("Diketahui")
                    print("Jari-jari        :",r,"cm")
                    print("Tinggi           :",t,"cm")
                    print("Maka Volume dan Luas Permukaan Tabung adalah")
                    print("Volume               :",round(volume,2),"cm")
                    print("Luas Selimut Kerucut :",round(ls,2),"cm") 
                    print("Luas Permukaan       :",round(lp,2),"cm")
                else:
                    if p == 5:
                        print("Program Menghitung Volume dan Luas Permukaan Bola")
                        r=float(input("Masukkan nilai jari jari : "))
                        if r%7==0:
                            lp=4*(22/7)*r*r
                            volume=(4*((22/7)*r*r*r))/3
                        else:
                            lp=4*3.14*r*r
                            volume=(4*(3.14*r*r*r))/3
                        print("Diketahui")
                        print("Jari-jari        :",r,"cm")
                        print("Maka Volume dan Luas Permukaan Bola adalah")
                        print("Volume           :",round(volume,2),"cm")
                        print("Luas Permukaan   :",round(lp,2),"cm")
                    else:
                        if p == 6:
                            print("Program Menghitung Volume dan Luas Tabung")
                            r=float(input("Masukkan nilai jari jari : "))
                            t=float(input("Masukkan nilai tinggi    : "))
                            if r%7==0:
                                lp=2*(22/7)r(r+t)
                                volume=(22/7)*r*r*t
                            else:
                                lp=2*3.14*r*(r+t)
                                volume=3.14*r*r*t
                            print("Diketahui")
                            print("Jari-jari        :",r,"cm")
                            print("Tinggi           :",t,"cm")
                            print("Maka Volume dan Luas Permukaan Tabung adalah")
                            print("Volume           :",round(volume,2),"cm")
                            print("Luas Permukaan   :",round(lp,2),"cm")
    print("Apakah anda ingin menghitung bangun datar yang lainnya?(y/n)")
    pilih = input()