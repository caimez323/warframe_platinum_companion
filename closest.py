
import difflib, requests

warfarme_database = [] #load from json


def create_database(lang):
    tab = []
    for part in [warframe_parts, warframe_name, weapons_name,weapons_parts]:
        if type(part) == dict:
            part = part[lang]
        for word in part:
            tab.append(word)
    return tab

def load_database():
    pass

def get_closest_wrf(word):

    warfarme_database = create_database("fr")
    r = (difflib.get_close_matches(word,warfarme_database))
    print(r)
    return r

#POUR VOIR S ILS SONT VAULTE, REGARDER L API SNKEW
#Plein d'autres infos dedans
#penser à save and load les datas, on les chargera une fois au début et quand l'utilisateur fera une maj


warframe_r = requests.get("https://wf.snekw.com/warframes-wiki")
weapons_r = requests.get("https://wf.snekw.com/weapons-wiki")

warframes_list = warframe_r.json()["data"]["Warframes"]
weapons_list = weapons_r.json()["data"]

warframe_parts =    {"fr":\
                    ["Neuroptics","Châssis","Systèmes"],\
                    "en":\
                    ["Neuroptics","Chassis","Systems"]}

weapons_parts = {"fr":\
                ["Cannon","Culasse","Crosse","Lame","Poignée"],\
                "en":\
                ["Barrel","Receiver","Stock","Blade","Handle"]}

warframe_name_exclusion = ["Sevagoth's shadow","Stalker"]
warframe_name = [name for name in warframes_list if name not in warframe_name_exclusion]

weapons_name = [name for name in weapons_list if "Prime" in name]

#print(warframe_name)
#print(weapons_name)

warfarme_database = create_database("fr")

