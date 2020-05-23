def echo_shout(word):
    echo_word = word+word
    def change():
        nonlocal echo_word
    
        echo_word+='!!!'
        return echo_word
        
    
        
    return change

a = echo_shout('roshan')
print(a())