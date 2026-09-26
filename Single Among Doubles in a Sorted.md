## 01. Single Among Doubles in a Sorted

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1)

### Problem Description

**Task:** Given a sorted array arr[]. Find the element that appears only once in the array. All other elements appear exactly twice.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
```
- **Output:**
```text
4
```
- **Explanation:** 4 is the only element that appears exactly once.

##### Example 2

- **Input:**
```text
arr[] = [5]
```
- **Output:**
```text
5
```

##### Example 3

- **Input:**
```text
arr[] = [1, 2, 2, 3, 3]
```
- **Output:**
```text
1
```

#### Constraints

- **1.** `1 ≤ arr.size() ≤ 2 * 10⁶¹ ≤ arr[i] ≤ 10⁶`

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (4)

#### Solution 1 (Python)

- **Submitted:** 2026-09-26 11:26:36
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            if n == 1:
                return arr[0]
            elif i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]
            elif i == (n - 1):
                if arr[i] != arr[i - 1]:
                    return arr[i]
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]
        
        
        # n = len(arr)
        # mpp = {}
        
        # for i in arr:
        #     if i in mpp:
        #         mpp[i] +=1
        #     else:
        #         mpp[i] = 1
        
        # for key, value in mpp.items():
        #     if value == 1:
        #         return key
```

#### Solution 2 (Python)

- **Submitted:** 2026-09-26 11:22:13
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            if n == 1:
                return arr[0]
            elif i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]
            elif i == (n - 1):
                if arr[i] != arr[i - 1]:
                    return arr[i]
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]
        
        
        # n = len(arr)
        # mpp = {}
        
        # for i in arr:
        #     if i in mpp:
        #         mpp[i] +=1
        #     else:
        #         mpp[i] = 1
        
        # for key, value in mpp.items():
        #     if value == 1:
        #         return key
```

#### Solution 3 (Python)

- **Submitted:** 2026-09-26 11:16:30
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        
        for i in range(n):
            if n == 1:
                return arr[0]
            elif i == 0:
                if arr[i] != arr[i + 1]:
                    return arr[i]
            elif i == (n - 1):
                if arr[i] != arr[i - 1]:
                    return arr[i]
            else:
                if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                    return arr[i]
        
        
        # n = len(arr)
        # mpp = {}
        
        # for i in arr:
        #     if i in mpp:
        #         mpp[i] +=1
        #     else:
        #         mpp[i] = 1
        
        # for key, value in mpp.items():
        #     if value == 1:
        #         return key
```

#### Solution 4 (Python)

- **Submitted:** 2026-09-26 11:06:04
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def single(self, arr):
        # code here
        n = len(arr)
        mpp = {}
        
        for i in arr:
            if i in mpp:
                mpp[i] +=1
            else:
                mpp[i] = 1
        
        for key, value in mpp.items():
            if value == 1:
                return key
```

*Generated on: 9/26/2026, 11:32:02 AM*