let myCar = {
    make: "Ford",
    model: "Mustang",
    year: 1969,
  };

  for (const key in myCar) {
        const element = myCar[key];
        console.log(element);
  }

  let keys = Object.keys(myCar)

  console.log(keys);