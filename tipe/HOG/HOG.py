import matplotlib.pyplot as plt
import numpy as np

# img : 64*128

def gradient(img):
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    # Horizontal gradients
    dx = np.zeros_like(R)
    dx[:, 1:-1] = R[:, 2:] - R[:, :-2]
    dx[:, 0] = R[:, 1] - R[:, 0]
    dx[:, -1] = R[:, -1] - R[:, -2]

    dy = np.zeros_like(R)
    dy[1:-1, :] = R[:-2, :] - R[2:, :]
    dy[0, :] = R[1, :] - R[0, :]
    dy[-1, :] = R[-1, :] - R[-2, :]

    # Repeat for G and B
    dx_g, dx_b = dx.copy(), dx.copy()
    dy_g, dy_b = dy.copy(), dy.copy()

    dx_g[:, 1:-1] = G[:, 2:] - G[:, :-2]
    dx_b[:, 1:-1] = B[:, 2:] - B[:, :-2]

    dy_g[1:-1, :] = G[:-2, :] - G[2:, :]
    dy_b[1:-1, :] = B[:-2, :] - B[2:, :]

    return dx, dx_g, dx_b, dy, dy_g, dy_b

def magnitude_gradient(dx, dx_g, dx_b, dy, dy_g, dy_b):
    mag_r = np.sqrt(dx ** 2 + dy ** 2)
    mag_g = np.sqrt(dx_g ** 2 + dy_g ** 2)
    mag_b = np.sqrt(dx_b ** 2 + dy_b ** 2)

    mag = np.maximum(np.maximum(mag_r, mag_g), mag_b)

    # Return magnitudes and associated gradients for visualization
    grad_x = np.where(mag == mag_r, dx, np.where(mag == mag_g, dx_g, dx_b))
    grad_y = np.where(mag == mag_r, dy, np.where(mag == mag_g, dy_g, dy_b))

    return mag, grad_x, grad_y

def angle_gradient(grad_x, grad_y):
    angle = np.arctan2(grad_y, grad_x)  # Use arctan2 for full circle calculation
    angle = np.degrees(angle) % 360  # Convert to degrees and normalize to [0, 360[
    return angle

def mat_histogramme(mag, angle):
    bins = np.arange(0, 181, 20)  # 9 bins for 0-160 degrees
    histo = np.zeros((mag.shape[0] // 8, mag.shape[1] // 8, len(bins) - 1))

    for i in range(0, mag.shape[0], 8):
        for j in range(0, mag.shape[1], 8):
            block_mag = mag[i:i+8, j:j+8]
            block_angle = angle[i:i+8, j:j+8]
            for k in range(8):
                for l in range(8):
                    bin_index = np.digitize(block_angle[k, l], bins, right=False) - 1
                    histo[i // 8, j // 8, bin_index] += block_mag[k, l]

    # Normalize histograms to have unit length
    norm = np.linalg.norm(histo, axis=2, keepdims=True)
    histo = np.where(norm != 0, histo / norm, histo)  # Avoid division by zero

    return histo

def histogramme_blocs(histo):
    for i in range(histo.shape[0]):
        for j in range(histo.shape[1]):
            plt.figure(figsize=(10, 4))
            plt.bar(np.arange(len(histo[i, j, :])), histo[i, j, :], color='blue', edgecolor='red')
            plt.title(f"Histogram for block ({i}, {j})")
            plt.show()

def HOG(img):
    dx, dx_g, dx_b, dy, dy_g, dy_b = gradient(img)
    mag, grad_x, grad_y = magnitude_gradient(dx, dx_g, dx_b, dy, dy_g, dy_b)
    angle = angle_gradient(grad_x, grad_y)
    histo = mat_histogramme(mag, angle)
    histogramme_blocs(histo)

