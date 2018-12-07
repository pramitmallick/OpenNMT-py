import unicodecsv
import sys 
import argparse
import re
import io

source_file_name="IWSLT15.TED.dev2010.en-de.en.xml"
target_file_name="IWSLT15.TED.dev2010.en-de.de.xml"
source = io.open(source_file_name, 'r', encoding='utf-8').readlines()
target = io.open(target_file_name, 'r', encoding='utf-8').readlines()

def clean(sentence):
    return sentence.replace("  ", " ").strip()

def fails(sentence):
    return (
        (sentence.count('seg')==0 and sentence.count('"') % 2)
        or " " not in sentence
        or len(re.split(r'[.!?]+?[ ]+', sentence))>1
        or ": " in sentence
        or re.search(r'[\%]+', sentence)
        #or not re.search("^[A-Z]", sentence)
        #or sentence[-1] not in (".", "!", "?")
    )   
sf = io.open("src-val.txt",'w', encoding='utf-8')
tf = io.open("tgt-val.txt",'w', encoding='utf-8')
vs=[]
vt=[]
for index in range(len(source)):
    sk = clean(source[index])
    tk = clean(target[index])
    if sk.count('seg')==0 or tk.count('seg')==0:
        #print("Not seg")
        continue
    if re.findall(r'\d+', sk.split(">")[0])[0]!=re.findall(r'\d+', tk.split(">")[0])[0]:
        print("ID not matching.")
        continue
    s=sk.split(">")[1].split("<")[0].strip()
    t=tk.split(">")[1].split("<")[0].strip()
    if (
        fails(s)
        #or fails(t)
        or s == t
    ):  
        continue
    sf.write(s+"\n")
    #print(s)
    vs+=s.replace("."," .").replace("?", " ?").replace("!", " !").replace(","," ,").split()
    tt=t.replace("."," .").replace("?", " ?").replace("!", " !").replace(","," ,")
    vt+=tt.split()
    #print(tt)
    tf.write(tt+"\n")
vs=list(set(vs))
vt=list(set(vt))
#fvs=open("vocab.s", "w")
#fvt=open("vocab.t", "w")
#fvs.write("\n".join(vs))
#fvt.write("\n".join(vt))
#fvs.close()
#fvt.close()
sf.close()
tf.close()