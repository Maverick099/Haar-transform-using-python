import matplotlib.pyplot as p
import pywt.data

# img = cv.imread("image.png")
# img_array = n.float32(img)
# img_array /= 255,

img_array = pywt.data.camera()

coeffs = pywt.dwt2(img_array, 'bior1.3')
LL, (LH, HL, HH) = coeffs
fig = p.figure(figsize=(12, 4))
titles = ['Approximation', ' Horizontal detail',
          'Vertical detail', 'Diagonal detail']

for i, a in enumerate([LL, LH, HL, HH]):
    ax = fig.add_subplot(1, 4, i + 1)
    ax.imshow(a, interpolation="nearest", cmap=p.cm.gray)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])

fig.tight_layout()
p.show()
