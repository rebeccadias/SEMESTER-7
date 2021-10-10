def union(A,B):
    u = {}
    for i in A:
        if i in B:
            u[i]=max(A[i],B[i])
        else:
            u[i]=A[i]
    for i in B:
        if i not in A:
            u[i]=B[i]
    return(u)

def intersection(A,B):
    inter = {}
    for i in A:
        if i in B:
            inter[i]=min(A[i],B[i])
        else:
            inter[i]=A[i]
    for i in B:
        if i not in A:
            inter[i]=B[i]
    return(inter)

def difference(A,B):
    comp_b = complement(B)
    diff = intersection(A,comp_b) 

def complement(A):
    comp_a={}
    for i in A:
        comp_a[i] = round((1-A[i]),1)
    return(comp_a)

def morgan(A,B):
    p = intersection(A,B)
    p_bar = complement(p)
    comp_a = complement(A)

    comp_b = complement(B)
    q = union(comp_a,comp_b)
    if(p_bar == q):
        print("(A n B)': ",p_bar)
        print("A' u B': ",q)
        print("Thus, (A n B)' = A' u B'")
        print("Law 1 proved")

    p = union(A,B)
    p_bar = complement(p)
    comp_a = complement(A)
    comp_b = complement(B)
    q = intersection(comp_a,comp_b)
    if(p_bar == q):
        print("\n(A u B)': ",p_bar)
        print("A' n B': ",q)
        print("Thus, (A u B)' = A' n B'")
        print("Law 2 proved")
        print("\nHence De Morgan's Law is proved")

def support(A):
    supp = dict((k,v) for k,v in A.items() if v > 0)
    supp_ele = []
    for i in supp.keys():
        supp_ele.append(i)
    if(len(supp_ele) == 0):
        return("PHI")
    else:
        return(supp_ele)
    
def core(A):
    core = dict((k,v) for k,v in A.items() if v == 1)
    core_ele = []
    for i in core.keys():
        core_ele.append(i)
    if(len(core_ele) == 0):
        return("PHI")
    else:
        return(core_ele)

def height(A):
    av = A.values()
    mx = max(av)
    return(mx)

def cardinality(A):
    av = A.values()
    sm = sum(av)
    return(sm)

def relative_cardinality(A):
    av = A.values()
    rc = str(format(sum(av)/len(av),".2f"))
    return(rc)

def alpha_cut(A,alpha):
    ac = dict((k,v) for k,v in A.items() if v >= alpha)
    ac_ele = []
    for i in ac.keys():
        ac_ele.append(i)
    if(len(ac_ele) == 0):
        return("PHI")
    else:
        return(ac_ele)

def strong_alpha_cut(A,alpha):
    sac = dict((k,v) for k,v in A.items() if v > alpha)
    sac_ele = []
    for i in sac.keys():
        sac_ele.append(i)
    if(len(sac_ele) == 0):
        return("PHI")
    else:
        return(sac_ele)

def check_normal_or_not(C,x):
    if(1 in C.values()):
        return(x,"is Normal")
    else:
        return(x,"is Subnormal")

def start():
    print('-'*93,'\n')
    u = union(mem_a,mem_b)
    print("Union: ",u)
    print()

    print('-'*93,'\n')
    inter = intersection(mem_a,mem_b)
    print("Intersection: ",inter)
    print()

    print('-'*93,'\n')
    diff = difference(mem_a,mem_b)
    print("Difference: ",diff)
    print()

    print('-'*93,'\n')
    comp_a = complement(mem_a)
    comp_b = complement(mem_b)
    print("A's complement: ",comp_a)
    print("B's complement: ",comp_b)
    print()

    print('-'*93,'\n')
    morgan(mem_a,mem_b)
    print()

    print('-'*93,'\n')
    supp_a = support(mem_a)
    supp_b = support(mem_b)
    print("Support of A: ",supp_a)
    print("Support of B: ",supp_b)
    print()

    print('-'*93,'\n')
    core_a = core(mem_a)
    core_b = core(mem_b)
    print("Core of A: ",core_a)
    print("Core of B: ",core_b)
    print()

    print('-'*93,'\n')
    height_a = height(mem_a)
    height_b = height(mem_b)
    print("Height of A = ",height_a)
    print("Height of B = ",height_b)
    print()

    print('-'*93,'\n')
    cardinality_a = cardinality(mem_a)
    cardinality_b = cardinality(mem_b)
    print("Cardinality of A: ",cardinality_a)
    print("Cardinality of B: ",cardinality_b)
    print()

    print('-'*93,'\n')
    relative_cardinality_a = relative_cardinality(mem_a)
    relative_cardinality_b = relative_cardinality(mem_b)
    print("Relative Cardinality of A: ",relative_cardinality_a)
    print("Relative Cardinality of B: ",relative_cardinality_b)
    print()

    print('-'*93,'\n')
    alpha_cut_a = alpha_cut(mem_a,alpha)
    alpha_cut_b = alpha_cut(mem_b,alpha)
    print("Alpha cut of A({}): {}".format(alpha,alpha_cut_a))
    print("Alpha cut of B({}): {}".format(alpha,alpha_cut_b))
    print()

    print('-'*93,'\n')
    strong_alpha_cut_a = strong_alpha_cut(mem_a,alpha)
    strong_alpha_cut_b = strong_alpha_cut(mem_b,alpha)
    print("Strong Alpha cut of A({}): {}".format(alpha,strong_alpha_cut_a))
    print("Strong Alpha cut of B({}): {}".format(alpha,strong_alpha_cut_b))
    print()

    print('-'*93,'\n')
    check_normal_or_not_a = check_normal_or_not(mem_a,'A')
    check_normal_or_not_b = check_normal_or_not(mem_b,'B')
    print(check_normal_or_not_a)
    print(check_normal_or_not_b)
    print()

def inputt():
    global mem_a, mem_b, alpha
    a=[]
    print('-'*40+' FUZZY_SET_A '+'-'*40)
    n=input("Enter the elements of set A: ")
    a=n.split(' ')
    print("Enter the membership value for each element: ")
    mem_a = {}
    for i in a:
        print(i,"= ",end='')
        mem_a[i] = float(input())
        if not 0 <= mem_a[i] <=1:
            print("Enter membership value between [0,1]!!")
            quit()
    print("Fuzzy Set A: ",mem_a)
    print()

    b=[]
    print('-'*40+' FUZZY_SET_B '+'-'*40)
    n=input("Enter the elements of set B: ")
    b=n.split(' ')
    print("Enter the membership value for each element: ")
    mem_b = {}
    for i in b:
        print(i,"= ",end='')
        mem_b[i] = float(input())
        if not 0 <= mem_a[i] <=1:
            print("Enter membership value between [0,1]!!")
            quit()
    print("Fuzzy Set B: ",mem_b)
    print()

    alpha = float(input("Enter the Alpha value between [0,1] for the alpha cut and strong alpha cut: "))
    print()

inputt()
start()
