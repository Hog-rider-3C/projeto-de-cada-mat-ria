# 📱 Desenvolvimento Mobile

## 📝 Descrição do Projeto/Atividade
Testes de programação para aprender

---

## 🧠 Reflexão de Aprendizado

### 1. O que aprendi?
Copiar e programar codigos "simples"

### 2. Para que serve (Por que aprendi)?
Aprender e ter noção basica de programação mobile

---

## 🛠️ Tecnologias e Ferramentas Utilizadas
*   React Native / Expo
*   TypeScript
*   [Outra biblioteca, ex: Axios, React Navigation, React Native Vector Icons]

---

## 💻 Demonstração e Como Rodar

### Código Relevante Comentado
[Insira aqui um trecho de código TypeScript/React Native que foi crucial para o projeto, comentando as linhas mais importantes para demonstrar seu entendimento. Exemplo:]
```tsx
// Exemplo de código (substitua pelo seu):
const fetchWeatherData = async (city: string) => {
  try {
    setLoading(true);
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=SUA_API_KEY`);
    const data = await response.json();
    setWeather(data);
  } catch (err) {
    setError('Não foi possível carregar os dados de clima.');
  } finally {
    setLoading(false);
  }
};
```

### Instruções para Executar
1. Instale as dependências na pasta do projeto:
   ```bash
   npm install
   ```
2. Inicialize o servidor de desenvolvimento do Expo:
   ```bash
   npx expo start
   ```
3. Use o aplicativo Expo Go em seu dispositivo móvel ou um emulador Android/iOS para visualizar.
