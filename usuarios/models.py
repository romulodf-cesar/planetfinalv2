from django.db import models

# orientação a objetos
    # Paradigma  - Orientado a Objetos 
# O que é Classe

    # Modelo, 
    # Define as propriedades e comportamentos,
    # Nada
    # Pessoa chique
    # Depende

    # Um conjunto de objetos

# O que é objeto

    # Um objeto é a instância de uma classe

# O que é construtor
    # um método especial para construir o objeto  
     
# O que é método
    # método é uma função dentro da classe
    # funcionalidades


# O que é atributo
    # caracteristica do objeto 
    # nome, idadeMax
    # variável
    # atributo

"""
  class Reptil:
      def __init__():
         pass

"""
# crie uma classe Reptil

# cria atributos 
# cria construtor

# cria três objetos
"""
class Reptil:
    # Atributos
    def __init__(self, nome, especie, idade, tem_veneno):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.tem_veneno = tem_veneno
    
    # Método para exibir informações
    def exibir_info(self):
        veneno = "Sim" if self.tem_veneno else "Não"
        return f"Nome: {self.nome}, Espécie: {self.especie}, Idade: {self.idade} anos, Venenoso: {veneno}"

# Criando três objetos
reptil1 = Reptil("Slyther", "Cobra", 5, True)
reptil2 = Reptil("Godzilla", "Lagarto", 10, False)
reptil3 = Reptil("Tartuga", "Tartaruga", 25, False)

# Exibindo informações dos objetos
print(reptil1.exibir_info())
print(reptil2.exibir_info())
print(reptil3.exibir_info())

"""
