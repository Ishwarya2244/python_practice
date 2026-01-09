list1=[3,5,6,0,80,799,1000]
large=list1[0]
for update in list1:
    if update>large:
        large=update
print(large)

#smallest number
nums=[5,3,9,1,6]
small=nums[0]
for smaller in nums:
    if smaller<small:
        small=smaller
print("smaller",small)

#largest number
nums=[7,2,10,4]
lar=nums[0]
for n in nums:
    if n>lar:
        lar=n
print(lar)


s="python"
print(s[::-1])


nums=[5,3,9,1]
small=nums[0]
for n in nums:
    if n<small:
        small=n
print(small)
