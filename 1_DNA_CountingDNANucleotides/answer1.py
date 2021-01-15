def countNuc(s:str)->str:
    count_dict = {"A":0,"C":0,"G":0,"T":0}
    for i in s:
        count_dict[i]+=1
    return f"{count_dict['A']} {count_dict['G']} {count_dict['C']} {count_dict['T']}"

def countNuc2(s:str)->str:
    return s.count("A"), s.count("G"), s.count("C"), s.count("T")

if __name__ == "__main__":
    with open("rosalind_dna.txt") as text_file:
        example = text_file.read().strip()
    print(countNuc(example))
    print(countNuc2(example))
