industrias_grupo_1 = False
industrias_grupo_2 = False
industrias_grupo_3 = False
indice_poluicao = 0.55

if indice_poluicao >= 0.3:
    industrias_grupo_1 = True
    if indice_poluicao >= 0.4:
        industria_grupo_2 = True
        if indice_poluicao >= 0.5:
            indutrias_grupo_3 = True

if (industrias_grupo_1):
    print("Notificadas industrias do grupo 1")
if (industrias_grupo_2):
    print("Notificadas industrias do grupo 2")
if (industrias_grupo_3):
    print("Notificadas industrias do grupo 3")

