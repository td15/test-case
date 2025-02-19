def find_X(A, B, C):
    # Initialize X to 0
    X = 0
    
    # Check each bit position
    for i in range(32):  # Assuming 32-bit integers
        bit_C = (C >> i) & 1
        bit_A = (A >> i) & 1
        bit_B = (B >> i) & 1
        
        if bit_C == 1:
            # If C's bit is 1, we need at least one of A or B to be 1 or set X's bit to 1
            if bit_A == 0 and bit_B == 0:
                # Both A and B are 0, we must set this bit in X
                X |= (1 << i)
        else:
            # If C's bit is 0, both A and B must have this bit as 0
            if bit_A == 1 or bit_B == 1:
                return -1  # Invalid case, cannot satisfy C's bit being 0
    
    # Now we need to check if the calculated X satisfies the original equation
    if ((A | X) & (B | X)) == C:
        return X
    else:
        return -1

# Read input
T = int(input())
for _ in range(T):
    A = int(input())
    B = int(input())
    C = int(input())
    result = find_X(A, B, C)
    print(result)
