#Author: Yosiyoshi
import difflib
import nltk
from nltk import CFG
from nltk import ChartParser
import nltk.parse
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import SnowballStemmer

class ThaiForeignEtymolgy():
    def Foreign2Thai(self, corpus, mode = "sk"):
        if mode == "sk":
            sk1 = corpus.replace("ara", "on")
            sk2 = sk1.replace("bh", "ph")
            sk3 = sk2.replace("ana", "an")
            sk4 = sk3.replace("t", "d")
            sk5 = sk4.replace("g", "gh")
            sk6 = sk5.replace("gh", "kh")
            sk7 = sk6.replace("usya", "ut")
            sk8 = sk7.replace("aka", "ok")
            sk9 = sk8.replace("j", "cha")
            sk10 = sk9.replace("asa", "atsa")
            sk11 = sk10.replace("di", "ti")
            sk12 = sk11.replace("rn", "n")
            sk13 = sk12.replace("sv", "sw")
            sk14 = sk13.replace("ry", "riy")
            sk15 = sk14.replace("tt", "d")
            sk16 = sk15.replace("d", "th")
            sk17 = sk16.replace("ao", "aa")
            skfinal = sk17.replace("v", "w")
            print(corpus, "(Sanskrit) ==>", skfinal)
        elif mode == "ch":
            ch1 = corpus.replace("g", "kh")
            ch2 = ch1.replace("ng", "n")
            ch3 = ch2.replace("j", "y")
            ch4 = ch3.replace("n", "y")
            ch5 = ch4.replace("e", "u")
            ch6 = ch5.replace("a", "ua")
            ch7 = ch6.replace("b", "ph")
            ch8 = ch7.replace("dz", "ch")
            ch9 = ch8.replace("hr", "h")
            chfinal = ch9.replace("ts", "s")
            print(corpus, "(Old Chinese) ==>", chfinal)
        else:
            print("invalid mode")

