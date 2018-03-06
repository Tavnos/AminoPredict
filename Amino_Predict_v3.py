import random as rd

class Nucleotide_Data:
    dna_base = []
    adenine = {'char':'a','dna':'a','match':'t','rna':'a'}
    guanine = {'char':'g','dna':'g','match':'c','rna':'g'}
    cytosine = {'char':'c','dna':'c','match':'g','rna':'c'}
    thymine = {'char':'t','dna':'t','match':'a','rna':'u'}
    uracil = {'char':'u','dna':'t','match':'a','rna':'u'}
    nucleotide = (adenine,guanine,cytosine,thymine,uracil)
    def __init__(self):
        for i in range(len(self.nucleotide)-1):
            self.dna_base.append(self.nucleotide[i]['char'])

class Peptide_Data:
    amino_acid = []
    methionine = {'config':('atg'),'name':'Methionine','letter_code':'M','tri_char':'Met','amino_class':'sulfuric','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':1.9,'amino_weight':149.208}
    leucine = {'config':('tta','ttg','ctt','ctc','cta','ctg'),'name':'leucine','letter_code':'L','tri_char':'Leu','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':3.8,'amino_weight':131.175}
    phenylalanine = {'config':('ttt','ttc'),'name':'phenylalanine','letter_code':'F','tri_char':'Phe','amino_class':'aromatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':2.8,'amino_weight':165.192}
    serine = {'config':('tct','tcc','tca','tcg','agc','agt'),'name':'serine','letter_code':'S','tri_char':'Ser','amino_class':'hydroxylic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':1.9,'amino_weight':149.208}
    cysteine = {'config':('tgt','tgc'),'name':'cysteine','letter_code':'C','tri_char':'Cys','amino_class':'sulfuric','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':2.5,'amino_weight':121.154}
    tryptophan = {'config':('tgg'),'name':'tryptophan','letter_code':'W','tri_char':'Trp','amino_class':'aromatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-0.9,'amino_weight':204.228}
    proline = {'config':('ccc','cca','cct','ccg'),'name':'proline','letter_code':'P','tri_char':'Pro','amino_class':'cyclic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-1.6,'amino_weight':115.132}
    histidine = {'config':('cat','cac'),'name':'histidine','letter_code':'H','tri_char':'His','amino_class':'basic-aromatic','amino_polarity':'basic-polar','amino_charge':'neutral-positive','amino_hydropathy':-3.2,'amino_weight':155.156}
    glutamine = {'config':('caa','cag'),'name':'glutamine','letter_code':'Q','tri_char':'Gln','amino_class':'amide','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-3.5,'amino_weight':146.146}
    arginine = {'config':('cgg','cgt','cgc','cga','agg','aga'),'name':'arginine','letter_code':'R','tri_char':'Arg','amino_class':'basic','amino_polarity':'basic-polar','amino_charge':'positive','amino_hydropathy':-4.5,'amino_weight':174.203}
    isoleucine = {'config':('att','atc','ata'),'name':'isoleucine','letter_code':'I','tri_char':'Ile','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':4.5,'amino_weight':131.175}
    valine = {'config':('gtg','gtt','gtc','gta'),'name':'valine','letter_code':'V','tri_char':'Val','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':4.2,'amino_weight':117.148}
    tyrosine = {'config':('tat','tac'),'name':'tyrosine','letter_code':'Y','tri_char':'Tyr','amino_class':'aromatic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-1.3,'amino_weight':181.191}
    threonine = {'config':('aca','acc','act','acg'),'name':'threonine','letter_code':'T','tri_char':'Thr','amino_class':'hydroxylic','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-0.7,'amino_weight':119.119}
    alanine = {'config':('gcg','gcc','gct','gca'),'name':'alanine','letter_code':'A','tri_char':'Ala','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':1.8,'amino_weight':89.094}
    asparagine = {'config':('aat','aag'),'name':'asparagine','letter_code':'N','tri_char':'Asn','amino_class':'amide','amino_polarity':'polar','amino_charge':'neutral','amino_hydropathy':-3.5,'amino_weight':132.119}
    lysine = {'config':('aaa','aag'),'name':'lysine','letter_code':'K','tri_char':'Lys','amino_class':'basic','amino_polarity':'basic-polar','amino_charge':'positive','amino_hydropathy':-3.9,'amino_weight':146.189}
    glutamic = {'config':('gaa','gag'),'name':'glutamic','letter_code':'E','tri_char':'Glu','amino_class':'acidic','amino_polarity':'acidic-polar','amino_charge':'negative','amino_hydropathy':-3.5,'amino_weight':147.131}
    aspartic = {'config':('gat','gac'),'name':'aspartic','letter_code':'D','tri_char':'Asp','amino_class':'acidic','amino_polarity':'acidic-polar','amino_charge':'negative','amino_hydropathy':-3.5,'amino_weight':133.104}
    glycine = {'config':('ggg','gga','ggc','ggt'),'name':'glycine','letter_code':'G','tri_char':'Gly','amino_class':'aliphatic','amino_polarity':'non-polar','amino_charge':'neutral','amino_hydropathy':-0.4,'amino_weight':133.104}
    ochre = {'config':('taa'),'name':'Ochre','letter_code':'X','tri_char':'_Ochre','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    amber = {'config':('tag'),'name':'Amber','letter_code':'B','tri_char':'_Amber','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    opal = {'config':('tga'),'name':'Opal','letter_code':'Z','tri_char':'_Opal','amino_class':'Stop','amino_polarity':None,'amino_charge':None,'amino_hydropathy':None,'amino_weight':0}
    amino_acids = (methionine,leucine,phenylalanine,serine,cysteine,tryptophan,proline,histidine,glutamine,arginine,isoleucine,valine,tyrosine,threonine,alanine,asparagine,lysine,glutamic,aspartic,glycine,ochre,amber,opal)
    blosum_62 = {'A':{'A':4, 'R':-1,'N':-2,'D':-2,'C':0, 'Q':-1,'E':-1,'G':0, 'H':-2,'I':-1,'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S':1, 'T':0, 'W':-3,'Y':-2,'V':0, 'X':0,'B':0,'Z':0},
                 'R':{'A':-1,'R':5, 'N':0, 'D':-2,'C':-3,'Q':1, 'E':0, 'G':-2,'H':0, 'I':-3,'L':-2,'K':2, 'M':-1,'F':-3,'P':-2,'S':-1,'T':-1,'W':-3,'Y':-2,'V':-3,'X':0,'B':0,'Z':0},
                 'N':{'A':-2,'R':0, 'N':6, 'D':1, 'C':-3,'Q':0, 'E':0, 'G':0, 'H':1, 'I':-3,'L':-3,'K':0, 'M':-2,'F':-3,'P':-2,'S':1, 'T':0, 'W':-4,'Y':-2,'V':-3,'X':0,'B':0,'Z':0},
                 'D':{'A':-2,'R':-2,'N':1, 'D':6, 'C':-3,'Q':0, 'E':2, 'G':-1,'H':-1,'I':-3,'L':-4,'K':-1,'M':-3,'F':-3,'P':-1,'S':-1,'T':-1,'W':-2,'Y':-2,'V':-1,'X':0,'B':0,'Z':0},
                 'C':{'A':0, 'R':-3,'N':-3,'D':-3,'C':9, 'Q':-3,'E':-4,'G':-3,'H':-3,'I':-1,'L':-1,'K':-3,'M':-1,'F':-2,'P':-3,'S':-1,'T':-1,'W':-2,'Y':-2,'V':-1,'X':0,'B':0,'Z':0},
                 'Q':{'A':-1,'R':1, 'N':0, 'D':0, 'C':-3,'Q':5, 'E':2, 'G':-2,'H':0, 'I':-3,'L':-2,'K':1, 'M':0, 'F':-3,'P':-1,'S':0, 'T':-1,'W':-2,'Y':-1,'V':-2,'X':0,'B':0,'Z':0},
                 'E':{'A':-1,'R':0, 'N':0, 'D':2, 'C':-4,'Q':2, 'E':5, 'G':-2,'H':0, 'I':-3,'L':-3,'K':1, 'M':-2,'F':-3,'P':-1,'S':0, 'T':-1,'W':-3,'Y':-2,'V':-2,'X':0,'B':0,'Z':0},
                 'G':{'A':0, 'R':-2,'N':0, 'D':-1,'C':-3,'Q':-2,'E':-2,'G':6, 'H':-2,'I':-4,'L':-4,'K':-2,'M':-3,'F':-3,'P':-2,'S':0, 'T':-2,'W':-2,'Y':-3,'V':-3,'X':0,'B':0,'Z':0},
                 'H':{'A':-2,'R':0, 'N':1, 'D':-1,'C':-3,'Q':0, 'E':0, 'G':-2,'H':8, 'I':-3,'L':-3,'K':-1,'M':-2,'F':-1,'P':-2,'S':-1,'T':-2,'W':-2,'Y':2, 'V':-3,'X':0,'B':0,'Z':0},
                 'I':{'A':-1,'R':-3,'N':-3,'D':-3,'C':-1,'Q':-3,'E':-3,'G':-4,'H':-3,'I':4, 'L':2, 'K':-3,'M':1, 'F':0, 'P':-3,'S':-2,'T':-1,'W':-3,'Y':-1,'V':3, 'X':0,'B':0,'Z':0},
                 'L':{'A':-1,'R':-2,'N':-3,'D':-4,'C':-1,'Q':-2,'E':-3,'G':-4,'H':-3,'I':2, 'L':4, 'K':-2,'M':2, 'F':0, 'P':-3,'S':-2,'T':-1,'W':-2,'Y':-1,'V':1, 'X':0,'B':0,'Z':0},
                 'K':{'A':-1,'R':2, 'N':0, 'D':-1,'C':-3,'Q':1, 'E':1, 'G':-2,'H':-1,'I':-3,'L':-2,'K':5, 'M':-1,'F':-3,'P':-1,'S':0, 'T':-1,'W':-3,'Y':-2,'V':-2,'X':0,'B':0,'Z':0},
                 'M':{'A':-1,'R':-1,'N':-2,'D':-3,'C':-1,'Q':0, 'E':-2,'G':-3,'H':-2,'I':1, 'L':2, 'K':-1,'M':5, 'F':0, 'P':-2,'S':-1,'T':-1,'W':-1,'Y':-1,'V':1, 'X':0,'B':0,'Z':0},
                 'F':{'A':-2,'R':-3,'N':-3,'D':-3,'C':-2,'Q':-3,'E':-3,'G':-3,'H':-1,'I':0, 'L':0, 'K':-3,'M':0, 'F':6, 'P':-4,'S':-2,'T':-2,'W':1, 'Y':3, 'V':-1,'X':0,'B':0,'Z':0},
                 'P':{'A':-1,'R':-2,'N':-2,'D':-1,'C':-3,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-3,'L':-3,'K':-1,'M':-2,'F':-4,'P':7, 'S':-1,'T':-1,'W':-4,'Y':-2,'V':-2,'X':0,'B':0,'Z':0},
                 'S':{'A':1, 'R':-1,'N':1, 'D':0, 'C':-1,'Q':0, 'E':0, 'G':0, 'H':-1,'I':-2,'L':-2,'K':0, 'M':-1,'F':-2,'P':-1,'S':4, 'T':1, 'W':-3,'Y':-2,'V':-2,'X':0,'B':0,'Z':0},
                 'T':{'A':0, 'R':-1,'N':0, 'D':-1,'C':-1,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-1,'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S':1, 'T':5, 'W':-2,'Y':-2,'V':0, 'X':0,'B':0,'Z':0},
                 'W':{'A':-3,'R':-3,'N':-4,'D':-4,'C':-2,'Q':-2,'E':-3,'G':-2,'H':-2,'I':-3,'L':-2,'K':-3,'M':-1,'F':1, 'P':-4,'S':-3,'T':-2,'W':11,'Y':-2,'V':-3,'X':0,'B':0,'Z':0},
                 'Y':{'A':-2,'R':-2,'N':-2,'D':-3,'C':-2,'Q':-1,'E':-2,'G':-3,'H':2, 'I':-1,'L':-1,'K':-2,'M':-1,'F':3, 'P':-3,'S':-2,'T':-2,'W':-2,'Y':7, 'V':-1,'X':0,'B':0,'Z':0},
                 'V':{'A':0, 'R':-3,'N':-3,'D':-3,'C':-1,'Q':-2,'E':-2,'G':-3,'H':-3,'I':3, 'L':1, 'K':-2,'M':1, 'F':-1,'P':-2,'S':-2,'T':0, 'W':-3,'Y':-1,'V':4, 'X':0,'B':0,'Z':0}}    
    def __init__(self):
        for i in range(len(self.amino_acids)-3):
            self.amino_acid.append(self.amino_acids[i]['letter_code'])

class Transcription:
    dna_data = Nucleotide_Data()
    dna_typed = []
    rna_typed = []
    dna_match = []
    def __init__(self):
        ans1 = input("Random sequence? (y/n)")
        if ans1 == 'y':
            ans2 = input("Enter sequence length.")
            self.input_seq = rd.choices(self.dna_data.dna_base, k=int(ans2))
            self.transcript()
        elif ans1 == 'n': 
            self.input_seq = input("Enter dna sequence")
            self.transcript()
        else:
            print("Enter valid lowercased mRNA or DNA letters without spaces or commas")
    def transcript(self):
        for i in range(len(self.input_seq)):
            for f in range(len(self.dna_data.nucleotide)):
                if self.input_seq[i] in self.dna_data.nucleotide[f]['char']:
                    self.dna_typed.append(self.dna_data.nucleotide[f]['dna'])
                    self.rna_typed.append(self.dna_data.nucleotide[f]['rna'])
                    self.dna_match.append(self.dna_data.nucleotide[f]['match'])

class Translation:
    direct_start_index = []
    reversed_start_index = []
    direct_sequences = []
    possible_chain = {}
    stopped_chains = {}
    stopped_chains_list = []
    translated_chains_letter = []
    translated_chains_chars = []
    translated_chains_weight = []
    translated_chains_total_weight = []        
    translated_chains_blosum_score = []
    translated_chains_blosum_total_score = []
    translated_chains_hydropathy = []
    translated_chains_class = []
    translated_chains_polarity = []
    translated_chains_charge = []
    translated_chains_name = []
    def __init__(self):
        self.dna_transcript = Transcription()
        self.amino_data = Peptide_Data()
        self.chain_sequence = ''.join(self.dna_transcript.dna_typed)
        self.dna_transcript.dna_typed.reverse()
        self.reversed_sequence = ''.join(self.dna_transcript.dna_typed)
        self.dna_transcript.dna_typed.reverse()
        for i in range(len(self.chain_sequence)):
            if self.chain_sequence[i:i+3] == self.amino_data.methionine['config']:
                self.direct_start_index.append(i)
        for i in range(len(self.reversed_sequence)):
            if self.reversed_sequence[i:i+3] == self.amino_data.methionine['config']:
                self.reversed_start_index.append(i)
        for i in range(len(self.direct_start_index)):
            index_var = self.direct_start_index[i]
            self.direct_sequences.append(self.chain_sequence[index_var:])
        for i in range(len(self.reversed_start_index)):
            index_var = self.reversed_start_index[i]
            self.direct_sequences.append(self.reversed_sequence[index_var:])
        for i in range(len(self.direct_sequences)):
            chain_names = "chain{}".format(i)
            for f in range(len(self.direct_sequences[i])):
                self.possible_chain[chain_names] = [self.direct_sequences[i][f:f+3] for f in range(0, len(self.direct_sequences[i]), 3)]
            for f in range(len(self.possible_chain[chain_names])):
                codon = self.possible_chain[chain_names][f]
                if codon == self.amino_data.opal['config'] or codon == self.amino_data.amber['config'] or codon == self.amino_data.ochre['config']:
                    stop_index = self.possible_chain[chain_names].index(codon)+1
                    self.stopped_chains[chain_names] = self.possible_chain[chain_names][0:stop_index]
        for i in self.stopped_chains:
            self.stopped_chains_list.append(self.stopped_chains[i])
        for i in range(len(self.stopped_chains_list)):
            self.translated_chains_letter.append([])
            self.translated_chains_chars.append([])
            self.translated_chains_weight.append([])
            self.translated_chains_total_weight += [0]
            self.translated_chains_blosum_score.append([])
            self.translated_chains_blosum_total_score += [0]
            self.translated_chains_hydropathy.append([])
            self.translated_chains_class.append([])
            self.translated_chains_polarity.append([])
            self.translated_chains_charge.append([])
            self.translated_chains_name.append([])
            for f in range(len(self.stopped_chains_list[i])):
                for k in range(len(self.amino_data.amino_acids)):
                    if self.stopped_chains_list[i][f] in self.amino_data.amino_acids[k]['config']:
                        self.translated_chains_letter[i].append(self.amino_data.amino_acids[k]['letter_code'])
                        self.translated_chains_chars[i].append(self.amino_data.amino_acids[k]['tri_char'])
                        self.translated_chains_weight[i].append(self.amino_data.amino_acids[k]['amino_weight'])
                        self.translated_chains_hydropathy[i].append(self.amino_data.amino_acids[k]['amino_hydropathy'])
                        self.translated_chains_class[i].append(self.amino_data.amino_acids[k]['amino_class'])
                        self.translated_chains_polarity[i].append(self.amino_data.amino_acids[k]['amino_polarity'])
                        self.translated_chains_charge[i].append(self.amino_data.amino_acids[k]['amino_charge'])
                        self.translated_chains_name[i].append(self.amino_data.amino_acids[k]['name'])
            for f in self.translated_chains_weight[i]:
                self.translated_chains_total_weight[i] = sum(self.translated_chains_weight[i])
            for f in range(len(self.translated_chains_letter[i])-1):
                self.translated_chains_blosum_score[i].append([])
                first_letter_var = self.translated_chains_letter[i][f]
                second_letter_var = self.translated_chains_letter[i][f+1]
                blosum_score_var = self.amino_data.blosum_62[first_letter_var][second_letter_var]
                self.translated_chains_blosum_score[i][f] = blosum_score_var    
            for f in self.translated_chains_blosum_score[i]:
                self.translated_chains_blosum_total_score[i] = sum(self.translated_chains_blosum_score[i])
        print("dna_typed:\n {}".format(''.join(self.dna_transcript.dna_typed)))
        print("rna_typed:\n {}".format(''.join(self.dna_transcript.rna_typed)))
        print("dna_match:\n {}".format(''.join(self.dna_transcript.dna_match)))
        print("Peptide ammount:\n {}".format(len(self.stopped_chains_list)))
        print("Peptide 1 letter:\n {}".format(self.translated_chains_letter))
        print("Peptide 3 letter:\n {}".format(self.translated_chains_chars))
        print("Peptide weight:\n {}".format(self.translated_chains_weight))
        print("Peptide total weight:\n {}".format(self.translated_chains_total_weight))
        print("Peptide BLOSUM62 Score:\n {}".format(self.translated_chains_blosum_score))
        print("Peptide BLOSUM62 Total Score:\n {}".format(self.translated_chains_blosum_total_score))
        print("Peptide hydropathy:\n {}".format(self.translated_chains_hydropathy))
        print("Peptide class:\n {}".format(self.translated_chains_class))
        print("Peptide polarity:\n {}".format(self.translated_chains_polarity))
        print("Peptide charge:\n {}".format(self.translated_chains_charge))
        print("Peptide names:\n {}".format(self.translated_chains_name))

class Prediction:
    possible_range = 7
    def __init__(self):
        self.possible_config = [[],[],[],[],[],[],[]]
        self.amino_data = Peptide_Data()
        ans1 = input("Random sequence? (y/n)")
        if ans1 == 'y':
            ans2 = input("Enter sequence length.")
            self.input_seq = "".join(rd.choices(self.amino_data.amino_acid, k=int(ans2)))
        else:
            self.input_seq = input("Enter amino sequence")
        for i in range(len(self.input_seq)):
            if self.input_seq[i] == 'M':
                for i in range(self.possible_range):
                    self.possible_config[i].append('atg')
            elif self.input_seq[i] == 'L':
                self.possible_config[0].append('tta')
                self.possible_config[1].append('ttg')
                self.possible_config[2].append('ctt')
                self.possible_config[3].append('ctc')
                self.possible_config[4].append('cta')
                self.possible_config[5].append('ctg')
                self.possible_config[6].append(''.join(rd.choices(['tta','ttg','ctt','ctc','cta','ctg'],k=1)))
            elif self.input_seq[i] == 'F':
                self.possible_config[0].append('ttt')
                self.possible_config[1].append('ttc')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['ttt','ttc'],k=1)))
            elif self.input_seq[i] == 'S':
                self.possible_config[0].append('tct')
                self.possible_config[1].append('tcc')
                self.possible_config[2].append('tca')
                self.possible_config[3].append('tcg')
                self.possible_config[4].append('agc')
                self.possible_config[5].append('agt')
                self.possible_config[6].append(''.join(rd.choices(['tct','tcc','tca','tcg','agc','agt'],k=1)))
            elif self.input_seq[i] == 'T':
                self.possible_config[0].append('tat')
                self.possible_config[1].append('tac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['tat','tac'],k=1)))
            elif self.input_seq[i] == 'C':
                self.possible_config[0].append('tgt')
                self.possible_config[1].append('tgc')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['tgt','tgc'],k=1)))
            elif self.input_seq[i] == 'W':
                for i in range(self.possible_range):
                    self.possible_config[i].append('tgg')
            elif self.input_seq[i] == 'P':
                self.possible_config[0].append('ccc')
                self.possible_config[1].append('cca')
                self.possible_config[2].append('cct')
                self.possible_config[3].append('ccg')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['ccc','cca','cct','ccg'],k=1)))
            elif self.input_seq[i] == 'H':
                self.possible_config[0].append('cat')
                self.possible_config[1].append('cac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['cac','cat'],k=1)))
            elif self.input_seq[i] == 'Q':
                self.possible_config[0].append('caa')
                self.possible_config[1].append('cag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['caa','cag'],k=1)))
            elif self.input_seq[i] == 'R':
                self.possible_config[0].append('cgg')
                self.possible_config[1].append('cgt')
                self.possible_config[2].append('cgc')
                self.possible_config[3].append('cga')
                self.possible_config[4].append('agg')
                self.possible_config[5].append('aga')
                self.possible_config[6].append(''.join(rd.choices(['cgg','cgt','cgc','cga','agg','aga'],k=1)))
            elif self.input_seq[i] == 'I':
                self.possible_config[0].append('att')
                self.possible_config[1].append('atc')
                self.possible_config[2].append('ata')
                for i in range(self.possible_range-3):
                    self.possible_config[i+3].append(''.join(rd.choices(['att','atc','ata'],k=1)))
            elif self.input_seq[i] == 'V':
                self.possible_config[0].append('gtg')
                self.possible_config[1].append('gtt')
                self.possible_config[2].append('gtc')
                self.possible_config[3].append('gta')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['gtg','gtt','gtc','gta'],k=1)))
            elif self.input_seq[i] == 'T':
                self.possible_config[0].append('aca')
                self.possible_config[1].append('acc')
                self.possible_config[2].append('act')
                self.possible_config[3].append('acg')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['aca','acc','act','acg'],k=1)))
            elif self.input_seq[i] == 'A':
                self.possible_config[0].append('gcg')
                self.possible_config[1].append('gcc')
                self.possible_config[2].append('gct')
                self.possible_config[3].append('gca')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['gcg','gcc','gct','gca'],k=1)))
            elif self.input_seq[i] == 'N':
                self.possible_config[0].append('aat')
                self.possible_config[1].append('aac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['aat','aac'],k=1)))
            elif self.input_seq[i] == 'K':
                self.possible_config[0].append('aaa')
                self.possible_config[1].append('aag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['aaa','aag'],k=1)))
            elif self.input_seq[i] == 'E':
                self.possible_config[0].append('gaa')
                self.possible_config[1].append('gag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['gaa','gag'],k=1)))
            elif self.input_seq[i] == 'D':
                self.possible_config[0].append('gat')
                self.possible_config[1].append('gac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['gat','gac'],k=1)))
            elif self.input_seq[i] == 'G':
                self.possible_config[0].append('ggg')
                self.possible_config[1].append('gga')
                self.possible_config[2].append('ggc')
                self.possible_config[3].append('ggt')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['ggg','gga','ggc','ggt'],k=1)))
            elif self.input_seq[i] == 'X':
                for i in range(self.possible_range):
                    self.possible_config[i].append('taa')
            elif self.input_seq[i] == 'B':
                for i in range(self.possible_range):
                    self.possible_config[i].append('tag')
            elif self.input_seq[i] == 'Z':
                for i in range(self.possible_range):
                    self.possible_config[i].append('tga')
        print("Peptide sequence:\n{}".format(''.join(self.input_seq)))
        print("possible config 1:\n{}".format(''.join(self.possible_config[0])))
        print("possible config 2:\n{}".format(''.join(self.possible_config[1])))
        print("possible config 3:\n{}".format(''.join(self.possible_config[2])))
        print("possible config 4:\n{}".format(''.join(self.possible_config[3])))
        print("possible config 5:\n{}".format(''.join(self.possible_config[4])))
        print("possible config 6:\n{}".format(''.join(self.possible_config[5])))
        print("rd config 7:\n{}".format(''.join(self.possible_config[6])))

class Sequence_Method:
    def __init__(self):
        ans0 = input("Options: Amino translate(a) or DNA predict(d)")
        if ans0 == 'a':
            translate_choice = Translation()
        elif ans0 == 'd':
            predict_choice = Prediction()
            
run_program = Sequence_Method()
