#Problema de Laberinto
lab = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1]]

res = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

def imprime(mat):
    for f in mat:
        for c in f:
            print(f"{c},", end="")
        print()
    print()

def valida(fil, col) -> bool:
    if fil >= len(lab):
        return False
    if col >= len(lab[0]):
        return False
    if fil < 0:
        return False
    if col < 0:
        return False
    if lab[fil][col] == 0:
        return False
    if res[fil][col] == 1:
        return False
    return True

def labbas(lab, res, fil, col) -> bool:
    if fil == 8 and col == 8:  
        if valida(fil, col):
            res[fil][col] = 1
            imprime(res)
            return True
        else:
            return False
    else:
        if valida(fil, col):
            res[fil][col] = 1
            imprime(res)

            if labbas(lab, res, fil + 1, col):   
                return True
            elif labbas(lab, res, fil, col + 1):  
                return True
            elif labbas(lab, res, fil, col - 1): 
                return True
            elif labbas(lab, res, fil - 1, col): 
                return True
            else:
                res[fil][col] = 0
                return False
        else:
            return False

##########
if labbas(lab, res, 0, 0):
    print("Salio")
else:
    print("No hay salida")