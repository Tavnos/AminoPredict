import random as rd


class Method_Data:
    data_dict={   'nucleic':{'a':{'dna':'a','rna':'a'},
                             'g':{'dna':'g','rna':'g'},
                             'c':{'dna':'c','rna':'c'},
                             't':{'dna':'t','rna':'u'},
                             'u':{'dna':'t','rna':'u'}},
                    'amino':{'M':{'abv':'Met',  'atp_cost':(21,23), 'mitp':131.04049, 's_c':'-CH₂CH₂SCH₃',        'config':(['atg'])},
                             'L':{'abv':'Leu',  'atp_cost':(-9,1),  'mitp':113.08406, 's_c':'-CH₂CH(CH₃)₂',       'config':('tta','ttg','ctt','ctc','cta','ctg')},
                             'F':{'abv':'Phe',  'atp_cost':(-6,2),  'mitp':147.06841, 's_c':'-CH₂C₆H₅',           'config':('ttt','ttc')},
                             'S':{'abv':'Ser',  'atp_cost':(-2,2),  'mitp':87.03203,  's_c':'-CH₂OH',            'config':('tct','tcc','tca','tcg','agc','agt')},
                             'C':{'abv':'Cys',  'atp_cost':(11,15), 'mitp':103.00919, 's_c':'-CH₂SH',            'config':('tgt','tgc')},
                             'W':{'abv':'Trp',  'atp_cost':(-7,7),  'mitp':186.07931, 's_c':'-CH₂C₈H₆N',          'config':(['tgg'])},
                             'P':{'abv':'Pro',  'atp_cost':(-2,4),  'mitp':97.05276,  's_c':'-CH₂CH₂CH₂-',         'config':('ccc','cca','cct','ccg')},
                             'H':{'abv':'His',  'atp_cost':(1,7),   'mitp':137.05891, 's_c':'-CH₂-C₃H₃N₂',         'config':('cat','cac')},
                             'Q':{'abv':'Gln',  'atp_cost':(-6,0),  'mitp':128.05858, 's_c':'-CH₂CH₂CONH₂',       'config':('caa','cag')},
                             'R':{'abv':'Arg',  'atp_cost':(5,13),  'mitp':156.10111, 's_c':'-(CH₂)₃NH-C(NH)NH₂', 'config':('cgg','cgt','cgc','cga','agg','aga')},
                             'I':{'abv':'Ile',  'atp_cost':(7,11),  'mitp':113.08406, 's_c':'-CH(CH₃)CH₂CH₃',     'config':('att','atc','ata')},
                             'V':{'abv':'Val',  'atp_cost':(-2,2),  'mitp':99.07931,  's_c':'-CH(CH₃)₂',          'config':('gtg','gtt','gtc','gta')},
                             'Y':{'abv':'Tyr',  'atp_cost':(-8,2),  'mitp':163.06333, 's_c':'-CH₂-C₆H₄OH',        'config':('tat','tac')},
                             'T':{'abv':'Thr',  'atp_cost':(6,8),   'mitp':101.04768, 's_c':'-CH(OH)CH₃',        'config':('aca','acc','act','acg')},
                             'A':{'abv':'Ala',  'atp_cost':(-1,1),  'mitp':71.03711,  's_c':'-CH₃',              'config':('gcg','gcc','gct','gca')},
                             'N':{'abv':'Asn',  'atp_cost':(3,5),   'mitp':114.04293, 's_c':'-CH₂CONH₂',         'config':('aat','aac')},
                             'K':{'abv':'Lys',  'atp_cost':(5,9),   'mitp':128.09496, 's_c':'-(CH₂)₄NH₂',         'config':('aaa','aag')},
                             'E':{'abv':'Glu',  'atp_cost':(-7,-1), 'mitp':129.04259, 's_c':'-CH₂CH₂COOH',        'config':('gaa','gag')},
                             'D':{'abv':'Asp',  'atp_cost':(0,2),   'mitp':115.02694, 's_c':'-CH₂COOH',          'config':('gat','gac')},
                             'G':{'abv':'Gly',  'atp_cost':(-2,2),  'mitp':57.02146,  's_c':'-(H)',             'config':('ggg','gga','ggc','ggt')},
                             'O':{'abv':'Ochre','atp_cost':(0,0),   'mitp':0,         's_c':'^',                'config':(['taa'])},
                             'B':{'abv':'Amber','atp_cost':(0,0),   'mitp':0,         's_c':'^',                'config':(['tag'])},
                             'U':{'abv':'Opal', 'atp_cost':(0,0),   'mitp':0,         's_c':'^',                'config':(['tga'])}}}

