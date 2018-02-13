import random

def translate_n_seq():
    dna_list = 'a','t','g','c'
    ans1 = input("Random DNA sequence? y/n")
    if ans1 == 'y':
        print("Choose length:")
        seq_len = int(input())
        input_seq = "".join(random.choices(dna_list,k = seq_len))
    elif ans1 != 'y':
        input_seq = "".join(input("Type sequence:"))
        seq_len = len(input_seq)
    dna_typed = []
    rna_typed = []
    dna_match = []
    unstopped_direct_chain_dict = {}
    unstopped_reversed_chain_dict = {}
    unstopped_chain_dict = {}
    unstopped_chain_codon_dict = {}
    possible_chain_dict = {}
    index_start_pos = []
    r_index_start_pos = []
    chain_list = []
    formated_possible_chain_list = []
    seq_len = len(input_seq)
    amino_chars_dict = {}
    amino_letter_dict = {}
    for i in range(seq_len):
        if input_seq[i] == 'a':
            dna_typed.append('a')
            dna_match.append('t')
            rna_typed.append('a')
        elif input_seq[i] == 't':
            dna_typed.append('t')
            dna_match.append('a')
            rna_typed.append('u')
        elif input_seq[i] == 'g':
            dna_typed.append('g')
            dna_match.append('c')
            rna_typed.append('g')
        elif input_seq[i] == 'c':
            dna_typed.append('c')
            dna_match.append('g')
            rna_typed.append('c')
        elif input_seq[i] == 'u':
            dna_typed.append('t')
            dna_match.append('a')
            rna_typed.append('u')
        else:
            pass
    dna_seq = ''.join(dna_typed)
    input_len = len(dna_seq)
    dna_list = list(dna_seq)
    dna_list.reverse()
    reversed_seq = "".join(dna_list)
    for i in range(input_len):
        if dna_seq[i:i+3] == 'atg':
            index_start_pos.append(i)
    for i in range(input_len):
        if reversed_seq[i:i+3] == 'atg':
            r_index_start_pos.append(i)  
    for i in range(len(index_start_pos)):
        unstopped_direct_chain_dict["dchain{}".format(i)] = dna_seq[index_start_pos[i]:]
    for i in range(len(r_index_start_pos)):
        unstopped_reversed_chain_dict["rchain{}".format(i)] = dna_seq[index_start_pos[i]:]
    for i in range(len(index_start_pos)):
        chain_list.append(unstopped_direct_chain_dict['dchain{}'.format(i)])
    for i in range(len(r_index_start_pos)):
        chain_list.append(unstopped_reversed_chain_dict['rchain{}'.format(i)])
    start_pos_ammount = len(index_start_pos) + len(r_index_start_pos)
    for i in range(start_pos_ammount):
        chain_names = "chain{}".format(i)
        unstopped_chain_dict[chain_names] = chain_list[i]
        for f in range(len(unstopped_chain_dict[chain_names])):
            chain_sizes = len(unstopped_chain_dict[chain_names])
            unstopped_chain_codon_dict[chain_names] = [unstopped_chain_dict[chain_names][f:f+3] for f in range(0, chain_sizes, 3)]
    for i in range(start_pos_ammount):
        chain_names = "chain{}".format(i)
        codon_sizes = len(unstopped_chain_codon_dict[chain_names])
        for f in range(codon_sizes):
            tri_codon = unstopped_chain_codon_dict[chain_names][f]
            if tri_codon == 'tga' or tri_codon == 'tag' or tri_codon == 'taa':
                stop_pos_index = unstopped_chain_codon_dict[chain_names].index(tri_codon)+1
                possible_chain_dict[chain_names] = unstopped_chain_codon_dict[chain_names][0:stop_pos_index]
    for n in possible_chain_dict:
        formated_possible_chain_list.append(possible_chain_dict[n])
    total_chain_ammount = len(formated_possible_chain_list)
    for i in range(total_chain_ammount):
        chain_names = "chain{}".format(i)
        codon_sizes = len(formated_possible_chain_list[i])
        amino_chars_dict[chain_names] = []
        amino_letter_dict[chain_names] = []
        for f in range(codon_sizes):
            tri_codon = formated_possible_chain_list[i][f]
            if tri_codon == 'atg':
                amino_chars_dict[chain_names].append('Met')
                amino_letter_dict[chain_names].append('M')
            elif tri_codon == 'tta' or tri_codon == 'ttg' or tri_codon == 'ctt' or tri_codon == 'ctc' or tri_codon == 'cta' or tri_codon == 'ctg':
                amino_chars_dict[chain_names].append('Leu')
                amino_letter_dict[chain_names].append('L')
            elif tri_codon == 'ttt' or tri_codon == 'ttc':
                amino_chars_dict[chain_names].append('Phe')
                amino_letter_dict[chain_names].append('F')
            elif tri_codon ==  'tct' or tri_codon == 'tcc' or tri_codon == 'tca' or tri_codon == 'tcg' or tri_codon == 'agc' or tri_codon == 'agt':
                amino_chars_dict[chain_names].append('Ser')
                amino_letter_dict[chain_names].append('S')
            elif tri_codon == 'tat' or tri_codon == 'tac':
                amino_chars_dict[chain_names].append('Tyr')
                amino_letter_dict[chain_names].append('T')
            elif tri_codon == 'tgt' or tri_codon == 'tgc':
                amino_chars_dict[chain_names].append('Cys')
                amino_letter_dict[chain_names].append('C')
            elif tri_codon == 'tgg':
                amino_chars_dict[chain_names].append('Trp')
                amino_letter_dict[chain_names].append('W')
            elif tri_codon == 'ccc' or tri_codon == 'cca' or tri_codon == 'cct' or tri_codon == 'ccg':
                amino_chars_dict[chain_names].append('Pro')
                amino_letter_dict[chain_names].append('P')
            elif tri_codon == 'cat' or tri_codon == 'cac':
                amino_chars_dict[chain_names].append('His')
                amino_letter_dict[chain_names].append('H')
            elif tri_codon == 'caa' or tri_codon == 'cag':
                amino_chars_dict[chain_names].append('Gln')
                amino_letter_dict[chain_names].append('Q')
            elif tri_codon == 'cgg' or tri_codon == 'cgt' or tri_codon == 'cgc' or tri_codon == 'cga' or tri_codon == 'agg' or tri_codon == 'aga':
                amino_chars_dict[chain_names].append('Arg')
                amino_letter_dict[chain_names].append('R')
            elif tri_codon == 'att' or tri_codon == 'atc' or tri_codon == 'ata':
                amino_chars_dict[chain_names].append('Ile')
                amino_letter_dict[chain_names].append('I')
            elif tri_codon == 'gtg' or tri_codon == 'gtt' or tri_codon == 'gtc' or tri_codon == 'gta':
                amino_chars_dict[chain_names].append('Val')
                amino_letter_dict[chain_names].append('V')
            elif tri_codon == 'aca' or tri_codon == 'acc' or tri_codon == 'act' or tri_codon == 'acg':
                amino_chars_dict[chain_names].append('Thr')
                amino_letter_dict[chain_names].append('T')
            elif tri_codon == 'gcg' or tri_codon == 'gcc' or tri_codon == 'gct' or tri_codon == 'gca':
                amino_chars_dict[chain_names].append('Ala')
                amino_letter_dict[chain_names].append('A')
            elif tri_codon == 'aat' or tri_codon == 'aac':
                amino_chars_dict[chain_names].append('Asn')
                amino_letter_dict[chain_names].append('N')
            elif tri_codon == 'aaa' or tri_codon == 'aag':
                amino_chars_dict[chain_names].append('Lys')
                amino_letter_dict[chain_names].append('K')
            elif tri_codon == 'gaa' or tri_codon == 'gag':
                amino_chars_dict[chain_names].append('Glu')
                amino_letter_dict[chain_names].append('E')
            elif tri_codon == 'gat' or tri_codon == 'gac':
                amino_chars_dict[chain_names].append('Asp')
                amino_letter_dict[chain_names].append('D')
            elif tri_codon == 'ggg' or tri_codon == 'gga' or tri_codon == 'ggc' or tri_codon == 'ggt':                
                amino_chars_dict[chain_names].append('Gly')
                amino_letter_dict[chain_names].append('G')
            elif tri_codon == 'taa':
                amino_chars_dict[chain_names].append('Ochre')
                amino_letter_dict[chain_names].append('X')
            elif tri_codon == 'tag':
                amino_chars_dict[chain_names].append('Amber')
                amino_letter_dict[chain_names].append('B')
            elif tri_codon == 'tga':
                amino_chars_dict[chain_names].append('Opal')
                amino_letter_dict[chain_names].append('Z')
    print("Nucleotides ammount:{}".format(len(dna_typed)))
    print("DNA:\n{}".format(''.join(dna_typed)))
    print("Match:\n{}".format(''.join(dna_match)))
    print("RNA:\n{}".format(''.join(rna_typed)))
    print("Amino possible chain chars:\n{}".format(amino_chars_dict))
    print("Amino possible chain letters:\n{}".format(amino_letter_dict))
