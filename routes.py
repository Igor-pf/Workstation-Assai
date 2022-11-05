from werkzeug.utils import secure_filename
from flask import request
from flask import render_template
from folder import *
from datetime import datetime
from json_dados import *
from converter_dados import *
import os
user = os.environ.get('USERNAME')


@app.route('/')
@app.route("/visao-geral-auditoria")
def visao_geral_auditoria():
    for d in json_dados("dados-auditoria-atual"):
        nao_lidos = d['Não Lidos']
        lidos_com_estoque = d['Lidos Com Estoque']
        lidos_sem_estoque = d['Lidos Sem Estoque']
        auditoria = d['Auditoria']
        colaboradores_ativos = d['Colaboradores Ativos']
        desatualizadas = d['Etiquetas Desatualizadas']
    
    if int(desatualizadas) >= 1 :
        
        desatualizadas_ativado = 'block'
    else:
        desatualizadas_ativado = 'none'

       
    
    parcial_classe_produto()
        
    
    return render_template("/auditoria/visao-geral.html", active_visao_geral_auditoria="w3-blue", nao_lidos=nao_lidos, lidos_com_estoque=lidos_com_estoque, lidos_sem_estoque=lidos_sem_estoque, auditoria=auditoria, colaboradores_ativos=colaboradores_ativos, desatualizadas=desatualizadas, desatualizadas_ativado=desatualizadas_ativado, user=user)


## Aqui faz o calculo da parcial de auditoria 
@app.route("/calcular-parcial-auditoria")
def calcular_parcial_auditoria():

    try:

        for d in json_dados("dados-auditoria-atual"):
            SKU = d['SKU']
            print(SKU)
            if d['Auditoria'] == "Presença":
                            
                    SEM_PRESENCA = 'Sem Presença e Com Estoque'
                    print("Auditoria de Presenca")
        
            elif d['Auditoria'] == "Etiqueta":
                    SEM_PRESENCA = 'Não lidos com estoque'
                    print("Auditoria de Etiqueta")

        
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
        TOTAL = 0
        PARCIAL = 0
     
        HORA_DATA = datetime.today().strftime('%H:%M – %d/%m/%Y')

        for d in json_dados("dados"):
            
            if d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'ALTO GIRO':
                ALTO_GIRO = ALTO_GIRO + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'BAZAR':
                BAZAR = BAZAR + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'DPH':
                DPH = DPH + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'DIVERSOS':
                DIVERSOS = DIVERSOS + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'FLV':
                FLV = FLV + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'LATICINIOS 1':
                LATICINIOS = LATICINIOS + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'LIQUIDA':
                LIQUIDA = LIQUIDA + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 1':
                PERECIVEL1 = PERECIVEL1 + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 2':
                PERECIVEL2 = PERECIVEL2 + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 2 B':
                PERECIVEL2B = PERECIVEL2B + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'PERECIVEL 3':
                PERECIVEL3 = PERECIVEL3 + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA DOCE':
                SECA_DOCE = SECA_DOCE + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA SALGADA':
                SECA_SALGADA = SECA_SALGADA + 1
                TOTAL = TOTAL + 1
            elif d[SITUACAO] == SEM_PRESENCA and d[CLASSE_RAIZ] == 'SECA SALGADA 2':
                SECA_SALGADA2 = SECA_SALGADA2 + 1
                TOTAL = TOTAL + 1

        PARCIAL = round(TOTAL/int(SKU)*100,2)
    except:
        return render_template("/auditoria/sem-leituras-com-estoque.html", active_parcial_auditoria="w3-blue", hora_data="Número SKU inválido!!!")
    
    for d in json_dados("dados-auditoria-atual"):
            auditoria = d['Auditoria']

    return render_template("/auditoria/sem-leituras-com-estoque.html", active_parcial_auditoria="w3-blue", \
       alto_giro=ALTO_GIRO, bazar=BAZAR, dph=DPH, diversos=DIVERSOS, flv=FLV, laticinios=LATICINIOS, \
        liquida=LIQUIDA, perecivel1=PERECIVEL1, perecivel2=PERECIVEL2, perecivel2b=PERECIVEL2B, perecivel3=PERECIVEL3, seca_doce=SECA_DOCE, \
            seca_salgada=SECA_SALGADA, seca_salgada2=SECA_SALGADA2, hora_data=HORA_DATA, total=TOTAL, auditoria=auditoria, sku=SKU, parcial_auditoria=PARCIAL, user=user)


@app.route("/parcial-colaboradores")
def parcial_colaboradores():
    for d in json_dados("dados-auditoria-atual"):
            auditoria = d['Auditoria']
    parcial_colaboradores_json()
    return render_template("/auditoria/leituras-por-colaboradores.html", active_parcial_colaboradores="w3-blue",user=user, auditoria=auditoria)

@app.route("/parcial-corredores")
def parcial_corredores():
    for d in json_dados("dados-auditoria-atual"):
            SKU = d['SKU']
    parcial_corredores_json(SKU)
    return render_template("/auditoria/corredores-em-alta.html", active_parcial_corredores="w3-blue", user=user)

## Aqui faz o upload do banco de dados


@app.route("/auditoria/upload-xlsx")
def upload_file():
    return render_template("/auditoria/upload.html", data=DATA, user=user, active_upload="active")

DATA = datetime.today().strftime('%Y-%m-%d')
@app.route("/auditoria/upload", methods=['POST'])
def upload():
    try:
        
        file = request.files['file']
        sku = request.form['sku']
        input_data = datetime.strptime(request.form['data_auditoria'], '%Y-%m-%d').strftime('%d/%m/%Y')
        
        savePath = os.path.join(UPLOADER_FOLDER, secure_filename(file.filename))
        file.save(savePath)
        if os.path.isfile(file_local):
            os.remove(file_local)
            os.rename(savePath, file_local)
        else:
        # Rename the file
            os.rename(savePath, file_local)
        
        converter_dados_upload(sku,input_data)
        

        
        return render_template("/auditoria/upload.html", active_upload="active", data=DATA, user=user, insert_file="Arquivo enviado com sucesso!")
    except Exception:
       
        erro_leitura = "Ocorreu um erro de leitura dos dados!"
            
        return render_template("/auditoria/upload.html", active_upload="active", data=DATA, user=user, insert_file=erro_leitura)

@app.route('/creditos')
def creditos():

    return render_template("/creditos.html")

@app.route('/nova-versao')
def nova_versao():
    
    return render_template("/nova-versao.html")

@app.route('/nova-versao-link')
def nova_versao_link():
    os.system("start \"\" https://github.com/Igor-pf/Workstation-Assai")
    return render_template("/nova-versao.html")
