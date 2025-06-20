class ArcanisTutor:
    def __init__(self):
        print("🧙‍♂️ Saudações, planeswalker! Eu sou Arcanis, o Tutor das Regras de Magic: The Gathering.")
        print("Pergunte-me qualquer coisa sobre as regras, e eu responderei com sabedoria!")
        print("Digite 'sair' para encerrar.\n")

    def escutar_perguntas(self):
        while True:
            pergunta = input("❓ Sua pergunta: ").lower().strip()
            if pergunta == "sair":
                print("Que a sabedoria de Dominária te acompanhe!")
                break
            resposta = self.responder(pergunta)
            print("\n📜 Arcanis responde:")
            print(resposta + "\n")

    def responder(self, pergunta):
        # Palavras-chave simples para análise da pergunta
        if "turno" in pergunta:
            return (
                "Cada turno é dividido em fases: Desvirar, Manutenção, Compra, Fase Principal 1, "
                "Combate, Fase Principal 2 e Encerramento. A maioria das mágicas só pode ser jogada nas fases principais."
            )
        elif "mana" in pergunta:
            return (
                "Mana é a energia usada para conjurar magias. Existem 5 cores (Branco, Azul, Preto, Vermelho e Verde) "
                "e mana incolor. Os terrenos são a principal fonte de mana."
            )
        elif "pilha" in pergunta or "stack" in pergunta:
            return (
                "A pilha é onde as mágicas e habilidades esperam para resolver. Funciona no estilo LIFO: o último a entrar, primeiro a sair. "
                "Você pode responder a mágicas antes que elas resolvam usando instants ou habilidades ativadas."
            )
        elif "voar" in pergunta:
            return (
                "Voar é uma habilidade de evasão. Criaturas com voar só podem ser bloqueadas por outras criaturas com voar ou alcance (reach)."
            )
        elif "mulligan" in pergunta:
            return (
                "No mulligan de Londres, você embaralha sua mão e compra 7 cartas. Depois, para cada mulligan que fizer, "
                "você devolve uma carta ao fundo do grimório no final. Ex: 1 mulligan = 7 cartas, escolha 1 para devolver."
            )
        elif "atacar" in pergunta:
            return (
                "Somente criaturas que você controla e que não tenham 'enjoo de invocação' (ou tenham ímpeto) podem atacar. "
                "Você declara atacantes, o oponente declara bloqueadores, e o dano é atribuído."
            )
        elif "commander" in pergunta:
            return (
                "Commander é um formato casual onde cada jogador usa um baralho de 100 cartas sem repetição, liderado por um comandante. "
                "Você começa com 40 de vida e pode conjurar seu comandante da zona de comando pagando o custo adicional de +2 para cada vez anterior que ele foi conjurado."
            )
        elif "planeswalker" in pergunta:
            return (
                "Planeswalkers são aliados poderosos que entram com marcadores de lealdade. Você pode ativar uma habilidade por turno, "
                "aumentando ou diminuindo a lealdade conforme o custo indicado. O oponente pode atacá-los diretamente."
            )
        elif "feitiço" in pergunta or "instantânea" in pergunta:
            return (
                "Feitiços (sorceries) só podem ser jogados na sua fase principal e quando a pilha estiver vazia. "
                "Mágicas instantâneas (instants) podem ser jogadas a qualquer momento, até durante o turno do oponente."
            )
        elif "vida" in pergunta:
            return (
                "Cada jogador começa com 20 de vida (ou 40 no Commander). Se sua vida chegar a 0 ou menos, você perde. "
                "Alguns efeitos podem causar dano direto, e outros aumentam sua vida."
            )
        else:
            return "Hmm... Essa é uma questão arcana! Ainda não tenho resposta preparada. Reformule ou seja mais específico."

# Execução do assistente
if __name__ == "__main__":
    arcanis = ArcanisTutor()
    arcanis.escutar_perguntas()
