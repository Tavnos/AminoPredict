import random as rd


class Nucleic_Base:
    adenine = {'char':'a', 'dna':'a','match':'t','rna':'a'}
    guanine = {'char':'g', 'dna':'g','match':'c','rna':'g'}
    cytosine = {'char':'c', 'dna':'c','match':'g','rna':'c'}
    thymine = {'char':'t', 'dna':'t','match':'a','rna':'u'}
    uracil = {'char':'u', 'dna':'t','match':'a','rna':'u'}
    all_nuc = (adenine, guanine, cytosine, thymine, uracil)
    nucleotide_letter = 'a', 't', 'g', 'c'
    def __init__(self):
        self.dna_typed = []
        self.rna_typed = []
        self.dna_match = []
        ans1 = input("Random sequence? (y/n)")
        if ans1 == 'y':
            ans2 = input("Enter sequence length.")
            self.input_seq = "".join(rd.choices(self.nucleotide_letter, k=int(ans2)))
        else: 
            self.input_seq = input("Enter dna sequence")
        for i in range(len(self.input_seq)):
            for f in range(len(self.all_nuc)):
                if self.input_seq[i] in self.all_nuc[f]['char']:
                    self.dna_typed.append(self.all_nuc[f]['dna'])
                    self.rna_typed.append(self.all_nuc[f]['rna'])
                    self.dna_match.append(self.all_nuc[f]['match'])
                    
