def strong_password(password):
    if len(password) >= 8:
        digit_cnt = 0
        register_flag = False
        symbols_flag = False
        temp_register = None
        for ch in password:
            if ch.isdecimal() and digit_cnt < 2:
                digit_cnt += 1
            
            if ch.isalpha() and not register_flag:
                if temp_register == None:
                    if ch.islower():
                        temp_register = "lower"
                    elif ch.isupper():
                        temp_register = "upper"
                elif temp_register == "lower" and ch.isupper or temp_register == "upper" and ch.islower:
                    register_flag = True
            
            if not ch.isalnum():
                symbols_flag = True
            
        return True if digit_cnt >= 2 and register_flag and symbols_flag else False           
    else:
        return False



# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False