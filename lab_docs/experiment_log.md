# Experiment Log - Python Test Case Design

## Q1 Factorial Test Cases
- TC_FAC_01: n=5, expected=120 (positive case)
- TC_FAC_02: n=0, expected=1 (boundary zero)
- TC_FAC_03: n=-4, expected=ValueError (negative input)
- TC_FAC_04: n=3.2, expected=TypeError (invalid type)

## Q2 Palindrome Test Cases
- TC_PAL_01: "madam", expected=True (odd length letters)
- TC_PAL_02: "abba", expected=True (even length letters)
- TC_PAL_03: "A man, a plan, a canal: Panama!", expected=True (mixed characters)
- TC_PAL_04: "12321", expected=True (digits)
- TC_PAL_05: "python", expected=False (non-palindrome)

## Q3 Prime Test Cases
- TC_PRM_01: n=29, expected=True (prime)
- TC_PRM_02: n=100, expected=False (composite)
- TC_PRM_03: n=-7, expected=False (negative)
- TC_PRM_04: n=0, expected=False (zero)
- TC_PRM_05: n=1, expected=False (one)

## Q4 Sort Test Cases
- TC_SRT_01: [], expected=[] (empty list)
- TC_SRT_02: [7], expected=[7] (single element)
- TC_SRT_03: [5,1,4,2], expected=[1,2,4,5] (unsorted)
- TC_SRT_04: [3,1,3,2,2], expected=[1,2,2,3,3] (repeated elements)

## Q5 Fibonacci Test Cases
- TC_FIB_01: n=0, expected=[0] (zero case)
- TC_FIB_02: n=10, expected=[0,1,1,2,3,5,8] (positive case)
- TC_FIB_03: n=-2, expected=ValueError (negative input)
- TC_FIB_04: n=5.5, expected=TypeError (invalid type)

## Execution Summary
- Command: pytest -q
- Status: 26 passed in 0.12s
- Re-run Status: 26 passed in 0.04s
