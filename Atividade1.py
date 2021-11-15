#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 07:35:22 2020

@author: Carlos Pinto da Silva Neto
"""
import pandas as pd 
import numpy as np 


##############################################################################

'''
Complete a tabela abaixo com um conjunto de 12 números entre 1 e 50.
Utilizando os dados criados por você, calcular:

Regras
•	Pelo menos um valor deve estar repetido.
•	O conjunto de dados deve apresentar, pelo menos, 6 valores únicos.
•	NÃO É PERMITIDO escolher todos os números iguais.
•	Trabalho Individual
•	Entrega até 10/04/2020 às 23:59h.
Trabalhos com os mesmos dados serão considerados inválidos


           5	,  8, 10, 5, 23, 50, 7,	6, 20, 12, 13, 15

            •	Média = 14.5
            •	Moda = 5
            •	Mediana = 11
            •	Variância amostral = 158.4545
            •	Desvio padrão amostral = 12.5879
            •	Coeficiente de variação = 0.8681
            


'''


##############################################################################
'''
A) Escreva um código para ler um arquivo .txt, onde cada linha possui os 12 números escolhidos por um aluno.
Esse código deve verificar as regras estabelecidas e retornar todas as medidas de posição e variação solicitadas, com precisão de 4 casas decimais.


    O exercicio foi resolvido pela criação de uma classe que leva o nome do exercio.  
    Como nenhum modelo de arquivo .txt foi passado, assumi que seria um txt separado por vírgula
    sem cabeçalho. 

    
    arquivo txt: numeros.txt (primeira linha representa os valores escolhidos para a tarefa anterior)

    
    Os resultados são exportados para um aquivo excel chamado Answers_A.slsx

''' 


class ExercicioA(): 
    '''
    Read txt file which each line has 12 numbers 
    separated by comma. The file should not have any column name
    
    ex: 1,2,3,4,5,6,7,8,9,10,11,12
    `   2,4,6,8,10,12,14,16,18,20,22,24
        1,3,5,7,9,11,13,15,17,19,21,23
    
    Checks for every line if numbers are complient with rules: 
        
        1 - At least one number has to be repited
        2 - Has at least 6 unique numbers


    '''
    
    def __init__(self,txtfile):
        
        "txttile - file .txt to be read"
        
        self.file = txtfile
        
        #Call functions
        
        self.read_open()
        
        #Dictionary that will store the position measures
        self.answers = { 'Mean':[],
                         'Median':[],
                         'Mode':[],
                         'Variance':[],
                         'Standard dev':[],
                         'Variation Coef':[]}
        
        
        
        #Checks the validity of each row and already computes the positions measures - avoid going into other loop
        self.checks_validity()

        #Change from a dictionary to a dataframe with rounded values
        self.answers = pd.DataFrame(self.answers).round(4) # change from dictionary to dataframe with 4 digitis
        
    def read_open(self):
        
        ' Read .txt file and store as a dataframe'
        
        self.df = pd.read_csv(self.file, header=None,  index_col=False)
        
        
    def checks_validity(self):
        '''Checks the validity of the numbers folowing the rules: 
            1 - Each line has to have exactly 12 numbers
            2 - At least one number has to be repited
            3 - Has at least 6 unique numbers
        '''
        nrow, ncolumns = self.df.shape     # get the number of rows and columns
        
        
        for x in range(0, nrow):
            listofnumbers = self.df.iloc[x,:].dropna()   # get the whole row droping any missing value
            
            n_numbers = len(listofnumbers)      # get the size of the row
            n_uniques = len(listofnumbers.unique())  # get the number of uniques
            
            maximum = listofnumbers.max()
            minimo = listofnumbers.min()
            
            # checks if row contains 12 numbers
            if n_numbers < 12: 
                valid = False
                
                print( "row number %s on the txt file has less then 12 values. Check input" % str(x+1) )  # rows count starts on 1
                break
            
            # checks number of uniques
            elif (n_uniques < 6) or (n_uniques == 12):    # at least 6 uniques, at least 1 repeting number
                valid = False
                print("row number %s has none or too many repeting numbers. Check input" % str(x+1) )
                break
            
            # Checks if numbers are all under 50
            elif maximum > 50 or minimo <1 :
                print("row number %s has a value greater then 50 or lower than 1. Check input" % str(x+1) )
                valid = False
                
            #If all conditions are met then calculate the position measures 
            else:
                valid = True 
                self.medidas_de_pos(listofnumbers)
        
        return valid


    def medidas_de_pos(self,row):
        '''
        Function that will compute the position measures of each row. 
        '''
        
        mean = row.mean()
        median = row.median()
        mode = list(row.mode())
        variance = row.var() # ( N-1 )
        std = row.std() #  ( N-1 )
        cv = row.std()/row.mean()
        

        self.answers['Mean'].append(mean)
        self.answers['Median'].append(median)
        self.answers['Mode'].append(mode)
        self.answers['Variance'].append(variance)
        self.answers['Standard dev'].append(std)
        self.answers['Variation Coef'].append(cv)               
 

       
Result = ExercicioA(txtfile = 'numeros.txt')
Result.answers.to_excel('Answers_A.xlsx')

#%%
##############################################################################
'''

B) Escreva um código para gerar aleatoriamente valores para 50 alunos, 
com distribuição uniforme, de modo a respeitar as regras do trabalho.
   
   - Resolvido atraves da criação de uma classe chamada ExercicioB
   A classe cria os numeros para 50 alunos e exporta para um .txt
   chamado ValuesFor50Students.txt
   
   
   Na parte inferior, realizo a atividade A (código a cima)
   utilizando os valores gerados pelo ExercicioB - Valores são exportados 
   para um excel chamado Answers-50-studants.xlsx.
'''


from random import randint
import numpy as np 

class ExercicioB():
    '''
    Generate numbers randomly in a normal distribution for 50 cases. 
    Each case contains 12 numbers where: 
            1 - Each case has exaclty 12 numbers
            2 - At least one number has to be repited
            3 - Has at least 6 unique numbers
            
            
    parameters
    ----------
    mu : Mean (“centre”) of the distribution
    sigma: Standard deviation (spread or “width”) of the distribution
    
    '''
    
    def __init__(self, output_txt):
        
        self.Output = output_txt
                
        self.creates50rows()

        
        
    def creates50rows(self):
        '''
        Generate 50 cases and export as a txt
        
        '''
        lista = [] 
        
        #Creates 50 rows
        while len(lista)<50:
            # genereta a row of 12 numbers 
            row = np.random.randint(low=1,high=51,size=12)
            
            #checks if it contains at least one repeting number by counting the number or unique values
            if len(np.unique(row)) == 12:       # if 12 unique values chose a random to be repeated and placed as the last item
                index = randint(0,11)
                row[-1] = row[index]
                
            if self.checks_validity(row):
                lista.append(row)
                
        
        #Lists of lists appended to a dataframe
        self.df = pd.DataFrame(columns=[1,2,3,4,5,6,7,8,9,10,11,12],data=lista)
        self.df.to_csv(self.Output, index=False, header=False)   
            
        
    
    
    def checks_validity(self, row):
        ''''Checks the validity of the numbers folowing the rules: 
            1 - At least one number has to be repited
            2 - Has at least 6 unique numbers        

        '''
        #Transform the list into a 
        row = pd.Series(row)
        n_uniques = len(row.unique())  # get the number of uniques           
        maximum = row.max()    
        minimo = row.min()

        # checks number of uniques
        if (n_uniques < 6) or (n_uniques == 12):    # at least 6 uniques, at least 1 repeting number
            valid = False
            
            
        
        # Checks if numbers are all under 50
        elif maximum > 50 or minimo <1 :
            valid = False
         
        # if all conditions are met then return True
        else:
            valid = True 

    
        return valid        
        
        
    
        
    

#Chama a classe
ExercicioB( output_txt = 'Novos50Valores.txt')

#Calcula os valores do exercicio A com a series criads no exercicio B
#Result = ExercicioA(txtfile = 'ValuesFor50Students.txt')
#Result.answers.to_excel('Answers-50-studants.xlsx')