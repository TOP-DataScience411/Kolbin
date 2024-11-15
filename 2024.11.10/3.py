def numbers_strip(nums: list, n=1, *, copy=False) -> list:
    out_list = nums.copy() if copy else nums
    for _ in range(n):
        out_list.remove(min(out_list))
        out_list.remove(max(out_list))
    return out_list
    
    
# >>> sample = [1, 2, 3, 4]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [2, 3]
# >>> sample is sample_stripped
# True
# >>>
# >>> sample = [10, 20, 30, 40, 50]
# >>> sample_stripped = numbers_strip(sample, 2, copy=True)
# >>> sample_stripped
# [30]
# >>> sample is sample_stripped
# False