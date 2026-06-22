//exercicio 1 

let multiplicador: number = 7;

for (let i = 1; i <= 10; i++) {
  console.log(`${multiplicador} x ${i} = ${multiplicador * i}`);
}

//exercício 2

let inventario: string[] = [
    "Poção de Vida",
    "Espada",
    "Escudo",
    "Mapa"
  ];
  
  for (let item of inventario) {
    console.log(`Item equipado: ${item}`);
  }

//exercício 3

interface LancheProps {
    nome: string;
    preco: number;
    vegano: boolean;
  }
  
  const lanches: LancheProps[] = [
    { nome: "Hambúrguer", preco: 20, vegano: false },
    { nome: "Salada", preco: 15, vegano: true },
    { nome: "Batata Frita", preco: 10, vegano: true },
    { nome: "Hot Dog", preco: 18, vegano: false }
  ];
  
  function mostrarLanche(lanche: LancheProps): string {
    return `${lanche.nome} - ${lanche.preco}`;
  }
  
  const veganos = lanches
    .filter(lanche => lanche.vegano)
    .map(lanche => mostrarLanche(lanche));
  
veganos.forEach(i => console.log(i));


//exercicio 4

interface CarroProps {
    modelo: string;
    valor: number;
  }
  
  const carros: CarroProps[] = [
    { modelo: "Gol", valor: 45000 },
    { modelo: "Civic", valor: 90000 },
    { modelo: "Onix", valor: 60000 },
    { modelo: "Uno", valor: 30000 }
  ];
  
  function mostrarCarro(carro: CarroProps): string {
    return `Veículo: ${carro.modelo} - R$ ${carro.valor}`;
  }
  
  const baratos = carros
    .filter(carro => carro.valor < 65000)
    .map(carro => mostrarCarro(carro));
  
  baratos.forEach(i => console.log(i));


