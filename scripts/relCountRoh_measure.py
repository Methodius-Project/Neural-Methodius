import sys
import os, re, string 
from termcolor import colored 
from collections import Counter
import numpy as np


 
def less_length(file_rst,file_facts,nmber): 
    with open(file_rst, 'r') as rrl, open(file_facts, 'r') as con: 
        rrlines0 = rrl.readlines() 
        conlines0 = con.readlines() 
        rrlines = [k.replace("depicts", "shows").replace("you recently saw", "").replace("  ", " ").replace("was originally", "originates").replace("now", "currently") for k in rrlines0] 
        conlines = [k.replace("depicts", "shows").replace("you recently saw", "").replace("  ", " ").replace("was originally", "originates").replace("now", "currently")  for k in conlines0] 
        count = 0 
        found = 0 
        f_list = [] 
        f0_list = [] 
        for i in rrlines: 
            for j in conlines: 
                if re.search(r"H-\d+\t",i) and re.search(r"H-\d+\t",j): 
                    if re.search(r"(H-\d+)\t",i).group(1)==re.search(r"(H-\d+)\t",j).group(1): 
                        count=count+1 
                        num = re.search(r"H-(\d+)\t",i).group(1) 
                        for z in rrlines0: 
                            if z.startswith("T-{}\t".format(num)): 
                                if  len(z) < nmber: 
                                    ztext = re.search(r"T-\d+.*(\[text\].*$)",z).group(1) 
                                    itext = re.search(r"H-\d+.*(\[text\].*$)",i).group(1) 
                                    jtext = re.search(r"H-\d+.*(\[text\].*$)",j).group(1) 
                                    print('FOUND') 
                                    found = found + 1 
                                    print(found) 
                                    print(colored(z,  'green', attrs=['bold', 'dark'])) 
                                    print(colored(rrlines0[rrlines0.index(z)-1], 'green', attrs=['bold', 'dark'])) 
                                    print(colored(rrlines0[rrlines.index(i)],  'blue', attrs=['bold', 'dark'])) 
                                    print(colored(rrlines0[rrlines.index(i)-2],'blue', attrs=['bold', 'dark'])) 
                                    print(colored(conlines0[conlines.index(j)],  'white', attrs=['bold', 'dark'])) 
                                    print(colored(conlines0[conlines.index(j)-2])) 
                                    f_list.append((ztext, rrlines0[rrlines.index(i)-2], itext, jtext, conlines0[conlines.index(j)-2])) 
                                    f0_list.append((z, rrlines0[rrlines.index(i)-2], rrlines0[rrlines.index(i)], conlines0[conlines.index(j)], conlines0[conlines.index(j)-2])) 
 
 
 
 
 
 
 
 
def check_slots_using_ref_text(file): 
    mismatch_list = [] 
    like_list = [] 
    with open(file, 'r') as rfile: 
        rfile_lines = rfile.readlines() 
        for i in rfile_lines: 
            if re.search(r"H-\d+\t",i): 
                t = rfile_lines[rfile_lines.index(i)-1] 
                t_list = [] 
                for be_token in t.split(): 
                    if be_token.startswith("begin") and be_token.endswith("end"): 
                        t_list.append(be_token) 
                i_list = [] 
                for ie_token in i.split(): 
                    if ie_token.startswith("begin") and ie_token.endswith("end"): 
                        i_list.append(ie_token) 
                print(i) 
                print(set(i_list)) 
                print("---------------------------") 
                print(set(t_list)) 
                print(t) 
                print(colored(rfile_lines[rfile_lines.index(i)-2],  'white', attrs=['bold', 'dark'])) 
                print(colored(set(t_list).difference(set(i_list)), 'blue', attrs=['bold', 'dark'])) 
                print(colored(set(i_list).difference(set(t_list)), 'yellow', attrs=['bold', 'dark'])) 
                alll = [x.group(1) for x in re.finditer(r"arg\d\s+(.*?)\s+\]", rfile_lines[rfile_lines.index(i)-2], re.IGNORECASE)] 
                print(alll) 
                print(colored(t.split(), 'blue', attrs=['bold', 'dark']))  
                print(colored(i.split(), 'yellow', attrs=['bold', 'dark'])) 
                for d in i.split(): 
                    if re.search(r"[a-z]\w*\d", d): 
                        if d not in t.split() and not d.startswith("begin"): 
                            print(colored(d, 'red', attrs=['bold', 'dark'])) 
                for z in t.split(): 
                    if re.search(r"[a-z]+\w*\d", z) and z not in i.split() and not z.startswith("begin"): 
                        print(colored(z, 'blue', attrs=['bold', 'dark'])) 
                print(colored(set(t.split())-set(i.split()), 'red', attrs=['dark'])) 
                print(colored(set(i.split())-set(t.split()), 'green', attrs=['dark'])) 
                t_i = set(t.split())-set(i.split())  
                i_t = set(i.split())-set(t.split()) 
                sym_diff_i_t = t_i | i_t 
                tokos = set([]) 
                for si in sym_diff_i_t: 
                    if re.search(r"[a-z]+\w*\d", si): 
                        tokos.add(si) 
                print(tokos) 
                su = 0 
                if tokos: 
                    for to in tokos: 
                        if re.search(r"[a-z]+\w*\d", to):                         
                            su=+Counter(i.split())[to] 
                            su=+Counter(t.split())[to] 
                    print(su) 
                    mismatch_list.append((i,su)) 
                    print(len(mismatch_list)) 



