def liste_clients():
    rows = db().select(db.client.ALL);
    return response.render('client/liste_clients.html', dict(clients=rows))

def ajout_client():
    if request.method == 'POST':
        db.client.insert(
            nom = request.vars.nom,
            prenom = request.vars.prenom,
            adresse = request.vars.adresse,
            email = request.vars.email,
            telephone = request.vars.telephone
        )
        redirect(URL('client', 'liste_clients'))
    return response.render('client/ajout_client.html')

def modifier_client():
    id = request.vars.id
    client = db(db.client.id == id).select().first()
    if request.method == 'POST':
        db(db.client.id == id).update(
            nom = request.vars.nom,
            prenom = request.vars.prenom,
            adresse = request.vars.adresse,
            email = request.vars.email,
            telephone = request.vars.telephone
        )
        redirect(URL('client', 'liste_clients'))
    return response.render('client/modifier_client.html', dict(donne=client))

def supprimer_client():
    id = request.vars.id
    db(db.client.id == id).delete()
    redirect(URL('client', 'liste_clients'))