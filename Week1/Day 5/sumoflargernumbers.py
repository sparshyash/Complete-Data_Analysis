class Solution:
	def findSum(self, s1, s2):
		
		
		res=[]
		
		carry =0
		i,j =len(s1)-1,len(s2)-1
		
		while i>=0  or j>=0 or carry>0 :
		    val1=int(s1[i]) if i>=0 else 0
		    
		    val2=int(s2[j]) if j>=0 else 0
		    
		    column_sum=val1 +val2 +carry
		    
		    carry =column_sum//10 
		    
		    res.append(str(column_sum%10))
		    
		    i-=1
		    j-=1
		    
		    
		    
		result_str="".join(res[::-1])
		result_str=result_str.lstrip('0')
		return result_str if result_str else '0'