import numpy as np

def compute_loss(W):
    return 0.5 * (W[0] ** 2) + 2*W[1]**2

def analytical_gradiet(W):
    grad_w1 = W[0]
    grad_w2 = 4.0 * W[1]
    return np.vstack((grad_w1,grad_w2))

def numerically_gradiet(W , epsilon = 1e-5):
    num = W.shape[0]
    perburbation = np.eye(num) * epsilon

    W_plus = W + perburbation
    W_minus = W - perburbation

    L_plus = compute_loss(W_plus)
    L_minus = compute_loss(W_minus)

    grid = (L_plus - L_minus)/(2 * epsilon)
    return grid.reshape(num , 1)


W = np.array([[3.0],[2.0]])
epsilon = 1e-5

print("current position: ",W)
print("scaler loss: ",compute_loss(W))

grad_analytical = analytical_gradiet(W)
grad_numerical = numerically_gradiet(W, epsilon)

print(f"Analytical Gradient Vector:{grad_analytical}")
print(f"Numerical Gradient Vector (Epsilon={epsilon}):{grad_numerical}")

error = np.abs(grad_analytical - grad_numerical)
max_error = np.max(error)

print("Max absolute error : ", max_error)

# deep learning error should be less than 1e-5

if max_error < 1e-5:
    print("secure")
else:
    print("failure")