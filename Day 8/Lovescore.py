def calculate_love_score(name1, name2):
    names=name1+name2
    total_true=0
    total_love=0
    for letter in names:
        if letter in "true":
            total_true+=1
        if letter in "love":
            total_love+=1
    print(f"{total_true}{total_love}")
    
calculate_love_score("Anya", "Myko")