const Chooser = require('./chooser.js')

const prompt = require('prompt-sync')();

const main = () => {
  const c = new Chooser();
  console.log("Your list:")
  console.log(c.getWordList())
  const userInput = prompt("enter something: ")
}


main()