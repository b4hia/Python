class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)
        else:
            # Ignora valores duplicados
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, no_atual):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivo(valor, no_atual.esquerda)
        else:
            return self._buscar_recursivo(valor, no_atual.direita)

# Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print(arvore.buscar(50))  # Saída: True
print(arvore.buscar(90))  # Saída: False
