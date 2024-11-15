def mostrar_grafico_area_pesquisa():
    areas = [cientista[1] for cientista in dados_cientistas[1:]]
    plt.hist(areas, bins=len(set(areas)))
    plt.xlabel("Área de Pesquisa")
    plt.ylabel("Número de Cientistas")
    plt.title("Distribuição das Áreas de Pesquisa")
    plt.show()
