
def func_select_text(func):

    if 'red_filter' in str(func):
        f = open("/home/vk_bot/text/red_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt   

    elif 'blue_filter' in str(func):
        f = open("/home/vk_bot/text/blue_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 

    elif 'yellow_green_filter' in str(func):
        f = open("/home/vk_bot/text/yellow_green_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 

    elif 'pink_filter' in str(func):
        f = open("/home/vk_bot/text/pink_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 

    elif 'white_blue_filter' in str(func):
        f = open("/home/vk_bot/text/white_blue_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 

    elif 'black_filter' in str(func):
        f = open("/home/vk_bot/text/black_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 
    
    elif 'green_filter' in str(func):
        f = open("/home/vk_bot/text/green_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 
    
    elif 'negative_filter' in str(func):
        f = open("/home/vk_bot/text/negative_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 
    
    elif 'green_pink_filter' in str(func):
        f = open("/home/vk_bot/text/green_pink_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 
    
    elif 'blue_red_filter' in str(func):
        f = open("/home/vk_bot/text/blue_red_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt     
    
    elif 'pink_green_filter' in str(func):
        f = open("/home/vk_bot/text/pink_green_filter.txt", 'rb')
        txt = f.read().decode('utf-8')
        
        return txt 
