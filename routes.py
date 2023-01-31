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




from werkzeug.utils import secure_filename
from flask import request
from flask import render_template
from folder import *
from datetime import datetime
from json_dados import *
from converter_dados import *
import os
user = os.environ.get('HOMEPATH')[7:17]


@app.route('/')
@app.route("/dashboard-auditoria")
def visao_geral_auditoria():
    
    for d in json_dados("dados-auditoria-atual"):
        nao_lidos = d['Não Lidos']
        lidos_com_estoque = d['Lidos Com Estoque']
        lidos_sem_estoque = d['Lidos Sem Estoque']
        lidos_nao_pertence = d['Lidos n\u00e3o pertence']
        auditoria = d['Auditoria']
        colaboradores_ativos = d['Colaboradores Ativos']
        desatualizadas = d['Etiquetas Desatualizadas']
        sku = d['SKU']
        parcial = d['Parcial']
    
    if int(desatualizadas) >= 1 :
        
        desatualizadas_ativado = 'block'
    else:
        desatualizadas_ativado = 'none'

    if auditoria == "Presença":
        card_nlcaecv = 'block'
    else:
        card_nlcaecv = 'none'


    parcial_classe_produto()

    return render_template("/auditoria/dashboard.html", nao_lidos_com_alto_estoque=json_dados("dados-produtos-sem-leituras"),\
         nao_lidos_com_alto_estoque_com_vendas=json_dados("dados-produtos-sem-leituras-com-vendas"), card_nlcaecv=card_nlcaecv,\
         nao_lidos=nao_lidos, lidos_com_estoque=lidos_com_estoque, lidos_sem_estoque=lidos_sem_estoque, auditoria=auditoria, \
         colaboradores_ativos=colaboradores_ativos, desatualizadas=desatualizadas, desatualizadas_ativado=desatualizadas_ativado,\
         lidos_nao_pertence=lidos_nao_pertence, sku=sku, parcial=parcial ,user=user, active_parcial_dasboard="active")

## Aqui faz o calculo da parcial de auditoria 
@app.route("/setor")
def calcular_parcial_auditoria():

    try:

        for d in json_dados("dados-auditoria-atual"):
            SKU = d['SKU']
            TOTAL = d['N\u00e3o Lidos']
            PARCIAL = d['Parcial']
     
        HORA_DATA = datetime.today().strftime('%H:%M – %d/%m/%Y')

    except:
            return render_template("/auditoria/sem-leituras-com-estoque.html", active_parcial_auditoria="active", hora_data="Número SKU inválido!!!")
    
    for d in json_dados("dados-auditoria-atual"):
            auditoria = d['Auditoria']

    return render_template("/auditoria/parcial.html", active_parcial_auditoria="active", \
       SETOR=json_dados("dados-setor") , hora_data=HORA_DATA, total=TOTAL, auditoria=auditoria, sku=SKU, parcial_auditoria=PARCIAL, user=user)


@app.route("/parcial-colaboradores")
def parcial_colaboradores():
    for d in json_dados("dados-auditoria-atual"):
            auditoria = d['Auditoria']
    parcial_colaboradores_json()
    return render_template("/auditoria/colaboradores.html", active_parcial_colaboradores="active",user=user, auditoria=auditoria)

@app.route("/parcial-corredores")
def parcial_corredores():
    for d in json_dados("dados-auditoria-atual"):
            SKU = d['SKU']
    parcial_corredores_json(SKU)
    return render_template("/auditoria/corredores.html", active_parcial_corredores="active", user=user)

## Aqui faz o upload do banco de dados para auditoria

@app.route("/upload-xlsx")
def upload_file():
    return render_template("/upload.html", data=DATA, user=user, active_upload="active")

DATA = datetime.today().strftime('%Y-%m-%d')
@app.route("/upload", methods=['POST'])
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
        
        if os.path.isfile(file_local):
            os.remove(file_local)
        
        return render_template("/upload.html", back_upload="history.back();", active_upload="active", data=DATA, user=user, color_ms="color: #009CFF;", insert_file="Arquivo enviado com sucesso!")
    except Exception:
       
        
        erro_leitura = "Ocorreu um erro de leitura dos dados, certifique-se de que você selecionou o arquivo correto!"
            
        return render_template("/upload.html", active_upload="active", data=DATA, user=user, insert_file=erro_leitura, color_ms="color: red;")

@app.route('/creditos')
def creditos():

    return render_template("/creditos.html", user=user)

@app.route('/nova-versao')
def nova_versao():
    
    return render_template("/nova-versao.html", user=user)
