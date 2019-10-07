# Thuane França - Projeto 2 SO
# uso paginacao.py 


# Algorítimo FIFO 


def FIFO(n, paginas): #primeiro a entrar é o primeiro a sair
  quadros = [None for _ in range(n)] 
  posicao,falta = 0,0
  for i in range(len(paginas)):
    if paginas[i] not in quadros: 
      quadros[posicao % n] = paginas[i] # lista circular
      posicao += 1; falta += 1 

  print(f"FIFO {falta}")

# Algoritimo Otimo

def OTM(n, paginas): #prevê as páginas futuras e faz a melhor troca
  quadros = []
  posicao, falta = 0, 0 

  for i in paginas:  
    if i in quadros:
      posicao += 1 

    elif i not in quadros:
      if len(quadros) < n:
      
        quadros.append(i)
        falta += 1
        posicao += 1
    
      elif len(quadros) == n:
        #calcular pagina a remover
        futuro = paginas[posicao:] #paginas futuras
        ind = []  
        atual = quadros.copy() # estado atual
        for x in atual:  
            try: ind.append(futuro.index(x))
            except: ind.append(100000)
        remover = ind.index(max(ind))

        quadros.pop(remover)
        quadros.append(i)  
        falta += 1  
        posicao += 1  


  print(f"OTM {falta}") 



# Algorítimo LRU (Ultimo Usado no Final)

def LRU(n, paginas): #tira o mais antigo sem ser usado
  quadros = []
  falta = 0 

  for x in paginas:
    if x in quadros: 
      quadros.remove(x); quadros.append(x)
    elif x not in quadros:
      if len(quadros) < n: 
        quadros.append(x) 
        falta += 1
      elif len(quadros) == n: 
        quadros.append(x); quadros.pop(0)
        falta +=1
    
  print(f"LRU {falta}") 



if __name__ == '__main__':
  with open('teste.txt') as val: 
    val = [int(x.rstrip()) for x in val.readlines()]
    n = val.pop(0)
    paginas = val.copy()


  FIFO(n, paginas)
  OTM(n, paginas)
  LRU(n, paginas)  