def translate_a_seq():
    amino_name_typed = []
    amino_letter_typed = []
    possible_config0 = []
    possible_config1 = []
    possible_config2 = []
    possible_config3 = []
    possible_config4 = []
    possible_config5 = []
    possible_config6 = []
    reader = 0
    amino_list = 'M','L','F','S','T','C','W','P','H','Q','R','I','V','T','A','N','K','E','D','G','X','B','Z'
    ans1 = input("Random amino sequence? y/n")
    if ans1 == 'y':
        print("Choose length:")
        seq_len = int(input())
        input_seq = "".join(random.choices(amino_list,k = seq_len))
    elif ans1 != 'y':
        input_seq = "".join(input("Type sequence:"))
        seq_len = len(input_seq)
    while reader < seq_len-1:
        for x_amino in input_seq:
            if input_seq[reader] == 'M':
                amino_name_typed.append('(Start)Methionine')
                amino_letter_typed.append('*Met')
                possible_config0.append('atg')
                possible_config1.append('atg')
                possible_config2.append('atg')
                possible_config3.append('atg')
                possible_config4.append('atg')
                possible_config5.append('atg')
                possible_config6.append('atg')
                reader += 1
                pass
            elif input_seq[reader] == 'L':
                amino_name_typed.append('Leucine')
                amino_letter_typed.append('Leu')
                possible_config0.append('tta')
                possible_config1.append('ttg')
                possible_config2.append('ctt')
                possible_config3.append('ctc')
                possible_config4.append('cta')
                possible_config5.append('ctg')
                possible_config6.append(''.join(random.choices(['tta','ttg','ctt','ctc','cta','ctg'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'F':
                amino_name_typed.append('Phenylalanine')
                amino_letter_typed.append('Phe')
                possible_config0.append('ttt')
                possible_config1.append('ttc')
                possible_config2.append(''.join(random.choices(['ttt','ttc'],k=1)))
                possible_config3.append(''.join(random.choices(['ttt','ttc'],k=1)))
                possible_config4.append(''.join(random.choices(['ttt','ttc'],k=1)))
                possible_config5.append(''.join(random.choices(['ttt','ttc'],k=1)))
                possible_config6.append(''.join(random.choices(['ttt','ttc'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'S':
                amino_name_typed.append('Serine')
                amino_letter_typed.append('Ser')
                possible_config0.append('tct')
                possible_config1.append('tcc')
                possible_config2.append('tca')
                possible_config3.append('tcg')
                possible_config4.append('agc')
                possible_config5.append('agt')
                possible_config6.append(''.join(random.choices(['tct','tcc','tca','tcg','agc','agt'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'T':
                amino_name_typed.append('Tyrosine')
                amino_letter_typed.append('Tyr')
                possible_config0.append('tat')
                possible_config1.append('tac')
                possible_config2.append(''.join(random.choices(['tat','tac'],k=1)))
                possible_config3.append(''.join(random.choices(['tat','tac'],k=1)))
                possible_config4.append(''.join(random.choices(['tat','tac'],k=1)))
                possible_config5.append(''.join(random.choices(['tat','tac'],k=1)))
                possible_config6.append(''.join(random.choices(['tat','tac'],k=1)))
                reader += 1
                pass

            elif input_seq[reader] == 'C':
                amino_name_typed.append('Cysteine')
                amino_letter_typed.append('Cys')
                possible_config0.append('tgt')
                possible_config1.append('tgc')
                possible_config2.append(''.join(random.choices(['tgt','tgc'],k=1)))
                possible_config3.append(''.join(random.choices(['tgt','tgc'],k=1)))
                possible_config4.append(''.join(random.choices(['tgt','tgc'],k=1)))
                possible_config5.append(''.join(random.choices(['tgt','tgc'],k=1)))
                possible_config6.append(''.join(random.choices(['tgt','tgc'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'W':
                amino_name_typed.append('Tryptophan')
                amino_letter_typed.append('Trp')
                possible_config0.append('tgg')
                possible_config1.append('tgg')
                possible_config2.append('tgg')
                possible_config3.append('tgg')
                possible_config4.append('tgg')
                possible_config5.append('tgg')
                possible_config6.append('tgg')
                reader += 1
                pass
            elif input_seq[reader] == 'P':
                amino_name_typed.append('Proline')
                amino_letter_typed.append('Pro')
                possible_config0.append('ccc')
                possible_config1.append('cca')
                possible_config2.append('cct')
                possible_config3.append('ccg')
                possible_config4.append(''.join(random.choices(['ccc','cca','cct','ccg'],k=1)))
                possible_config5.append(''.join(random.choices(['ccc','cca','cct','ccg'],k=1)))
                possible_config6.append(''.join(random.choices(['ccc','cca','cct','ccg'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'H':
                amino_name_typed.append('Histidine')
                amino_letter_typed.append('His')
                possible_config0.append('cat')
                possible_config1.append('cac')
                possible_config2.append(''.join(random.choices(['cac','cat'],k=1)))
                possible_config3.append(''.join(random.choices(['cac','cat'],k=1)))
                possible_config4.append(''.join(random.choices(['cac','cat'],k=1)))
                possible_config5.append(''.join(random.choices(['cac','cat'],k=1)))
                possible_config5.append(''.join(random.choices(['cac','cat'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'Q':
                amino_name_typed.append('Glutamine')
                amino_letter_typed.append('Gln')
                possible_config0.append('caa')
                possible_config1.append('cag')
                possible_config2.append(''.join(random.choices(['caa','cag'],k=1)))
                possible_config3.append(''.join(random.choices(['caa','cag'],k=1)))
                possible_config4.append(''.join(random.choices(['caa','cag'],k=1)))
                possible_config5.append(''.join(random.choices(['caa','cag'],k=1)))
                possible_config6.append(''.join(random.choices(['caa','cag'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'R':
                amino_name_typed.append('Arginine')
                amino_letter_typed.append('Arg')
                possible_config0.append('cgg')
                possible_config1.append('cgt')
                possible_config2.append('cgc')
                possible_config3.append('cga')
                possible_config4.append('agg')
                possible_config5.append('aga')
                possible_config6.append(''.join(random.choices(['cgg','cgt','cgc','cga','agg','aga'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'I':
                amino_name_typed.append('Isoleucine')
                amino_letter_typed.append('Ile')
                possible_config0.append('att')
                possible_config1.append('atc')
                possible_config2.append('ata')
                possible_config3.append(''.join(random.choices(['att','atc','ata'],k=1)))
                possible_config4.append(''.join(random.choices(['att','atc','ata'],k=1)))
                possible_config5.append(''.join(random.choices(['att','atc','ata'],k=1)))
                possible_config6.append(''.join(random.choices(['att','atc','ata'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'V':
                amino_name_typed.append('Valine')
                amino_letter_typed.append('Val')
                possible_config0.append('gtg')
                possible_config1.append('gtt')
                possible_config2.append('gtc')
                possible_config3.append('gta')
                possible_config4.append(''.join(random.choices(['gtg','gtt','gtc','gta'],k=1)))
                possible_config5.append(''.join(random.choices(['gtg','gtt','gtc','gta'],k=1)))
                possible_config6.append(''.join(random.choices(['gtg','gtt','gtc','gta'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'T':
                amino_name_typed.append('Threonine')
                amino_letter_typed.append('Thr')
                possible_config0.append('aca')
                possible_config1.append('acc')
                possible_config2.append('act')
                possible_config3.append('acg')
                possible_config4.append(''.join(random.choices(['aca','acc','act','acg'],k=1)))
                possible_config5.append(''.join(random.choices(['aca','acc','act','acg'],k=1)))
                possible_config6.append(''.join(random.choices(['aca','acc','act','acg'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'A':
                amino_name_typed.append('Alanine')
                amino_letter_typed.append('Ala')
                possible_config0.append('gcg')
                possible_config1.append('gcc')
                possible_config2.append('gct')
                possible_config3.append('gca')
                possible_config4.append(''.join(random.choices(['gcg','gcc','gct','gca'],k=1)))
                possible_config5.append(''.join(random.choices(['gcg','gcc','gct','gca'],k=1)))
                possible_config6.append(''.join(random.choices(['gcg','gcc','gct','gca'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'N':
                amino_name_typed.append('Asparagine')
                amino_letter_typed.append('Asn')
                possible_config0.append('aat')
                possible_config1.append('aac')
                possible_config2.append(''.join(random.choices(['aat','aac'],k=1)))
                possible_config3.append(''.join(random.choices(['aat','aac'],k=1)))
                possible_config4.append(''.join(random.choices(['aat','aac'],k=1)))
                possible_config5.append(''.join(random.choices(['aat','aac'],k=1)))
                possible_config6.append(''.join(random.choices(['aat','aac'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'K':
                amino_name_typed.append('Lysine')
                amino_letter_typed.append('Lys')
                possible_config0.append('aaa')
                possible_config1.append('aag')
                possible_config2.append(''.join(random.choices(['aaa','aag'],k=1)))
                possible_config3.append(''.join(random.choices(['aaa','aag'],k=1)))
                possible_config4.append(''.join(random.choices(['aaa','aag'],k=1)))
                possible_config5.append(''.join(random.choices(['aaa','aag'],k=1)))
                possible_config6.append(''.join(random.choices(['aaa','aag'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'E':
                amino_name_typed.append('GlutamicAcid')
                amino_letter_typed.append('Glu')
                possible_config0.append('gaa')
                possible_config1.append('gag')
                possible_config2.append(''.join(random.choices(['gaa','gag'],k=1)))
                possible_config3.append(''.join(random.choices(['gaa','gag'],k=1)))
                possible_config4.append(''.join(random.choices(['gaa','gag'],k=1)))
                possible_config5.append(''.join(random.choices(['gaa','gag'],k=1)))
                possible_config6.append(''.join(random.choices(['gaa','gag'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'D':
                amino_name_typed.append('AspparticAcid')
                amino_letter_typed.append('Asp')
                possible_config0.append('gat')
                possible_config1.append('gac')
                possible_config2.append(''.join(random.choices(['gat','gac'],k=1)))
                possible_config3.append(''.join(random.choices(['gat','gac'],k=1)))
                possible_config4.append(''.join(random.choices(['gat','gac'],k=1)))
                possible_config5.append(''.join(random.choices(['gat','gac'],k=1)))
                possible_config6.append(''.join(random.choices(['gat','gac'],k=1)))
                reader += 1
                pass            
            elif input_seq[reader] == 'G':
                amino_name_typed.append('Glycine')
                amino_letter_typed.append('Gly')
                possible_config0.append('ggg')
                possible_config1.append('gga')
                possible_config2.append('ggc')
                possible_config3.append('ggt')
                possible_config4.append(''.join(random.choices(['ggg','gga','ggc','ggt'],k=1)))
                possible_config5.append(''.join(random.choices(['ggg','gga','ggc','ggt'],k=1)))
                possible_config6.append(''.join(random.choices(['ggg','gga','ggc','ggt'],k=1)))
                reader += 1
                pass
            elif input_seq[reader] == 'X':
                amino_name_typed.append('Ochre, Stop. ')
                amino_letter_typed.append('X*')
                possible_config0.append('taa')
                possible_config1.append('taa')
                possible_config2.append('taa')
                possible_config3.append('taa')
                possible_config4.append('taa')
                possible_config5.append('taa')
                possible_config6.append('taa')
                reader += 1
                pass
            elif input_seq[reader] == 'B':
                amino_name_typed.append('Amber, Stop. ')
                amino_letter_typed.append('B*')
                possible_config0.append('tag')
                possible_config1.append('tag')
                possible_config2.append('tag')
                possible_config3.append('tag')
                possible_config4.append('tag')
                possible_config5.append('tag')
                possible_config6.append('tag')
                reader += 1
                pass
            elif input_seq[reader] == 'Z':
                amino_name_typed.append('Opal, Stop. ')
                amino_letter_typed.append('Z*')
                possible_config0.append('tga')
                possible_config1.append('tga')
                possible_config2.append('tga')
                possible_config3.append('tga')
                possible_config4.append('tga')
                possible_config5.append('tga')
                possible_config6.append('tga')
                reader += 1
                pass
            else:
                break
    print("*Amino sequence*:\n{}".format(''.join(input_seq)))
    print("*Amino name*:\n{}".format(''.join(amino_name_typed)))
    print("*Amino letters*:\n{}".format(''.join(amino_letter_typed)))
    print("possible config 0:\n{}".format(''.join(possible_config0)))
    print("possible config 1:\n{}".format(''.join(possible_config1)))
    print("possible config 2:\n{}".format(''.join(possible_config2)))
    print("possible config 3:\n{}".format(''.join(possible_config3)))
    print("possible config 4:\n{}".format(''.join(possible_config4)))
    print("possible config 5:\n{}".format(''.join(possible_config5)))
    print("total random config 6:\n{}".format(''.join(possible_config6)))

def get_seq_type():
    ans0 = input("Enter input type: DNA/RNA(n), Amino(a)")
    if ans0 == 'n':
        translate_n_seq()
        return
    if ans0 == 'a':
        translate_a_seq()
        return
    else:
        print("Please describe input type either with: 'n' for DNA/RNA or 'a' for Amino")
get_seq_type()
