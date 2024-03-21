from collections import defaultdict

mi_dic = {'uno':'verde', 'dos': 'azul', 'tres':'amarillo'}

print(mi_dic['dos'])
# print(mi_dic['cuatro'])

dic = defaultdict(lambda: 'nada')
print(dic['cualquiera'])
print(dic['cuatro'])