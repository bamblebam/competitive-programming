class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        x=zip_longest(version1,version2,fillvalue="0")
        for v1,v2 in zip_longest(version1,version2,fillvalue="0"):
            if int(v1)==int(v2):
                continue
            if int(v1)>int(v2):
                return 1
            if int(v1)<int(v2):
                return -1
        return 0