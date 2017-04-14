def merge_ranges(tup_list):
    
    times = sorted(tup_list)
    
    merged_meetings = [times[0]]
    
    
    for start, end in times[1:]:
        
        last_merged_start, last_merged_end = merged_meetings[-1]
        
        if start <= last_merged_end:
            merged_meetings[-1] = (last_merged_start, max(end, last_merged_end))
            
        else:
            merged_meetings.append((start, end))
            
    return merged_meetings


print merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])