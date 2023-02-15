list_ = []
score_list = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_ += [[name, score]]
        score_list += [score]
    sl= sorted(list(set(score_list)))[1]
    
    for nm, sc in sorted(list_):
        if sc == sl:
            print(nm)
    
