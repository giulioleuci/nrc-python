# Lexicon downloaded from https://saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm
# and converted to .json files attached
# date: 5 jan 22

import json

def get_emolex(file='nrc_emolex.json'):
    f = open(file)
    j = json.load(f)
    f.close()
    return j

def get_vad(file='nrc_vad.json'):
    f = open(file)
    j = json.load(f)
    f.close()
    return j
    
def emolex(text,lexicon):
    text = text.split()
    
    total_word = len(text)
    
    emotions = {'anger':0,
                'anticipation':0,
                'disgust':0,
                'fear':0,
                'joy':0,
                'sadness':0,
                'surprise':0,
                'trust':0}
    words_with_emo = 0
    emotion_level = 0
    
    for word in text:
        if word in lexicon:
            words_with_emo+=1
            for emo in lexicon[word]:
                emotion_level+=1
                emotions[emo]+=1
    return emotions, emotion_level, words_with_emo, total_word
    
def vad(text,lexicon):
    text = text.split()
    
    total_word = len(text)
    
    emotions = {'valence':0,
                'arousal':0,
                'dominance':0}
    words_with_emo = 0
    
    for word in text:
        if word in lexicon:
            words_with_emo+=1
            for emo in lexicon[word]:
                emotions[emo]+=lexicon[word][emo]
    return emotions, words_with_emo, total_word
