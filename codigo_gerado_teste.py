def calcular_saldos(transacoes):
    saldos = {}

    for t in transacoes:
        cliente = t["cliente"]
        tipo = t["tipo"]
        valor = t["valor"]

        if cliente not in saldos:
            saldos[cliente] = 0.0

        if tipo == "entrada":
            saldos[cliente] += valor
        elif tipo == "saida":
            saldos[cliente] -= valor

    return saldos
