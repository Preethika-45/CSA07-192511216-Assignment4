import math
print(f"Pure ALOHA: {1/(2*math.e):.2%}")
print(f"Slotted ALOHA: {1/math.e:.2%}")
t=2500/(2*10**8); bits=10_000_000*(2*t)
print(f"Round-trip propagation: {2*t*1e6:.1f} us")
print(f"Minimum frame (simplified): {bits:.0f} bits = {bits/8:.2f} bytes")
print(f"ATM header overhead: {5/53:.2%}")
