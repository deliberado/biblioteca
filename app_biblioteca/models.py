from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField(max_length=15)
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    edicao = models.CharField(max_length=50)
    editora = models.CharField(max_length=150)
    ano_publicacao = models.IntegerField()
    categoria = models.ManyToManyField(Categoria)
    autor = models.CharField(max_length=150)
    tipo = models.BooleanField('É digital?', default=False)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    pessoa = models.ForeignKey(Pessoa, related_name='pessoas', null=True, blank=True, on_delete=models.SET_NULL)
    livro = models.ForeignKey(Livro, null=True, blank=True, on_delete=models.SET_NULL)
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_estimada_devolucao = models.DateField()
    data_efetiva_devolucao = models.DateTimeField(null=True, blank=True)
    funcionario = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} pegou livro {} no dia {} e deverá devolver na data {}'.format(self.pessoa.nome, self.livro.titulo, self.data_emprestimo.strftime("%d/%m/%y"), self.data_estimada_devolucao.strftime("%d/%m/%y"))