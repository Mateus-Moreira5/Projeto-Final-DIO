def converter_moeda(valor, taxa):
    return valor * taxa

valor_libra = float(input("Coloque o valor da moeda em libra: "))
valor_real = float(input("Coloque o valor da moeda em real: "))

taxa_libra_para_dolar = 1.35  # 1 GBP = 1.35 USD
taxa_real_para_dolar = 0.19   # 1 BRL = 0.19 USD

valor_em_dolar_de_libra = converter_moeda(valor_libra, taxa_libra_para_dolar)
valor_em_dolar_de_real = converter_moeda(valor_real, taxa_real_para_dolar)

print(f"O valor da moeda em libra convertido para dólar é: {valor_em_dolar_de_libra}")
print(f"O valor da moeda em real convertido para dólar é: {valor_em_dolar_de_real}")