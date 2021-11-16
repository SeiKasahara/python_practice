pokemon_go_data = {'bentspoon':
                  {'Rattata': 203, 'Pidgey': 120, 'Drowzee': 89, 'Squirtle': 35, 'Pikachu': 3, 'Eevee': 34, 'Magikarp': 300, 'Paras': 38},
                  'Laurne':
                  {'Pidgey': 169, 'Rattata': 245, 'Squirtle': 9, 'Caterpie': 38, 'Weedle': 97, 'Pikachu': 6, 'Nidoran': 44, 'Clefairy': 15, 'Zubat': 79, 'Dratini': 4},
                  'picklejarlid':
                  {'Rattata': 32, 'Drowzee': 15, 'Nidoran': 4, 'Bulbasaur': 3, 'Pidgey': 56, 'Weedle': 21, 'Oddish': 18, 'Magmar': 6, 'Spearow': 14},
                  'professoroak':
                  {'Charmander': 11, 'Ponyta': 9, 'Rattata': 107, 'Belsprout': 29, 'Seel': 19, 'Pidgey': 93, 'Shellder': 43, 'Drowzee': 245, 'Tauros': 18, 'Lapras': 18}}
def get_dict_value(dic,new_dic = {}):
    for key in dic.keys():
        data = dic[key]
        if isinstance(data, dict):
            get_dict_value(data,new_dic=new_dic)
        if isinstance(data, dict) != True:
            if key not in new_dic:
                new_dic[key] = dic[key]
            else:
                new_dic[key] += dic[key]
    return new_dic
d = get_dict_value(pokemon_go_data)
most_common_pokemon = sorted(d,key = lambda k:d[k],reverse =True)[0]
print(most_common_pokemon)