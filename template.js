// Exercise 1
function reduceFraction(num, den) {
    let common_factor = Math.min(num, den);
    while(num % common_factor != 0 || den % common_factor != 0) {
        common_factor -=1
    }
    let num_simplified = num / common_factor;
    let den_simplified = den / common_factor;

    return [Number(num_simplified), Number(den_simplified)]
}

    
// Exercise 2
function isMagicDate(day, month, year) {
    if (Number(String(year).slice(-2)) === day * month) {
        return true;
      } else {
        return false;
      }
    }
   

// Exercise 3
function sublist(l) {
    new_array = [[]]
        for (let i = 0; i < l.length; i++) {
            for (let j = i + 1; j < l.length + 1; j++) {
                new_array.push(l.slice(i,j));
            }
        }

    return new_array
}

// Exercise 4
function pigLatin(word) {
    function isUpperCase(str) {
        return str === str.toUpperCase();
    }
    let vowel = 'aeiuo';
    let newword = word;
    let punc = '';
    let punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~';
    if (punctuation.includes(word.slice(-1))) {
        punc = word.slice(-1);
        newword = word.slice(0 , -1);
    }
    let i = 0
    while (!(vowel.includes(word[i].toLowerCase()))) {
        newword = newword.slice(1) + newword[0].toLowerCase();
        i ++;

        if (i === newword.length) {
           break
        }
    }

    if (isUpperCase(word[0])) {
        newword = newword[0].toUpperCase() + newword.slice(1);
    }

    if (vowel.includes(word[0].toLowerCase())){
        newword += 'way' + punc;
    } else {
        newword += 'ay' + punc;
    } 

    return newword
}


// Exercise 5
function morseCode(message) {
    morse_coder = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
       
        message = message.replace(/[^\w]|_/g, '');
        morse = []
    
        for (i in message) {
           let letter = message[i].toLowerCase();
           let morse_letter = morse_coder[letter];
           morse.push(morse_letter);
        }
        
        let morse_message = morse.join(" ");
    
    return morse_message;
    
}

// Exercise 6
function int2Text(num) {
    num_to_letters = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                  '8': 'eight', '9': 'nine',
                  '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
                  '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty',
                  '30': 'thirty',
                  '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety',
                  '100': 'hundred'
                  }

transcribe = [];

if (num < 21) {
    transcribe.push(num_to_letters[num]);
}
else if (num.toString().length == 2) {
    transcribe.push(num_to_letters[parseInt(num.toString()[0]) * 10]);
    if (parseInt(num.toString()[1]) != 0) {
        transcribe.push(num_to_letters[parseInt(num.toString()[1])]);
    }
}   
else if (num.toString().length === 3) {
    transcribe.push(num_to_letters[parseInt(num.toString()[0])]);
    transcribe.push(num_to_letters[100]);

    if (parseInt(num.toString()[1]) == 0 && parseInt(num.toString()[2]) != 0) {
        transcribe.push(num_to_letters[parseInt(num.toString()[2])]);   
    }
    else if (parseInt(num.toString()[1]) == 1){
        transcribe.push(num_to_letters[parseInt(num.toString().slice(1))]);
    }
    else {
        if (parseInt(num.toString()[1]) != 0) {
            transcribe.push(num_to_letters[parseInt(num.toString()[1]) * 10 ]);
        }
        if (parseInt(num.toString()[2]) != 0) {
            transcribe.push(num_to_letters[parseInt(num.toString()[2])]);
        }
    }
}

let num_as_word = transcribe.join(" ");

return num_as_word

}
  
  


// Exercise 7
function missingComment(filename) {
    let fs = require('fs');
    let file = fs.readFileSync(filename, {encoding: 'utf8', flag: 'r'})
    file = file.split('\n');
    function_index = [];

    for( i in file){        
        if (file[i].slice(0,8) === 'function') {
            function_index.push(parseInt(i));
        }
    }
    functions = [];
    for (i in function_index) {
        if (function_index[i] === 0) {
            functions.push(file[function_index[i]].split('(')[0].slice(9));
        }

        else if (file [function_index[i]-1].slice(0,2) != '//') {
            functions.push(file [function_index[i]].split('(')[0].slice(9));
        }
    }
    return functions
}
    

// Exercise 8
function consistentLineLength(filename, length) {
    let fs = require('fs');
    let file = fs.readFileSync(filename, {encoding: 'utf8', flag: 'r'})
    let output = []; 
    let characters = file.replace(/\r?\n|\r/g, ' ').split('');

    while (characters.length >= length) {
        let i = length;
        while (characters[i] != ' ') {
            i --; 
        }
    
        let justify = characters.slice(0, i);
        let letter = justify.join('');
        
        output.push(letter);
        characters = characters.slice(i +1);
    }
    justify = characters;
        
    let letter = justify.join('');
    
    output.push(letter);
    
    return output
}

// Exercise 9
function knight(start, end, moves) {
    return undefined
}

// Exercise 10
function warOfSpecies(environment) {
    return undefined
}

module.exports = {
    reduceFraction: reduceFraction,
    isMagicDate: isMagicDate,
    sublist: sublist,
    pigLatin: pigLatin,
    morseCode: morseCode,
    int2Text: int2Text,
    missingComment: missingComment,
    consistentLineLength: consistentLineLength,
    knight: knight,
    warOfSpecies: warOfSpecies
}