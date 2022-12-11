###################################################
## ------------------------------------------------
## ✵  　　  ·　　✷  　　　 * * 　 
## 　 　 ✵  ˚ regurgitate.py 　
## 　　　  ✺ 　　　✷    　 
##  .　*  ✹   ✫ 2022 alexandria ahluwalia
## ------------------------------------------------
###################################################


import re
import random
from random import sample 
import math
from datetime import datetime
import nltk
from nltk import word_tokenize


###############################################
## ------------------------------------------------
## formatting variables for printing thesis
## \n is a line break, play with spaces to centre
## ------------------------------------------------
###################################################

author = "Alexandria Ahluwalia" 
course = "MA Internet Equalities"
university = "UAL CCI"
total_word_count = 7500 # Desired word count 


title_l1 = "\"How Technologies Write and How"
title_l2 ="We are Written by Technologies\""
date = "[ DATE " + datetime.now().strftime('%d/%m/%Y')+" ]"
hz_line = "\n"+"------------------------------------------------"+"\n"
title_references = "\n"+"-------------------REFERENCES-------------------"+"\n"
# play with the spacing here if the title changes to centre on receipt
header = "\n\n\n\n\n\n"+"                   MA THESIS"+"\n\n\n"+\
    "         "+title_l1+"\n"+"         "+title_l2+\
    "\n\n"+"              "+author+"\n\n"+"            "+course+"\n"+\
    "                    "+university+"\n\n\n"



###################################################
## ------------------------------------------------
## import text data and list of refernces
## change the name of the files below to add your own text/references
## ------------------------------------------------
###################################################

sources = "sources.txt"
#reference_list = open("mini-references.txt").read()
reference_list = open("references.txt").read()
text_data_ac = open("book_of_units.txt").read()

# use all sources text for body of thesis
# use text from book of units for abstract and conlusion
text_data = open(sources).read()

# "clean" text data by removing spaces and brackets from text
text_data = ''.join([i for i in text_data if not i.isdigit()]).replace("\n", " ").\
    replace("(","").replace(")","").replace("/","").replace("[","").\
    replace("]","").replace("/","").replace("  ","").replace("<","").\
    replace(">","").replace(".,","").replace("|","").split(' ')

## "A typical structure is to have an Abstract, Introduction, Literature Review, Methods, 
## Presentation of the Work, Discussion, Conclusions --- all of roughly equal length 
## except the Abstract and Conclusion which are typically just one paragraph."

#special cleaning of text for travesty functions
regex = re.compile('[^a-zA-Z]')
input_file = regex.sub(' ',open(sources).read())

