// Variable Declarations
let name = "John"; // Block-scoped variable
const age = 30; // Block-scoped constant
var city = "New York"; // Function-scoped variable

// Functions

function fazAlgo(objeto){
  if (fruits.includes(objeto)){
    salad.push(objeto);
    console.log("essa fruta está disponível pra salada");
  } else{
    fruits.push(objeto);
    console.log("a opção estará disponível assim que possível.")
  }

}

function percorre(lista){
  for(let i = 0; i< lista.length(); i++){
    console.log(`na posicao ${i} o valor é ${lista[i]}`)
  }

// for (let item of lista) -> similar ao for each

}

// Arrow Functions
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;
const square = x => {
  return x * x;
};

const somatorioTotal = (array) => {
  let soma;
  for (let i = 0; i< array.length(); i++){
    soma+= array[i];
  }
  return soma;
}

//callback functions


// Array Methods
const fruits = ["apple", "banana", "mango"];
fruits.push("orange"); // Adds an element to the end
let firstFruit = fruits.shift(); // Removes the first element and return it
fruits.pop() // removes the last element
fruits.push("tangerine", "watermelon", "lemon", "tomato");
let fruitIndex = fruits.indexOf("banana"); // Finds the index of an element

const salad = fruits.slice(0, fruits.length()/2);
console.log(fruits);
console.log(salad);

salad.splice(0, 3, "grapes");// (index of start, indx of end, element to add in their place)
const dish = fruits.concat(salad);
console.log(dish);

//matrizes

/*O array funcionarios é um array de duas dimensões. Há 3 arrays dentro dele, e para acessar os
valores em funcionarios precisamos de 2 colchetes “[ ] [ ]”.
O primeiro colchete será usado para escolher qual dos 3 arrays dentro de funcionarios será acessado
O segundo colchete será usado para acessar a informação dentro do array escolhido.
*/

const nomes = ["Ana", "Juliana", "Leonardo"];
const idades = [30, 35, 28];
const faculdade = [false, true, true];

const funcionarios = [nomes, idades, faculdade];

//desestruturação de lista, quebrando ela em 2 arrays automaticamente

const personagens = [["finn", "jake", "mordomo menta", "marceline"],["rei gelado", "lich", "morte", "princesa jujuba"]];
const [herois, viloes] = personagens;




// Async Features
const fetchData = async () => {
  try {
    let response = await fetch('https://api.example.com/data');
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

fetchData();