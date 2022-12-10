# Text Regurgitation

*Text Regurgitation* aims to critique Large Language Models often unacknowledged but harmful decontextualization of language. Text Regurgitation is simultaneously is a commentary on western education systems and knowledge production. Regurgitation refers to the act of bringing up something that has been previously swallowed or digested. In the context of information, regurgitation refers to the repetition of previously learned information without understanding it. Language models can not understand; they can only regurgitate without meaning, even if the produced text is seemingly coherent. 

## About the Algorithms

The project takes form as multiple receipts, each containing a “thesis.” These theses have been generated intentionally without using Large Language Models. Instead, the text is generated using various functions that take inspiration from algorithms, some over 100 years old. The text corpus was created from the assigned readings for the course “MA Internet Equalities.” This is the repository for the code that generates the thesis, with created text copora. An example thesis generated using this code is availble in this repository as `output.txt`,

* Context-Free Grammar with NLTK (2001)
* Travesty (1984)
* Markov (1906)
* Dada (1920)

- - - 

░█▀▀█ ░█▀▀▀ ░█▀▀█ 　 ░█──░█ ▀█▀ ▀▀█▀▀ ░█─░█ 　 ░█▄─░█ ░█─── ▀▀█▀▀ ░█─▄▀ \
░█─── ░█▀▀▀ ░█─▄▄ 　 ░█░█░█ ░█─ ─░█── ░█▀▀█ 　 ░█░█░█ ░█─── ─░█── ░█▀▄─ \
░█▄▄█ ░█─── ░█▄▄█ 　 ░█▄▀▄█ ▄█▄ ─░█── ░█─░█ 　 ░█──▀█ ░█▄▄█ ─░█── ░█─░█

CGF (Context-Free Grammar) refers to a sytem that represents all possible strings in a given formal language.  

NLTK is a tool in Python to work with human language data, often used in Natural Language Processing. It is used in this code to tokenize and categorize text. See <a href="https://www.nltk.org/install.html" target="_blank">Installing NLTK</a> for installation help.   

### Abstract and Conclusion
* context free grammar
* https://www.nltk.org/

- - - 

▀▀█▀▀ ░█▀▀█ ─█▀▀█ ░█──░█ ░█▀▀▀ ░█▀▀▀█ ▀▀█▀▀ ░█──░█ \
─░█── ░█▄▄▀ ░█▄▄█ ─░█░█─ ░█▀▀▀ ─▀▀▀▄▄ ─░█── ░█▄▄▄█ \
─░█── ░█─░█ ░█─░█ ──▀▄▀─ ░█▄▄▄ ░█▄▄▄█ ─░█── ──░█──

<a href="https://archive.org/details/byte-magazine-1984-11/page/n448/mode/1up?view=theater" target="_blank">A Travesty Generator for Micros by Hugh Kenner and Joseph O'Rourke</a> was published in BYTE Magazine in 1984. With the subtitle, "nonsense imitation can be disconcertingly recognizable," this algorithm is an application of Markov chains and scrambles text in a way that can feel familiar bevause it has the same frequency of which pairs of words or characters that appear in the original text. (Read more <a href="https://www.cs.otago.ac.nz/cosc348/hmm/hmm.pdf" target="_blank">here</a>). 

> A text, such as a passage from a novel, is among other things a set of characters. It consists of so many e's, so many f's, and so on. It's also a set of character pairs (so many ex's, so many ch's, etc.) and of triplets (die's, wkw's, etc.), and so on. For any same-size group of characters — call the size *n* — it's possible to make a frequency table for a particular text. From that table, another text can be constructed that shares statistical properties, but only those properties, with the first one. That's what Travesty does. It produces an output text that duplicates the frequenciesof *n*-character groups in the input text. (Description source: Virtual Muse: Experiments in Computer Poetry by CO Hartman, 1996)

