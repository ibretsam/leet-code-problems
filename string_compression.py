def compress(chars):
    for i, c in enumerate(chars):
        count = 0
        if i != len(chars) - 1 and chars[i + 1] == c:
            count += 1
            j = i + 1
            while j <= len(chars) - 1 and chars[j] == c:
                count += 1
                chars.pop(j)
            if count < 9:
                chars.insert(i + 1, str(count))
            else:
                print(count)
                for k, ch in enumerate(str(count)):
                    chars.insert(i + k + 1, ch)
    return chars
    
# print(compress(["a","a","b","b","c","c","c","c"]))
print(compress(["a", "a", "2", "2", "2"]))
# print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
# print(compress(["b","l","l","l","l","l","l","4","4","W","W","&","d","d","d","@","D","D",".",".",".","8","8","8","U","V",">","J","J","k","H","H","=","l","[","[","[","[","[","[","[","a","a","'","<","[","[","y","V","l","l","'","$","E","`","v","k","E","E","t","t","t","t","t","=","=","0","C","a","l","l","l","r","R","M","M","c","c","c","A","A","S","9","9","9","9",")",")","\\","s","\\","\\","y","W","W","W","J","J","J","J","6","6","<","<","E","u","e","e","e","e","e","e","e","e","e","9","9","9","9","R","8","?","F","3","&","&","&","&","f","%","%","2","2","2",")",")",")","J","p","|","D","D","D","s","t","V","V","?","^","^","S","3","3","3","3","h","*","|","|","b","b","a","a","a","r","r","r","r","J",".","^","^","~","g",":",":",":","(","4","4","4","4","w","w","w","w","w","w","w","C","?","=","d","L",":","0","0","c","w","w","w","w","w","w","{","{","t","k","k","k","&","&","&","h","j","j","j","0","3","l",";",";",";",";",";",".",".",".","%","1","1","1","l","9","?","?","?","t",">","E","N","N","@",">",".",".","I","a","a","a","a","B","7","7","{","o","o","-","+","+","+","+","o","o","}","B","B","r","r","r","q","4","4","4","9","W","W","W","W","W","'","'","'","g","J","(","(","(","(","t","t","?",";","g","g","g","0","]","]","]"]))
    