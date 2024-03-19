let frutas = ["pera", "Manzana", "Naranja", "Kiwi"]

for (let i = 0; i < frutas.length; i++) {
    const element = frutas[i];
    console.log(element, i);
}

for (const fruta of frutas) {
    console.log(fruta);
}