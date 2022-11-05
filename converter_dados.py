import pandas
import json
from folder import *
from json_dados import *


def converter_dados_upload(SKU, INPUT_DATA):
    
    
    
    
    
    auditoria_atual = []
    fluxo_auditoria = []
    try:

        try:
            excel_data_df = pandas.read_excel(file_local, sheet_name='Itens da Auditoria de Presença')
            print("Auditoria de Presenca")
            
            auditoria = "Presença"
        except:
            excel_data_df = pandas.read_excel(file_local, sheet_name='Itens da Auditoria de Etiqueta')
            auditoria = "Etiqueta"
            print("Auditoria de Etiqueta")
    except:
        
        return 'Erro de Leitura'
        
    
    thisisjson = excel_data_df.to_json(orient='records')

    
    thisisjson_dict = json.loads(thisisjson)

    
    with open(file_json, 'w') as json_file:
        json.dump(thisisjson_dict, json_file)
    
    nao_lidos = 0
    lidos_com_estoque = 0
    lidos_sem_estoque = 0
    desatualizadas = 0
    colaboradores = 0
    
    

    for d in json_dados("dados"):
        
        fluxo_horas = d['Auditado em.1']
        res_fluxo = fluxo_horas[:5]

        if not d['Usuário'] == None:
            fluxo_auditoria.append({
                
                'Fluxo' : INPUT_DATA+' '+res_fluxo

            })

    
        
        if auditoria == "Presença":

                if d['Situação'] == "Sem Presença e Com Estoque":
                    nao_lidos = nao_lidos+1
                
                if d['Situação'] == "Com Presença e Com Estoque":
                    lidos_com_estoque = lidos_com_estoque+1
                if d['Situação'] == "Com Presença e Sem Estoque":
                    lidos_sem_estoque = lidos_sem_estoque+1
                

        
        elif auditoria == "Etiqueta":

                if d['Situação'] == "Não lidos com estoque":
                    nao_lidos = nao_lidos+1
                if d['Situação'] == "Lido sem estoque":
                    lidos_sem_estoque = lidos_sem_estoque+1
                if d['Situação'] == "Desatualizado":
                    desatualizadas = desatualizadas+1

   


    if auditoria == "Etiqueta":
        lidos_com_estoque = int(SKU)-int(nao_lidos)

    unique = { each['Usu\u00e1rio'] : each for each in json_dados("dados") }.values()

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

        


    dados_fluxo = "var ctx_produtos_lidos = document.getElementById('ProdutosChart').getContext('2d'); var myChart = new Chart(ctx_produtos_lidos, { type: 'line', options: {  responsive: true,  maintainAspectRatio: false,  scales: {  xAxes: [{ display: true, type: 'time', time: { parser: 'DD/MM/YYYY HH:mm:ss', tooltipFormat: 'll HH:mm:ss', unitStepSize: 1, displayFormats: {  'day': 'DD/MM/YYYY' } } }]  } }, data: {  datasets: [{  label: 'Fluxo de Leituras',  data: "+str(append_fluxo)+",  backgroundColor: [  'rgba(255, 99, 132, 0.2)' ],  borderColor: [  'rgba(255,99,132,1)'  ],  borderWidth: 2  }] } });"
    
    with open(os.path.join(os.getcwd(),'static', 'js')+"\\fluxo-de-leituras.js", "w") as outfile: 
            outfile.write(dados_fluxo)




    

    auditoria_atual.append({'Auditoria' : auditoria, 'SKU': SKU, 'Não Lidos': nao_lidos, 'Lidos Com Estoque': lidos_com_estoque, 'Lidos Sem Estoque':
    lidos_sem_estoque, 'Colaboradores Ativos': colaboradores , 'Etiquetas Desatualizadas': desatualizadas})
    
  
    
    

    json_output(auditoria_atual, "auditoria-atual")
                    