class Amino_Acid:
    methionine = {'config':('atg'), 'name': 'Methionine', 'letter_code': 'M', 'tri_char': 'Met', 'amino_class': 'sulfuric', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 1.9, 'amino_weight': 149.208}
    leucine = {'config':('tta','ttg','ctt','ctc','cta','ctg'), 'name': 'leucine', 'letter_code': 'L', 'tri_char': 'Leu', 'amino_class': 'aliphatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 3.8, 'amino_weight': 131.175}
    phenylalanine = {'config':('ttt','ttc'),'name': 'phenylalanine', 'letter_code': 'F','tri_char': 'Phe','amino_class': 'aromatic','amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 2.8, 'amino_weight': 165.192}
    serine = {'config':('tct','tcc','tca','tcg','agc','agt'), 'name': 'serine', 'letter_code': 'S', 'tri_char': 'Ser', 'amino_class': 'hydroxylic', 'amino_polarity': 'polar', 'amino_charge': 'neutral', 'amino_hydropathy': 1.9, 'amino_weight': 149.208}
    cysteine = {'config':('tgt','tgc'), 'name': 'cysteine', 'letter_code': 'C', 'tri_char': 'Cys', 'amino_class': 'sulfuric', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 2.5, 'amino_weight': 121.154}
    tryptophan = {'config':('tgg'), 'name': 'tryptophan', 'letter_code': 'W', 'tri_char': 'Trp', 'amino_class': 'aromatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': -0.9, 'amino_weight': 204.228}
    proline = {'config':('ccc','cca','cct','ccg'), 'name': 'proline', 'letter_code': 'P', 'tri_char': 'Pro', 'amino_class': 'cyclic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': -1.6, 'amino_weight': 115.132}
    histidine = {'config':('cat','cac'), 'name': 'histidine', 'letter_code': 'H', 'tri_char': 'His', 'amino_class': 'basic-aromatic', 'amino_polarity': 'basic-polar', 'amino_charge': 'neutral-positive', 'amino_hydropathy': -3.2, 'amino_weight': 155.156}
    glutamine = {'config':('caa','cag'), 'name': 'glutamine', 'letter_code': 'Q', 'tri_char': 'Gln', 'amino_class': 'amide', 'amino_polarity': 'polar', 'amino_charge': 'neutral', 'amino_hydropathy': -3.5, 'amino_weight': 146.146}
    arginine = {'config':('cgg','cgt','cgc','cga','agg','aga'), 'name': 'arginine', 'letter_code': 'R', 'tri_char': 'Arg', 'amino_class': 'basic', 'amino_polarity': 'basic-polar', 'amino_charge': 'positive', 'amino_hydropathy': -4.5, 'amino_weight': 174.203}
    isoleucine = {'config':('att','atc','ata'), 'name': 'isoleucine', 'letter_code': 'I', 'tri_char': 'Ile', 'amino_class': 'aliphatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 4.5, 'amino_weight': 131.175}
    valine = {'config':('gtg','gtt','gtc','gta'), 'name': 'valine', 'letter_code': 'V', 'tri_char': 'Val', 'amino_class': 'aliphatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 4.2, 'amino_weight': 117.148}
    tyrosine = {'config':('tat','tac'), 'name': 'tyrosine', 'letter_code': 'Y', 'tri_char': 'Tyr', 'amino_class': 'aromatic', 'amino_polarity': 'polar', 'amino_charge': 'neutral', 'amino_hydropathy': -1.3, 'amino_weight': 181.191}
    threonine = {'config':('aca','acc','act','acg'), 'name': 'threonine', 'letter_code': 'T', 'tri_char': 'Thr', 'amino_class': 'hydroxylic', 'amino_polarity': 'polar', 'amino_charge': 'neutral', 'amino_hydropathy': -0.7, 'amino_weight': 119.119}
    alanine = {'config':('gcg','gcc','gct','gca'), 'name': 'alanine', 'letter_code': 'A', 'tri_char': 'Ala', 'amino_class': 'aliphatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': 1.8, 'amino_weight': 89.094}
    asparagine = {'config':('aat','aag'), 'name': 'asparagine', 'letter_code': 'N', 'tri_char': 'Asn', 'amino_class': 'amide', 'amino_polarity': 'polar', 'amino_charge': 'neutral', 'amino_hydropathy': -3.5, 'amino_weight': 132.119}
    lysine = {'config':('aaa','aag'), 'name': 'lysine', 'letter_code': 'K', 'tri_char': 'Lys', 'amino_class': 'basic', 'amino_polarity': 'basic-polar', 'amino_charge': 'positive', 'amino_hydropathy': -3.9, 'amino_weight': 146.189}
    glutamic = {'config':('gaa','gag'), 'name': 'glutamic', 'letter_code': 'E', 'tri_char': 'Glu', 'amino_class': 'acidic', 'amino_polarity': 'acidic-polar', 'amino_charge': 'negative', 'amino_hydropathy': -3.5, 'amino_weight': 147.131}
    aspartic = {'config':('gat','gac'), 'name': 'aspartic', 'letter_code': 'D', 'tri_char': 'Asp', 'amino_class': 'acidic', 'amino_polarity': 'acidic-polar', 'amino_charge': 'negative', 'amino_hydropathy': -3.5, 'amino_weight': 133.104}
    glycine = {'config':('ggg','gga','ggc','ggt'), 'name': 'glycine', 'letter_code': 'G', 'tri_char': 'Gly', 'amino_class': 'aliphatic', 'amino_polarity': 'non-polar', 'amino_charge': 'neutral', 'amino_hydropathy': -0.4, 'amino_weight': 133.104}
    ochre = {'config':('taa'), 'name': 'Ochre', 'letter_code': 'X', 'tri_char': '_Ochre', 'amino_class': 'Stop', 'amino_polarity': None, 'amino_charge': None, 'amino_hydropathy': None, 'amino_weight': None}
    amber = {'config':('tag'), 'name': 'Amber', 'letter_code': 'B', 'tri_char': '_Amber', 'amino_class': 'Stop', 'amino_polarity': None, 'amino_charge': None, 'amino_hydropathy': None, 'amino_weight': None}
    opal = {'config':('tga'), 'name': 'Opal', 'letter_code': 'Z', 'tri_char': '_Opal', 'amino_class': 'Stop', 'amino_polarity': None, 'amino_charge': None, 'amino_hydropathy': None, 'amino_weight': None}
    all_amino = (methionine, leucine, phenylalanine, serine, cysteine, tryptophan, proline, histidine, glutamine, arginine, isoleucine, valine, tyrosine, threonine, alanine, asparagine, lysine, glutamic, aspartic, glycine, ochre, amber, opal)
    amino_letter = 'M','L','F','S','T','C','W','P','H','Q','R','I','V','T','A','N','K','E','D','G','X','B','Z'
    def __init__(self):
        self.nb_call = Nucleic_Base()
        self.direct_start_index = []
        self.reversed_start_index = []
        self.direct_sequences = []
        self.possible_chain = {}
        self.stopped_chains = {}
        self.stopped_chains_list = []
        self.translated_chains_letter = []
        self.translated_chains_chars = []
        self.translated_chains_weight = []
        self.translated_chains_hydropathy = []
        self.translated_chains_class = []
        self.translated_chains_polarity = []
        self.translated_chains_charge = []
        self.translated_chains_name = []
        self.chain_sequence = ''.join(self.nb_call.dna_typed)
        self.nb_call.dna_typed.reverse()
        self.reversed_sequence = ''.join(self.nb_call.dna_typed)
        self.nb_call.dna_typed.reverse()
        for i in range(len(self.chain_sequence)):
            if self.chain_sequence[i:i+3] == self.methionine['config']:
                self.direct_start_index.append(i)
        for i in range(len(self.reversed_sequence)):
            if self.reversed_sequence[i:i+3] == self.methionine['config']:
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
                if codon == self.opal['config'] or codon == self.amber['config'] or codon == self.ochre['config']:
                    stop_index = self.possible_chain[chain_names].index(codon)+1
                    self.stopped_chains[chain_names] = self.possible_chain[chain_names][0:stop_index]
        for i in self.stopped_chains:
            self.stopped_chains_list.append(self.stopped_chains[i])
        for i in range(len(self.stopped_chains_list)):
            self.translated_chains_letter.append([])
            self.translated_chains_chars.append([])
            self.translated_chains_weight.append([])
            self.translated_chains_hydropathy.append([])
            self.translated_chains_class.append([])
            self.translated_chains_polarity.append([])
            self.translated_chains_charge.append([])
            self.translated_chains_name.append([])
            for f in range(len(self.stopped_chains_list[i])):
                for k in range(len(self.all_amino)):
                    if self.stopped_chains_list[i][f] in self.all_amino[k]['config']:
                        self.translated_chains_letter[i].append(self.all_amino[k]['letter_code'])
                        self.translated_chains_chars[i].append(self.all_amino[k]['tri_char'])
                        self.translated_chains_weight[i].append(self.all_amino[k]['amino_weight'])
                        self.translated_chains_hydropathy[i].append(self.all_amino[k]['amino_hydropathy'])
                        self.translated_chains_class[i].append(self.all_amino[k]['amino_class'])
                        self.translated_chains_polarity[i].append(self.all_amino[k]['amino_polarity'])
                        self.translated_chains_charge[i].append(self.all_amino[k]['amino_charge'])
                        self.translated_chains_name[i].append(self.all_amino[k]['name'])
        print("dna_typed:\n {}".format(''.join(self.nb_call.dna_typed)))
        print("rna_typed:\n {}".format(''.join(self.nb_call.rna_typed)))
        print("dna_match:\n {}".format(''.join(self.nb_call.dna_match)))
        print("Peptide 1 letter:\n {}".format(self.translated_chains_letter))
        print("Peptide 3 letter:\n {}".format(self.translated_chains_chars))
        print("Peptide weight:\n {}".format(self.translated_chains_weight))
        print("Peptide hydropathy:\n {}".format(self.translated_chains_hydropathy))
        print("Peptide class:\n {}".format(self.translated_chains_class))
        print("Peptide polarity:\n {}".format(self.translated_chains_polarity))
        print("Peptide charge:\n {}".format(self.translated_chains_charge))
        print("Peptide names:\n {}".format(self.translated_chains_name))
        
class DNA_Prediction:
    possible_config = [[],[],[],[],[],[],[]]
    possible_range = 7
    def __init__(self):
        ans1 = input("Random sequence? (y/n)")
        if ans1 == 'y':
            ans2 = input("Enter sequence length.")
            self.input_seq = "".join(rd.choices(self.amino_list, k=ans2))
        else:
            self.input_seq = input("Enter amino sequence")
        for i in range(len(self.input_seq)):
            if self.input_seq[i] == 'M':
                for i in range(self.possible_range):
                    self.possible_config[i].append('atg')
            if self.input_seq[i] == 'L':
                self.possible_config[0].append('tta')
                self.possible_config[1].append('ttg')
                self.possible_config[2].append('ctt')
                self.possible_config[3].append('ctc')
                self.possible_config[4].append('cta')
                self.possible_config[5].append('ctg')
                self.possible_config[6].append(''.join(rd.choices(['tta','ttg','ctt','ctc','cta','ctg'],k=1)))
            if self.input_seq[i] == 'F':
                self.possible_config[0].append('ttt')
                self.possible_config[1].append('ttc')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['ttt','ttc'],k=1)))
            if self.input_seq[i] == 'S':
                self.possible_config[0].append('tct')
                self.possible_config[1].append('tcc')
                self.possible_config[2].append('tca')
                self.possible_config[3].append('tcg')
                self.possible_config[4].append('agc')
                self.possible_config[5].append('agt')
                self.possible_config[6].append(''.join(rd.choices(['tct','tcc','tca','tcg','agc','agt'],k=1)))
            if self.input_seq[i] == 'T':
                self.possible_config[0].append('tat')
                self.possible_config[1].append('tac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['tat','tac'],k=1)))
            if self.input_seq[i] == 'C':
                self.possible_config[0].append('tgt')
                self.possible_config[1].append('tgc')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['tgt','tgc'],k=1)))
            if self.input_seq[i] == 'W':
                for i in range(self.possible_range):
                    self.possible_config[i].append('tgg')
            if self.input_seq[i] == 'P':
                self.possible_config[0].append('ccc')
                self.possible_config[1].append('cca')
                self.possible_config[2].append('cct')
                self.possible_config[3].append('ccg')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['ccc','cca','cct','ccg'],k=1)))
            if self.input_seq[i] == 'H':
                self.possible_config[0].append('cat')
                self.possible_config[1].append('cac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['cac','cat'],k=1)))
            if self.input_seq[i] == 'Q':
                self.possible_config[0].append('caa')
                self.possible_config[1].append('cag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['caa','cag'],k=1)))
            if self.input_seq[i] == 'R':
                self.possible_config[0].append('cgg')
                self.possible_config[1].append('cgt')
                self.possible_config[2].append('cgc')
                self.possible_config[3].append('cga')
                self.possible_config[4].append('agg')
                self.possible_config[5].append('aga')
                self.possible_config[6].append(''.join(rd.choices(['cgg','cgt','cgc','cga','agg','aga'],k=1)))
            if self.input_seq[i] == 'I':
                self.possible_config[0].append('att')
                self.possible_config[1].append('atc')
                self.possible_config[2].append('ata')
                for i in range(self.possible_range-3):
                    self.possible_config[i+3].append(''.join(rd.choices(['att','atc','ata'],k=1)))
            if self.input_seq[i] == 'V':
                self.possible_config[0].append('gtg')
                self.possible_config[1].append('gtt')
                self.possible_config[2].append('gtc')
                self.possible_config[3].append('gta')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['gtg','gtt','gtc','gta'],k=1)))
            if self.input_seq[i] == 'T':
                self.possible_config[0].append('aca')
                self.possible_config[1].append('acc')
                self.possible_config[2].append('act')
                self.possible_config[3].append('acg')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['aca','acc','act','acg'],k=1)))
            if self.input_seq[i] == 'A':
                self.possible_config[0].append('gcg')
                self.possible_config[1].append('gcc')
                self.possible_config[2].append('gct')
                self.possible_config[3].append('gca')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['gcg','gcc','gct','gca'],k=1)))
            if self.input_seq[i] == 'N':
                self.possible_config[0].append('aat')
                self.possible_config[1].append('aac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['aat','aac'],k=1)))
            if self.input_seq[i] == 'K':
                self.possible_config[0].append('aaa')
                self.possible_config[1].append('aag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['aaa','aag'],k=1)))
            if self.input_seq[i] == 'E':
                self.possible_config[0].append('gaa')
                self.possible_config[1].append('gag')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['gaa','gag'],k=1)))
            if self.input_seq[i] == 'D':
                self.possible_config[0].append('gat')
                self.possible_config[1].append('gac')
                for i in range(self.possible_range-2):
                    self.possible_config[i+2].append(''.join(rd.choices(['gat','gac'],k=1)))
            if self.input_seq[i] == 'G':
                self.possible_config[0].append('ggg')
                self.possible_config[1].append('gga')
                self.possible_config[2].append('ggc')
                self.possible_config[3].append('ggt')
                for i in range(self.possible_range-4):
                    self.possible_config[i+4].append(''.join(rd.choices(['ggg','gga','ggc','ggt'],k=1)))
            if self.input_seq[i] == 'X':
                for i in range(self.possible_range):
                    self.possible_config[i].append('taa')
            if self.input_seq[i] == 'B':
                for i in range(self.possible_range):
                    self.possible_config[i].append('tag')
            if self.input_seq[i] == 'Z':
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
            translate_choice = Amino_Acid()
        elif ans0 == 'd':
            predict_choice = DNA_Prediction()
            
sm_run = Sequence_Method()
