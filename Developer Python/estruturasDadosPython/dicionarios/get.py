contatos = {"silas_vieira@outlook.com":{"nome": "Silas VIeira", "telefone": "(11)9 8237-0570"}}

#contatos["chave"]

print(contatos.get("chave"))
print(contatos.get("chave", {}))
print(contatos.get("silas_vieira@outlook.com", {}))