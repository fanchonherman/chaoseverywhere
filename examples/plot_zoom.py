"""
Animation of a zoom
======================
"""

################################
# Some Setup
# -------------------



import chaoseverywhere as chaos
import matplotlib.pyplot as plt
import os
import matplotlib.animation as animation

im_init = chaos.Mandelbrot_disp(-.5,0,1.5)
im_init = im_init.mandelbrot()

fig = plt.figure()
im = plt.imshow(im_init, cmap='bone', animated=True)

results_dir = '../doc/_build/html/_images/'

ims = []
for i in range(150):
    im = plt.imshow(chaos.Mandelbrot_disp(-1, -.3, 0.4-i/300,
            t_max=100,
            precision=400).mandelbrot(), animated=True, cmap='bone')
    ims.append([im])

sample_file_name = "Mandel_zoom"
os.makedirs(results_dir, exist_ok=True)

ani = animation.ArtistAnimation(fig, ims, interval=50)
ani.save(results_dir + sample_file_name + '.mp4')

plt.close()


########################
# The video
# ----------------
# .. raw:: html
#
#          <video controls src="../../../_build/html/_images/Mandel_zoom.mp4"></video>



#################################
# See a self-similar structure
# -----------------------------------
# The Mandelbrot set is clearly not a self-similar object. But inside it, we can see structures repeating themselves.



plt.figure()
plt.axis('off')
plt.imshow(chaos.Mandelbrot_disp(-1, -.3, 0.4-110/300,
            t_max=100,
            precision=400).mandelbrot(), cmap='bone')
plt.show()



