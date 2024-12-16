const numero1 = 10
const numero2 = 50

//soma
const soma = numero1 + numero2

//subtracao
const subtracao = numero2 - numero1

//multiplicacao
const multiplicacao = numero1 * numero2

//divisao
const divisao = numero1/numero2


console.log({soma})
console.log({subtracao})
console.log({multiplicacao})
console.log({divisao})

const nomes = ['Samuel', 'Fabio','Marcia']

console.log('Ola', nomes[1])
console.log('Ola', nomes[0])

//adicionar dado
const rl = require('readline')

const prompt = rl.createInterface({
    input: process.stdin,
    output: process.stdout
})

prompt.question('Qual sua idade?: ', (resposta) =>{
    console.log(`Sua idade é: ${resposta}`)
})
