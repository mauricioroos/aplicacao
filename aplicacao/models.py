from django.db import models

class Produto(models.Model):
    nome = models.CharField("Nome", max_length=200,null = True)
    preco = models.DecimalField("preco", decimal_places=2,max_digits = 8)
    quantidade = models.PositiveIntegerField("Quantidade", default=0,null = True)

    def __str__(self):
        return self.nome
    
class cliente(models.Model):
    nome = models.CharField("Nome", max_length=200,null = True)
    email = models.DecimalField("email", decimal_places=2,max_digits = 8)
    
class PerfilCliente(models.Model):
    endereco = models.CharField("endereco", max_length=200,null = True)
    telefone = models.DecimalField("telefone", decimal_places=2,max_digits = 8)

class PerfilCliente(models.Model):
    endereco = models.CharField("endereco", max_length=200,null = True)
    telefone = models.DecimalField("telefone", decimal_places=2,max_digits = 8)
    
class venda(models.Model):
        data = models.DateTimeField("Data", null= True)

class itemVenda(models.Model):
        quantidade = models.IntegerField("Quantidade", null=true)
        itemVenda = models.ForeignKey(
            "venda", on_delete=models.CASCADE, related_name"itemVenda"
            "Produto", on_delete=models 
        )
        
    

  