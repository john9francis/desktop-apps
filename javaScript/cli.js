const Chooser = require('./chooser.js')

const main = () => {
  const c = new Chooser();
  console.log("Your list:")
  console.log(c.getWordList())
}


main()