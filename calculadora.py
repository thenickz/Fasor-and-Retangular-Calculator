import numpy as np
import PySimpleGUI as sg
from math import radians, atan2

lista = []
lista1 = ''
sg.theme('Reddit')

layout = [
        # ROW 1 Label
        [sg.Text('Retangular -> Polar')],

        # ROW 2 inputs retangulares e botão
        [sg.Text('Retangular:'),
         sg.InputText(key='realRet1', size=(6, 1)),
         sg.InputText(key='imaRet1', size=(6, 1)),
         sg.Text('j'),
         sg.Text('='),
         sg.Button('Polar', key='botaoRetPol'),
         sg.Text('', key='polar1', size=(10, 1))],

        # ROW 3 label
        [sg.Text('Polar -> Retangular')],

        # ROW 4 inputs polares e botão
        [sg.Text('Polar:'), sg.InputText(key='pol', size=(7, 1)),
         sg.Text('∠'),
         sg.InputText(key='angle', size=(7, 1)),
         sg.Text('°'),
         sg.Text('='),
         sg.Button('Retangular', key='botaoPolRet'),
         sg.Text('', key='retangular1', size=(13, 1))],

        # ROW 5 label
        [sg.Text('Somar e Subtrair')],

        # ROW 6 inputs de soma fasor
        [sg.InputText(key='somar1', size=(10, 1)),
         # sg.InputText(key= 'somar2', size=(10,1)),
         sg.Text('±'),
         # sg.InputText(key= 'somar3', size=(10,1)),
         sg.InputText(key='somar4', size=(10, 1))],

        # ROW 7 botões e contas
        [sg.Button('Somar', key='contaSomar'),
         sg.Text('', key='somar0', size=(10, 1)),
         sg.Button('Subtrair', key='contaSubtrair'),
         sg.Text('', key='subtrair0', size=(10, 1))],

        # ROW 8 label
        [sg.Text('Multiplicar e Dividir')],

        # ROW 9 inputs de multiplicação e divisão
        [sg.InputText(key='multi1', size=(10, 1)),
         # sg.InputText(key= 'multi2',  size=(10,1)),
         sg.Text('/'),
         # sg.InputText(key= 'multi3', size=(10,1)),
         sg.InputText(key='multi4',  size=(10, 1))],

        # ROW 10 botões e contas
        [sg.Button('Multiplicar', key='contaMultiplicar'),
         sg.Text('', key='multi00', size=(10, 1)),
         sg.Button('Dividisão', key='contaDividir'),
         sg.Text(key='div0', size=(10, 1))]
]

janela = sg.Window('Calculadora de Fasor', layout)

while True:
    event, value = janela.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    if event == 'botaoRetPol':
        dummy1 = dummy2 = 0
        dummy3 = False
        while True:
            try:
                if dummy3:
                    value['realRet1'] = dummy1
                    value['imaRet1'] = dummy2
                x1 = float(value['realRet1'])
                y1 = float(value['imaRet1'])
                conta1 = np.sqrt((x1 ** 2) + (y1 ** 2))
                angle = np.degrees(atan2(y1, x1))
                janela['polar1'].update('{:.2f}∠{:.2f}°'.format(conta1, angle))

                break
            
            except ValueError:
                try:
                    if not dummy3:
                        dummy1 = value['realRet1'].replace(',', '.')
                        dummy2 = value['imaRet1'].replace(',', '.')
                        dummy3 = True
                        continue
                    else:
                        sg.Popup('Ocorreu um Erro!\nEscreva apenas números e tente\
                                 não usar Virgulas!',
                                 keep_on_top=True,
                                 text_color='red',
                                 title='Ocorreu um Erro',
                                 button_color='red')
                        break
                except ValueError:
                    pass
    if event == 'botaoPolRet':
        dummy1 = dummy2 = 0
        dummy4 = False
        while True:
            try:
                if dummy4:
                    value['pol'] = dummy1
                    value['angle'] = dummy2
                x2 = float(value['pol'])
                y2 = radians(float(value['angle']))
                conta2 = x2 * np.sin(y2)
                conta3 = x2 * np.cos(y2)
                janela['retangular1'].update('{:.2f} + {:.2f}j'
                                             .format(conta3, conta2))
                break
            except ValueError:
                try:
                    if not dummy4:
                        dummy1 = value['pol'].replace(',', '.')
                        dummy2 = value['angle'].replace(',', '.')
                        dummy4 = True
                        continue
                    else:
                        sg.Popup('Ocorreu um Erro!! Escreva apenas números e \
                                 tente não usar Virgulas!',
                                 keep_on_top=True,
                                 text_color='red',
                                 title='Ocorreu um Erro',
                                 button_color='red')
                        break
                except ValueError:
                    pass
    #  if event == 'contaSomar':
    #      x3 = value['somar1']
    #      y3 = value['somar4']
    #      for letra in x3:
    #          if '+-' in letra:
    #              real = lista
    #         else:
    #             lista1 = f'{lista1}+{lista1}+'
    # # if event == 'contaSubtrair':
