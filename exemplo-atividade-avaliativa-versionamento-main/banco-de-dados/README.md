# 🗄️ Banco de Dados

## 📝 Descrição do Projeto/Atividade
tabelas a serem relacionadas

---

## 🧠 Reflexão de Aprendizado

### 1. O que aprendi?
fazer modelagem em banco de dados e relacionar tabelas

### 2. Para que serve (Por que aprendi)?
aprender a mexer com esse tipo de programação

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
*   [SGBD Utilizado, ex: MySQL, PostgreSQL, SQLite, SQL Server]
*   [Ferramenta de Modelagem, ex: brModelo, dbdiagram.io, draw.io]
*   DBeaver ou cliente SQL similar

---

## 💻 Demonstração e Como Rodar

### Código/Script SQL Relevante Comentado
[Insira aqui um trecho de código SQL que demonstre consultas complexas (utilizando JOIN, GROUP BY ou subqueries) ou a criação do esquema físico, comentando as principais partes. Exemplo:]
```sql
-- Exemplo de query SQL (substitua pela sua):
SELECT 
    alunos.nome AS nome_aluno,
    livros.titulo AS titulo_livro,
    emprestimos.data_emprestimo
FROM emprestimos
INNER JOIN alunos ON emprestimos.id_aluno = alunos.id
INNER JOIN livros ON emprestimos.id_livro = livros.id
WHERE emprestimos.status = 'pendente'
ORDER BY emprestimos.data_emprestimo ASC;
```

### Instruções para Executar
1. Copie o script DDL (como `schema.sql`) e execute em seu SGBD de preferência para gerar a estrutura de tabelas.
2. Execute o script de população de dados (como `seed.sql`) para inserir os registros de teste.
3. Utilize as queries documentadas no arquivo para realizar as consultas e verificar os resultados.
