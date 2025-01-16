# Desafio: Gerenciador de Estudantes
# Crie uma classe chamada Student para gerenciar informações de estudantes. Essa classe deverá armazenar o nome, idade, notas e outras informações básicas do estudante. Além disso, implemente alguns métodos para manipular esses dados.

# Requisitos:
# A classe deve ter os seguintes atributos:

# name (nome do estudante)
# age (idade do estudante)
# grades (uma lista de notas do estudante)
# A classe deve ter os seguintes métodos:

# add_grade(grade): Adicione uma nota à lista de notas.
# average_grade(): Retorne a média das notas.
# info(): Retorne uma string com as informações do estudante no formato:

# Nome: <name>, Idade: <age>, Média: <average_grade>

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 10:
            self.grades.append(grade)
        else:
            print('Nota inválida! Insira uma nota entre 0 e 10.')
    
    def average_grade(self):
        if self.grades == True:
            return sum(self.grades)/len(self.grades)
        else:
            return 0
    def info(self):
        return f'Nome: {self.name}, Idade: {self.age}, Média: {self.average_grade():.2f}'
        
def main():
    student1 = Student('Ana', 30)
    student2 = Student('Pedro', 34)

    student1.add_grade(10)
    student1.add_grade(8.45)

    print(student1.info())

if __name__ == '__main__':
    main()
