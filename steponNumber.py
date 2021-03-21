listItem = []
listItem2 = []
listItem4 = []
listItem5 = []
# LIST INI BERISIKAN DERET PERTAMA 0,1,4,5,8,9,12
for item in range (0,13,4):
    listItem.append(item)
# print(listItem)
for item2 in range(1,10,4):
    listItem2.append(item2)
# print(listItem2)
list3 = list(listItem + listItem2) #MENGGABUNGKAN DERET PERTAMA DENGAN DERET KEDUA
list3.sort()
set3 = set(list3) #MERUBAH DARI LIST MENJADI SET AGAR BISA DIINTERSECT
# print(set3) = UNTUK MEMBUKTIKAN

#LIST INI BERISIKAN DERET KEDUA 2,3,6,7,10,11
for item3 in range (2,11,4):
    listItem4.append(item3)
# print(listItem4)
for item4 in range (3,12,4):
    listItem5.append(item4)
# print(listItem5)
list4 = list(listItem4 + listItem5) #MENGGABUNGKAN DERET PERTAMA DENGAN DERET KEDUA
list4.sort()
set4 = set(list4) #MERUBAH DARI LIST MENJADI SET AGAR BISA DIINTERSECT
# print(set4) = UNTUK MEMBUKTIKAN

listSoal = [[4,2],
            [6,6],
            [3,4]]
penambahan = 0
listFinal = []
for i in listSoal:
    # print(i)
    for j in i:
        penambahan = penambahan+j
        if penambahan >= 5 and penambahan <= 20: #INI AGAR MUNCUL ANGKA 6,12,18
            penambahan
            # print(penambahan)
            listFinal.append(penambahan)
# print(listFinal) UNTUK MEMBUKTIKAN

setFinal = set(listFinal) #INI MEMBUAT 6,12,18 MENJADI SET AGAR BISA DIINTERSECT
intersect1 = setFinal.intersection(set3) # INI UNTUK INTERSECT DENGAN SET PERTAMA
intersect2 = setFinal.intersection(set4) # INI UNTUK INTERSECT DENGAN SET KEDUA
if intersect2 != False: # INI UNTUK MEMUNCULKAN APABILA TIDAK ADA ANGKA, MAKA PRINT 'NO NUMBER'
    NoNumber = ['No Number']
mantap1 = list(intersect1)+list(intersect2) # INI  UNTUK MENGGABUNGKAN YANG SUDAH DIINTERSECT
mantap1.sort() #INI UNTUK MENGURUTKAN YANG SUDAH DIINTERSECT
List_awal = mantap1 + NoNumber # INI UNTUK MENGGABUNGKAN DENGAN YANG TIDAK ADA DI SET

def steponNumber (x): # INI UNTUK FORMULANYA
    return List_awal
print(steponNumber(List_awal))