# word count for each paragraph
# word count for abstract and conclusio
count = math.ceil((total_word_count*16)//100)
ac_count = math.ceil(total_word_count//10)

## variables for markov word level and dada word level (Lit review and presentation of work)
index = 1
chain = {}



###################################################
## ------------------------------------------------
## ABSTRACT 
## ------------------------------------------------
###################################################

# this can be replaced, but has not been tested
# source: https://cpb-ap-se2.wpmucdn.com/sites.rmit.edu.au/dist/b/55/files/2018/04/Abstract-Guidelines-Nature-Journal-qip46l.pdf

# replace with any abstract you fancy 
ideal_abstract = "Thematic analysis is a poorly demarcated, rarely acknowledged, yet widely used qualitative analytic method within psychology. In this paper, we argue that it offers an accessible and theoretically flexible approach to analysing qualitative data. We outline what thematic analysis is, locating it in relation to other qualitative analytic methods that search for themes or patterns, and in relation to different epistemological and ontological positions. We then provide clear guidelines to those wanting to start thematic analysis, or conduct it in a more deliberate and rigorous way, and consider potential pitfalls in conducting thematic analysis. Finally, we outline the disadvantages and advantages of thematic analysis. We conclude by advocating thematic analysis as a useful and flexible method for qualitative research in and beyond psychology."
#"Organizations are rapidly deploying artificial intelligence (AI) systems to manage their workers. However, AI has been found at times to be unfair to workers. Unfairness toward workers has been associated with decreased worker effort and increased worker turnover. To avoid such problems, AI systems must be designed to support fairness and redress instances of unfairness. Despite the attention related to AI unfairness, there has not been a theoretical and systematic approach to developing a design agenda. This paper addresses the issue in three ways. First, we introduce the organizational justice theory, three different fairness types (distributive, procedural, interactional), and the frameworks for redressing instances of unfairness (retributive justice, restorative justice). Second, we review the design literature that specifically focuses on issues of AI fairness in organizations. Third, we propose a design agenda for AI fairness in organizations that applies each of the fairness types to organizational scenarios. Then, the paper concludes with implications for future research."
# "Cursors, avatars, virtual hands or tools, and other rendered graphical objects, enable users to interact with computers such as PCs, game consoles or virtual reality systems. We analyze the role of these various objects from a user perspective under the unifying concept of “User Representations”. These representations are virtual objects that artificially extend the users’ physical bodies, enabling them to manipulate the virtual environment by performing motor actions that are continuously mapped to their User Representations. In this paper, we identify a set of concepts that are relevant for different User Representations, and provide a multidisciplinary review of the multisensory and cognitive factors underlying the control and subjective experience of User Representations. These concepts include visual appearance, multimodal feedback, sense of agency, input methods, peripersonal space, visual perspective, and body ownership. We further suggest a research agenda for these concepts, which can lead the human-computer interaction community towards a wider perspective of how users perceive and interact through their User Representations."
#"During cell division, mitotic spindles are assembled by microtubule-based motor proteins. The bipolar organization of spindles is essential for proper segregation of chromosomes, and requires plus-end-directed homotetrameric motor proteins of the widely conserved kinesin-5 family. Hypotheses for bipolar spindle formation include the 'push−pull mitotic muscle' model, in which kinesin-5 and opposing motor proteins act between overlapping microtubule. However, the precise roles of kinesin-5 during this process are unknown. Here we show that the vertebrate kinesin-5 Eg5 drives the sliding of microtubules depending on their relative orientation. We found in controlled in vitro assays that Eg5 has the remarkable capability of simultaneously moving a towards the plus-ends of each of the two microtubules it crosslinks. For anti-parallel microtubules, this results in relative sliding, comparable to spindle pole separation rates in vivo6 . Furthermore, we found that Eg5 can tether microtubule plus-ends, suggesting an additional microtubule-binding mode for Eg5. Our results demonstrate how members of the kinesin-5 family are likely to function in mitosis, pushing apart interpolar microtubules as well as recruiting microtubules into bundles that are subsequently polarized by relative sliding. We anticipate our assay to be a starting point for more sophisticated in vitro models of mitotic spindles. For example, the individual and combined action of multiple mitotic motors could be tested, including minus-enddirected motors opposing Eg5 motility. Furthermore, Eg5 inhibition is a major target of anti-cancer drug development, and a well-defined and quantitative assay for motor function will be relevant for such developments."

# tokenize and tag abstract
abstract_t = word_tokenize(ideal_abstract) 
abstract_td = nltk.pos_tag(abstract_t)
a = abstract_td
ag = []
for inner in a:
    ag.append(inner[1])
    
input_t = word_tokenize(text_data_ac)
random.shuffle(input_t)
input_td = nltk.pos_tag(input_t)

abstract_td_uz = list(zip(*abstract_td))
abstract_g = abstract_td_uz[1] # grammar of abstract as a tuple
abstract_s=', '.join(abstract_g) # grammar of abstract as a string

a_list = abstract_s.replace(" ","").split(',')
replace = list(map(list,input_td))
new_list = []
for item in a_list:
    for i, (value, key) in enumerate(replace):
        if key == item:
            new_list.append(value)
            del replace[i]
            break
    else:
        new_list.append(item)

new_list[0].title()
abstract_text = " ".join(new_list)
abstract = "ABSTRACT"+"\n"+abstract_text



###################################################
## ------------------------------------------------
## 1 Introduction
## Travesty
## ------------------------------------------------
###################################################

# source: https://github.com/rodneyshupe/travestypy
# "Travesty in Python" - MIT License, Copyright (c) 2019 Rodney Shupe

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# `travesty-intro.txt`` was generated using the first command 
# using the code referenced above
# see github.com/lexahl/text-regurgitation for details
travesty_intro = open("travesty-intro.txt").read()
travesty_intro = travesty_intro.replace("\n","").replace("course", "thesis")
introduction = "\n"+hz_line+"1 - INTRODUCTION"+hz_line+travesty_intro



###################################################
## ------------------------------------------------
## 2 Literature Review 
## Markov word level
## ------------------------------------------------
###################################################

# This loop creates a dicitonary called "chain". Each key is a word, and the value of each key
# is an array of the words that immediately followed it. 
for word in text_data[index:]: 
	key = text_data[index - 1]
	if key in chain:
		chain[key].append(word)
	else:
		chain[key] = [word]
	index += 1

word1 = random.choice(list(chain.keys())) #random first word
lit_review = "."+"\n"+hz_line+"2 - LITERATURE REVIEW"+hz_line+word1.capitalize()

# Picks the next word over and over until word count achieved
while len(lit_review.split(' ')) < count:
	word2 = random.choice(chain[word1])
	word1 = word2
	lit_review += ' ' + word2



###################################################
## ------------------------------------------------
## 3 Methods
## Markov Character Level
## ------------------------------------------------
###################################################

# source:https://github.com/aparrish/rwet/blob/master/ngrams-and-markov-chains.ipynb
# shmarkov.py, simple and concise markov chain text generation

# Copyright (C) 2018 Allison Parrish
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def add_to_model(model, n, seq):
    seq = list(seq[:]) + [None]
    for i in range(len(seq)-n):
        gram = tuple(seq[i:i+n])
        next_item = seq[i+n]            
        if gram not in model:
            model[gram] = []
        model[gram].append(next_item)

def markov_model(n, seq):
    model = {}
    add_to_model(model, n, seq)
    return model

def gen_from_model(n, model, start=None, max_gen=count):
    if start is None:
        start = random.choice(list(model.keys()))
    output = list(start)
    for i in range(max_gen):
        start = tuple(output[-n:])
        next_item = random.choice(model[start])
        if next_item is None:
            break
        else:
            output.append(next_item)
    return output

def markov_model_from_sequences(n, sequences):
    model = {}
    for item in sequences:
        add_to_model(model, n, item)
    return model

def markov_generate_from_sequences(n, sequences, count, max_gen=count):
    starts = [item[:n] for item in sequences if len(item) >= n]
    model = markov_model_from_sequences(n, sequences)
    return [gen_from_model(n, model, random.choice(starts), max_gen)
           for i in range(count)]

def markov_generate_from_lines_in_file(n, filehandle, count, level='char', max_gen=count):
    if level == 'char':
        glue = ''
        sequences = [item.strip() for item in filehandle.readlines()]
    elif level == 'word':
        glue = ' '
        sequences = [item.strip().split() for item in filehandle.readlines()]
    generated = markov_generate_from_sequences(n, sequences, count, max_gen)
    return [glue.join(item) for item in generated]

# On average, text contains between 5 and 6.5 characters per word 
# including spaces and punctuation. For example, The Great Gatsby 
# averages 5.44 characters per word.
# source: https://charactercounter.com/characters-to-words


int_count = int(count)//5
methods_list=[]
for item in markov_generate_from_lines_in_file(3, open(sources), int_count, 'char'):
    methods_list+=item


methods = "\n"+hz_line+"3 - METHODS"+hz_line+ "".join(methods_list)+"."



###################################################
## ------------------------------------------------
## 4 Presentation of Work 
## Dada word level
## ------------------------------------------------
###################################################

# TO MAKE A DADAIST POEM
# Take a newspaper.
# Take some scissors.
# Choose from this paper an article of the length you want to make your poem.
# Cut out the article.
# Next carefully cut out each of the words that makes up this article and put them all in a bag.
# Shake gently.
dadaword = random.sample(text_data, total_word_count)
word1_dada = random.choice(dadaword).capitalize()

# Next take out each cutting one after the other.
# Copy conscientiously in the order in which they left the bag.
# The poem will resemble you.
# And there you are—an infinitely original author of charming sensibility, 
# even though unappreciated by the vulgar herd.
# — Tristan Tzara, 1920
presentation_of_work = "\n"+hz_line+"4 - PRESENTATION OF WORK"+hz_line+word1_dada

while len(presentation_of_work.split(' ')) < count:
    word2_dada = random.choice(dadaword)
    word1_dada = word2_dada
    presentation_of_work += ' ' + word2_dada



###################################################
## ------------------------------------------------
## 5 Discussion
## Dada Character Level
## ------------------------------------------------
###################################################

# join all and split character level
sources_concat= " ".join(text_data)
dada_split_chars = list(sources_concat)

# take out each cutting one after the other
discussion = "\n"+hz_line+"5 - DISCUSSION"+hz_line

# Copy conscientiously in the order in which they left the bag.
while len(discussion.split(' ')) < count:
    char2_dada = random.choice(dada_split_chars)
    char1_dada = char2_dada
    discussion +=''+ char2_dada

# remove extra spaces    
discussion.replace("  "," ").replace("-"," ")



###################################################
## ------------------------------------------------
## Conclusion
## (just the abstract scrambled, data word-level)
## ------------------------------------------------
###################################################

conclusion_word = random.sample(abstract_text.split(), 50)
word1_conclusion = random.choice(conclusion_word).capitalize()

conclusion = "\n"+hz_line+"CONCLUSION"+hz_line+word1_conclusion

while len(conclusion.split(' ')) < ac_count:
    word2_conclusion = random.choice(conclusion_word)
    word1_conclusion = word2_conclusion
    conclusion += ' ' + word2_conclusion



###################################################
## ------------------------------------------------
## generate thesis with all elements 
## print and write file
## ------------------------------------------------
###################################################

all_words = abstract + introduction + lit_review + methods +\
    presentation_of_work + discussion + conclusion


word_count = len(all_words.split())
        
total_words= "[ WORD COUNT: "+str(word_count)+" ]\n"+"\n"


###################################################
## ------------------------------------------------
## generate thesis with all elements 
## print and write file
## ------------------------------------------------
###################################################

# write thesis into output.txt file
thesis = header + date + hz_line + abstract + introduction + lit_review + methods +\
    presentation_of_work + discussion + conclusion + "\n" + hz_line + "REFERENCE LIST" +\
    hz_line + reference_list + "\n" + hz_line + total_words

# creates new file with output and prints it to the terminal
with open("output.txt", "w") as file:
	file.write(thesis)

# write thesis to file "output.txt" and displays the output in terminal
output = open("output.txt")
print(output.read())


###################################################
## ------------------------------------------------
## ✵  　　  ·　　✷  　　　 * * 　 
## 　 　 ✵  ˚ regurgitate.py 　
## 　　　  ✺ 　　　✷    　 
##  .　*  ✹   ✫ 2022 alexandria ahluwalia
## ------------------------------------------------
###################################################
