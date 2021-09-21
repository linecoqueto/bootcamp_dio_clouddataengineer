##-------------------------------------------------------------##
## GERE, COPIE, MOVE, ESCREVA E LEIA INFORMAÇÕES DE ARQ EXTERNOS
##-------------------------------------------------------------##

#open :: criar ou abrir um arquivo
#write (w) :: escrever um arquivo novo, substitui linhas se existir no arquivo
#close :: fechar o arquivo
#(a) :: atualizar um arquivo, não substitui linhas se existir

#arquivo = open('teste.txt','w')
#arquivo.write('minha primeira escrita')
# arquivo = open('teste.txt','a')
# arquivo.write('\nSegunda escrita')
# arquivo.close()

import shutil ##biblioteca para copiar ou mover arquivos

def escrever_arquivo(texto):
    #diretorio = 'C:/aline'
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste.txt','a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for a x in aluno:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(lista_notas)

############ copia arquivo
def copia_arquivo (nome_arquivo):
    shutil.copy(nome_arquivo,'C:/aline/treinamento/notas_alunos.txt')

############ move arquivo
def move_arquivo (nome_arquivo):
    shutil.move(nome_arquivo,'C:/aline/treinamento/notas_alunos.txt')

############
if __name__ == '__main__':
    copia_arquivo('notas.txt')
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #escrever_arquivo('Primeira Linha.\n')
    #atualizar_arquivo('segunda linha.\n')
    #ler_arquivo('teste.txt')

