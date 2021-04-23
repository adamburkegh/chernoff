
# 
# Based on https://gist.github.com/aflaxman/4043086
# 

# from pylab import *

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from numpy import arctan, cos, sin, pi


UPPER_FACE=0; LOWER_FACE_OVERLAP=1; VERTICAL_OVERLAP=2; UPPER_FACE_WIDTH=3;
LOWER_FACE_WIDTH=4; NOSE_LENGTH=5; MOUTH_VERTICAL=6; MOUTH_CURVE=7; 
MOUTH_WIDTH=8; EYE_VERTICAL=9; EYE_SEPARATION=10; EYE_SLANT=11; EYE_ECCEN=12;
EYE_SIZE=13; PUPIL_POS=14; EYEBROW_POS=15; EYEBROW_SLANT=16; EYEBROW_SIZE=17;
HAIR_SIZE=18


'''
Nose, hair and eyebrows can be turned off entirely by setting to zero the parameters nose_length, eyebrow_size and hair_size, respectively.
'''
def cface(ax, upper_face,lower_face_overlap,vertical_overlap,upper_face_width,
              lower_face_width,nose_length,mouth_vertical,mouth_curve,
              mouth_width,eye_vertical,eye_separation,eye_slant,eye_eccen,
              eye_size,pupil_pos,eyebrow_pos,eyebrow_slant,eyebrow_size,
              hair_size):

    x1 = upper_face             # height  of upper face
    x2 = lower_face_overlap     # overlap of lower face
    x3 = vertical_overlap       # half of vertical size of face
    x4 = upper_face_width       # width of upper face
    x5 = lower_face_width       # width of lower face
    x6 = nose_length            # length of nose
    x7 = mouth_vertical         # vertical position of mouth
    x8 = mouth_curve            # curvature of mouth
    x9 = mouth_width            # width of mouth
    x10 = eye_vertical          # vertical position of eyes
    x11 = eye_separation        # separation of eyes
    x12 = eye_slant             # slant of eyes
    x13 = eye_eccen             # eccentricity of eyes
    x14 = eye_size              # size of eyes
    x15 = pupil_pos             # position of pupils
    x16 = eyebrow_pos           # vertical position of eyebrows
    x17 = eyebrow_slant         # slant of eyebrows
    x18 = eyebrow_size          # size of eyebrows
    # x19 = hair_size           # size of hair spikes, but use var directly

    # print(locals())
    
    # transform some values so that input between 0,1 yields variety of output
    x3 = 1.9*(x3-.5)
    x4 = (x4+.25)
    x5 = (x5+.2)
    x6 = .3*(x6+0.01)
    x8 = 2*(x8+.001)    # changed
    x9 = 4*x9           # changed
    x11 /= 5
    x12 = 2*(x12-.5)
    x13 += .05
    x14 += .1
    x14 /= 2.0
    x15 = .5*(x15-.5)
    x16 = 0.6+.25*eyebrow_pos
    x17 = .5*(x17-.5)
    x18 = .5*(x18+.1)

    DRAW_COLOUR='black'

    # top of face, in box with l=-x4, r=x4, t=x1, b=x3
    e = mpl.patches.Ellipse( (0,(x1+x3)/2), 2*x4, (x1-x3), fc='white', linewidth=2)
    ax.add_artist(e)

    # bottom of face, in box with l=-x5, r=x5, b=-x1, t=x2+x3
    e = mpl.patches.Ellipse( (0,(-x1+x2+x3)/2), 2*x5, (x1+x2+x3), fc='white', linewidth=2)
    ax.add_artist(e)

    # cover overlaps
    e = mpl.patches.Ellipse( (0,(x1+x3)/2), 2*x4, (x1-x3), fc='white', ec='none')
    ax.add_artist(e)
    e = mpl.patches.Ellipse( (0,(-x1+x2+x3)/2), 2*x5, (x1+x2+x3), fc='white', ec='none')
    ax.add_artist(e)
    
    # draw nose
    if nose_length != 0:
        plt.plot([0,0], [-x6/2, x6/2], 'k')
    
    # draw mouth
    p = mpl.patches.Arc( (0,-x7+.5/x8), 1/x8, 1/x8, theta1=270-180/pi*arctan(x8*x9), theta2=270+180/pi*arctan(x8*x9))
    ax.add_artist(p)
    
    # draw eyes
    p = mpl.patches.Ellipse( (-x11-x14/2,x10), x14, x13*x14, angle=-180/pi*x12, facecolor='white',edgecolor=DRAW_COLOUR)
    ax.add_artist(p)
    
    p = mpl.patches.Ellipse( (x11+x14/2,x10), x14, x13*x14, angle=180/pi*x12, facecolor='white',edgecolor=DRAW_COLOUR)
    ax.add_artist(p)

    # draw pupils
    pupil_size = x14/2.0
    p = mpl.patches.Ellipse( (-x11-x14/2-x15*x14/2, x10), pupil_size, pupil_size, facecolor=DRAW_COLOUR)
    ax.add_artist(p)
    p = mpl.patches.Ellipse( (x11+x14/2-x15*x14/2, x10), pupil_size, pupil_size, facecolor=DRAW_COLOUR)
    ax.add_artist(p)
    
    # draw eyebrows
    if eyebrow_size != 0:
        plt.plot([-x11-x14/2-x14*x18/2,-x11-x14/2+x14*x18/2],
                 [x10+x13*x14*(x16+x17),x10+x13*x14*(x16-x17)],'k')
        plt.plot([x11+x14/2+x14*x18/2,x11+x14/2-x14*x18/2],
                 [x10+x13*x14*(x16+x17),x10+x13*x14*(x16-x17)],'k')

    # draw face
    face_height = 1.9
    face_width = face_height # 2.1
    p = mpl.patches.Ellipse( (0,0), face_height, face_width, fill=False )
    ax.add_artist(p)

    # draw hair
    if hair_size != 0:
        face_rad = face_width / 2.0
        hair_rad = face_rad + 0.25*hair_size
        num_spikes = 10 # round(10*hair_size)
        angle_inc = pi / num_spikes
        spike_inc = angle_inc / 2.0
        x_series = []; y_series = [];
        ct_angle = -spike_inc
        for spike in range(num_spikes):
            ct_angle += angle_inc 
            pt_x = hair_rad*cos(ct_angle)
            pt_y = hair_rad*sin(ct_angle)
            x_series += [face_rad*cos(ct_angle-spike_inc),
                            hair_rad*cos(ct_angle),
                         face_rad*cos(ct_angle+spike_inc) ]
            y_series += [face_rad*sin(ct_angle-spike_inc),
                            hair_rad*sin(ct_angle),
                         face_rad*sin(ct_angle+spike_inc) ]
        plt.plot(x_series, y_series, 'k') 



