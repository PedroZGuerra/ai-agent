import requests

def buscar_carta(nome):
    url = f"https://api.scryfall.com/cards/named?fuzzy={nome}"
    resp = requests.get(url)
    if resp.status_code == 200:
        dados = resp.json()
        return {
            'nome': dados['name'],
            'preco': float(dados['prices']['usd'] or 0),
            'texto': dados.get('oracle_text', '').lower(),
            'tipo': dados.get('type_line', ''),
            'cores': dados.get('colors', []),
            'cmc': int(dados.get('cmc', 0)),
        }
    return None

# Configuração de cada efeito: padrões de detecção, padrões de busca e filtro de tipo
EFEITOS_CONFIG = [
    {
        "name": "discard chosen card",
        "detect_patterns": ["target opponent reveals their hand", "you choose a nonland card", "that player discards"],
        "search_patterns": ["target opponent reveals their hand", "you choose a nonland card", "that player discards that card"],
        "type_filter": "type:instant or type:sorcery",
        "require_all": True
    },
    {
        "name": "counter spell",
        "detect_patterns": ["counter target spell"],
        "search_patterns": ["counter target spell"],
        "type_filter": "type:instant",
        "require_all": False
    },
    {
        "name": "draw card",
        "detect_patterns": ["draw two cards", "draw a card"],
        "search_patterns": ["draw two cards", "draw a card"],
        "type_filter": "type:instant or type:sorcery",
        "require_all": False
    },
    {
        "name": "burn",
        "detect_patterns": ["deals 3 damage to any target", "deals 2 damage to any target", "deal damage to any target"],
        "search_patterns": ["deals 3 damage to any target", "deals 2 damage to any target", "deal damage to any target"],
        "type_filter": "type:instant or type:sorcery",
        "require_all": False
    },
    {
        "name": "destroy creature",
        "detect_patterns": ["destroy target creature"],
        "search_patterns": ["destroy target creature"],
        "type_filter": "type:instant or type:sorcery",
        "require_all": False
    },
    {
        "name": "buff (+power/toughness)",
        "detect_patterns": ["gets +", "put a +1/+1 counter"],
        "search_patterns": ["gets +", "put a +1/+1 counter"],
        "type_filter": "type:instant or type:enchantment or type:sorcery",
        "require_all": False
    },
    {
        "name": "create token",
        "detect_patterns": ["create a 1/1", "create two", "create x"],
        "search_patterns": ["create a 1/1", "create two", "create x"],
        "type_filter": "type:instant or type:sorcery or type:creature or type:enchantment",
        "require_all": False
    },
]

def identificar_efeito_central(texto):
    for cfg in EFEITOS_CONFIG:
        if cfg["require_all"]:
            if all(p in texto for p in cfg["detect_patterns"]):
                return cfg
        else:
            if any(p in texto for p in cfg["detect_patterns"]):
                return cfg
    return None

def buscar_similares_otimizado(carta_base, cfg):
    if not cfg:
        return []

    # Monta a query Scryfall: um oracle:"..." para cada padrão de busca
    parts = [f'oracle:"{pat}"' for pat in cfg["search_patterns"]]
    parts.append(cfg["type_filter"])
    parts.append(f'cmc>={carta_base["cmc"] - 2}')
    parts.append(f'cmc<={carta_base["cmc"] + 2}')
    parts.append('unique:cards')
    parts.append('sort:usd-asc')
    query = ' '.join(parts)

    url = f'https://api.scryfall.com/cards/search?q={query}'
    resp = requests.get(url)
    if resp.status_code != 200:
        return []

    similares = []
    for c in resp.json().get('data', []):
        preco = c['prices']['usd']
        if preco is None:
            continue
        preco = float(preco)
        cores = c.get('colors', [])
        cmc = c.get('cmc', 0)
        # só sugere se for mais barato e tiver as mesmas cores
        if preco < carta_base['preco'] and all(col in cores for col in carta_base['cores']):
            similares.append({
                'nome': c['name'],
                'preco': preco,
                'cmc': cmc,
                'cores': cores,
                'url': c['scryfall_uri']
            })
    return similares

def agente_magic(nome_carta):
    carta = buscar_carta(nome_carta)
    if not carta:
        print("Carta não encontrada.")
        return

    print(f"\n🔍 Alternativas para '{carta['nome']}'")
    print(f"- Preço: US${carta['preco']}")
    print(f"- CMC: {carta['cmc']}")
    print(f"- Cores: {carta['cores'] or 'Incolor'}")

    cfg = identificar_efeito_central(carta['texto'])
    if not cfg:
        print("⚠️ Efeito principal não identificado.")
        return

    print(f"- Efeito principal: '{cfg['name']}'\n")

    similares = buscar_similares_otimizado(carta, cfg)
    if not similares:
        print("Nenhuma alternativa mais barata encontrada.")
    else:
        print("✨ Cartas sugeridas:\n")
        for c in similares[:5]:
            cor_str = ','.join(c['cores']) if c['cores'] else 'Incolor'
            print(f"- {c['nome']} | CMC: {c['cmc']} | Cores: {cor_str} | US${c['preco']} | {c['url']}")

# Testes
agente_magic("Thoughtseize")
agente_magic("Lightning Bolt")
agente_magic("Counterspell")
agente_magic("Opt")