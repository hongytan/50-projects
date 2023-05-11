def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        
        count = 1
        
        while h * bounce > window:
            count += 2
            h *= bounce
            
        return count
    
    else:
        return -1
    
def testing(h,b,w):
    print(bouncing_ball(h,b,w))

testing(2, 0.5, 1)
testing(3, 0.66, 1.5)
testing(30, 0.66, 1.5)
testing(30, 0.75, 1.5)