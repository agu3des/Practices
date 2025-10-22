from django import forms
from .models import Editora, Autor, Livro, Publica

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']

class LivroForm(forms.ModelForm):
    autores = forms.ModelMultipleChoiceField(
        queryset=Autor.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Livro
        fields = ['ISBN', 'titulo', 'publicacao', 'preco', 'estoque', 'editora', 'autores']

    def save(self, commit=True):
        # salva o livro e sincroniza a tabela through Publica
        livro = super().save(commit=commit)
        if commit:
            # sincroniza Publica: remove existentes e recria conforme seleção
            Publica.objects.filter(livro=livro).delete()
            for autor in self.cleaned_data.get('autores', []):
                Publica.objects.create(livro=livro, autor=autor)
        return livro

class PublicaForm(forms.ModelForm):
    class Meta:
        model = Publica
        fields = ['livro', 'autor']