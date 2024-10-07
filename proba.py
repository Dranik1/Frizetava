import json
'''Dalibnieka_dzimums="s"
Dalibnieka_svars=68


kategorijas_siev=[51, 56, 62, 69, 300]
kategorijas_siev_name=["-50 kg", "51-55 kg", "56-61 kg", "62-68 kg", "69+ kg"]
if Dalibnieka_dzimums[0]=="s":
    for i in range(6):
        a=0
        if Dalibnieka_svars in range(1, kategorijas_siev[i]):
            print(a)
            break
        elif Dalibnieka_svars in range(kategorijas_siev[i], kategorijas_siev[i+1]):
            print(a)
if Dalibnieka_svars in range(1, 51):
    print(Dalibnieka_dzimums)
stop=False
a=0
b=1
c=1
while stop!=True:
    if Dalibnieka_svars in range(1, kategorijas_siev[0]):
        print(kategorijas_siev_name[c-1])
        stop=True
    elif Dalibnieka_svars in range(kategorijas_siev[a], kategorijas_siev[b]):
        c+=1
        print(kategorijas_siev_name[c-1])
        stop=True
    else:
        a=a+1
        b=b+1
        c+=1





kataJson={ 'kata': [{
    "1": "Anan",
    "2": "Anan Dai",
    "3": "Annanko",
    "4": "Aoyagi",
    "5": "Bassai",
    "6": "Bassai Dai",
    "7": "Bassai Sho",
    "8": "Chatanyara Kusanku",
    "9": "Chibana No Kushanku",
    "10": "Chinte",
    "11": "Chinto",
    "12": "Enpi",
    "13": "Fukyugata Ichi",
    "14": "Fukyugata Ni",
    "15": "Gankaku",
    "16": "Garyu",
    "17": "Gekisai (Geksai) 1",
    "18": "Gekisai (Geksai) 2",
    "19": "Gojushiho",
    "20": "Gojushiho Dai",
    "21": "Gojushiho Sho",
    "22": "Hakusho",
    "23": "Hangetsu",
    "24": "Haufa (Haffa)",
    "25": "Heian Shodan",
    "26": "Heian Nidan",
    "27": "Heian Sandan",
    "28": "Heian Yondan",
    "29": "Heian Godan",
    "30": "Heiku",
    "31": "Ishimine Bassai",
    "32": "Itosu Rohai Shodan",
    "33": "Itosu Rohai Nidan",
    "34": "Itosu Rohai Sandan",
    "35": "Jiin",
    "36": "Jion",
    "37": "Jitte",
    "38": "Juroku",
    "39": "Kanchin",
    "40": "Kanku Dai",
    "41": "Kanku Sho",
    "42": "Kanshu",
    "43": "Kishimono No Kushanku",
    "44": "Kousoukun",
    "45": "Kousoukun Dai",
    "46": "Kousoukun Sho",
    "47": "Kururunfa",
    "48": "Kusanku",
    "49": "Kyan No Chinto",
    "50": "Kyan No Wanshu",
    "51": "Matsukaze",
    "52": "Matsumura Bassai",
    "53": "Matsumura Rohai",
    "54": "Meikyo",
    "55": "Myojo",
    "56": "Naifanchin Shodan",
    "57": "Naifanchin Nidan",
    "58": "Naifanchin Sandan",
    "59": "Naihanchi",
    "60": "Nijushiho",
    "61": "Nipaipo",
    "62": "Niseishi",
    "63": "Ohan",
    "64": "Ohan Dai",
    "65": "Oyadomari No Passai",
    "66": "Pachu",
    "67": "Paiku",
    "68": "Papuren",
    "69": "Passai",
    "70": "Pinan Shodan",
    "71": "Pinan Nidan",
    "72": "Pinan Sandan",
    "73": "Pinan Yondan",
    "74": "Pinan Godan",
    "75": "Rohai",
    "76": "Saifa",
    "77": "Sanchin",
    "78": "Sansai",
    "79": "Sanseiru",
    "80": "Sanseru",
    "81": "Seichin",
    "82": "Seienchin (Seiyunchin)",
    "83": "Seipai",
    "84": "Seiryu",
    "85": "Seishan",
    "86": "Seisan (Sesan)",
    "87": "Shiho Kousoukun",
    "88": "Shinpa",
    "89": "Shinsei",
    "90": "Shisochin",
    "91": "Sochin",
    "92": "Suparinpei",
    "93": "Tekki Shodan",
    "94": "Tekki Nidan",
    "95": "Tekki Sandan",
    "96": "Tensho",
    "97": "Tomari Bassai",
    "98": "Unshu",
    "99": "Unsu",
    "100": "Useishi",
    "101": "Wankan",
    "102": "Wanshu"
}]         }'''
#kata_n=json.loads(kataJson)
#print(kataJson)

'''stop_kata=False
while stop_kata!=True:
    kata_name=int(input("Kata number: "))
    agree=input(f"Is your kata {kataJson["kata_name"]}? Please ansewer True or False.")
    if agree==True:
        print("Your kata is registrated")
        stop_kata=True
    else:
        print("Try another")
    
kata_num=input()
for i in kataJson["kata"]:
    if i[kata_num]:
        print(i[kata_num])'''





Dalibnieka_dzimums='v'
Dalibnieka_vards='d'
Dalibnieka_uzvards='c'
Dalibnieka_vecums=1
Dalibnieka_svars=5
Dalibnieka_josta=0
Dalibnieka_pk=9
Dalibnieka_kata='Anan'
Dalibnieka_id=1
def registration():
        if Dalibnieka_dzimums[0]=="v":
            gender="virietis"
        elif Dalibnieka_dzimums[0]=="s":
            gender="sieviete"
        else:
            gender=None
        dalibnieka_data={
            "name":Dalibnieka_vards,
            "surname":Dalibnieka_uzvards,
            "gender":gender,
            "age":Dalibnieka_vecums,
            "weight":Dalibnieka_svars,
            "belt":Dalibnieka_josta,
            "personal code":Dalibnieka_pk,
            "kata":Dalibnieka_kata,
            "id":Dalibnieka_id
        }

        #with open("dalibnieks.json", mode="a") as jsonfile:
             #json.dump(dalibnieka_data, jsonfile)

        with open('dalibnieks.json') as f:
             data=json.load(f)
            
        data.append(dalibnieka_data)

        with open('dalibnieks.json', 'w') as f:
             json.dump(data, f, indent=2)

        
registration()