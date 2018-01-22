import random


def translate_n_seq():
    dna_typed = []
    rna_typed = []
    dna_match = []
    reader = 0
    base_list = 'a','t','g','c','u'
    ans1 = input("Random dna sequence? y/n")
    if ans1 == 'y':
        print("Choose length:")
        seq_len = int(input())
        input_seq = "".join(random.choices(base_list,k = seq_len))
    elif ans1 != 'y':
        input_seq = "".join(input("Type sequence:"))
    seq_len = len(input_seq)
    while reader < seq_len:
        for chars in input_seq:
            if input_seq[reader] == 'a':
                dna_typed.append('a')
                dna_match.append('t')
                rna_typed.append('a')
                reader += 1
                pass
            elif input_seq[reader] == 't':
                dna_typed.append('t')
                dna_match.append('a')
                rna_typed.append('u')
                reader += 1
                pass
            elif input_seq[reader] == 'g':
                dna_typed.append('g')
                dna_match.append('c')
                rna_typed.append('g')
                reader += 1
                pass
            elif input_seq[reader] == 'c':
                dna_typed.append('c')
                dna_match.append('g')
                rna_typed.append('c')
                reader += 1
                pass
            elif input_seq[reader] == 'u':
                dna_typed.append('t')
                dna_match.append('a')
                rna_typed.append('u')
                reader += 1
                pass
            else:
                break
    amino_chars = []
    amino_letter = []
    aareader = 0
    while aareader < seq_len-2:
        codon_char = dna_typed[aareader:aareader+3]
        if codon_char == ['a','t','g']:
            amino_chars.append('Met')
            amino_letter.append('M')
            aareader += 3
            pass
        elif codon_char == ['t','t','a'] or codon_char == ['t','t','g'] or codon_char == ['c','t','t'] or codon_char == ['c','t','c'] or codon_char == ['c','t','a'] or codon_char == ['c','t','g']:
            amino_chars.append('Leu')
            amino_letter.append('L')
            aareader += 3
            pass
        elif codon_char == ['t','t','t'] or codon_char == ['t','t','c']:
            amino_chars.append('Phe')
            amino_letter.append('F')
            aareader += 3
            pass
        elif codon_char ==  ['t','c','t'] or codon_char == ['t','c','c'] or codon_char == ['t','c','a'] or codon_char == ['t','c','g'] or codon_char == ['a','g','c'] or codon_char == ['a','g','t']:
            amino_chars.append('Ser')
            amino_letter.append('S')
            aareader += 3
            pass
        elif codon_char == ['t','a','t'] or codon_char == ['t','a','c']:
            amino_chars.append('Tyr')
            amino_letter.append('T')
            aareader += 3
            pass
        elif codon_char == ['t','g','t'] or codon_char == ['t','g','c']:
            amino_chars.append('Cys')
            amino_letter.append('C')
            aareader += 3
            pass
        elif codon_char == ['t','g','g']:
            amino_chars.append('Trp')
            amino_letter.append('W')
            aareader += 3
            pass
        elif codon_char == ['c','c','c'] or codon_char == ['c','c','a'] or codon_char == ['c','c','t'] or codon_char == ['c','c','g']:
            amino_chars.append('Pro')
            amino_letter.append('P')
            aareader += 3
            pass
        elif codon_char == ['c','a','t'] or codon_char == ['c','a','c']:
            amino_chars.append('His')
            amino_letter.append('H')
            aareader += 3
            pass
        elif codon_char == ['c','a','a'] or codon_char == ['c','a','g']:
            amino_chars.append('Gln')
            amino_letter.append('Q')
            aareader += 3
            pass
        elif codon_char == ['c','g','g'] or codon_char == ['c','g','t'] or codon_char == ['c','g','c'] or codon_char == ['c','g','a'] or codon_char == ['a','g','g'] or codon_char == ['a','g','a']:
            amino_chars.append('Arg')
            amino_letter.append('R')
            aareader += 3
            pass
        elif codon_char == ['a','t','t'] or codon_char == ['a','t','c'] or codon_char == ['a','t','a']:
            amino_chars.append('Ile')
            amino_letter.append('I')
            aareader += 3
            pass
        elif codon_char == ['g','t','g'] or codon_char == ['g','t','t'] or codon_char == ['g','t','c'] or codon_char == ['g','t','a']:
            amino_chars.append('Val')
            amino_letter.append('V')
            aareader += 3
            pass
        elif codon_char == ['a','c','a'] or codon_char == ['a','c','c'] or codon_char == ['a','c','t'] or codon_char == ['a','c','g']:
            amino_chars.append('Thr')
            amino_letter.append('T')
            aareader += 3
            pass
        elif codon_char == ['g','c','g'] or codon_char == ['g','c','c'] or codon_char == ['g','c','t'] or codon_char == ['g','c','a']:
            amino_chars.append('Ala')
            amino_letter.append('A')
            aareader += 3
            pass
        elif codon_char == ['a','a','t'] or codon_char == ['a','a','c']:
            amino_chars.append('Asn')
            amino_letter.append('N')
            aareader += 3
            pass
        elif codon_char == ['a','a','a'] or codon_char == ['a','a','g']:
            amino_chars.append('Lys')
            amino_letter.append('K')
            aareader += 3
            pass
        elif codon_char == ['g','a','a'] or codon_char == ['g','a','g']:
            amino_chars.append('Glu')
            amino_letter.append('E')
            aareader += 3
            pass
        elif codon_char == ['g','a','t'] or codon_char == ['g','a','c']:
            amino_chars.append('Asp')
            amino_letter.append('D')
            aareader += 3
            pass
        elif codon_char == ['g','g','g'] or codon_char == ['g','g','a'] or codon_char == ['g','g','c'] or codon_char == ['g','g','t']:                
            amino_chars.append('Gly')
            amino_letter.append('G')
            aareader += 3
            pass
        elif codon_char == ['t','a','a']:
            amino_chars.append('Ochre, stop')
            amino_letter.append('X')
            aareader += 3
            pass
        elif codon_char == ['t','a','g']:
            amino_chars.append('Amber, stop')
            amino_letter.append('B')
            aareader += 3
            pass
        elif codon_char == ['t','g','a']:
            amino_chars.append('Opal, stop')
            amino_letter.append('Z')
            aareader += 3
            pass
        else:
            break
    print("*DNA*:{}".format(''.join(dna_typed)))
    print("Match:{}".format(''.join(dna_match)))
    print("~RNA~:{}".format(''.join(rna_typed)))
    print("Amino name:\n{}".format(''.join(amino_chars)))
    print("Amino letter code:\n{}".format(''.join(amino_letter)))
    print("DNA len:{}".format(len(dna_typed)))
    print("Amino len:{}".format(len(amino_letter)))
    
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
