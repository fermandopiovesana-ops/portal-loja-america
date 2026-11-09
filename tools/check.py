"""Valida o site antes de publicar: JSON legível, ids únicos, traduções alinhadas e fotos existentes.
Uso: python3 tools/check.py  (sai com erro se algo estiver errado)"""
import json, os, sys
B = os.path.join(os.path.dirname(__file__), '..', 'site')
M = json.load(open(f'{B}/data/marcos.json', encoding='utf-8'))
err = []
ids = [m.get('id') for m in M]
if None in ids: err.append('marco sem id')
if len(ids) != len(set(ids)): err.append('ids duplicados')
for m in M:
    for f in m.get('fotos', []) or []:
        if not os.path.exists(f"{B}/{f['f']}"): err.append(f"foto ausente: {f['f']}")
for lang in ('en', 'es'):
    T = json.load(open(f'{B}/data/i18n/{lang}.json', encoding='utf-8'))['marcos']
    for m in M:
        x = T.get(m['id'])
        if not x: err.append(f'{lang}: falta tradução de {m["id"]}'); continue
        for k, mk in (('detalhe', 'detalhe'), ('fotos', 'fotos'), ('papeis', 'irmaos')):
            if k in x and m.get(mk) and len(x[k]) != len(m[mk]):
                err.append(f'{lang}: {m["id"]} {k} com {len(x[k])} itens, PT tem {len(m[mk])}')
print('\n'.join(err) or f'ok: {len(M)} marcos')
sys.exit(1 if err else 0)
