#!/usr/bin/env python
#------------------------------
#from psalgos.pypsalgos import local_minimums_2d, local_maximums_2d, local_maximums_rank1_cross_2d
import psalgos.pypsalgos as algos
import numpy as np
#------------------------------
#import pyimgalgos.NDArrGenerators as ag
#data = ag.random_standard(shape=sh, mu=200, sigma=25, dtype=np.float64)
#------------------------------

def test01(tname='1', NUMBER_OF_EVENTS=10, DO_PRINT=False) :


    print 'local extrema : %s' % ('minimums' if tname=='1'\
                             else 'maximums')

    from time import time
    from pyimgalgos.GlobalUtils import print_ndarr
    import pyimgalgos.GlobalGraphics as gg

    #sh, fs = (200,200), (11,10)
    sh, fs = (1000,1000), (11,10)
    #sh, fs = (185,388), (11,5)
    fig1, axim1, axcb1, imsh1 = gg.fig_axim_axcb_imsh(figsize=fs)
    fig2, axim2, axcb2, imsh2 = gg.fig_axim_axcb_imsh(figsize=fs)

    print 'Image shape: %s' % str(sh)

    mu, sigma = 200, 25

    for evnum in range(NUMBER_OF_EVENTS) :

        data = np.array(mu + sigma*np.random.standard_normal(sh), dtype=np.float64)
        mask = np.ones(sh, dtype=np.uint16).flatten()
        #mask = np.random.binomial(2, 0.80, data.size).astype(dtype=np.uint16)
        extrema = np.zeros(sh, dtype=np.uint16).flatten()

        rank=5
        
        nmax = 0

        if DO_PRINT : print_ndarr(data, 'input data')
        t0_sec = time()

        #----------
        if   tname=='1' : nmax = algos.local_minima_1d(data.flatten(), mask, rank, extrema)
        elif tname=='2' : nmax = algos.local_maxima_1d(data.flatten(), mask, rank, extrema)
        #----------
        print 'Event: %4d,  consumed time = %10.6f(sec),  nmax = %d' % (evnum, time()-t0_sec, nmax)

        extrema.shape = sh
        
        if DO_PRINT : print_ndarr(extrema, 'output extrema')
        
        img1 = data
        img2 = extrema

        axim1.clear()
        if imsh1 is not None : del imsh1
        imsh1 = None

        axim2.clear()
        if imsh2 is not None : del imsh2
        imsh2 = None
        
        ave, rms = img1.mean(), img1.std()
        amin, amax = ave-1*rms, ave+5*rms
        gg.plot_imgcb(fig1, axim1, axcb1, imsh1, img1, amin=amin, amax=amax, title='Event: %d, Data'%evnum, cmap='inferno')
        gg.move_fig(fig1, x0=400, y0=30)
        
        gg.plot_imgcb(fig2, axim2, axcb2, imsh2, img2, amin=0, amax=5, title='Event: %d, Local extrema'%evnum, cmap='inferno')
        gg.move_fig(fig2, x0=0, y0=30)
        
        gg.show(mode='DO_NOT_HOLD')
    gg.show()

#------------------------------
#------------------------------
#------------------------------
#------------------------------

if __name__ == "__main__" :
    import sys; global sys
    tname = sys.argv[1] if len(sys.argv) > 1 else '1'
    print 50*'_', '\nTest %s:' % tname
    if   tname == '1' : test01(tname)
    elif tname == '2' : test01(tname)
    else : sys.exit('Test %s is not implemented' % tname)
    sys.exit('End of test %s' % tname)

#------------------------------
