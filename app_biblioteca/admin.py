from django.contrib import admin
from .models import Pessoa, Funcionario, Livro, Categoria, Emprestimo


admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Livro)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
