def liste_employes():
    rows = db().select(db.employe.ALL);
    return response.render('employe/liste_employes.html', dict(employes=rows))

def ajout_employe():
    if request.method == 'POST':
        db.employe.insert(
            nom = request.vars.nom,
            prenom = request.vars.prenom,
            adresse = request.vars.adresse,
            email = request.vars.email,
            telephone = request.vars.telephone
        )
        redirect(URL('employe', 'liste_employes'))
    return response.render('employe/ajout_employe.html')

def modifier_employe():
    id = request.vars.id
    employe = db(db.employe.id == id).select().first()
    if request.method == 'POST':
        db(db.employe.id == id).update(
            nom = request.vars.nom,
            prenom = request.vars.prenom,
            adresse = request.vars.adresse,
            email = request.vars.email,
            telephone = request.vars.telephone
        )
        redirect(URL('employe', 'liste_employes'))
    return response.render('employe/modifier_employe.html', dict(donne=employe))

def supprimer_employe():
    id = request.vars.id
    db(db.employe.id == id).delete()
    redirect(URL('employe', 'liste_employes'))