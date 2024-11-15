def to_decimal(num: str, orig_sys: int, digits_dict: dict) -> float | None:
    order_int = num.find(".") - 1
    order_float = (len(num) - num.find(".") - 1) * -1
    cnt_o_f = -1
    num_decimal = 0
    
    for i in range(len(num)):
        if num[i] != "." and digits_dict[num[i]] >= orig_sys:
            return None    
        if order_int < 0:
            num_decimal += digits_dict[num[i]] * (orig_sys**(len(num) - 1 - i))
        elif order_int >= 0 and num[i] != ".":
            if i <= order_int:
                num_decimal += digits_dict[num[i]] * (orig_sys**(order_int - i))
            else:
                num_decimal += digits_dict[num[i]] * (orig_sys**cnt_o_f)
                cnt_o_f -= 1
                if order_float == cnt_o_f + 1:
                    break
            
    return num_decimal
    
    
    
def decimal_to_target(num: float, target_sys: int, digits_dict: dict) -> str | None:
    order_int = num // 1
    order_float = num % 1
    num_target = ""
    
    while True:  
        if not order_int:
            break
        num_val = order_int % target_sys
        if num_val >= target_sys:
            return None
        for key, val in digits_dict.items():
            if val == num_val:
                num_target = key + num_target
        order_int //= target_sys
        
    if order_float:
        num_target_float = ""
        for i in range(8):
            float_val = order_float * target_sys
            if float_val >= target_sys:
                return None
            for key, val in digits_dict.items():
                if val == float_val // 1:
                    if not val and num_target_float[-1] == "0":
                        # if num_target_float:
                        num_target += "." + num_target_float
                        return num_target[:-1]
                    num_target_float += key
                    order_float = float_val - val
        num_target += "." + num_target_float   
         
    return num_target



def int_base(num: str, orig_sys: int, target_sys: int) -> str | None:
    for ch in num:
        if not ch.isalnum() and ch != ".":
            return None
    if 36 < orig_sys < 2 or 36 < target_sys < 2:
        return None

    # Создание словаря чисел
    digits_dict = {}
    for i in range(36):
        if i < 10:
            digits_dict[chr(i+48)] = i
        else:
            digits_dict[chr(i+87)] = i
           
    num_decimal = to_decimal(num, orig_sys, digits_dict)
    num_out = decimal_to_target(num_decimal, target_sys, digits_dict) if num_decimal else None
    return num_out
        


# >>> int_base('ff00', 16, 2)
# '1111111100000000'
# >>> int_base('1101010', 2, 30)
# '3g'
# >>> int_base('110.1010', 2, 30)
# '6.imf'
# >>> int_base('ff0.af40', 36, 27)
# '10b0.7lqqqqqq'