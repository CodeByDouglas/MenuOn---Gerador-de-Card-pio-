# MenuOn---Gerador-de-Card-pio-

Gerador de cardápio para restaurantes

Criar ambiente virtual:

python3 -m venv venv
source venv/bin/activate

Instalar as dependências:

pip install -r requirements.txt

Rodar servidor Flask:

python run.py

Docker:

1. Subindo o container
   No terminal, com Docker rodando:
   docker compose up -d
   "-d roda em background"

Se for a primeira vez, ele baixa a imagem (~200 MB).

2. Verifique se tudo está vivo

   docker compose ps
   Você deve ver algo como:

markdown
Copiar
Editar
Name Command State Ports

---

meu-postgres_db_1 docker-entrypoint.sh postgres Up 0.0.0.0:5432->5432/tcp
E, para logs:

docker compose logs -f db

3. Conectando ao banco
   Via terminal (psql)

psql -h localhost -U douglas -d meu_banco

4. Derruba o Docker
   docker compose down
