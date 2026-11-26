# Simply Invest – publicação automática no Instagram

Publica uma imagem + legenda na conta @simp.invest pela Instagram Graph API, usando GitHub Actions (grátis).

## Como usar
1. Repositório **público** (o Instagram precisa baixar a imagem pela URL).
2. Em Settings > Secrets and variables > Actions, crie:
   - `IG_TOKEN`: o token de acesso (NUNCA coloque no código)
   - `IG_USER_ID`: `17841441253956976`
3. Em Actions > "Publicar no Instagram" > Run workflow, escolha a imagem e a legenda.

Para novos posts: envie a imagem para `images/`, crie um `.txt` de legenda e rode o workflow.

Requisitos: conta Business/Creator ligada a uma Página do Facebook, token com `instagram_content_publish`.
