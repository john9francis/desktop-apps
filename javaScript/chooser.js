class Chooser{
  constructor(){
    this.wordList = [];
  }

  addToWordList(csvString){
    // split the string into words
    let words = csvString.split(",");
    
    // clean the words
    words = words.map(word => word.trim());

    this.wordList.push(...words);
  }

  getWordList(){
    return this.wordList
  }

  getRandomWord(){
    return this.wordList[Math.floor(Math.random() * this.wordList.length)];
  }

  clearWordList(){
    this.wordList = [];
  }
}


module.exports = Chooser