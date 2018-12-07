import unicodecsv
import sys 
import argparse
import re
import io

source_file_name="train.tags.en-de.en"
target_file_name="train.tags.en-de.de"
source = io.open(source_file_name, 'r', encoding='utf-8').readlines()
target = io.open(target_file_name, 'r', encoding='utf-8').readlines()

def clean(sentence):
    return sentence.replace("  ", " ").strip()

def fails(sentence):
    return (
        (sentence.count('seg')==0 and sentence.count('"') % 2)
        or " " not in sentence
        or len(re.split(r'[.!?]+?[ ]+', sentence))>1
        or re.search(r'[\%]+', sentence)
        or not re.search("^[A-Za-z]", sentence)
        #or sentence[-1] not in (".", "!", "?")
    )   

def fails_chinese(sentence):
    return (
        (sentence.count('seg')==0 and sentence.count('"') % 2)
        or re.search(r'[\%]+', sentence)
        or sentence[-1] not in ("\x82",".", "!", "?")
    )
sf = io.open("src-train.txt", "w", encoding='utf-8')
tf = io.open("tgt-train.txt", "w", encoding='utf-8')
vs=[]
vt=[]
target_type="german"
missed=0
for index in range(len(source)):
    s = clean(source[index])
    t = clean(target[index])
    #print(s)
    if (
        fails(s)
        #or fails(t)
        or s == t
    ):
        missed+=1
        continue
    sf.write(s+"\n")
    vs+=s.replace("."," .").replace("?", " ?").replace("!", " !").replace(","," ,").split()
    tt=t.replace("."," .").replace("?", " ?").replace("!", " !").replace(","," ,")
    #vt+=tt.split()
    tf.write(tt+"\n")
# vs=list(set(vs))
# vt=list(set(vt))
# fvs=open("vocab.s", "w")
# fvt=open("vocab.t", "w")
# fvs.write("\n".join(vs))
# fvt.write("\n".join(vt))
# fvs.close()
# fvt.close()
sf.close()
tf.close()
print(missed)
