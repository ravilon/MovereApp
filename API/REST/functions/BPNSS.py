import json
from REST import database
from fuzzy_methods import fuzzy

def calculate(params):
    factorid = params.get('factorid')
    userid = params.get('userid')
    
    db = database.get_db()
    
    # case factorid
    if factorid == "Autonomia":
        return autonomia(userid, db, factorid)
    elif factorid == "Competencia":
        return competencia(userid, db, factorid)
    elif factorid == "Afinidade":
        return afinidade(userid, db, factorid)
    else:
        return "Invalid factorid"
    
def getBPNSSFactorMap():
    # Correct file path
    with open('API/REST/mapBPNSS.json') as json_file:
        data = json.load(json_file)
    return data['factor']

def autonomia(userid, database, factorid):
    mapBPNSS = getBPNSSFactorMap()
    collection = mapBPNSS[factorid]['collection']
    fields = mapBPNSS[factorid]['columns']
    
    doc_ref = database.collection(collection).document(userid)
    doc = doc_ref.get()
    
    if doc.exists:
        autonomia = doc.to_dict()
    else:
        autonomia = {}

    soma = sum(autonomia.get(field, 0) for field in fields) / len(fields)
    
    autonomiaFuzzy = fuzzy.calcfuzzy(soma, 1, 6)
    maiorAutonomiaFuzzy = max(autonomiaFuzzy)        
    for i in range(len(autonomiaFuzzy)):
        if autonomiaFuzzy[i] == maiorAutonomiaFuzzy:
            autonomiaFuzzy[i] = 1
        else:
            autonomiaFuzzy[i] = 0
    return autonomiaFuzzy

def competencia(userid, database, factorid):
    mapBPNSS = getBPNSSFactorMap()
    collection = mapBPNSS[factorid]['collection']
    fields = mapBPNSS[factorid]['columns']
    
    doc_ref = database.collection(collection).document(userid)
    doc = doc_ref.get()
    
    if doc.exists:
        competencia = doc.to_dict()
    else:
        competencia = {}
    
    soma = sum(competencia.get(field, 0) for field in fields) / len(fields)
    competenciaFuzzy = fuzzy.calcfuzzy(soma, 1, 6)
    maiorCompetenciaFuzzy = max(competenciaFuzzy)        
    
    for i in range(len(competenciaFuzzy)):
        if competenciaFuzzy[i] == maiorCompetenciaFuzzy:
            competenciaFuzzy[i] = 1
        else:
            competenciaFuzzy[i] = 0
            
    return competenciaFuzzy

def afinidade(userid, database, factorid):
    mapBPNSS = getBPNSSFactorMap()
    collection = mapBPNSS[factorid]['collection']
    fields = mapBPNSS[factorid]['columns']
    
    doc_ref = database.collection(collection).document(userid)
    doc = doc_ref.get()
    
    if doc.exists:
        afinidade = doc.to_dict()
    else:
        afinidade = {}
    
    soma = sum(afinidade.get(field, 0) for field in fields) / len(fields)
    
    afinidadeFuzzy = fuzzy.calcfuzzy(soma, 1, 6)
    maior_afinidadeFuzzy = max(afinidadeFuzzy)        
    for i in range(len(afinidadeFuzzy)):
        if afinidadeFuzzy[i] == maior_afinidadeFuzzy:
            afinidadeFuzzy[i] = 1
        else:
            afinidadeFuzzy[i] = 0
    return afinidadeFuzzy

#print(calculomotivacao(bnpss(2), autonomia(2), competencia(2), afinidade(2)))