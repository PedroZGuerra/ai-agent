import json
import os
import difflib
import random

class ArcanisTutor:
    DATA_FILE = 'responses.json'

    def __init__(self):
        self.responses = self._load_responses()
        self.templates = self.responses.pop("templates", [
            "Claro, aqui está o que você precisa saber sobre {topic}:",
            "Deixe-me explicar o conceito de {topic}:",
            "Veja uma explicação sobre {topic}:",
            "Entendido! Aqui vai sobre {topic}:"
        ])
        print("✨🧙‍♂️ Saudações, planeswalker! Eu sou *Arcanis*, o Tutor das Regras de *Magic: The Gathering*.")
        print("📜 Pergunte qualquer coisa sobre as regras e responderei com sabedoria ancestral.")
        print("💬 Digite 'sair' para encerrar ou 'ajuda' para ver tópicos disponíveis.\n")

    def _load_responses(self):
        if not os.path.exists(self.DATA_FILE):
            raise FileNotFoundError(f"Arquivo {self.DATA_FILE} não encontrado.")
        with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

    def escutar_perguntas(self):
        while True:
            pergunta = input('🔮> ').lower().strip()
            if pergunta == 'sair':
                print('🛡️ Encerrando tutor. Que a sabedoria te acompanhe em suas partidas!')
                break
            if pergunta == 'ajuda':
                self._mostrar_topicos()
                continue
            resposta = self.responder(pergunta)
            print(f"\n{resposta}\n")

    def responder(self, pergunta):
        detected = set()
        simple_keys = {k: v for k, v in self.responses.items() if '_' not in k}
        composite_keys = {k: v for k, v in self.responses.items() if '_' in k}

        for key, entry in simple_keys.items():
            if any(kw in pergunta for kw in entry['keywords']):
                detected.add(key)

        if len(detected) >= 2:
            for comp_key, entry in composite_keys.items():
                parts = comp_key.split('_')
                if all(part in detected for part in parts):
                    return self._resposta_com_template(comp_key, entry['response'])

        kw_resp = []
        for key, entry in self.responses.items():
            for kw in entry['keywords']:
                kw_resp.append((kw, entry['response'], key))
        kw_resp.sort(key=lambda x: len(x[0]), reverse=True)

        for kw, resp, topic in kw_resp:
            if kw in pergunta:
                return self._resposta_com_template(topic, resp)

        all_keys = [kw for entry in self.responses.values() for kw in entry['keywords']]
        match = difflib.get_close_matches(pergunta, all_keys, n=1, cutoff=0.6)
        if match:
            for key, entry in self.responses.items():
                if match[0] in entry['keywords']:
                    return self._resposta_com_template(key, entry['response'])

        return 'Hmm... Não conheço esse termo. Digite "ajuda" para ver tópicos disponíveis.'

    def _resposta_com_template(self, topic, resp):
        template = random.choice(self.templates)
        introducao = template.format(topic=topic.replace('_', ' '))
        return f"{introducao}\n{resp}"

    def _mostrar_topicos(self):
        topicos = sorted(self.responses.keys())
        print('\nTópicos disponíveis:')
        for t in topicos:
            print('-', t)
        print()

if __name__ == '__main__':
    tutor = ArcanisTutor()
    tutor.escutar_perguntas()
