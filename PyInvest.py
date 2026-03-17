import math
import random
import datetime
import statistics as st
import locale

locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')

#entrada 

capital = float(input('Capital inicial: '))
aporte = float(input('Aporte inicial: '))
meses = float(input('Prazo(meses): '))
cdi_anual = float(input('CDI anual (%): '))/100
perc_cdb = float(input('Percentua do CDI - CDB (%): '))/100
perc_lci = float(input('Percentual do CDI - LCI (%): '))/100
taxa_fii = float(input('Rentabilidade do FII (%): '))/100
meta = float(input('Meta finaceira (R$): '))

#conversão do CDI
cdi_mensal = math.pow((1+cdi_anual), 1/12) - 1

#total investido
total_investido = capital + (aporte * meses)

#CDB
taxa_cdb = cdi_mensal * perc_cdb
montante_cdb = (capital * math.pow((1+taxa_cdb), meses))+(aporte * meses)
lucro_cdb = montante_cdb - total_investido
montante_cdb_liquido = total_investido + (lucro_cdb * 0.85)

#LCI/LCA
taxa_lci = cdi_mensal * perc_lci
montante_lci = (capital * math.pow((1+taxa_lci), meses)) +(aporte * meses)

#Poupança
taxa_poupanca = 0.005 
montante_poupanca = (capital * math.pow((1+taxa_poupanca), meses)) + (aporte * meses)

#FII
montante_fii = (capital * math.pow((1+taxa_fii), meses)) + (aporte * meses) 
vari1 = random.uniform(-0.003, 0.003)
vari2 = random.uniform(-0.003, 0.003)
vari3 = random.uniform(-0.003, 0.003)
vari4 = random.uniform(-0.003, 0.003)
vari5 = random.uniform(-0.003, 0.003)

simu1 = montante_fii + (montante_fii * vari1)
simu2 = montante_fii + (montante_fii * vari2)
simu3 = montante_fii + (montante_fii * vari3)
simu4 = montante_fii + (montante_fii * vari4)
simu5 = montante_fii + (montante_fii * vari5)

media_fii = st.mean((simu1, simu2, simu3, simu4, simu5))
mediana_fii = st.median((simu1, simu2, simu3, simu4, simu5))
desvio_fii = st.stdev((simu1, simu2, simu3, simu4, simu5))

#GRAFICO
blocos_cdb = int(montante_cdb_liquido )/ 1000
blocos_lci = int(montante_lci )/ 1000
blocos_poupamca = int(montante_poupanca )/ 1000
blocos_fii = int(montante_fii )/ 1000

#data
data_inicial = datetime.date.today()
data_final = data_inicial + datetime.timedelta(days= meses * 30)

#Formatar datas
data_simulacao = data_inicial.strftime('%d/%m/%Y')
data_resgate_fmt = data_final.strftime('%d/%m/%Y')

#meta
meta_atingida = media_fii >=meta

print('-' * 40)
print(" PyInvest Simulador de Investimentos")
print('=' * 40)
print(f'Data da simulacao:{data_inicial.strftime("%d/%m/%Y")}')
print(f'Data de resgaste:{data_final.strftime("%d/%m/%Y")}')
print('=' * 40)
print('       ')
print(f'Total investido:{locale.currency(total_investido, grouping=True)}')
print('       ')
print('--- RESULTADOS FINANCEIROS ---')
print(f'CDB: {locale.currency(montante_cdb_liquido, grouping=True)}')
print(f'{'█'* int(montante_cdb_liquido / 1000)}')
print('       ')
print(f'LCI:{locale.currency(montante_lci, grouping=True)}')
print(f'{'█'* int(montante_lci / 1000)}')
print('       ')
print(f'Poupanca:{locale.currency(montante_poupanca, grouping=True)}')
print(f'{'█'* int(montante_poupanca / 1000)}')
print('       ')
print(f'FII(media:{locale.currency(media_fii, grouping=True)}')
print(f'{'█'* int(media_fii / 1000)}')
print('       ')
print('--- ESTATISTICAS FII ---')
print(f'Mediana:{locale.currency(mediana_fii, grouping=True)}')
print(f'Desvio padrao:{locale.currency(desvio_fii, grouping=True)}')
print('       ')
print(f'Meta atingida?:{media_fii >= meta}')
print('='*40)