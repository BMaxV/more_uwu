import random

def uwu(my_string,intensity=0.5):
    """
    
    the benchmark is of course, this
    
    https://i-am-a-fish.tumblr.com/post/168157413417/imagine-reading-a-post-but-over-the-course-of-it
    
    as a video
    
    https://www.youtube.com/watch?v=7mBqm8uO4Cg
    
    for readability, there should be some balance between replacement
    and readability.
    
    I've seen things be so messed up the original message gets
    lost and it's possible that's not the goal.
    
    I've also seen cases where replacement is actually wrong because
    it breaks the flow of reading and doesn't actually sound "uwu".
    
    what I have in my is there is an intensity value and whether or
    not a uwufication happens is based on the scaling you set and 
    "distortion" by the uwufication.
    
    please -> pwease low distortion
    
    trolling -> twowwing high distortion
    
    hello world -> hewwo wowwd high distortion
    
    so what we occasionally really want is measuring the relative
    frequency of matches we may want to replace and only replace some.
    
    trolling -> 1 r 2 l -> twolling 1/3 "intensity.
    
    For that we need to find the "maximum uwu" potential of a string
    
    UNFORTUNATELY, standard python replacement just replaces everything,
    so here ewwing go.
    
    complex patterns should be matched and replaced first, ideally
    saving "modification points" so we don't modify too much.
    
    """
    
    #first thing to do is split the string so we can treat words individually
    # and can refer to words by index in the list
    
    my_string=my_string.split(" ")
    
    #this is simple.
    
    my_dict={
    "ted":"did",
    "er":"ew",
    "th":"d",
    "l":"w",
    "r":"w",
    "ch":"h",
    "ck":"gg",
    "ex":"eggs",
    }
    
    intense_dict={
    "you":"uwu",
    }
    
    my_new_string=[]
    for x in my_string:
        mycount=count(x,my_dict)
        
        #relative share of uwu modifications I can do.
        potential=mycount/len(x)
        
        # frequency
        r=random.random()
        if r > intensity:
            my_new_string.append(x)
            continue
        
        x=basic_uwu(x,my_dict,intensity)
        x=insert_uwu(x,intensity)
        if intensity > 0.75:
           x=basic_uwu(x,intense_dict,intensity)
        
        my_new_string.append(x)
        
    my_string=" ".join(my_new_string)
    
    return my_string


def insert_uwu(my_string,intensity):
    """ next challenge is to insert w's 
    between vocal and consonants and 
    y's around a's? """
    
    
    vocal=["a","e","i","o","u"]
    consonants=["t","d","c","b","s","m","g","f","p"]
    
    for x in vocal:
        for x2 in consonants:
            if x+x2 in my_string:
                #this should be find all, unfortunately.
                r=random.random()
                
                #filter entire words
                if r > intensity:
                    continue
                    
                my_string=detail_insert(my_string,x+x2)
                
            if x2+x in my_string:
                r=random.random()
                if r > intensity:
                    continue
                
                my_string=detail_insert(my_string,x2+x)
                
    return my_string

def detail_insert(my_string,pair,shift=1):
    
    #if pair["0"]=="w":
        
    
    while True:
        match_list=find_all(my_string,pair)
        for match in match_list:
            #this converts everything again.
            my_string=my_string[:match+1]+"w"+my_string[match+1:]
            break
        break
    return my_string

def count(my_string,my_dict):
    "add base"
    match_counts=my_string.count("w")
    for key in my_dict:
        match_counts+=my_string.count(key)
        
    return match_counts

def my_replace(my_string,old,new,intensity=1,verbose=False):
    matches=find_all(my_string,old)
    
    
    #that's not really ok.
    # I should rather split the string into bits and then reassamble?
    
    #this will mess with the lengths and the count will be off.
    
    if verbose:
        for match in matches:
            print(match,my_string,my_string[match:match+len(old)])
    my_rest_string=""
    c=0
    for x in matches:
        if x == len(my_string)-1:
            continue
        else:
            c=len(my_rest_string[:x-c])
            my_string=my_string[:x]+new+my_string[x+len(old):]
    return my_string
    
def find_all(my_string,search_term):
    c=0
    l=[]
    while True:
        
        x=my_string[c:].find(search_term)
        if x==-1:
            break
            
        l.append(x+c)
        c+=x+len(search_term)
    
    return l

def basic_uwu(my_string,my_dict,intensity):
    for key in my_dict:
        
        my_string=my_replace(my_string,key,my_dict[key],intensity)
        
    return my_string
        
def test_uwu():
    p="Do you expect me to talk? No Mister Bond I expect you to die."
    p1=uwu(p,intensity=1)
    print(p1)
    p2=uwu(p,intensity=0.5)
    print(p2)
    p3=uwu(p,intensity=0.1)
    print(p3)
    
    
    p="hello world"
    p4=uwu(p,intensity=1)
    print(p4)
if __name__=="__main__":
    test_uwu()
