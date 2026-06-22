const totalBimestre = 4;

for (let i = 1 ; i <= totalBimestre ; i++) {
    console.log (`fechando notas do ${i}° Bimerstre..`);
}

const disciplinas: string[] = [
    "Desenvolvimento Mobile",
    "Back-end",
    "Front-end"
];
for (const material of disciplinas){
    console.log (`Disciplina matriculada: 
    ${material}`);
}