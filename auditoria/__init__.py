from datetime import datetime
from openpyxl import Workbook, load_workbook
from folder import *
from flask import render_template


def calcular_parcial():
    SKU = 9222
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
    print("oi")
    planilha = load_workbook(file_local)
    aba_ativa = planilha.active
    for celula in aba_ativa["C"]:
        TOTAL = TOTAL + 1
        if celula.value == "ALTO GIRO":
            ALTO_GIRO = ALTO_GIRO + 1
        if celula.value == "BAZAR":
            BAZAR = BAZAR + 1
        if celula.value == "DPH":
            DPH = DPH + 1
        if celula.value == "DIVERSOS":
            DIVERSOS = DIVERSOS + 1
        if celula.value == "FLV":
            FLV = FLV + 1
        if celula.value == "LATICINIOS 1":
            LATICINIOS = LATICINIOS + 1
        if celula.value == "LIQUIDA":
            LIQUIDA = LIQUIDA + 1
        if celula.value == "PERECIVEL 1":
            PERECIVEL1 = PERECIVEL1 + 1
        if celula.value == "PERECIVEL 2":
            PERECIVEL2 = PERECIVEL2 + 1
        if celula.value == "PERECIVEL 2 B":
            PERECIVEL2B = PERECIVEL2B + 1
        if celula.value == "PERECIVEL 3":
            PERECIVEL3 = PERECIVEL3 + 1
        if celula.value == "SECA DOCE":
            SECA_DOCE = SECA_DOCE + 1
        if celula.value == "SECA SALGADA":
            SECA_SALGADA = SECA_SALGADA + 1
        if celula.value == "SECA SALGADA 2":
            SECA_SALGADA2 = SECA_SALGADA2 + 1
    def parcial():
        PARCIAL = round(TOTAL/SKU*100,2)
        return str(PARCIAL) + "%"
    PARCIAL = parcial()
    
    return 