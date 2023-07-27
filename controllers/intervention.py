def liste_interventions():
    rows = db().select(db.intervention.ALL)
    return response.render('intervention/liste_interventions.html', dict(interventions=rows))

def ajout_intervention():
    contrats = db().select(db.contrat.ALL)
    if request.method == 'POST':
        db.intervention.insert(
            contrat = request.vars.contrat,
            date_intervention = request.vars.date_intervention,
            date_fin = request.vars.date_fin,
        )
        print(request.vars.contrat)
        redirect(URL('intervention', 'liste_interventions'))
    return response.render('intervention/ajout_intervention.html', dict(contrats=contrats))

def modifier_intervention():
    id = request.vars.id
    contrats = db().select(db.contrat.ALL)
    intervention = db(db.intervention.id == id).select().first()
    if request.method == 'POST':
        db(db.intervention.id == id).update(
            contrat = request.vars.contrat,
            date_intervention = request.vars.date_intervention,
            date_fin = request.vars.date_fin,
        )
        redirect(URL('intervention', 'liste_interventions'))
    return response.render('intervention/modifier_intervention.html', dict(donne=intervention, contrats=contrats))

def supprimer_intervention():
    id = request.vars.id
    db(db.intervention.id == id).delete()
    redirect(URL('intervention', 'liste_interventions'))
