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
- Formulário "Portal de Memória da Loja América nº 189 – Contribuições dos Irmãos" (id `1agNJw98j3SxvmHIfOWzMXz9cb1L1PH179kmQfTuI_28`).
- Planilha de respostas: `1fheuioFHOZejrlDbTIVdrXroT7yrSmF479MbCtPJV8c`, aba "Respostas ao formulário 1".
  Leia as colunas pelo **cabeçalho**, não pela posição: A data/hora, B nome, C contato, D assunto, E data/período,
  F local/endereço, G descrição, H quem aparece, I arquivos (links do Drive), J autorização, K e-mail,
  L **tipo da contribuição** ("O que você deseja enviar?"), M **fonte/como confirmar**.
  Linhas antigas sem tipo (L vazia) são "Evento".
- Arquivos: links do Google Drive na coluna "Fotos e documentos" (pasta de uploads do formulário).
- Aprovador: Ir∴ Fernando Piovesana, fermando.piovesana@gmail.com (Gmail conectado).

### Tipos de contribuição (coluna L) e o que cada um gera

| Tipo (começa com) | Proposta | Arquivos que pode alterar (só após aprovação) |
|---|---|---|
| Evento, fotos ou documentos de um evento | marco novo (ou fotos/detalhes num marco existente) | `site/data/marcos.json`, `i18n/en.json`, `i18n/es.json`, `site/fotos/` |
| Correção ou alteração de algo já publicado | lista de alterações pontuais: onde, texto atual, texto proposto, fonte | o arquivo do item citado, exceto os proibidos abaixo |
| Documento, ata, diploma, convite ou recorte | arquivo otimizado + marco ou anexo ao marco/ata correspondente | `site/fotos/`, `marcos.json` (+ i18n) |
| Personagem | entrada nova ou ajuste em `site/data/ilustres.json` (e, se Venerável, `veneraveis.json`) com bio curta, período, destaques e fontes | `ilustres.json`, `veneraveis.json`, `site/fotos/ilustres/`, `site/fotos/veneraveis/` |
| Sede ou endereço | nova sede ou ajuste em `site/data/sedes.json` (endereço, período, fonte) | `sedes.json` |
| Outra sugestão | só um e-mail de resumo ao aprovador, sem alterar arquivos, salvo se for claramente um dos tipos acima | — |

Regras para todos os tipos:
- Não invente fatos: use só o que o Irmão relatou e o que se confirma nas atas/dados existentes. Compare a sugestão com
  `atas.json`, `membros.json`, `marcos.json`, `sedes.json`, `ilustres.json` e diga na proposta se confere, contradiz ou
  não pode ser verificada. Se contradisser as atas, **não altere**: apresente a divergência ao aprovador com as duas fontes.
- Correção de dado vindo das atas ou de transcrição (`site/data/atas.json`, `membros.json`, `site/img/`, transcrições)
  **nunca é aplicada por este fluxo**: vira uma nota em "A conferir" no índice (Indice_Atas_Loja_America.xlsx) e é
  encaminhada ao aprovador para decisão manual.
- Português formal, "Ir∴" antes do nome de Irmão, sem "[?]". Não publique telefone nem e-mail de quem enviou.
- Se faltar a data exata, use a informada e diga que é aproximada.
- Sem autorização marcada (coluna J), ignore a linha.

A cada execução:
1. **Respostas novas** (linhas depois de `ultima_linha_lida`): para cada uma, identifique o tipo (coluna L), baixe os
   arquivos, otimize fotos com `tools/foto.py` para `contrib/pendentes/<id>/` e redija a proposta conforme a tabela.
   Se o envio já está coberto por algo existente, proponha acrescentar em vez de duplicar.
2. Grave a proposta em `contrib/pendentes/<id>/proposta.json` (campo `tipo`; marco PT + traduções EN/ES quando houver
   texto público; para correções, lista `alteracoes` com arquivo, campo, valor atual e valor proposto) e registre em
   `contrib/estado.json` (`propostas`: id, linha, tipo, remetente, status `aguardando`, threadId do e-mail).
3. **Envie e-mail de aprovação** para fermando.piovesana@gmail.com, assunto
   `[Portal Loja América] Aprovação: <título> (#<id>)` (para correção: `Correção: <item> (#<id>)`; para personagem/sede,
   o nome ou endereço), com: tipo, quem enviou, o texto proposto (ou o "antes e depois" nas correções), a verificação
   contra as atas e as fotos anexadas em tamanho reduzido. Peça resposta "ok" para publicar ou a correção desejada.
4. **Respostas do aprovador**: leia os threads das propostas `aguardando`. Mensagem do aprovador (que não seja a enviada
   pela tarefa) dizendo ok/aprovado/pode publicar → publique (passo 5). Pedido de ajuste → ajuste, reenvie no mesmo
   thread e mantenha `aguardando`. "Não"/recusa → status `recusada`, nada publicado.
5. **Publicar**: aplique a proposta aprovada nos arquivos permitidos para o tipo, copie as fotos para `site/fotos/`,
   rode `python3 tools/check.py` (tem de dar ok), commit e push na `main`. O Cloudflare publica sozinho em ~2 minutos.
   Marque `publicada` e responda no thread confirmando, com o link do portal.
6. Atualize `ultima_linha_lida` e faça commit de `contrib/` mesmo quando nada for publicado.

Nunca publique sem a aprovação explícita do aprovador no thread. Nunca altere `site/img/`, `site/data/atas.json`,
`site/data/membros.json` nem as transcrições por este fluxo. Se nada houver de novo, termine sem enviar e-mail.
