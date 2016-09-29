#from django import forms
#
#class ContactForm(forms.Form):
#    def clean(self):
#        cleaned_data = super(ContactForm, self).clean()
#        sujet = cleaned_data.get('sujet')
#        message = cleaned_data.get('message')
#    
#        if sujet and message:  # Est-ce que sujet et message sont valides ?
#            if "pizza" in sujet and "pizza" in message:
#                msg = "Vous parlez déjà de pizzas dans le sujet, n'en parlez plus dans le message !"
#                self.add_error("message", msg)
#    
#        return cleaned_data  # N'oublions pas de renvoyer les données si tout est OK
#
#    sujet = forms.CharField(max_length=100)
#    message = forms.CharField(widget=forms.Textarea)
#    envoyeur = forms.EmailField(label="Votre adresse mail")
#    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)

from django import forms
#from blog.models import Article

#class ArticleForm(forms.ModelForm):
#    class Meta:
#        model = Article
#        #exclude = ('auteur','categorie','slug')
#        fields = ('auteur', 'contenu')

class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()