def sym_diff_measure_beam_tupled(file):  
    with open(file, 'r') as rfile:   
        rfile_lines = rfile.readlines()  
        sdiff_measure = np.array([0., 0., 0., 0.]) 
        h_length = 0  
        num_groups = [] 
        for i in rfile_lines:   
            if re.search(r"H-(\d+)\t",i):  
                num = re.search(r"H-(\d+)\t",i).group(1)  
                numg = [z for z in rfile_lines if re.search(r"H-{}\t".format(str(num)), z)] 
                t = "" 
                for j in rfile_lines: 
                    if re.search(r"T-{}\t".format(str(num)), j): 
                        t+=j         
                numg.append(t)                   
                if numg not in num_groups: 
                    num_groups.append(numg) 
        for k in num_groups: 
            summa = np.array([0., 0., 0., 0.])  
            for e in k[:-1]: 
                summa = np.add(summa, np.true_divide(diff_hyp_ref_tupled(e, k[-1]), len(k[:-1]))) 
            sdiff_measure = np.add(sdiff_measure, summa) 
        print(sdiff_measure/len(num_groups)) 
        print(len(num_groups)) 
                                                                                                                                                                               

def sym_diff_measure_beam(file):  
    with open(file, 'r') as rfile:   
        rfile_lines = rfile.readlines()  
        sdiff_measure = 0  
        h_length = 0  
        num_groups = [] 
        for i in rfile_lines:   
            if re.search(r"H-(\d+)\t",i):  
                num = re.search(r"H-(\d+)\t",i).group(1)  
                numg = [z for z in rfile_lines if re.search(r"H-{}\t".format(str(num)), z)] 
                t = "" 
                for j in  rfile_lines: 
                    if re.search(r"T-{}\t".format(str(num)), j): 
                        t+=j   
                numg.append(t)                   
                if numg not in num_groups: 
                    num_groups.append(numg) 
        for k in num_groups: 
            summa = 0 
            for e in k[:-1]: 
                summa += diff_hyp_ref(e, k[-1])/len(k[:-1]) 
            sdiff_measure += summa 
        print(sdiff_measure/len(num_groups)) 
        print(len(num_groups)) 
                                                                                                                                                                               

