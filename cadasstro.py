
#crie um programa para categorizara os produtos de uma revendedora de bebidas.
#cada produto tem um código.O tipo dde produto é dado pelas 3  primeiras letras do código.
#ex:
#vinho -> BEB12302 , CERVEAAJA->ABEB12043 ,VODKA->BEB34501 , GUARANÁ->BSA11104,COCA->BSA54301,SPRITE->BSA34012,ÁGUA->BSA09871
#repare que bebidas sem álcool começam BSA e bebidas com álcool com BEB
#crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais produtos devem se enviados para a área de bebdidas alcóolicas.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#percorrer toda a minha lista de produtos
#pra cada produto,verficar se ele é bebida alcoolica
#se for bebida alcoolica,exibir a mensagem Enviar...

'''def ehalcoolico(bebida,):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False'''
'''def naoalcoolico(bebida,):
    bebida = bebida.upper()
    if 'BSA' in bebida:
        return True
    else:
        return False'''
def ehdacategoria(bebida,cod_categoria):
    bebida = bebida.upper()
    if cod_categoria in bebida:
        return True
    else:
        return False
        

produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','BSA54301','BSA34012']

for produto in produtos:
    #if ehalcoolico(produto,):
        #print(f'Enviar {produto} para setor de bebidas alcoolicas')
    #elif  naoalcoolico(produto):
        #print(f'Enviar {produto} para setor de bebidas não alcoolicas')
    if ehdacategoria(produto,'BEB'):     
        print(f'Enviar {produto} para setor de bebidas alcoolicas')
    elif ehdacategoria(produto,'BSA'):
        print(f'Enviar {produto} para setor de bebidas não alcoolicas')
qtd_produtos = len(produtos)
print('Meus produtos são :', produtos ,'e a quantidade é de ', qtd_produtos ,sep='\n')