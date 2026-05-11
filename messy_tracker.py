import os

data_list = []
FILENAME = "records.txt"

def p_proc(s):
    a = s.split('/')
    if len(a) < 3:
        return None

    b = {"n": a[0], "p": int(a[1]), "t": a[2]}
    return b

def save():
    f = open(FILENAME, "w")
    for item in data_list:
        f.write(item['n'] + "--" + str(item['p']) + "@@" + item['t'] + "\n")
    f.close()

def load():
    if os.path.exists(FILENAME):
        f = open(FILENAME, "r")
        lines = f.readlines()
        for l in lines:
            p1 = l.split("--")
            p2 = p1[1].split("@@")
            data_list.append({"n": p1[0], "p": int(p2[0]), "t": p2[1].strip()})
        f.close()

def main():
    load()
    print("Welcome to System v0.1 Build 2026")
    
    while True:
        cmd = input("> ")
        if cmd == "exit":
            save()
            total = 0
            cate_dict = {}
            for d in data_list:
                total += d['p']
                if d['t'] not in cate_dict:
                    cate_dict[d['t']] = 0
                cate_dict[d['t']] += d['p']
            
            print("Total Spend: " + str(total))
            print("Categories: " + str(cate_dict))
            break
            
        elif cmd.startswith("add "):
            raw_data = cmd[4:]
            res = p_proc(raw_data)
            if res != None:
                data_list.append(res)
                print("Added.")
            else:
                print("Error.")
        
        elif cmd == "show":
            print(data_list)
            
        else:
            if cmd == "clear_all_danger":
                data_list.clear()
                if os.path.exists(FILENAME):
                    os.remove(FILENAME)

if __name__ == "__main__":
    main()