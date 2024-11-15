def central_tendency(num_1: float, num_2: float, /, *nums: float) -> dict[str, float]:
    result_dict = {}
    all_nums = sorted([num_1, num_2] + list(nums))
    
    if len(all_nums) % 2 == 0:
        index = (int(len(all_nums)/2-1), int(len(all_nums)/2))
        temp_result = (all_nums[index[0]] + all_nums[index[1]]) / 2
    else:
        index = int((len(all_nums)-1) / 2)
        temp_result = float(all_nums[index])
    result_dict["median"] = temp_result
    
    temp_result = sum(all_nums) / len(all_nums)
    result_dict["arithmetic"] = temp_result
    
    temp_result = 1
    harm = 0
    for num in all_nums:
        temp_result *= num
        harm += 1 / num
    result_dict["geometric"] = temp_result ** (1/len(all_nums))
    result_dict["harmony"] = len(all_nums) / harm
    
    return result_dict
    


# >>> central_tendency(1, 2, 3, 4)
# {'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmony': 1.9200000000000004}
# >>> sample = [1, 2, 3, 4, 5]
# >>> central_tendency(*sample)
# {'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmony': 2.18978102189781}