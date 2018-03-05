# This is Work in progress, since the code has not been tested yet.


def nearly_equal(str1, str2):
   """Count the # of differences between equal length strings str1 and str2"""
        
        diff_count = 0
        if str1 == str2:
		        print("Both are equal.")
            return
       
        for char1, char2 in zip(str1, str2):
                if ch1 != ch2:
                        diffs += 1
        if diffs <= 1:
            return False
            
            
if __name__ == "__main__":
    import sys
    nearly_equal(sys.argv[1],sys.argv[2])
