def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    charac_dict={}
    text_lower=text.lower()
    for l in text_lower:
            if l not in charac_dict:
                charac_dict[l]=1
            else:
                charac_dict[l]+=1
    return(charac_dict)

def sort_on(ls):
    return ls["num"]
    

def insert_keys(lett):
    empty_list=[]
    for i in lett:
        if i.isalpha():
            keys_list={"char": i, "num": lett[i]}
            empty_list.append(keys_list)
        
    return empty_list



    
       
        
        
        




    

     
    

   

