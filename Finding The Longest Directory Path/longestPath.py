def lengthLongestPath(path) -> int:
    	# Split the input by lines.
        input = path.split('\n')
        st = []
        res = 0
		
        for i in input:
		#  '\t' will give the level at which this line input is.
            t = i.count('\t')
			
		# Remove all the saved answers which have level equal or greater.
		# In other words, Find the parent.
		
            while st and st[-1][1] >=  t:
                st.pop()
                
		# The absolute path till here will be  parent + '/' + the value of this line - '\t' :
            newString = st[-1][0] + '/' +  i.lstrip('\t') if st else '' + i
			
		# If this has '.' in it, note the length of the solution.
		
            if "." in newString:
                res = max(res , len(newString))
		# Add the newly created path to the stack.
		
            st.append([ newString , t])
        return res


path = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(lengthLongestPath(path))


