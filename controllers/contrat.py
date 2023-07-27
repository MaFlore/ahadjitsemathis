def liste_contrats():
    rows = db().select(db.contrat.ALL)
    return response.render('contrat/liste_contrats.html', dict(contrats=rows))

def ajout_contrat():
    qualification = db().select(db.qualification.ALL)
    if request.method == 'POST':
        db.contrat.insert(
            description = request.vars.description,
            date_debut = request.vars.date_debut,
            nombre_employe = request.vars.nombre_employe,
            qualification = request.vars.qualification
        )
        print(request.vars.qualification)
        redirect(URL('contrat', 'liste_contrats'))
    return response.render('contrat/ajout_contrat.html', dict(qualifications=qualification))

def modifier_contrat():
    id = request.vars.id
    qualification = db().select(db.qualification.ALL)
    contrat = db(db.contrat.id == id).select().first()
    if request.method == 'POST':
        db(db.contrat.id == id).update(
            description = request.vars.description,
            date_debut = request.vars.date_debut,
            nombre_employe = request.vars.nombre_employe,
            qualification = request.vars.qualification
        )
        redirect(URL('contrat', 'liste_contrats'))
    return response.render('contrat/modifier_contrat.html', dict(donne=contrat, qualifications=qualification))

def supprimer_contrat():
    id = request.vars.id
    db(db.contrats.id == id).delete()
    redirect(URL('contrat', 'liste_contrats'))