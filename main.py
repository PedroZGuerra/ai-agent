import json
import os
import difflib

class ArcanisTutor:
    DATA_FILE = 'responses.json'

    def __init__(self):
        self.responses = self._load_responses()
        print('Saudações, planeswalker! Eu sou Arcanis, o Tutor das Regras de Magic: The Gathering.')
        print('Pergunte qualquer coisa sobre as regras e responderei com sabedoria.')
        print("Digite 'sair' para encerrar ou 'ajuda' para ver tópicos disponíveis.\n")

    def _load_responses(self):
        if not os.path.exists(self.DATA_FILE):
            raise FileNotFoundError(f"Arquivo {self.DATA_FILE} não encontrado.")
        with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escutar_perguntas(self):
        while True:
            pergunta = input('> ').lower().strip()
            if pergunta == 'sair':
                print('Encerrando tutor. Que a sabedoria te acompanhe!')
                break
            if pergunta == 'ajuda':
                self._mostrar_topicos()
                continue

            resposta = self.responder(pergunta)
            print(f"\n{resposta}\n")

            # pergunta interativa de continuação
            continuar = input('Deseja saber sobre outro tópico? (s/n): ').lower().strip()
            if continuar != 's':
                print('Até breve, planeswalker!')
                break

    def responder(self, pergunta):
        # Prioriza correspondências mais longas
        kw_resp = []
        for entry in self.responses.values():
            for kw in entry['keywords']:
                kw_resp.append((kw, entry['response']))
        kw_resp.sort(key=lambda x: len(x[0]), reverse=True)

        for kw, resp in kw_resp:
            if kw in pergunta:
                return resp

        # Fallback fuzzy
        all_keys = [kw for entry in self.responses.values() for kw in entry['keywords']]
        match = difflib.get_close_matches(pergunta, all_keys, n=1, cutoff=0.6)
        if match:
            for entry in self.responses.values():
                if match[0] in entry['keywords']:
                    return entry['response']

        return 'Hmm... Não conheço esse termo. Digite "ajuda" para ver tópicos disponíveis.'

    def _mostrar_topicos(self):
        topicos = [f"- {key}" for key in sorted(self.responses.keys())]
        print('\nTópicos disponíveis:')
        print('\n'.join(topicos))
        print()

if __name__ == '__main__':
    tutor = ArcanisTutor()
    tutor.escutar_perguntas()
