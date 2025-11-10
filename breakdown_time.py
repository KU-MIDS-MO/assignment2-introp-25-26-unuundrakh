def breakdown_time(seconds):
    if not isinstance(seconds, int) or seconds < 0:
        return -1
   
    if seconds == 0:
        return {}
  
    units = [3600, 60, 1] 
    
    return {u: v for u in units
            for v in [seconds // u if u == 3600 else (seconds % 3600) 
            // 60 if u == 60 else seconds % 60] if v !=0}

    
