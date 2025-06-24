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
        if "turno" in pergunta or "turn" in pergunta:
            return (
                "Cada turno (turn) é dividido em fases: Desvirar (Untap), Manutenção (Upkeep), Compra (Draw), Fase Principal 1 (Main Phase 1), Combate (Combat), Fase Principal 2 (Main Phase 2) e Encerramento (End)."
            )
        elif "mana" in pergunta:
            return (
                "Mana é a energia usada para conjurar magias. Existem 5 cores (Branco/White, Azul/Blue, Preto/Black, Vermelho/Red e Verde/Green) e mana incolor (Colorless)."
            )
        elif "pilha" in pergunta or "stack" in pergunta:
            return (
                "A pilha (stack) é onde as mágicas e habilidades esperam para resolver. Funciona como LIFO: o último a entrar, primeiro a sair."
            )
        elif "voar" in pergunta or "flying" in pergunta:
            return (
                "Voar (Flying) é uma habilidade de evasão. Criaturas com voar só podem ser bloqueadas por criaturas com voar ou alcance (reach)."
            )
        elif "alcance" in pergunta or "reach" in pergunta:
            return (
                "Alcance (Reach) permite que a criatura bloqueie criaturas com voar (Flying)."
            )
        elif "vigilancia" in pergunta or "vigilance" in pergunta:
            return (
                "Vigilância (Vigilance) faz com que a criatura não vire ao atacar, permitindo usá-la também para bloquear no turno adversário."
            )
        elif "flash" in pergunta:
            return (
                "Flash permite que você jogue a mágica como se fosse uma instantânea, em qualquer momento em que você poderia jogar um instant."
            )
        elif "impeto" in pergunta or "ímpeto" in pergunta or "haste" in pergunta:
            return (
                "Ímpeto (Haste) faz com que a criatura ignore enjoo de invocação (summoning sickness) e possa atacar ou usar habilidades viradas no mesmo turno em que entrou em jogo."
            )
        elif "iniciativa" in pergunta or "first strike" in pergunta:
            return (
                "Iniciativa (First Strike) permite que a criatura cause dano na etapa de dano prévia, antes das sem First Strike resolverem."
            )

        elif "golpe duplo" in pergunta or "double strike" in pergunta:
            return (
                "Golpe Duplo (Double Strike) faz a criatura causar dano tanto na etapa de First Strike quanto na etapa normal de dano."
            )
        elif "toque mortifero" in pergunta or "toque mortífero" in pergunta or "deathtouch" in pergunta:
            return (
                "Toque Mortífero (Deathtouch) faz com que qualquer quantidade de dano causado destrua criaturas, independentemente da resistência delas."
            )
        elif "lifelink" in pergunta or "ganho de vida" in pergunta or "vida" in pergunta:
            return (
                "Lifelink faz com que o controlador ganhe vida igual ao dano causado pela criatura ou fonte."
            )
        elif "atropelar" in pergunta or "trample" in pergunta:
            return (
                "Atropelar (Trample) permite que o dano excedente de uma criatura bloqueada seja atribuído ao jogador ou planeswalker defensor."
            )
        elif "protecao" in pergunta or "proteção" in pergunta or "protection" in pergunta:
            return (
                "Proteção (Protection) de [qualquer coisa] previne que a criatura receba dano, seja alvo, bloqueada ou encantada por permanentes daquela qualidade."
            )
        elif "hexproof" in pergunta or "hex proof" in pergunta:
            return (
                "Hexproof impede que a criatura ou jogador seja alvo de mágicas ou habilidades controladas por oponentes."
            )
        elif "indestrutivel" in pergunta or "indestrutível" in pergunta or "indestructible" in pergunta:
            return (
                "Indestrutível (Indestructible) faz com que a criatura não seja destruída por dano ou efeitos que digam 'destroy'."
            )
        elif "artefato" in pergunta or "artifact" in pergunta:
            return (
                "Artefatos (Artifacts) são permanentes incolores com diversos efeitos. Equipamentos (Equipment) são artefatos que podem ser anexados a criaturas."
            )
        elif "encantamento" in pergunta or "enchantment" in pergunta:
            return (
                "Encantamentos (Enchantments) são permanentes que fornecem efeitos contínuos. Auras (subtipo) se anexam a permanentes específicas."
            )
        elif "equipamento" in pergunta or "equipment" in pergunta:
            return (
                "Equipamento (Equipment) é um artefato que pode ser anexado a uma criatura para dar habilidades ou bônus."
            )
        elif "sorcery" in pergunta or "feitiço" in pergunta or "instant" in pergunta or "instantânea" in pergunta:
            return (
                "Feitiços (Sorceries) só podem ser jogados em fases principais quando a pilha está vazia. Instants (Instantâneas) podem ser jogados a qualquer momento."
            )
        elif "veneno" in pergunta or "poison" in pergunta or "toxic" in pergunta:
            return (
                "Toxic adiciona marcadores de veneno (poison counters) a jogadores; ao chegar a 10, você perde o jogo."
            )
        elif "mulligan" in pergunta:
            return (
                "No mulligan de Londres (London Mulligan), você compra 7 cartas e devolve cartas ao grimório igual ao número de mulligans feitos."
            )
        elif "commander" in pergunta:
            return (
                "Commander é um formato multiplayer com deck de 100 cartas, sem repetições, liderado por um comandante na zona de comando."
            )
        elif "planeswalker" in pergunta:
            return (
                "Planeswalkers entram com marcadores de lealdade. Você pode ativar apenas uma habilidade de lealdade por turno."
            )
        elif "compra" in pergunta or "draw" in pergunta:
            return (
                "Na fase de compra (Draw), você compra uma carta do seu grimório. Algumas habilidades modificam essa ação."
            )
        elif "marcador" in pergunta or "counter" in pergunta:
            return (
                "Marcadores (Counters) podem modificar atributos de permanentes ou representar contadores de veneno, +1/+1 ou outros efeitos."
            )
        elif "ficha" in pergunta or "token" in pergunta:
            return (
                "Fichas (Tokens) são permanentes criados por efeitos de mágicas ou habilidades, geralmente criaturas sem card propriamente dito."
            )
        elif "ativada" in pergunta or "activated ability" in pergunta:
            return (
                "Habilidades Ativadas são representadas por 'Custo: Efeito' e podem ser ativadas quando você tiver prioridade e puder pagar o custo."
            )
        elif "disparada" in pergunta or "triggered ability" in pergunta:
            return (
                "Habilidades Disparadas começam com 'Quando', 'Sempre que' ou 'Toda vez que' e se resolvem automaticamente ao cumprir a condição."
            )
        else:
            return "Hmm... Essa é uma questão arcana! Ainda não tenho resposta preparada. Reformule ou seja mais específico."

if __name__ == "__main__":
    arcanis = ArcanisTutor()
    arcanis.escutar_perguntas()
