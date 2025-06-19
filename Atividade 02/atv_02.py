nomeProduto = "Camiseta";
precoOriginal = 50;
porcentagemDesconto = 0.20;

desconto = precoOriginal * porcentagemDesconto;
valorFinal = precoOriginal - desconto;

print(f"O valor do desconto é de R${desconto:.2f} e o total a pagar é R${valorFinal:.2f}")

