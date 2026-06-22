const http = require("http")
const servidor = http.createServer((req,res)=>{
    res.write("Servidor funcionando!");
    res.end();
});

servidor.listen(3000, ()=>{
    console.log("Servidor rodando em http://localhost:3000");
});
