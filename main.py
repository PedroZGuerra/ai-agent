import json
import os
import difflib

class ArcanisTutor:
    DATA_FILE = 'responses.json'

    def __init__(self):
        self.responses = self._load_responses()
        self.context = {'last_topic': None}
        print('Saudacoes, planeswalker! Eu sou Arcanis, o Tutor das Regras de Magic: The Gathering.')
        print('Pergunte qualquer coisa sobre as regras e responderei com sabedoria.')
        print("Digite 'sair' para encerrar.\n")

    def _load_responses(self):
        if not os.path.exists(self.DATA_FILE):
            raise FileNotFoundError(f"Arquivo {self.DATA_FILE} nao encontrado.")
        with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escutar_perguntas(self):
        while True:
            pergunta = input('Sua pergunta: ').lower().strip()
            if pergunta == 'sair':
                print('Encerrando tutor.')
                break
            resposta = self.responder(pergunta)
            print(resposta)

    def responder(self, pergunta):
        # Prioriza correspondencias mais longas (p.ex: termos compostos primeiro)
        kw_resp = []
        for entry in self.responses.values():
            for kw in entry['keywords']:
                kw_resp.append((kw, entry['response']))
        # Ordena por comprimento de keyword decrescente
        kw_resp.sort(key=lambda x: len(x[0]), reverse=True)
        # Tenta match exato
        for kw, resp in kw_resp:
            if kw in pergunta:
                return resp
        # Fallback fuzzy
        all_keys = [kw for entry in self.responses.values() for kw in entry['keywords']]
        match = difflib.get_close_matches(pergunta, all_keys, n=1, cutoff=0.6)
        if match:
            # encontra qual resposta corresponde
            for entry in self.responses.values():
                if match[0] in entry['keywords']:
                    return entry['response']
        # fallback genérico
        return 'Hmm... Nao conheco esse termo.'

if __name__ == '__main__':
    tutor = ArcanisTutor()
    tutor.escutar_perguntas()
