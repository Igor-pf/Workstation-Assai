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

from app import app
import os

app.config['UPLOAD_EXTENSIONS'] = ['.xlsx','.csv']
UPLOADER_FOLDER = os.path.join(os.getcwd(), 'upload')
file_local = UPLOADER_FOLDER+"\\dados.xlsx"
file_json = UPLOADER_FOLDER+"\\dados-auditoria.json"


