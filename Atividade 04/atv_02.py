def calcular_media_turma():
  
    notas = []
    print("Digite as notas dos alunos (de 0 a 10). Digite 'fim' para terminar.")

    while True:
        entrada = input("Nota: ").lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada) 

            if 0 <= nota <= 10: 
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, digite um número entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\n--- Resultado ---")
        print(f"Notas registradas: {notas}")
        print(f"Número total de notas válidas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("\nNenhuma nota válida foi registrada.")

calcular_media_turma()