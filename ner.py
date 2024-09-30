from main import words
from nltk import pos_tag, ne_chunk

#POS tagging to identify the role of each word
pos_tag = pos_tag(words)

#Named entity recognition
ner_tree = ne_chunk(pos_tag)

named_entities = []
for chunk in ner_tree:
    if hasattr(chunk, 'label'):
        entity_name = ' '.join(c[0] for c in chunk)  # The named entity
        entity_type = chunk.label()  # PERSON, GPE (geo-political), etc.
        named_entities.append((entity_name, entity_type))


print("Named Entities found:")
for entity in named_entities:
    print(f"{entity[0]} ({entity[1]})")
