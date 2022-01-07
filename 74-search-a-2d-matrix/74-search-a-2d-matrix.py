class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.row_len, self.col_len = len(matrix), len(matrix[0])
        def _do_bin_search_on_row(row, col_start, col_end):
            if col_end >= col_start:
                mid = ( col_start + col_end ) // 2
                if mid < 0 or mid >= self.col_len: return -1
                elif matrix[row][mid] == target: return 1
                elif matrix[row][mid] < target: return _do_bin_search_on_row(row, mid + 1, col_end)
                else: return _do_bin_search_on_row(row, col_start, mid - 1)
            return -1
        
        def _do_scan_column(row_start, row_end):
            if row_end >= row_start:
                mid = (row_start + row_end) // 2
                if mid < 0 or mid >= self.row_len: return False
                elif _do_bin_search_on_row(mid, 0, self.col_len) == 1: return True
                elif matrix[mid][0] > target: return _do_scan_column(row_start, mid - 1)
                else: return _do_scan_column(mid + 1, row_end)
            return False

        return _do_scan_column(0, self.row_len)