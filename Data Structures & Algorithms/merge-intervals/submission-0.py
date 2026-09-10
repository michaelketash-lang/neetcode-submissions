class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Edge case: empty list
        if not intervals:
            return []
        # Step 1: Sort by start time (Crucial for O(N log N) logic)
        intervals.sort(key=lambda x: x[0])
    
        # Initialize with the first interval
        merged = [intervals[0]]    
        # Step 2: Iterate through the rest
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            # Get the last interval added to our result list
            last_merged_start, last_merged_end = merged[-1]
            # Step 3: Check for overlap
            if current_start <= last_merged_end:
                # Overlap detected! Merge by extending the end time.
                # We take the MAX because the current interval might end BEFORE the previous one
                # Example: [1, 10] and [2, 3] -> merges to [1, 10]
                merged[-1][1] = max(last_merged_end, current_end)
            else:
                # No overlap: simply append the new interval
                merged.append(intervals[i])
        return merged