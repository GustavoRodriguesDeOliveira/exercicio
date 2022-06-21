import this

import ExerciciosModel

this.opcao = -1

def Menu():
    print('Menu\n\n'
          '\n1. Exercicio 01'
          '\n2. exercicio 02'
          '\n3. Exercicio 03'
          '\n4. Exercicio 04'
          '\n5. Exercicio 05'
          '\n6. Exercicio 06'
          '\n7. exercicio 07'
          '\n8. Exercicio 08'
          '\n9. Exercicio 09'
          '\n10. Exercicio 10'
          '\n11. Exercicio 11'
          '\n12. Exercicio 12'
          '\n13. Exercicio 13'
          '\n14. Exercicio 14'
          '\n15. Exercicio 15'
          '\n16. Exercicio 16'
          '\n17. Exercicio 17'
          '\n18. Exercicio 18'
          '\n19. Exercicio 19'
          '\n0. Sair'
          '\nEscolha uma das opçôes acima: ')
    this.opcao = int(input())

def Executar():
    while(this.opcao != 0):
        Menu()
        if this.opcao == 0:
            print('Obrigado')
        elif this.opcao == 1:
            print(ExerciciosModel.exercicio01())
        elif this.opcao == 2:
            print(ExerciciosModel.exercicio02())
        elif this.opcao == 3:
            print(ExerciciosModel.exercicio03())
        elif this.opcao == 4:
            print(ExerciciosModel.exercicio04())
        elif this.opcao == 5:
            print(ExerciciosModel.exercicio05())
        elif this.opcao == 6:
            print(ExerciciosModel.exercicio06())
        elif this.opcao == 7:
            print(ExerciciosModel.exercicio07())
        elif this.opcao == 8:
            print(ExerciciosModel.exercicio08())
        elif this.opcao == 9:
            print(ExerciciosModel.exercicio09())
        elif this.opcao == 10:
            print(ExerciciosModel.exercicio10())
        elif this.opcao == 11:
            print(ExerciciosModel.exercicio11())
        elif this.opcao == 12:
            print(ExerciciosModel.exercicio12())
        elif this.opcao == 13:
            print(ExerciciosModel.exercicio13())
        elif this.opcao == 14:
            print(ExerciciosModel.exercicio14())
        elif this.opcao == 15:
            print(ExerciciosModel.exercicio15())
        elif this.opcao == 16:
            print(ExerciciosModel.exercicio16())
        elif this.opcao == 17:
            print(ExerciciosModel.exercicio17())
        elif this.opcao == 18:
            print(ExerciciosModel.exercicio18())
        elif this.opcao == 19:
            print(ExerciciosModel.exercicio19())
        else:
            print('Opção informada não é válida!')
