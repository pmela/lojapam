from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=128, )
    data_nascimento = models.DateField(max_length=8, null=True)
    email = models.EmailField(max_length=64, unique=True)
    cpf = models.CharField(max_length=16, unique=True, null=True)
    senha = models.CharField(max_length=32)
    telefone = models.ForeignKey('Telefone', on_delete=models.PROTECT, null=True)
    endereco = models.ForeignKey('Endereco', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    cep = models.CharField(max_length=16)
    logradouro = models.CharField(max_length=256)
    numero = models.CharField(max_length=8)
    complemento = models.CharField(max_length=32)
    bairro = models.CharField(max_length=64)
    cidade = models.CharField(max_length=64)
    estado = models.CharField(max_length=64)

    def __str__(self):
        return self.logradouro + ' ' + self.cep


class Telefone(models.Model):
    numero_celular = models.CharField(max_length=16)

    def __str__(self):
        return self.numero_celular


class Cartao(models.Model):
    numero_cartao = models.CharField(max_length=32)
    data_vencimento = models.CharField(max_length=16)
    cod_de_verificacao = models.CharField(max_length=16)
    cpf_titular = models.CharField(max_length=16)
    nome_titular = models.CharField(max_length=32)
    usuario = models.ForeignKey('Usuario', on_delete=models.PROTECT)

    def __str__(self):
        return self.numero_cartao


class Categoria(models.Model):
    nome = models.CharField(max_length=32)

    def __str__(self):
        return self.nome


class Estoque(models.Model):
    nome = models.CharField(max_length=64)
    quantidade = models.CharField(max_length=32)
    cor = models.CharField(max_length=16)
    tamanho = models.CharField(max_length=16)
    marca = models.CharField(max_length=32)
    material = models.CharField(max_length=32)
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)

    def __str__(self):
        return self.quantidade


class Produto(models.Model):
    nome = models.CharField(max_length=64)
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT)
    imagem = models.FileField(upload_to='fotos/')
    estoque: [Estoque]
    valor= models.FloatField()

    def __str__(self):
        return self.nome


class Venda(models.Model):
    produto_vendido = models.CharField(max_length=32)
    data_venda = models.DateField(max_length=8)
    hora_venda = models.TimeField(max_length=8)
    produto = models.ForeignKey('Produto', on_delete=models.PROTECT)

    def __str__(self):
        return self.produto_vendido