def diff_hyp_ref_tupled(i_text, t_text):  
    t_list = []   
    i_list = []   
    t_text_lower = t_text.lower()  
    i_text_lower = i_text.lower()   
    print(t_text_lower, "\n AND \n", i_text_lower)  
    sdiff_repeat  = 0. #repeating actual material  
    sdiff_drop = 0.    #dropping actual material  
    sdiff_haluc = 0.    #halucinating   
    sdiff_inter_under = 0.  #undergenerating actual material  
    for be_token in t_text_lower.split():           
        if (be_token.startswith("begin") and be_token.endswith("end")) or re.search(r"[a-z]+\d", be_token):   
            t_list.append(be_token)              
    for ie_token in i_text_lower.split():   
        if (ie_token.startswith("begin") and ie_token.endswith("end")) or re.search(r"[a-z]+\d", ie_token):  
            i_list.append(ie_token)  
    inter = set(i_list)&set(t_list)  
    set_sym_diff = set(i_list) ^ set(t_list)    
    print("intresection is ", inter)  
    print("symmetric difference is", set_sym_diff)      
    for s in set_sym_diff:          
        if s in set(t_list):  
            sdiff_drop   += t_list.count(s)  
            print("\t dropping", s)  
        else:     
            sdiff_haluc  += i_list.count(s)  
            print("\t halucinating", s)  
    for se in inter:  
        if t_list.count(se) > i_list.count(se):  
            sdiff_inter_under += t_list.count(se) - i_list.count(se)  
            print("\t under generating:", se)  
        if t_list.count(se) < i_list.count(se):  
            sdiff_repeat += i_list.count(se) - t_list.count(se)  
            print("\t repeating:", se)              
    print(sdiff_repeat, " repeating actual material\n", sdiff_drop, '  dropping actual material\n', sdiff_haluc, "   halucinating\n", sdiff_inter_under, "    undergenerating actual material")  
    print(str(np.array([sdiff_repeat, sdiff_drop, sdiff_haluc, sdiff_inter_under])))
    print('repeat, drop, haluc, inter_under')
    return np.array([sdiff_repeat, sdiff_drop, sdiff_haluc, sdiff_inter_under]) 
                                                                                                                                                                               

def diff_hyp_ref(i_text, t_text):  
    t_list = []   
    i_list = []   
    t_text_lower = t_text.lower()  
    i_text_lower = i_text.lower()   
    print(t_text_lower, "AAANNNDDD", i_text_lower)  
    sdiff_repeat  = 0 #repeating actual material  
    sdiff_drop = 0    #dropping actual material  
    sdiff_haluc = 0    #halucinating   
    sdiff_inter_under = 0  #undergenerating actual material  
    for be_token in t_text_lower.split():           
        if (be_token.startswith("begin") and be_token.endswith("end")) or re.search(r"[a-z]+\d", be_token):   
            t_list.append(be_token)              
    for ie_token in i_text_lower.split():   
        if (ie_token.startswith("begin") and ie_token.endswith("end")) or re.search(r"[a-z]+\d", ie_token):  
            i_list.append(ie_token)  
    inter = set(i_list)&set(t_list)  
    set_sym_diff = set(i_list) ^ set(t_list)    
    print("intresection is ", inter)  
    print("symmetric difference is", set_sym_diff)      
    for s in set_sym_diff:          
        if s in set(t_list):  
            sdiff_drop   += t_list.count(s)  
            print("dropping", s)  
        else:     
            sdiff_haluc  += i_list.count(s)  
            print("halucinating", s)  
    for se in inter:  
        if t_list.count(se) > i_list.count(se):  
            sdiff_inter_under += t_list.count(se) - i_list.count(se)  
            print("under generating:", se)  
        if t_list.count(se) < i_list.count(se):  
            sdiff_repeat += i_list.count(se) - t_list.count(se)  
            print("repeating:", se)              
    print(sdiff_repeat, " repeating actual material\n", sdiff_drop, '  dropping actual material\n', sdiff_haluc, "   halucinating\n", sdiff_inter_under, "    undergenerating actual material")  
    return sdiff_repeat + sdiff_drop + sdiff_haluc + sdiff_inter_under 
                                                                         



