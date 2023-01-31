#   Copyright (c) 2023 Igor Pereira Formighieri <igorpereira1069@gmail.com>
#
#   A permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia
#   deste software e arquivos de documentação associados (o "Software"), para lidar
#   no Software sem restrições, incluindo, sem limitação, os direitos
#   usar, copiar, modificar, fundir, publicar, distribuir, sublicenciar e/ou vender
#   cópias do Software e para permitir que as pessoas a quem o Software é
#   munidos para o efeito, nas seguintes condições:
#
#   O aviso de direitos autorais acima e este aviso de permissão devem ser incluídos em todos os
#   cópias ou partes substanciais do Software.
#
#   O SOFTWARE É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU
#   IMPLÍCITAS, INCLUINDO, SEM LIMITAÇÃO, AS GARANTIAS DE COMERCIALIZAÇÃO,
#   ADEQUAÇÃO PARA UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUM CASO O
#   OS AUTORES OU DETENTORES DOS DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER REIVINDICAÇÃO, DANOS OU OUTROS
#   RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE,
#   FORA DE OU EM CONEXÃO COM O SOFTWARE OU O USO OU OUTROS NEGÓCIOS NO
#   PROGRAMAS.

import pandas
import json
from folder import *
from json_dados import *
from datetime import datetime

