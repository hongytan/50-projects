template = "Today I went to the zoo. I saw a(n) ADJECTIVE NOUN jumping up and down in its tree. He VERB ADVERB through the large tunnel that led to its ADJECTIVE NOUN. I got some peanuts and passed them through the cage to a gigantic gray NOUN towering above my head. Feeding that animal made me hungry. I went to get a ADJECTIVE scoop of ice cream. It filled my stomach. Afterwards I had to VERB ADVERB to catch our bus. When I got home I VERB my mom for a ADJECTIVE day at the zoo."

template = template.split()

madlibs = ['ADJECTIVE', 'NOUN', 'VERB', 'ADVERB.', 'ADJECTIVE.', 'NOUN.', 'VERB.', 'ADVERB'] # All possible madlibs

for i in range(len(template)):
    word = template[i]
    if word in madlibs: # word is madlib
        template[i] = input(f'{word}: ')

print(' '.join(template))