def counter_of_relation(file_rst): 
    with open(file_rst, 'r') as rrl:  
        rrlines0 = rrl.readlines()  
        rrlines = [k.replace("depicts", "shows").replace("you recently saw", "").replace("  ", " ").replace("was originally", "originates") for k in rrlines0]  
        uu_found = 0 
        ll_found = 0 
        ul_found = 0 
        lu_found = 0 
        no_rel_found = 0 
        other_cases = 0 
        uu_list = []  
        ll_list = [] 
        ul_list = [] 
        lu_list = []  
        no_rel_list = [] 
        contrast_unlike = []
        contr_unlike = 0
        similarity_like = []
        similar_like = 0
        other_cases_list = [] 
        for i in rrlines:  
            for j in rrlines:  
                if re.search(r"H-\d+\t",i, re.IGNORECASE) and re.search(r"T-\d+\t",j, re.IGNORECASE): 
                    if re.search(r"H-(\d+)\t",i, re.IGNORECASE).group(1)==re.search(r"T-(\d+)\t",j, re.IGNORECASE).group(1):  
                        num = re.search(r"H-(\d+)\t",i, re.IGNORECASE).group(1)                          
                        if ' unlike' in j and ' unlike' in i: 
                            print(" >> unlike unlike")
                            uu_found +=1                                     
                            uu_list.append((i,j)) 
                            print(colored(i,  'blue', attrs=['bold', 'dark'])) 
                            print(colored(j,  'blue', attrs=['bold', 'dark'])) 
                            print(colored(rrlines[rrlines.index(i)-2]))  
                            print(" << unlike unlike")
                        elif ' like' in j and ' like' in i: 
                            print(" >> like like")
                            ll_found += 1 
                            ll_list.append((i,j)) 
                            print(colored(i,  'green', attrs=['bold', 'dark'])) 
                            print(colored(j,  'green', attrs=['bold', 'dark'])) 
                            print(colored(rrlines[rrlines.index(i)-2])) 
                            print(" << like like")
                        elif ' unlike' in j and ' like' in i: 
                            print(" >> unlike like")
                            ul_found +=1 
                            ul_list.append((i,j)) 
                            print(colored(i,  'red', attrs=['bold', 'dark'])) 
                            print(colored(j,  'red', attrs=['bold', 'dark'])) 
                            print(colored(rrlines[rrlines.index(i)-2])) 
                            print(" << unlike like")
                        elif ' like' in j and ' unlike' in i: 
                            print(" >> like unlike")
                            lu_found +=1  
                            lu_list.append((i,j)) 
                            print(colored(i,  'white', attrs=['bold', 'dark'])) 
                            print(colored(j,  'white', attrs=['bold', 'dark'])) 
                            print(colored(rrlines[rrlines.index(i)-2])) 
                            print(" << like unlike")
                        elif 'like' not in j and 'like' not in i: 
                            no_rel_found +=1 
                            no_rel_list.append((i,j)) 
                            print(colored(i,  'cyan', attrs=['bold', 'dark'])) 
                            print(colored(j,  'cyan', attrs=['bold', 'dark'])) 
                            print(colored(rrlines[rrlines.index(i)-2])) 
                            print(" << norel norel")
                        elif 'contrast' in rrlines[rrlines.index(i)-2] and 'unlike' not in j and 'unlike' in i:
                            print("Contrast in ContPlan and no Unlike in Ref but Unlike in Hyp")
                            contrast_unlike.append((i,j))
                            contr_unlike += 1                                   
                            print(i)
                            print(j)
                        elif 'similarity' in rrlines[rrlines.index(i)-2] and 'like' not in j and 'like' in i:
                            print("Similarity in ContPlan and no Like in Ref but Like in hyp")
                            similarity_like.append((i,j))
                            similar_like += 1   
                        else: 
                            print(">> An other case")
                            other_cases +=1 
                            other_cases_list.append((i,j))
                            print(i)
                            print(j)
                            print(colored(rrlines[rrlines.index(i)-2])) 
                            print("<< An other case")
        print("Unlike ", uu_found) 
        print("Like ", ll_found) 
        print("Unlike VS Like ", ul_found) 
        print("Like VS Unlike", lu_found) 
        print("No relation in both ", no_rel_found) 
        print("contrast-unlike, similarity-like")
        print(contr_unlike, similar_like)
        print("The rest of cases ", other_cases) 
        print("-----------------------------------------------------------------------------------")
        print(uu_found, ll_found, ul_found, lu_found, no_rel_found, other_cases) 
        print("<><><><><><><><><><><><><><>")
        print("Mistakes: "+str(ul_found+lu_found+other_cases))
         




if __name__ == "__main__":
    if len(sys.argv) == 2:
        sym_diff_measure_beam_tupled(sys.argv[1])
    if len(sys.argv) == 3 and sys.argv[2] == 'relcount':
        counter_of_relation(sys.argv[1])    
