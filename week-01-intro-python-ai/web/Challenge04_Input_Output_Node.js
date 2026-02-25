/*
Challenge 04 - Node.js version
Build a short profile collector (name, age, country, favorite topic) and print a 2-line summary.
Ask for temperature in Celsius and print a rough Fahrenheit conversion.
Ask for three numbers and print their average.
*/
const info = " neurothrone / python-for-aipython-for-ai / week-01-intro-python-ai / 03-input-output / 04-challenge.md\n"
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function ask(question) {
    return new Promise(resolve => rl.question(question, resolve));
}

function printMenu() {
    console.log(`
Menu:
1. Profile Collector
2. Temperature Converter
3. Average Calculator
4. Exit
`);
}

async function profileCollector() {
    console.log("\nProfile Collector");
    const name = await ask("Name? ");
    const age = await ask("Age? ");
    const country = await ask("Country? ");
    const favoriteTopic = await ask("Favorite topic? ");

    console.log(`Name: ${name}, Age: ${age}`);
    console.log(`Country: ${country}, Favorite topic: ${favoriteTopic}`);
}

async function temperatureConverter() {
    console.log("\nTemperature Converter");
    const celsius = parseFloat(await ask("Temperature in Celsius? "));
    const fahrenheit = celsius * 9 / 5 + 32;
    console.log(`Temperature in Fahrenheit: ${fahrenheit.toFixed(2)}`);
}

async function averageCalculator() {
    console.log("\nAverage Calculator");
    const num1 = parseFloat(await ask("First number? "));
    const num2 = parseFloat(await ask("Second number? "));
    const num3 = parseFloat(await ask("Third number? "));
    const average = (num1 + num2 + num3) / 3;
    console.log(`Average: ${average.toFixed(2)}`);
}

async function main() {

    while (true) {
        printMenu();
        const choice = await ask("Enter your choice (1-4): ");

        if (choice === "1") {
            await profileCollector();
        }
        else if (choice === "2") {
            await temperatureConverter();
        }
        else if (choice === "3") {
            await averageCalculator();
        }
        else if (choice === "4") {
            console.log("Goodbye!");
            rl.close();
            break;
        }
        else {
            console.log("Invalid choice. Please select 1-4.");
        }
    }
}
console.log(info)
main();