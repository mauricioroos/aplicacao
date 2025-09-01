from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=200,null = True)
    preco = models.DecimalField("preco", decimal_places=2,max_digits = 8)
    quantidade = models.PositiveIntegerField("Quantidade", default=0,null = True)
    def __str__(self):
        return self.nome
    
class Perfil(models.Model):
    cliente = models.OneToOneField(cliente,on_delete= models.CASCADE)
    telefone = models.CharField("telefone", max_legth=20)
    rua = models.CharField("Rua",max_length=200)
    numero = models.PositiveBigIntegerField("Nº",max_length=10)
    cep = models.CharField("CEP",max_length=20)
    bairro = models.CharField("Bairro",max_length=50)
    cidade = models.CharField("Cidade",max_length=50)
    complemento = models.CharField("Complemento",max_length=200)
   
    def __str__(self):
         return f"{self.rua}, {self.numero} - {self.bairro}"

class venda(models.Model):
        data = models.DateTimeField("Data", null= True)
        venda = models.ManyToManyField(
              Produto,
              through='vendaProduto',)

    def __str_(self):
         return str(self.cliente)

class itemVenda(models.Model):
        quantidade = models.IntegerField("Quantidade", null=true)
        itemVenda = models.ForeignKey(
            "venda", on_delete = models.CASCADE, related_name="itemVenda"
            "Produto", on_delete=models.CASCADE, related_name="itemvendaProduto")
    
    def __str__(self):
        return str(self.itemVenda)
        
    

  