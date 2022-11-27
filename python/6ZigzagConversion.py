#https://leetcode.com/problems/zigzag-conversion/

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"

#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string s, int numRows);
 

#Example 1:

#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Example 2:

#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#Example 3:

#Input: s = "A", numRows = 1
#Output: "A"
 

#Constraints:

#1 <= s.length <= 1000
#s consists of English letters (lower-case and upper-case), ',' and '.'.
#1 <= numRows <= 1000

class Solution(object):
    def convertDEBUG(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        c = 1000
        r = 1000
        letters = [["" for x in range(c)] for y in range(r)]
        DEBUG = 1

        columns = 1
        rows = 1
        zigzig = ""
        b_fullColumn = True
        zigRow = numRows - 1

        for i in range(len(s)):
            if b_fullColumn:
                if rows == (numRows + 1):
                    columns += 1
                    rows = 1
                    if numRows > 2:
                        b_fullColumn = False
                        zigRow = numRows - 1
                        if DEBUG:
                            print("3zigRow="+str(zigRow)+",columns="+str(columns)+"="+s[i])
                        letters[columns][zigRow] = s[i]
                        zigRow -= 1
                    else:
                        if DEBUG:
                            print("1rows="+str(rows)+",columns="+str(columns)+"="+s[i])
                        letters[columns][rows] = s[i]
                        rows += 1
                else:
                    if DEBUG:
                        print("1rows="+str(rows)+",columns="+str(columns)+"="+s[i])
                    letters[columns][rows] = s[i]
                    rows += 1
            else:
                columns += 1
                if zigRow <= 1:
                    b_fullColumn = True
                    rows = 1
                    if DEBUG:
                        print("2rows="+str(rows)+",columns="+str(columns)+"="+s[i])
                    letters[columns][rows] = s[i]
                    rows += 1
                else:
                    if DEBUG:
                        print("4zigRow="+str(zigRow)+",columns="+str(columns)+"="+s[i])
                    letters[columns][zigRow] = s[i]
                    zigRow -= 1
        
        if DEBUG:
            print("columns="+str(columns))
            print("rows="+str(numRows))

        for row in range(1,numRows + 1):
            for column in range(1,columns + 1):
                if len(letters[column][row]) == 1 :
                    if DEBUG:
                        print("row="+str(row)+",column="+str(column)+"="+letters[column][row])
                    zigzig += letters[column][row]
        return zigzig

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        c = 1000
        r = 1000
        letters = [["" for x in range(c)] for y in range(r)]
        
        columns = 1
        rows = 1
        zigzig = ""
        b_fullColumn = True
        zigRow = numRows - 1

        for i in range(len(s)):
            if b_fullColumn:
                if rows == (numRows + 1):
                    columns += 1
                    rows = 1
                    if numRows > 2:
                        b_fullColumn = False
                        zigRow = numRows - 1
                        letters[columns][zigRow] = s[i]
                        zigRow -= 1
                    else:
                        letters[columns][rows] = s[i]
                        rows += 1
                else:
                    letters[columns][rows] = s[i]
                    rows += 1
            else:
                columns += 1
                if zigRow <= 1:
                    b_fullColumn = True
                    rows = 1
                    letters[columns][rows] = s[i]
                    rows += 1
                else:
                    letters[columns][zigRow] = s[i]
                    zigRow -= 1

        for row in range(1,numRows + 1):
            for column in range(1,columns + 1):
                if len(letters[column][row]) == 1 :
                    zigzig += letters[column][row]
        return zigzig

sol = Solution()
#print(sol.convert("PAYPALISHIRING", 3))  #PAHNAPLSIIGYIR
#print(sol.convert("PAYPALISHIRING", 4))  #PINALSIGYAHRPI
#print(sol.convert("AB", 1))  #AB     
#print(sol.convert("ABC", 1))  #ABC
#print(sol.convert("ABCD", 2))  #ACBD
print(sol.convert("hqtripfqcbkifiniulyqqziheiztnagxszqaovtsydaennoibmyrniatqcndetayvqzjnuemzesmugwxuuqierbu", 72))
print(sol.convert("gkwuaheyvohletjqpopdjslkoelfynzeavaaceazuimydypvmgyxblhppuunkttkqtmvanuuvjvahmvvuvsvhzkywhmgchqvdcqd",32))
print(sol.convert("wyhdsqaylwpekgzbnvyqnrajrouupxqlxxospqqapgfzmgcbcc",28))
print(sol.convert("icwsodpwtqrpyuearhwgfnpaqelofrsotqiktxipqzeqvlqmuoubbjbrpmixfclbstnosv",2))
print(sol.convert("pvgcwteylwkbyubxruwszshxpmjrhfawdibzbfypdksbhtaapzsorbnjpz",19))
print(sol.convert("kwvhnwalznmnrbuicygxjxylixrbtvbdrzngxnrwcglujfcme",49))
print(sol.convert("oqqpjojeqoifrqiqwfocbpofkasomzdbpvsa",22))
print(sol.convert("naehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpg",79))
print(sol.convert("zvmwnuufnnxvloyvgmliuqandlyavfauaosnlnv",1))
print(sol.convert("oqqpjojeqoifrqiqwfocbpofkasomzdbpvsa",22))
print(sol.convert("spqzvuqivzptlpvooynyapgvswoaosaghrffnxnjyeeltzaizniccozwknwyhzgpqlwfkjqipuujvwtxlbznryjdo",45))