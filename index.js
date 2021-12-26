let firstName ="mohamed";
let lastName ="azman";
let age = 22;

if (age=>18)
console.log("major");
else
console.log("minor");
console.log(firstName,lastName,age);


//obj

const person1 = {
         firstName: "md",
         lastName: "azman",
         age: 50,
        eyeColor: "blue"
    };
 console.log(person1);

// //obj another model

const person = {};
person.firstName = "John";
person.lastName = "Doe";
person.age = 50;
person.eyeColor = "blue";
console.log(person);

const person2 = {
    firstName:"John",
    lastName:"Doe",
    age:50, eyeColor:"blue"
  }
  
  const x = person2;
  x.age = 10; // Will change both x.age and person.age
  console.log(person2);
  








  