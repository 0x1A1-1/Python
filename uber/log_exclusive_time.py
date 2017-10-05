def exclusive_time(log_list):
    
    if log_list is None:
        return 0 
        
    stack = []
    # time tracker for the overall timeline
    curr_time = 0 
    time_table = {}
    
    for log in log_list:
        if curr_time == 0:
            curr_time = log[2]
            
        # enter function
        if log[1] == 0:
            if len(stack) == 0:
                stack.append([log[0], log[2]])
                time_table[log[0]] = 0
                continue
            
            if log[0] not in time_table:
                time_table[log[0]] = 0

            # if we have function time recorded already 
            time_table[stack[-1][0]] += log[2] - curr_time
                
            stack.append([log[0], log[2]])
            
            
        # exit function 
        else:
            
            #exception case, when exited function isn't on the top of stack
            if stack[len(stack)-1][0] != log[0]:
                raise Exception('error')
            else:
                time_table[stack[-1][0]] += log[2] -  curr_time
                print time_table[stack[-1][0]]
            
            stack.pop(len(stack)-1)
            
        curr_time = log[2]
                
                
    if len(stack) > 0 :
        raise Exception('error')
    else:
        print time_table
log = [["foo", 0, 1],["baz", 0, 2],["foo", 0, 3], ["foo",1,4],["baz", 1, 5],["lid", 0, 6],["lid", 1, 7],["foo", 1, 10]]
exclusive_time(log)
log = [["foo", 0, 1],["foo", 1, 2]]
exclusive_time(log)
