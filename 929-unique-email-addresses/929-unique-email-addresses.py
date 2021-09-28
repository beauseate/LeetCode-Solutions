class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        emailSet = set()

        for m in emails:
            i = 0
            first = ''
            last = ''
            while m[i] not in ['+', '@']:
                if m[i] != '.':
                    first += m[i]
                i += 1
            while m[i] != '@':
                i += 1
            while i < len(m):
                last += m[i]
                i += 1
            name = first + last
            emailSet.add(name)
        return len(emailSet)
        