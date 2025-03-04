yiyecek=["ekmek","zeytin","peynir","çikolata"]
elektronik=["buzdolabı","televizyon","bilgisayar"]

urun=input("Ürünün adını giriniz: ")
fiyat=int(input("Girdiğiniz ürünün fiyatını giriniz: "))
def kdv():
    if urun in yiyecek:
        kdvlifiyat=(fiyat*10)/100+fiyat
        print("Ürünün KDV'li fiyatı:",kdvlifiyat)
    elif urun in elektronik:
        kdvlifiyat2=(fiyat*20)/100+fiyat
        print("Ürünün KDV'li fiyatı:",kdvlifiyat2)
kdv()