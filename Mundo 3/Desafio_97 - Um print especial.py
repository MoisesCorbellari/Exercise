'''
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
Ex:
escreva('Olá, Mundo!') 
Saída:                                                                                                                          
~~~~~~~~~
Olá, Mundo!                                                                                                                                                         
~~~~~~~~~'''

def escreva(msg):
    txt = len(msg) + 10
    print('*'*txt)
    print(f'{msg:^{txt}}')

escreva('Hello World!')
escreva('Course of Python.')