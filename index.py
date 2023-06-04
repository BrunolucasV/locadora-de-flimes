flimes={
    "alien" : 10,
    "De volta para o futuro" : 10,
    "karate kid" : 10,
    "o senhor dos aneis" : 10,
    "top gun" : 10,
}
print (flimes)
escolha=input("escolha um flime da nossa lista: ")

def alugar (escolha) :
    if escolha in flimes.keys():
        x=flimes.get(escolha)
        x=x-1
        return flimes.update({escolha:x})
    else:
        print("Esse filme não existe ou não está disponível ")
alugar(escolha)
print(flimes)
