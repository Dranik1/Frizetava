import itertools
import datetime as dt
import json



            

class Dalibnieks:
    Dalibnieka_vards=""
    Dalibnieka_uzvards=""
    Dalibnieka_dzimums=""
    Dalibnieka_vecums=""
    Dalibnieka_svars=0
    Dalibnieka_josta=""
    Dalibnieka_pk=""

    id_iter_dalibnieks=itertools.count()

    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        self.Dalibnieka_vards=vards
        self.Dalibnieka_uzvards=uzvards
        self.Dalibnieka_dzimums=dzimums
        self.Dalibnieka_vecums=vecums
        self.Dalibnieka_svars=svars
        self.Dalibnieka_josta=josta
        self.Dalibnieka_pk=pk
        self.Dalibnieka_id=next(self.id_iter_dalibnieks)+1

    def dalibnieka_info(self):
        return[
            self.Dalibnieka_vards, self.Dalibnieka_uzvards, self.Dalibnieka_dzimums, self.Dalibnieka_vecums, self.Dalibnieka_svars, self.Dalibnieka_josta, self.Dalibnieka_pk
        ]

    

class Kumite(Dalibnieks):
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
    kategorijas_vir=[61, 68, 76, 85, 300]
    kategorijas_vir_name=["-60 kg", "61-67 kg", "68-75 kg", "76-84 kg", "85+ kg"]
    kategorijas_siev=[51, 56, 62, 69, 300]
    kategorijas_siev_name=["-50 kg", "51-55 kg", "56-61 kg", "62-68 kg", "69+ kg"]
    def svara_kategorija(self):
        self.Dalibnieka_svara_kategorija=""
        if self.Dalibnieka_dzimums[0]=="s":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_siev[0]):
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_siev[a], self.kategorijas_siev[b]):
                    c+=1
                    print(self.kategorijas_siev_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_siev_name[c-1]
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        elif self.Dalibnieka_dzimums[0]=="v":
            stop=False
            a=0
            b=1
            c=1
            while stop!=True:
                if self.Dalibnieka_svars in range(1, self.kategorijas_vir[0]):
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    stop=True
                elif self.Dalibnieka_svars in range(self.kategorijas_vir[a], self.kategorijas_vir[b]):
                    c+=1
                    print(self.kategorijas_vir_name[c-1])
                    self.Dalibnieka_svara_kategorija=self.kategorijas_vir_name[c-1]
                    stop=True
                else:
                    a=a+1
                    b=b+1
                    c+=1
        else:
            print("Who are you?")


    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        dalibnieka_data={
            "name":self.Dalibnieka_vards,
            "surname":self.Dalibnieka_uzvards,
            "gender":self.gender,
            "age":self.Dalibnieka_vecums,
            "weight":self.Dalibnieka_svars,
            "belt":self.Dalibnieka_josta,
            "personal code":self.Dalibnieka_pk,
            "weight cathegory":self.Dalibnieka_svara_kategorija,
            "id":self.Dalibnieka_id
        }

        with open("dalibnieki.json", mode="w", encoding="utf-8") as write_file:
            json.dump(dalibnieka_data, write_file)


class Kata(Dalibnieks):
    def __init__(self, vards, uzvards, dzimums, vecums, svars, josta, pk):
        super().__init__(vards, uzvards, dzimums, vecums, svars, josta, pk)
        self.Dalibnieka_kata=""
    
    def kata(self):
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
}]         }
        print(kataJson)
        
        
        stop=False
        while stop!=True:
            kata_num=input("Kata id: ")
            for i in kataJson["kata"]:
                if i[kata_num]:
                    agree=input(f'Is {i[kata_num]} your kata? Please answer True or False.')
                    if agree=="True":
                        print("You can be registrated")
                        self.Dalibnieka_kata=i[kata_num]
                        stop=True
                    else:
                        print("Try again")
        
    def registration(self):
        if self.Dalibnieka_dzimums[0]=="v":
            self.gender="virietis"
        elif self.Dalibnieka_dzimums[0]=="s":
            self.gender="sieviete"
        else:
            self.gender=None
        dalibnieka_data={
            "name":self.Dalibnieka_vards,
            "surname":self.Dalibnieka_uzvards,
            "gender":self.gender,
            "age":self.Dalibnieka_vecums,
            "weight":self.Dalibnieka_svars,
            "belt":self.Dalibnieka_josta,
            "personal code":self.Dalibnieka_pk,
            "kata":self.Dalibnieka_kata,
            "id":self.Dalibnieka_id
        }
        dalibnieka_str=json.dumps(dalibnieka_data)
        with open("dalibnieki.json", mode="w", encoding="utf-8") as write_file:
            write_file.write(dalibnieka_str)


        
        

           
           
           




''''-dal1=Dalibnieks("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.dalibnieka_info()
dal1=Kumite("anna", "h", "sieviete", 17, 45, "3 Kyu", "123456-78900")
dal1.svara_kategorija()
dal1.registration()'''

dal2=Dalibnieks("viktor", "h", "v", 17, 199, "3 Kyu", "123456-78900")
dal2.dalibnieka_info()
dal2=Kata("viktor", "h", "v", 17, 199, "3 Kyu", "123456-78900")
dal2.kata()
dal2.registration()



