# LIST
# menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)

# tuples
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])

# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)

# sets (himpunan)
# data_sets = {10,4,3,2,7,6,5}
# print(data_sets)
# print(data_sets[0])


# # Dictionary

# list → array, mengakses dengan menggunakan index
data = ['ucup','rendi','salsa']
print(data[0])

# dictionary (dict) → associative array
# identifier → key
data_dict = {
    'key' : 'value',
    'cp' : 'ucup',
    'rd' : 'rendi',
    'sl' : 'salsa',
    'nmbr' : 100,
    'listt' :data_list
}
print(data_dict['sl'])
print(data_dict['nmbr'])
print(data_dict['listt'])


## ----- Operasi Dictionary -----

data_ddict = {
    "din":"masdin",
    "dan":"masdan",
    "sep":"asep"

}

# panjang dictionary
LENDICT = len(data_ddict)
print(f"panjang dictionary: {LENDICT}")

# mengecek key exist atau tidak
KEY = "din"
CHECKKEY = KEY in data_ddict
print(f"apakah {KEY} ada di data_ddict : {CHECKKEY}")

# mengakses value  (read) dengan get
print(data_ddict["dan"])
print(data_ddict.get("sep"))
print(data_ddict.get("kis","key tidak ditemukan"))#check key dengan message

# mengupdate data
data_ddict["din"] = "din josjis"
print(data_ddict)
data_ddict['dan'] = "adeknya masdin"
print(data_ddict)

data_ddict.update ({"din":"masdin bolokuhhh"})
print(data_ddict)
data_ddict.update ({"dan":"mas dan omaligu"})
print(data_ddict)

# menghapus data
del data_ddict["sep"]
print(data_ddict)


## -------Looping Dictionary-------

teman_teman ={
    "din":"mas dinnn west",
    "dan":"adiknya mas dinnn",
    "lur":"dulurku",
    "lerr":"mazzlerr"
}

# looping fisrt try (yang keluar hanya key)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for values in teman_teman.values():
    print(values)


items = teman_teman.items()
print(items)

for key,values in teman_teman.items():
    print(f"key={key}, value = {values}")