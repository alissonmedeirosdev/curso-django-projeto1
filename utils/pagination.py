import math

def make_pagination_range(
    page_range,
    qty_pages,
    current_page, 
):
    
    # 2 3 [4] 5 6

    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_page = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset
    
    if stop_range >= total_page:
        start_range = start_range - abs(total_page - stop_range)

    return page_range[start_range:stop_range]
