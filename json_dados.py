from ast import In
import json
from folder import *

def json_dados(json_file):

    with open(UPLOADER_FOLDER+"\\"+json_file+".json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
        return dados

def json_output(dados, name):
        json_object = json.dumps(dados, indent = 4) 
        with open(UPLOADER_FOLDER+"\\dados-"+name+".json", "w") as outfile: 
            outfile.write(json_object)

def parcial_colaboradores_json():

    

    unique = { each['Usu\u00e1rio'] : each for each in json_dados("dados") }.values()
    
    lines_unique=[]
    dictionary = []
    dados_parcial_name = []
    dados_parcial_values = []
    dados_parcial_complete = []

    for i in unique:
        lines_unique.append(i['Usu\u00e1rio'])

    
    for d in json_dados("dados"):

            dictionary.append(                                
                                {   
                                    d['Usu\u00e1rio'] : d['Situa\u00e7\u00e3o'], 
                                } 
                            )

    for dados_unique in lines_unique:
        numero = 5000
        
        for d in dictionary:
            if dados_unique in d:
                numero = numero+1
        
        if not dados_unique == None:
            dados_parcial_complete.append({
            
            "colaboradores": str(dados_unique),
            "valores": str(numero),
            }
            
            )
   
    final_colaboradores= sorted(dados_parcial_complete, key=lambda k: k['valores'], reverse=True)
    

    
    
    for f_colaboradores in final_colaboradores:

        
            dados_parcial_name.append(
                
                str(f_colaboradores["colaboradores"]),
                
                )
        
            dados_parcial_values.append(
            
                str(int(f_colaboradores["valores"])-5000),
            
            )
            
    dados_parcial_html = 'const CHART = document.getElementById("chart"); Chart.defaults.global.animation.duration = 1000; Chart.plugins.register({  beforeUpdate: function(chart) { if (chart.options.sort) { let labels = chart.data.labels;  let dataArray = chart.data.datasets[0].data.slice();  let mapValueLabel = {};  dataArray.forEach((value, index) => {    mapValueLabel[value] = labels[index];  });  dataArray.sort((a, b) => b - a);  let meta = chart.getDatasetMeta(0);  let newLabels = [];  dataArray.forEach((a, i) => {    newLabels[i] = mapValueLabel[a];  });  chart.data.datasets[0].data = dataArray;  chart.data.labels = newLabels;    }  } });  $(document).ready(function(){    var chartdata = {   labels: '+str(dados_parcial_name)+',    datasets: [{    label: "LEITURAS DE AUDITORIA",    data: '+str(dados_parcial_values)+',    backgroundColor: ["#4b4268", "#b15928", "#fb9a99", "#cab2d6", "#e31a1c", "#b2df8a", "#ff7f00", "#33a02c", "#1f78b4","#0563b5","#ac99e9","#5b762b", "#eb005b","#3a2e33","#35cbba","#284208","#66932f","#661e06","#000000","#65746b","#011278","#3a3d50","#919299","#d9b728","#1f5e6e","#c38280","#661411","#44a0f7"],    }] };   var barGraph = new Chart(CHART, {  type: "horizontalBar" ,  data: chartdata,  options: {    scales: {  xAxes: [{    ticks: {  beginAtZero: true    }  }] }  }    });  });'
    
    with open(os.path.join(os.getcwd(),'static', 'js')+"\\leituras-por-colaboradores.js", "w") as outfile: 
            outfile.write(dados_parcial_html) 

def parcial_corredores_json(sku):

     

    unique = { each['Local'] : each for each in json_dados("dados") }.values()

    for d in json_dados("dados-auditoria-atual"):
        if d['Auditoria'] == "Presença":
                        
                SEM_PRESENCA = 'Sem Presença e Com Estoque'
                print("Auditoria de Presenca")
    
        elif d['Auditoria'] == "Etiqueta":
                SEM_PRESENCA = 'Não lidos com estoque'
                print("Auditoria de Etiqueta")
   

    SITUACAO = 'Situa\u00e7\u00e3o'
    lines_unique=[]
    dictionary = []
    dados_parcial_name = []
    dados_parcial_values = []
    dados_parcial_complete = []

    for i in unique:
        lines_unique.append(i['Local'])

    for d in json_dados("dados"):

        
            dictionary.append(                                
                                {   
                                    d['Local'] : d[SITUACAO], 
                                    
                                } 
                            )
       


    for dados_unique in lines_unique:
        numero = 9000
        
        
        for d in dictionary:
           
           
            if dados_unique in d:
                
                    if d[dados_unique] == SEM_PRESENCA:
                        numero = numero+1
                        
                    
           
        if not dados_unique == None:
            dados_parcial_complete.append({
                "corredores": str(dados_unique),
                "valores": str(numero),
                
            }
                )


    final_corredores= sorted(dados_parcial_complete, key=lambda k: k['valores'], reverse=True)

    top_10_corredores = 0
    for f in final_corredores:

        top_10_corredores = top_10_corredores+1

        if top_10_corredores <= 15:
            dados_parcial_name.append(
                
                str(f["corredores"]),
                
                )
        
            dados_parcial_values.append(
            
                str(int(f["valores"])-9000),
            
            )

    dados_parcial_html = 'const CHART = document.getElementById("chart"); Chart.defaults.global.animation.duration = 1000; Chart.plugins.register({  beforeUpdate: function(chart) { if (chart.options.sort) { let labels = chart.data.labels;  let dataArray = chart.data.datasets[0].data.slice();  let mapValueLabel = {};  dataArray.forEach((value, index) => {    mapValueLabel[value] = labels[index];  });  dataArray.sort((a, b) => b - a);  let meta = chart.getDatasetMeta(0);  let newLabels = [];  dataArray.forEach((a, i) => {    newLabels[i] = mapValueLabel[a];  });  chart.data.datasets[0].data = dataArray;  chart.data.labels = newLabels;    }  } });  $(document).ready(function(){    var chartdata = {   labels: '+str(dados_parcial_name)+',    datasets: [{    label: "SEM LEITURAS",    data: '+str(dados_parcial_values)+',    backgroundColor: ["#4b4268", "#b15928", "#fb9a99", "#cab2d6", "#e31a1c", "#b2df8a", "#ff7f00", "#33a02c", "#1f78b4","#0563b5","#ac99e9","#5b762b", "#eb005b","#3a2e33","#35cbba","#284208","#66932f","#661e06","#000000","#65746b","#011278","#3a3d50","#919299","#d9b728","#1f5e6e","#c38280","#661411","#44a0f7"],    }] };   var barGraph = new Chart(CHART, {  type: "horizontalBar" ,  data: chartdata,  options: {    scales: {  xAxes: [{    ticks: {  beginAtZero: true    }  }] }  }    });  });'
    
    with open(os.path.join(os.getcwd(), 'static', 'js')+"\\corredores-em-alta.js", "w") as outfile: 
            outfile.write(dados_parcial_html) 

def parcial_corredores_com_vendas_json():

     

    unique = { each['Local'] : each for each in json_dados("dados") }.values()
    SEM_PRESENCA = 'Sem Presença e Com Estoque'
    SITUACAO = 'Situa\u00e7\u00e3o'
    lines_unique=[]
    dictionary = []
    dados_parcial_name = []
    dados_parcial_values = []
    dados_parcial_complete = []

    for i in unique:
        lines_unique.append(i['Local'])

    for d in json_dados("dados"):

            dictionary.append(                                
                                {   
                                    d['Local'] : d[SITUACAO], 
                                    "Dias Sem Vendas" : d['Dias sem venda'],
                                } 
                            )

    for dados_unique in lines_unique:
        numero = 9000
        
        
        for d in dictionary:
           
           
            if dados_unique in d:
                
                    if d[dados_unique] == SEM_PRESENCA:
                        numero = numero+1
                        
                    
           
        if not dados_unique == None:
            dados_parcial_complete.append({
                "corredores": str(dados_unique),
                "valores": str(numero),
                
            }
                )


    final_corredores= sorted(dados_parcial_complete, key=lambda k: k['valores'], reverse=True)

    top_10_corredores = 0
    for f in final_corredores:

        top_10_corredores = top_10_corredores+1

        if top_10_corredores <= 15:
            dados_parcial_name.append(
                
                str(f["corredores"]),
                
                )
        
            dados_parcial_values.append(
            
                str(int(f["valores"])-9000),
            
            )
    

    dados_parcial_html = 'const CHART = document.getElementById("chart"); Chart.defaults.global.animation.duration = 1000; Chart.plugins.register({  beforeUpdate: function(chart) { if (chart.options.sort) { let labels = chart.data.labels;  let dataArray = chart.data.datasets[0].data.slice();  let mapValueLabel = {};  dataArray.forEach((value, index) => {    mapValueLabel[value] = labels[index];  });  dataArray.sort((a, b) => b - a);  let meta = chart.getDatasetMeta(0);  let newLabels = [];  dataArray.forEach((a, i) => {    newLabels[i] = mapValueLabel[a];  });  chart.data.datasets[0].data = dataArray;  chart.data.labels = newLabels;    }  } });  $(document).ready(function(){    var chartdata = {   labels: '+str(dados_parcial_name)+',    datasets: [{    label: "SEM LEITURAS",    data: '+str(dados_parcial_values)+',    backgroundColor: ["#4b4268", "#b15928", "#fb9a99", "#cab2d6", "#e31a1c", "#b2df8a", "#ff7f00", "#33a02c", "#1f78b4","#0563b5","#ac99e9","#5b762b", "#eb005b","#3a2e33","#35cbba","#284208","#66932f","#661e06","#000000","#65746b","#011278","#3a3d50","#919299","#d9b728","#1f5e6e","#c38280","#661411","#44a0f7"],    }] };   var barGraph = new Chart(CHART, {  type: "horizontalBar" ,  data: chartdata,  options: {    scales: {  xAxes: [{    ticks: {  beginAtZero: true    }  }] }  }    });  });'
    
    with open(os.path.join(os.getcwd(), 'static', 'js')+"\\corredores-em-alta.js", "w") as outfile: 
            outfile.write(dados_parcial_html) 

def parcial_classe_produto():
    lines_unique=[]
    dados_parcial_complete = []
    dados_parcial_name = []
    dados_parcial_values = []

    unique = { each['Classe de Produto Raiz'] : each for each in json_dados("dados") }.values()
    for d in json_dados("dados-auditoria-atual"):
        if d['Auditoria'] == "Presença":
                        
                SEM_PRESENCA = 'Sem Presença e Com Estoque'
                print("Auditoria de Presenca")
    
        elif d['Auditoria'] == "Etiqueta":
                SEM_PRESENCA = 'Não lidos com estoque'
                print("Auditoria de Etiqueta")

    for i in unique:
        lines_unique.append(i['Classe de Produto Raiz'])


    
    for dados_unique in lines_unique:
        numero = 2000
        for d in json_dados("dados"):

            if dados_unique == d['Classe de Produto Raiz'] and d['Situação'] == SEM_PRESENCA:
              numero = numero+1
                              
  
        if not dados_unique == None:
            dados_parcial_complete.append({
                "Classe de Produto Raiz": str(dados_unique),
                "valores": str(numero),
                
            })

    final_classe_produto_raiz = sorted(dados_parcial_complete, key=lambda k: k['valores'], reverse=True)


    

    for f in final_classe_produto_raiz:

        
            dados_parcial_name.append(
                
                str(f["Classe de Produto Raiz"]),
                
                )
        
            dados_parcial_values.append(
            
                str(int(f["valores"])-2000),
            
            )
    
    dados_parcial_html = 'let ctx = document.getElementById("classe_produto_raiz"); let dados = { datasets: [{ data: '+str(dados_parcial_values)+', backgroundColor: ["rgb(255, 99, 132)", "#52697c", "#d5c832", "#00377a", "#fec9ff", "rgb(255, 199, 132)", "rgb(55, 99, 132)", "#9f2d67", "#afafaf", "#fd0000", "#420e0e", "#585726", "#787861", "#db4985", "#52e9aa", "#818187", "#620000"]}], labels: '+str(dados_parcial_name)+'}; let opcoes = { cutoutPercentage: 40};let meuDonutChart = new Chart(ctx, {type: "doughnut", data: dados, options: opcoes});'    
    
    
    ##dados_parcial_html = 'const CHART = document.getElementById("classe_produto_raiz"); Chart.defaults.global.animation.duration = 1000; Chart.plugins.register({  beforeUpdate: function(chart) { if (chart.options.sort) { let labels = chart.data.labels;  let dataArray = chart.data.datasets[0].data.slice();  let mapValueLabel = {};  dataArray.forEach((value, index) => {    mapValueLabel[value] = labels[index];  });  dataArray.sort((a, b) => b - a);  let meta = chart.getDatasetMeta(0);  let newLabels = [];  dataArray.forEach((a, i) => {    newLabels[i] = mapValueLabel[a];  });  chart.data.datasets[0].data = dataArray;  chart.data.labels = newLabels;    }  } });  $(document).ready(function(){    var chartdata = {   labels: '+str(dados_parcial_name)+',    datasets: [{    label: "SEM LEITURAS",    data: '+str(dados_parcial_values)+',    backgroundColor: ["#4b4268", "#b15928", "#fb9a99", "#cab2d6", "#e31a1c", "#b2df8a", "#ff7f00", "#33a02c", "#1f78b4","#0563b5","#ac99e9","#5b762b", "#eb005b","#3a2e33","#35cbba","#284208","#66932f","#661e06","#000000","#65746b","#011278","#3a3d50","#919299","#d9b728","#1f5e6e","#c38280","#661411","#44a0f7"],    }] };   var barGraph = new Chart(CHART, {  type: "pie" ,  data: chartdata,  options: {    scales: {  xAxes: [{    ticks: {  beginAtZero: true    }  }] }  }    });  });'
    
    
    
    with open(os.path.join(os.getcwd(), 'static', 'js')+"\\classe-produtos-raiz.js", "w") as outfile: 
            outfile.write(dados_parcial_html) 