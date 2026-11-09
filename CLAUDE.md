# Portal de Memória da Loja América nº 189

Site estático publicado pelo Cloudflare Pages a partir da pasta `site/` deste repositório.
Todo push na branch `main` publica automaticamente em https://memoria-loja-america.pages.dev
(link reservado aos Irmãos: `site/` tem noindex, robots.txt e `_headers` — não remover).

## Estrutura

- `site/index.html` — o portal (uma página; carrega os dados de `site/data/`).
- `site/data/marcos.json` — marcos da linha do tempo (lista em ordem cronológica).
- `site/data/i18n/en.json`, `site/data/i18n/es.json` — traduções; `marcos` é um objeto indexado pelo `id` do marco.
- `site/fotos/` — fotos dos marcos (WebP, até 1400 px). `site/img/` — fac-símiles das atas (não mexer).
- `contrib/estado.json` — controle das contribuições recebidas pelo formulário.
- `contrib/pendentes/<id>/` — fotos e proposta de marco aguardando aprovação (fora de `site/`, não é publicado).
- `tools/foto.py` (otimiza foto), `tools/check.py` (valida antes de publicar).

## Formato de um marco (`site/data/marcos.json`)

```json
{"id":"2026-palavras-do-titulo","ano":2026,"data":"DD/MM/AAAA","tema":"Fraternidade",
 "titulo":"…","texto":"2–3 frases","contexto":"1–2 frases de contexto histórico",
 "atas":[],"fora":true,"fonte":"Contribuição do Ir∴ Fulano (formulário do Acervo)",
 "detalhe":["parágrafo", "parágrafo"],
 "irmaos":[["Nome completo","papel no evento"]],
 "fotos":[{"f":"fotos/2026-evento-desc.webp","l":"legenda","c":"Acervo do Ir∴ Fulano"}]}
```
Temas existentes: Abolição, Cidadania, Cultura e educação, Filantropia, Fraternidade, Fundação, Guerra e paz,
Imprensa, Institucional, Maçonaria, Memória, Política, República, Rito Brasileiro, Sede, Sesquicentenário, Sociedade.
`id` = ano + até 5 primeiras palavras do título, sem acento, minúsculas, com hífens; único.
`fora: true` = marco que não vem das atas (aparece também em "Além das atas").

Tradução (em `en.json` e `es.json`, chave = id):
`{"titulo","texto","contexto","detalhe":[…],"papeis":[…],"fotos":[legendas…]}` — mesmas quantidades de itens do português.
Use "Bro∴"/"H∴" para Ir∴, "Worshipful Master"/"Venerable" para Venerável, "Lodge"/"Logia" para Loja.

## Fluxo das contribuições dos Irmãos (tarefa agendada a cada 2 h)

Fontes:
- Planilha de respostas: `1fheuioFHOZejrlDbTIVdrXroT7yrSmF479MbCtPJV8c`, aba "Respostas ao formulário 1"
  (colunas: data/hora, nome, contato, evento, data do evento, local, relato, quem aparece, arquivos (links do Drive), autorização, e-mail).
- Arquivos: links do Google Drive na coluna "Fotos e documentos" (pasta de uploads do formulário).
- Aprovador: Ir∴ Fernando Piovesana, fermando.piovesana@gmail.com (Gmail conectado).

A cada execução:
1. **Respostas novas** (linhas depois de `ultima_linha_lida`): ignore as sem autorização marcada. Para cada uma,
   baixe os arquivos, otimize com `tools/foto.py` para `contrib/pendentes/<id>/`, redija o marco (estilo dos marcos
   existentes: português formal, frases claras, "Ir∴" antes do nome de Irmão, sem "[?]"; não invente fatos: use só
   o que o Irmão relatou e o que se confirma nas atas/marcos existentes; se faltar a data exata, use a informada e diga
   que é aproximada). Se o envio já está coberto por um marco existente, proponha acrescentar as fotos/detalhes a ele.
   Não publique telefone nem e-mail de quem enviou.
2. Grave a proposta em `contrib/pendentes/<id>/proposta.json` (marco PT + traduções EN/ES) e registre em
   `contrib/estado.json` (`propostas`: id, linha, remetente, status `aguardando`, threadId do e-mail).
3. **Envie e-mail de aprovação** para fermando.piovesana@gmail.com, assunto
   `[Portal Loja América] Aprovação: <título> (#<id>)`, com: quem enviou, o texto proposto (título, data, texto, detalhe,
   Irmãos, legendas) e as fotos anexadas em tamanho reduzido. Peça resposta "ok" para publicar ou a correção desejada.
4. **Respostas do aprovador**: leia os threads das propostas `aguardando`. Mensagem do aprovador (que não seja a enviada
   pela tarefa) dizendo ok/aprovado/pode publicar → publique (passo 5). Pedido de ajuste → ajuste, reenvie no mesmo
   thread e mantenha `aguardando`. "Não"/recusa → status `recusada`, nada publicado.
5. **Publicar**: copie as fotos para `site/fotos/`, insira o marco em `site/data/marcos.json` na posição cronológica,
   insira as traduções, rode `python3 tools/check.py` (tem de dar ok), commit e push na `main`. O Cloudflare publica
   sozinho em ~2 minutos. Marque `publicada` e responda no thread confirmando, com o link do portal.
6. Atualize `ultima_linha_lida` e faça commit de `contrib/` mesmo quando nada for publicado.

Nunca publique sem a aprovação explícita do aprovador no thread. Nunca altere `site/img/`, `site/data/atas.json`,
`site/data/membros.json` nem as transcrições por este fluxo. Se nada houver de novo, termine sem enviar e-mail.