def converter_dados_upload(SKU, INPUT_DATA):
    
    auditoria_atual = []
    fluxo_auditoria = []
    produtos_sem_leituras = []
    produtos_sem_leituras_com_vendas = []
    auditoria = ""
    
    try:
        excel_data_df = pandas.read_excel(file_local, sheet_name='Itens da Auditoria de Presença')
        print("Auditoria de Presenca")
        auditoria = "Presença"
    except:
        excel_data_df = pandas.read_excel(file_local, sheet_name='Itens da Auditoria de Etiqueta')
        print("Auditoria de Etiqueta")
        auditoria = "Etiqueta"

 
    #excel_data_df['\u00daltima Compra'] = pandas.to_datetime(excel_data_df['\u00daltima Compra'], unit='d', origin='1899/12/30')
    thisisjson = excel_data_df.to_json(orient='records')

    thisisjson_dict = json.loads(thisisjson)

    if auditoria == "Etiqueta" or auditoria == "Presença":
        
        with open(file_json, 'w') as json_file:
            json.dump(thisisjson_dict, json_file)
        
        nao_lidos = 0
        lidos_com_estoque = 0
        lidos_sem_estoque = 0
        lidos_nao_pertence = 0
        desatualizadas = 0
        colaboradores = 0
        SITUACAO = 'Situa\u00e7\u00e3o'
        CLASSE_RAIZ = 'Classe de Produto Raiz'
        ALTO_GIRO = 0
        BAZAR = 0
        DIVERSOS = 0
        DPH = 0
        FLV = 0
        LATICINIOS = 0
        LIQUIDA = 0
        PERECIVEL1 = 0
        PERECIVEL2 = 0
        PERECIVEL2B = 0
        PERECIVEL3 = 0
        SECA_DOCE = 0
        SECA_SALGADA = 0
        SECA_SALGADA2 = 0
    
        SETOR = []
        if auditoria == "Presença":
                            
                    SEM_PRESENCA = 'Sem Presença e Com Estoque'
                    print("Auditoria de Presenca")
        
        elif auditoria == "Etiqueta":
                    SEM_PRESENCA = 'Não lidos com estoque'
                    print("Auditoria de Etiqueta")

        for d in json_dados("dados-auditoria"):

            if d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'ALTO GIRO':
                ALTO_GIRO = ALTO_GIRO + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'BAZAR':
                BAZAR = BAZAR + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'DPH':
                DPH = DPH + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'DIVERSOS':
                DIVERSOS = DIVERSOS + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'FLV':
                FLV = FLV + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'LATICINIOS 1':
                LATICINIOS = LATICINIOS + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'LIQUIDA':
                LIQUIDA = LIQUIDA + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 1':
                PERECIVEL1 = PERECIVEL1 + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 2':
                PERECIVEL2 = PERECIVEL2 + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 2 B':
                PERECIVEL2B = PERECIVEL2B + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 3':
                PERECIVEL3 = PERECIVEL3 + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA DOCE':
                SECA_DOCE = SECA_DOCE + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA SALGADA':
                SECA_SALGADA = SECA_SALGADA + 1
                
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA SALGADA 2':
                SECA_SALGADA2 = SECA_SALGADA2 + 1
                
            fluxo_horas = d['Auditado em.1']
            res_fluxo = fluxo_horas[:5]

            if type(d['Estoque atual']) == int:
                if d['Situa\u00e7\u00e3o'] == 'N\u00e3o lidos com estoque' or d['Situa\u00e7\u00e3o'] == 'Sem Presen\u00e7a e Com Estoque':
                    
                    produtos_sem_leituras.append({

                        'Código' : d['C\u00f3digo'],
                        'Produto' : d['Produto'],
                        'Classe Raiz' : d['Classe de Produto Raiz'],
                        'Local' : d['Local'],
                        'Estoque atual' : int(d['Estoque atual']),

                    })


            if not d['Usuário'] == None:

                fluxo_auditoria.append({
                    
                    'Fluxo' : INPUT_DATA+' '+res_fluxo

                })
 
            if auditoria == "Presença":

                    if type(d['Estoque atual']) == int:
                        if d['Situa\u00e7\u00e3o'] == 'Sem Presen\u00e7a e Com Estoque':
                            if d['Dias sem venda'] == 0:
                                produtos_sem_leituras_com_vendas.append({

                                    'Código' : d['C\u00f3digo'],
                                    'Produto' : d['Produto'],
                                    'Classe Raiz' : d['Classe de Produto Raiz'],
                                    'Local' : d['Local'],
                                    'Estoque atual' : int(d['Estoque atual']),

                                })

                    if d['Situação'] == "Sem Presença e Com Estoque":
                        nao_lidos = nao_lidos+1
                    
                    if d['Situação'] == "Com Presença e Com Estoque":
                        lidos_com_estoque = lidos_com_estoque+1
                    if d['Situação'] == "Com Presença e Sem Estoque":
                        lidos_sem_estoque = lidos_sem_estoque+1
                    
            if d['Situação'] == "Lido n\u00e3o pertence":
                        lidos_nao_pertence = lidos_nao_pertence+1
            
            elif auditoria == "Etiqueta":

                    if d['Situação'] == "Não lidos com estoque":
                        nao_lidos = nao_lidos+1
                    
                    if d['Situação'] == "Lido sem estoque":
                        lidos_sem_estoque = lidos_sem_estoque+1
                    if d['Situação'] == "Desatualizado":
                        desatualizadas = desatualizadas+1
        
        
        SETOR = {'SETOR' : 'ALTO GIRO','QTD' : ALTO_GIRO,}, { 'SETOR' : 'BAZAR', 'QTD' : BAZAR,  }, { 'SETOR' : 'DPH', 'QTD' : DPH,  }, { 'SETOR' : 'DIVERSOS', 'QTD' : DIVERSOS,  }, { 'SETOR' : 'FLV', 'QTD' : FLV,  }, { 'SETOR' : 'LATICINIOS 1', 'QTD' : LATICINIOS,  }, { 'SETOR' : 'LIQUIDA', 'QTD' : LIQUIDA,  }, { 'SETOR' : 'PERECIVEL 1', 'QTD' : PERECIVEL1,  }, { 'SETOR' : 'PERECIVEL 2', 'QTD' : PERECIVEL2,  }, { 'SETOR' : 'PERECIVEL 2 B', 'QTD' : PERECIVEL2B,  }, { 'SETOR' : 'PERECIVEL 3', 'QTD' : PERECIVEL3,  }, { 'SETOR' : 'SECA DOCE', 'QTD' : SECA_DOCE,  }, { 'SETOR' : 'SECA SALGADA', 'QTD' : SECA_SALGADA,  }, { 'SETOR' : 'SECA SALGADA 2', 'QTD' : SECA_SALGADA2,  }                 

        json_output(sorted(SETOR, key=lambda k: k['QTD'], reverse=True), "setor")
        json_output(produtos_sem_leituras, "produtos")
        produtos_sem_leituras_com_vendas_sorted = sorted(produtos_sem_leituras_com_vendas, key=lambda k: k['Estoque atual'], reverse=True)
        produtos_sem_leituras_sorted = sorted(produtos_sem_leituras, key=lambda k: k['Estoque atual'], reverse=True)

        if auditoria == "Etiqueta":
            lidos_com_estoque = int(SKU)-int(nao_lidos)

        unique = { each['Usu\u00e1rio'] : each for each in json_dados("dados-auditoria") }.values()

        for i in unique:
            if not i['Usuário'] == None:
                colaboradores = colaboradores+1

        unique = { each['Fluxo'] : each for each in fluxo_auditoria }.values()

        sorted_unique = sorted(unique, key=lambda k: k['Fluxo'], reverse=True)
        

        append_fluxo = []

        
        for i in sorted_unique:
            count_fluxo = 0

            for f in fluxo_auditoria:
                
                if i == f:
                    count_fluxo = count_fluxo+1
            

            append_fluxo.append({'t': i['Fluxo'], 'y': count_fluxo})

        dados_fluxo = "var ctx_produtos_lidos = document.getElementById('ProdutosChart').getContext('2d'); var myChart = new Chart(ctx_produtos_lidos, { type: 'line', options: {  responsive: true,  maintainAspectRatio: false,  scales: {  xAxes: [{ display: true, type: 'time', time: { parser: 'DD/MM/YYYY HH:mm:ss', tooltipFormat: 'll HH:mm:ss', unitStepSize: 1, displayFormats: {  'day': 'DD/MM/YYYY' } } }]  } }, data: {  datasets: [{  label: 'Leituras',  data: "+str(append_fluxo)+",  backgroundColor: [  'rgba(0, 156, 255, .3)' ],  borderColor: [  'rgba(0, 156, 255, .3)'  ],  borderWidth: 2  }] } });"
        
        with open(os.path.join(os.getcwd(),'static', 'js')+"\\fluxo-de-leituras.js", "w") as outfile: 
                outfile.write(dados_fluxo)

        auditoria_atual.append({'Auditoria' : auditoria, 'SKU': SKU, 'Não Lidos': nao_lidos, 'Lidos Com Estoque': lidos_com_estoque, 'Lidos Sem Estoque':
        lidos_sem_estoque, 'Colaboradores Ativos': colaboradores , 'Etiquetas Desatualizadas': desatualizadas, 'Lidos não pertence': lidos_nao_pertence, 'Parcial' : round(nao_lidos/int(SKU)*100,2)})
     
        json_output(auditoria_atual, "auditoria-atual")
        json_output(produtos_sem_leituras_sorted, "produtos-sem-leituras")
        json_output(produtos_sem_leituras_com_vendas_sorted, "produtos-sem-leituras-com-vendas")
