# steps:
# initialization
    # i need a table for the reduction rules
    # i need a table for the parsing table
# step 1
    # start call stack with $0
    # make input be the input but a stack version of it separated
# step 2
    # look at top of input and check what the number corresponding gives it 
# step 3 parse
    # check if its reduce or shift
        # if accept
            # return true
        # if shift
            # pop input character -> push input character into call stack with shift number
        # if reduce 
            # pop top of call stack
                # if value is in reduction rule
                    # temporarily store the reduced value
                    # grab number at the top of the call stack
                    # if the reduced value and the number exists on the parsing table
                        # push reduced value and then number to call stack
                    # else return false
                # else repeat line 17
                    # if you reach $ then return false
        # else return false