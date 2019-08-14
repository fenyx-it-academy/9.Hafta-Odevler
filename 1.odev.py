tek=list(filter(lambda x:x%2==1, range(1,11)))
cift=list(filter(lambda x:x%2==0, range(1,11)))
ucunkati=list(filter(lambda x:x%3==0, range(1,11)))
besinkati=list(filter(lambda x:x%5==0, range(1,11)))

def dogrulama(ilksayi,sonsayi):
    for i in range(ilksayi,sonsayi):
        if i in tek:
            print("{} sayisi bir tek sayidir".format(i))
        if i in cift:
            print("{} sayisi bir cift sayidir".format(i))
        if i in ucunkati:
            print("{} sayisi 3 sayisinin katidir".format(i))
        if i in besinkati:
            print("{} sayisi 5 sayisinin katidir".format(i))
    quit()

print(dogrulama(1,11))