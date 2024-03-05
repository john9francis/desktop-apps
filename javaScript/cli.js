const Chooser = require('./chooser.js')

const prompt = require('prompt-sync')();

const main = () => {
  const c = new Chooser();

  running = true
  while (running) {
    console.clear()
    console.log("Your list:")
    console.log(c.getWordList())
    console.log("Enter one of these choices:")
    console.log("q: quit")
    console.log("a: add to the list")
    console.log("r: choose randomly from list")
    console.log("c: clear list")
    const userInput = prompt("enter something: ")
    switch (userInput) {
      case "q":
        running = false
        console.log("Quitting...")
        break;
      case "a":
        let newWord = prompt("What word would you like to add?: ")
        c.addToWordList(newWord)
        console.log(`Adding ${newWord} to the word list...`)
        prompt("Press enter to continue: ")
        break;
      case "r":
        let r = c.getRandomWord()
        console.log(`Random word: ${r}`)
        prompt("Press enter to continue: ")
        break;
      case "c":
        console.log("Clearing list...")
        c.clearWordList()
        prompt("Press enter to continue: ")
        break;
      default:
        console.log(`Unknown input: "${userInput}."`)
        prompt("Press enter to continue: ")
    }
  }
}


main()