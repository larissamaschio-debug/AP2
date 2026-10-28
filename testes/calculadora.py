def soma(n1, n2):
    result = n1 + n2
    return result

def sub(n1,n2):
    result = n1 - n2
    return result 

def votacao(idade):

    if idade >= 16:
        return True
    else:
        return False

def calc_soma(opcao, n1, n2):
    match opcao: 
        case 1:
            soma(n1,n1)
        case 2:
            return sub(n1,n2)
                