* A Python adaptation of Travesty is used to generate the "Introduction" in the thesis. 
* Reference: <a href="https://github.com/rodneyshupe/travestypy" target="_blank">Travesty in Python by Rodney Shupe</a>, license below.

- - - 

░█▀▄▀█ ─█▀▀█ ░█▀▀█ ░█─▄▀ ░█▀▀▀█ ░█──░█ \
░█░█░█ ░█▄▄█ ░█▄▄▀ ░█▀▄─ ░█──░█ ─░█░█─ \
░█──░█ ░█─░█ ░█─░█ ░█─░█ ░█▄▄▄█ ──▀▄▀─


* Python adaptions of markov chains have been used to generate the "Literature Review" and "Methods" sections in the thesis.
* "Literature Review" is word-level and "Methods" is character-level
* Reference: <a href="https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb" target="_blank">N-grams and Markov chains by Allison Parrish</a>, license below.
- - -

░█▀▀▄ ─█▀▀█ ░█▀▀▄ ─█▀▀█ \
░█─░█ ░█▄▄█ ░█─░█ ░█▄▄█ \
░█▄▄▀ ░█─░█ ░█▄▄▀ ░█─░█

"Dada" text generating/regurgitating algorithms based on the guide "To Make a Dadaist Poem" (Pour Faire Un Poème Dadaiste, 1920) by Tristan Tzara. 

> Take a newspaper. Take some scissors. Choose from this paper an article of the length you want to make your poem. Cut out the article. Next carefully cut out each of the words that makes up this article and put them all in a bag. Shake gently. Next take out each cutting one after the other. Copy conscientiously in the order in which they left the bag. Them poem will resemble you. And there you are - an infinitely original author of charming sensibility, even though unappreciated by the vulgar herd. (Translation reference: <a href="https://lyricstranslate.com/fr/make-dadaist-poem-pour-faire-un-po%C3%A8me-dada%C3%AFste.html" target="_blank">Pour faire un poème dadaïste (traduction en anglais) by Alma Barroca</a>)

<img src="https://github.com/lexahl/text-regurgitation/blob/main/img/tt1920.png?raw=true" alt="Prenez un journal. Prenez des ciseaux. Choisissez dans ce journal un article ayant la longueur que vous comptez donner à votre poème. Découpez l’article. Découpez ensuite avec soin chacun des mots qui forment cet article et mettez-les dans un sac. Agitez doucement. Sortez ensuite chaque coupure l’une après l’autre. Copiez les consciencieusement dans l’ordre où elles ont quitté le sac. Le poème vous ressemblera. Et vous voilà un écrivain infiniment original et d’une sensibilité charmante, encore qu’incomprise du vulgaire." title="Text Regurgitation" width="200"/>


* Python adaptions of "To Make a Dadaist Poem" have been used to generate the "Presentation of Work" and "Discussion" sections in the thesis.
* "Presentation of Work" is word-level and "Discussion" is character-level


## How to Run (and Print) This Code
Download or clone repository to computer. Navigate in terminal/command line to the folder. Run:

```
python3 regurgitate.py
```

A file `output.txt` will be written with a "generated" thesis. The thesis will be different each time the command above is run. The thesis will also show in the terminal/command line. To print using CUPS, using the command line prompt below: 

```
lp -o lpi=10 -o cpi=17 output.txt
```

Modifications: Adjust value of `lpi` (lines per inch) and `cpi` (characters per inch) as needed. If you would like to use your own files, move your text files into the folder as `sources.txt` and `references.txt` after removing the original files. Edit the formatting directly in the `regurgitate.py` file in the ## formatting variables section. 



## References
==to do==
A complete list of references to generate the thesis with `regurgitate.py` and `sources.txt` is included in this repository as `references.txt.`



## Acknowledgements
==to do==


- - -

```
LICENSES
"Travesty in Python" - MIT License, Copyright (c) 2019 Rodney Shupe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



"N-grams and Markov chains" - Copyright © 2018 Allison Parrish

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
