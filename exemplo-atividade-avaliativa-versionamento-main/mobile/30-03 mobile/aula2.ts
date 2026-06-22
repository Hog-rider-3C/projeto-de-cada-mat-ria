interface PecaProps {
    nome : string;
    viado : string;
    categoria: string;
    compativel : boolean;

}

const carrinhoDeCommpras: PecaProps[] =[
    {nome: "Intel" , categoria: "Processador" , viado: "Manzilli" , compativel: true},
    {nome: "Rtx" , categoria: "Placa video" , viado: "Jão" , compativel: true},
    {nome: "b550m" , categoria: "Placa mãe" , viado: "João Pedro Alves 3C" , compativel: true},
    {nome: "ddr5" , categoria: "memoria-ram" , viado: "Careca" , compativel: false},
];

const renderizarPeca = (props : PecaProps) : string => {
    return `[${props.categoria}] ${props.nome} 
    Nome de viado : ${props.viado}
    Status : ${props.compativel ? 'OK' : 'Incompativel'}`; 
    
};

carrinhoDeCommpras 
    .filter (peca => peca.compativel === true)
    .map (peca => {
        const pecaFormatado = renderizarPeca(peca);
        console.log(pecaFormatado);
    });