# ⚙️ Desenvolvimento Back-end

## 📝 Descrição do Projeto/Atividade
rodar live server

---

## 🧠 Reflexão de Aprendizado

### 1. O que aprendi?
O conjunto de protocolos TCP/IP:

(Transmission Control Protocol/Internet Protocol) define como

os dados são enviados e recebidos na internet.

Ele é composto por quatro camadas principais:

Aplicação, Transporte, Internet e Rede.

Sua implementação permitiu a conexão de diferentes redes em um

sistema unificado, garantindo a transmissão confiável

de pacotes de dados.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
*   Node.js
*   Express
*   TypeScript
*   [Outra biblioteca ou ferramenta, ex: JWT, bcryptjs, Prisma, SQLite]

---

## 💻 Demonstração e Como Rodar

### Código Relevante Comentado
[Insira aqui um trecho de código do servidor ou rotas que foi crucial para a lógica da aplicação, comentando as linhas mais importantes. Exemplo:]
```javascript
// Exemplo de código Express (substitua pelo seu):
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await database.findUserByEmail(email);
  
  if (!user || !(await bcrypt.compare(password, user.passwordHash))) {
    return res.status(401).json({ error: 'Credenciais inválidas' }); // Erro de autenticação
  }
  
  const token = jwt.sign({ userId: user.id }, SECRET_KEY, { expiresIn: '1h' });
  return res.json({ token }); // Retorna o token para o cliente
});
```

### Instruções para Executar
1. Instale as dependências na pasta do projeto:
   ```bash
   npm install
   ```
2. Configure as variáveis de ambiente necessárias em um arquivo `.env` (se aplicável).
3. Execute o script de inicialização do servidor:
   ```bash
   npm start
   # ou para modo de desenvolvimento:
   npm run dev
   ```
4. Teste as rotas utilizando uma ferramenta de requisições HTTP (como Postman, Insomnia ou a extensão Thunder Client do VS Code).
