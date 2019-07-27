
def calcular_comissao(vendas_mensais, plano_do_vendedor):
    """
    Calcula a comissão do vendedor de acordo com o valor das vendas mensais.
    Caso o valor das vendas mensais seja maior ou igual que o valor mínimo do plano do vendedor, 
    calcula a comissão com base na porcentagem máxima.
    Caso contrário, calcula o valor da comissão com base na porcentagem mínima.
    """
    if vendas_mensais:
        if vendas_mensais >= plano_do_vendedor.valor_minimo:
            return (plano_do_vendedor.percent_max / 100) * vendas_mensais
        else:
            return (plano_do_vendedor.percent_min / 100) * vendas_mensais