class OmnibusStem:
    def stemmer(self, corpus):
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("n", "m")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        print(corpus, "=>", final)

    def compStemmer(self, corpus1, corpus2, skip=0, result=1):
        corpus = corpus1 + " " + corpus2
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("n", "m")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        l = final.split(" ")
        l1 = ''.join(l[0])
        l2 = ''.join(l[1])
        s = difflib.SequenceMatcher(None, l1, l2).ratio()
        if skip == 0:
            print(corpus1, ",", corpus2, "=>", l1, ",", l2, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    print("high possibility of co-etymology")
                else:
                    print("low possibility of co-etymology")
            else:
                return
        else:
            return

    def compStemmerStem(self, corpus, stem, skip=0, result=1):
        conju0 = corpus.replace("ri", "ni")
        conju0a = conju0.replace("ru", "ni")
        conju0b = conju0a.replace("zh", "ts")
        conju0c = conju0b.replace("q", "g")
        conju1 = conju0c.replace("w", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("hk", "k")
        conju5 =conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "j")
        conju8 = conju7.replace("p", "p")
        conju9 = conju8.replace("i", "e")
        conju10 = conju9.replace("n", "m")
        conju11 = conju10.replace("u", "e")
        conju12 = conju11.replace("b", "b")
        conju13 = conju12.replace("l", "l")
        conju14 = conju13.replace("h", "k")
        conju15 = conju14.replace("j", "g")
        conju16 = conju15.replace("kwh", "kw")
        conju17 = conju16.replace("z", "dy")
        conju18 = conju17.replace("v", "w")
        conju19 = conju18.replace("x", "k")
        final = conju19.replace("oe", "ew")
        s = difflib.SequenceMatcher(None, final, stem).ratio()
        if skip == 0:
            print(corpus, ",", stem, "=>", final, ",", stem, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    print("high possibility of co-etymology")
                else:
                    print("low possibility of co-etymology")
            else:
                return
        else:
            return

    def simpleComp(self, corpus1, corpus2, skip=0, result=1):
        s = difflib.SequenceMatcher(None, corpus1, corpus2).ratio()
        if skip == 0:
            print(corpus1, ",", corpus2, "=>", corpus1, ",", corpus2, ": simlilarity =", s)
            if result >= 1:
                if s >= 0.5:
                    print("high possibility of co-etymology")
                else:
                    print("low possibility of co-etymology")
            else:
                return
        else:
            return

    def help(self):
        print("""stemmer(self, corpus):
            `Proto-Indo-European, Proto-Sino-Tibetan etc. stemmer
            
            compStemmer(self, corpus1, corpus2, skip=0, result=1)
            if skip==0, print(corpus => stem, similarity)
            if result=1, print(high/low possibility of co-etymology)""")

class ThrHeadStem:
    def stemmer(self, s, lang):
        print("The original sentence: ", s)
        w = wordpunct_tokenize(s)
        print("Tokenized as: ", w)
        w0 = ''.join(w[0])
        w1 = ''.join(w[1])
        w2 = ''.join(w[2])
        print("The 3 headwords: ", w0, w1, w2)
        sbstem = SnowballStemmer(lang)
        print("Stems: ", sbstem.stem(w0), sbstem.stem(w1), sbstem.stem(w2), "(", lang, ")")

class JpStem:
    def stemmer(self, corpus):
        neg = corpus.replace("ない", "")
        past = neg.replace("た", "る")
        asm = past.replace("れば", "")
        negv = asm.replace("れ", "る")
        comv = negv.replace("ろ", "る")
        adj = comv.replace("く", "し")
        adj2 = adj.replace("き", "し")
        adj3 = adj2.replace("け", "し")
        fin1 = adj3.replace("す", "する")
        fin2 = fin1.replace("るる", "る")
        print(corpus, "->", fin2, "(Japanese Stem)")

    def help(self):
        print("""stemmer(self, corpus):
            `Japanese(Ancient/Modern) stemmer""")

class PieStem:
    def stemmer(self, corpus):
        conju1 = corpus.replace("wh", "kw")
        conju2 = conju1.replace("th", "t")
        conju3 = conju2.replace("d", "t")
        conju4 = conju3.replace("h", "k")
        conju5 = conju4.replace("c", "k")
        conju6 = conju5.replace("f", "p")
        conju7 = conju6.replace("y", "k")
        conju8 = conju7.replace("ou", "ew")
        conju9 = conju8.replace("a", "eh")
        final = conju9.replace("i", "he")
        print(corpus,"->", final, "(Proto-Indo-European)")

    def help(self):
        print("""stemmer(self, corpus):
            `Proto-Indo-European stemmer""")

class MCRecon:
    def MCRecLiao(self, corpus):
        liao1 = corpus.replace("q", "k")
        liao2 = liao1.replace("ang", "uang")
        liao3 = liao2.replace("ia", "e")
        liao4 = liao3.replace("o", "u")
        liao5 = liao4.replace("jin", "kin")
        liao6 = liao5.replace("j", "ts")
        liao7 = liao6.replace("c", "ts")
        liao8 = liao7.replace("sh", "dz")
        liao9 = liao8.replace("zh", "tshi")
        liao10 = liao9.replace("ch", "tshi")
        liao11 = liao10.replace("w", "m")
        liao12 = liao11.replace("f", "p")
        liao13 = liao12.replace("b", "ph")
        liao14 = liao13.replace("ua", "a")
        final = liao14.replace("r", "n")
        print(corpus, "->", final, "(Liao-age Middle Chinese)")

    def help(self):
        print("""MCRecLiao(self, corpus):
            Liao-age Middle Chinese Reconstructor""")
        
class ZhTokenDemo:
    def tokenizer(self, sent):
        print(sent)
        chinese_grammer = CFG.fromstring("""
        s -> NP VP
        PP -> P NP
        NP -> Det N | Det N PP | '我'
        VP -> V  NP | VP  PP | PP VP
        Det -> '个' | '我的'
        N -> '钱包' | '书包' | '商店'
        V -> '有' | '买' | '丢'
        P -> '在'
        """)
        parser = nltk.ChartParser(chinese_grammer)
        for tree in parser.parse(sent):
            print("->", tree)
            
    def help(self):
        print("""tokenizer(self, sent):
            sent = list[]""")

class MlTokenDemo:
    def tokenizer(self, sent):
        print(sent)
        malay_grammer = CFG.fromstring("""
        s -> NP VP
        PP -> P NP
        NP -> N Det | N Det PP | 'saya'
        VP -> V  NP | VP  PP | PP VP
        Det -> 'suatu' | 'itu'
        N -> 'buku' | 'kapor' | 'toko'
        V -> 'punya' | 'membeli' | 'menghilangi'
        P -> 'di'
        """)
        parser = nltk.ChartParser(malay_grammer)
        for tree in parser.parse(sent):
            print("->", tree)
    
    def help(self):
        print("""tokenizer(self, sent):
            sent = list[]""")

class Satemize:
    def satemizer(self, corpus, avs=0):
        conju1 = corpus.replace("e", "a")
        conju2 = conju1.replace("o", "a")
        conju3 = conju2.replace("h", "")
        conju4 = conju3.replace("k", "s")
        conju5 = conju4.replace("g", "j")
        conju6 = conju5.replace("w", "v")
        final = conju6.replace("l", "r")
        if avs==0:
            print(corpus, "->", final, "(Proto-Indo-Iranian)")
        else:
            conju7 = final.replace("s", "x")
            conju8 = conju7.replace("r", "arar")
            final2 = conju8.replace("j", "z")
            print(corpus, "->", final2, "(Avestan)")

    def help(self):
        print("""satemizer(self, corpus, avs=0):
            if avs==0, satemmizer in Proto-Indo-Iranian pronunciation;
            else, satemmizer in Avestan pronunciation""")

#Sample Codes:

#os = OmnibusStem()
#mr = MCRecon()
#js = JpStem()
#ps = PieStem()
#stm = Satemize()

#ps.stemmer("house")
#os.stemmer("house")

#ps.stemmer("earth")
#os.stemmer("earth")

#mr.MCRecLiao("jiang")
#os.stemmer("jiang")

#mr.MCRecLiao("zhonghua renmin gongheguo")
#os.stemmer("zhonghua renmin gongheguo")

#tfe = ThaiForeignEtymolgy()
#tfe.Foreign2Thai("taa aakaasa yaana svarnabhumi", "sk")
