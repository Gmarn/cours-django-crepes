#-*- coding: utf-8 -*-
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Article

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

# Il faut ajouter l'import get_object_or_404, attention !
def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})

#from blog.forms import ContactForm
#
#def contact(request):
#    if request.method == 'POST':  # S'il s'agit d'une requête POST
#        form = ContactForm(request.POST)  # Nous reprenons les données
#
#        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
#
#            # Ici nous pouvons traiter les données du formulaire
#            sujet = form.cleaned_data['sujet']
#            message = form.cleaned_data['message']
#            envoyeur = form.cleaned_data['envoyeur']
#            renvoi = form.cleaned_data['renvoi']
#
#            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
#
#            envoi = True
#
#    else: # Si ce n'est pas du POST, c'est probablement une requête GET
#        form = ContactForm()  # Nous créons un formulaire vide
#
#    return render(request, 'blog/contact.html', locals())


#from blog.forms import ArticleForm
#
#def contact(request):
#    if request.method == 'POST':  # S'il s'agit d'une requête POST
#        form = ArticleForm(request.POST)  # Nous reprenons les données
#		
#        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
#
#            # Ici nous pouvons traiter les données du formulaire
#            titre = form.cleaned_data['titre']
#            auteur = form.cleaned_data['auteur']
#            slug = form.cleaned_data['slug']
#            contenu = form.cleaned_data['contenu']
#            categorie = form.cleaned_data['categorie']
#            form.save()
#            # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer
#
#            envoi = True
#
#    else: # Si ce n'est pas du POST, c'est probablement une requête GET
#        form = ArticleForm()  # Nous créons un formulaire vide
#
#    return render(request, 'blog/contact.html', locals())

from blog.forms import NouveauContactForm
from blog.models import Contact

def contact(request):
    sauvegarde = False

    if request.method == "POST":
        form = NouveauContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = Contact()
            contact.nom = form.cleaned_data["nom"]
            contact.adresse = form.cleaned_data["adresse"]
            contact.photo = form.cleaned_data["photo"]
            contact.save()

            sauvegarde = True
    else:
        form = NouveauContactForm()

    return render(request, 'blog/contact.html', locals())

def voir_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'blog/voir_contacts.html', {'contacts': contacts})