class Prediction(Method_Data):
    def get_specific_content(self, codon_config, desired_content):
        self.rd_set_ls = []
        self.index_max_ls = []
        self.codon_pref_ls = []
        if desired_content != 'any':
            for i in codon_config:
                self.rd_set_ls += [(i.count(desired_content[0])+i.count(desired_content[1]))]
            for i in range(len(self.rd_set_ls)):
                if self.rd_set_ls[i] == max(self.rd_set_ls):
                    self.index_max_ls += [i]
            for i in self.index_max_ls:
                self.codon_pref_ls += [codon_config[i]]
        if desired_content == 'any':
            self.codon_pref_ls = codon_config
        return rd.choice(self.codon_pref_ls)
    def predict_sequence(self, sequence_typed, desired_content):
        self.possible_config = []
        self.cg_count = 0
        self.at_count = 0
        for i in sequence_typed:
            self.temp_config = self.data_dict['amino'][i]['config']
            self.possible_config += [self.get_specific_content(self.temp_config, desired_content)]
        self.predict_1 = "Peptide sequence typed:"
        self.predict_1_1 = (''.join(sequence_typed))
        self.predict_2 = "desired config:"
        self.predict_2_1 = ''.join(self.possible_config)
        self.chr_split = []
        for i in self.predict_2_1:
            self.chr_split += i
        self.cg_count = self.chr_split.count('c') + self.chr_split.count('g')
        self.at_count = self.chr_split.count('a') + self.chr_split.count('t')
        self.predict_3 = '{} % gc'.format((self.cg_count/len(self.chr_split))*100)
        self.predict_3_1 = '{} % at'.format((self.at_count/len(self.chr_split))*100)
        return '{}\n{}\n{}\n{}\n{}\n{}'.format(self.predict_1, self.predict_1_1, self.predict_2, self.predict_2_1, self.predict_3, self.predict_3_1)

class Translate_Data(Method_Data):
    def translate_nucleotides(self, str_input):
        self.dna_typed_ls = []
        self.rna_typed_ls = []
        self.amino_short_ls = []
        self.amino_abv_ls = []
        self.amino_aerobic_atp_ls = []
        self.amino_anaerobic_atp_ls = []
        self.amino_monoisotopic_mass_ls = []
        self.amino_side_chain_ls = []
        self.nuc_transcript = str_input.lower()
        for i in self.nuc_transcript:
            self.dna_typed_ls += self.data_dict['nucleic'][i]['dna']
            self.rna_typed_ls += self.data_dict['nucleic'][i]['rna']
        self.dna_direct_str = ''.join(self.dna_typed_ls)
        self.rna_direct_str = ''.join(self.rna_typed_ls)
        for i in range(0, len(self.dna_direct_str), 3):
            for f in self.data_dict['amino']:
                if self.dna_direct_str[i:i+3] in self.data_dict['amino'][f]['config']:
                    self.amino_short_ls += f
                    self.amino_abv_ls += self.data_dict['amino'][f]['abv']
                    self.amino_aerobic_atp_ls += [self.data_dict['amino'][f]['atp_cost'][0]]
                    self.amino_anaerobic_atp_ls += [self.data_dict['amino'][f]['atp_cost'][1]]
                    self.amino_monoisotopic_mass_ls += [self.data_dict['amino'][f]['mitp']]
                    self.amino_side_chain_ls += self.data_dict['amino'][f]['s_c']
        self.amino_short_str = ''.join(self.amino_short_ls)
        self.amino_abv_str = ''.join(self.amino_abv_ls)
        self.amino_aerobic_atp_tot = sum(self.amino_aerobic_atp_ls)
        self.amino_anaerobic_atp_tot = sum(self.amino_anaerobic_atp_ls)
        self.amino_monoisotopic_mass_tot = sum(self.amino_monoisotopic_mass_ls)
        self.amino_side_chain_str = ''.join(self.amino_side_chain_ls)
    def print_translation(self, str_input):
        self.translate_nucleotides(str_input)
        self.str_var_1 = 'DNA: ' + self.dna_direct_str.upper()
        self.str_var_2 = 'RNA: ' + self.rna_direct_str.upper()
        self.str_var_3 = 'Oligo-peptide Short: ' + self.amino_short_str
        self.str_var_4 = 'Oligo-peptide Abbreviated: ' 
        self.str_var_5 = self.amino_abv_str
        self.str_var_6 = 'Oligo-peptide aerobic cost: ' + str(self.amino_aerobic_atp_tot) + ' ATP'
        self.str_var_7 = 'Oligo-peptide anaerobic cost: ' + str(self.amino_anaerobic_atp_tot) + ' ATP'
        self.str_var_8 = 'Oligo-peptide monoisotopic mass: ' + str(round(self.amino_monoisotopic_mass_tot, 2)) + ' Da'
        self.str_var_9 = 'Oligo-peptide sidechain functional group:'
        self.str_var_10 = self.amino_side_chain_str 
        return '{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(self.str_var_1, self.str_var_2, self.str_var_3, self.str_var_4, 
             self.str_var_5, self.str_var_6, self.str_var_7, self.str_var_8, self.str_var_9, self.str_var_10)
    


class Simple_Query(Prediction, Translate_Data):
    def start_method(self):
        print('type P to get random DNA sequence or with specific GC/AT content from peptide')
        print('type T to translate DNA sequence into peptide and get peptide stat')
        print('type X to exit')
        self.input_answer = input('')
        return self.input_answer
    def __init__(self):
        self.start_method()
        if self.input_answer.upper() == 'P':
            print('input desired peptide')
            self.peptide_answer = input('')
            print('input desired content as gc, at or any')
            self.content_answer = input('')
            print(self.predict_sequence(self.peptide_answer,self.content_answer))
            return 
        elif self.input_answer.upper() == 'T':
            print('input DNA to be translated')
            self.dna_answer = input('')
            print(self.print_translation(self.dna_answer))
            return 
        elif self.input_answer.upper() == 'X':
            return
        else:
            print('could not understand what was typed try again')
            self.start_method()