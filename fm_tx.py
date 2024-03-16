#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: transmit using hackrf
# Author: YD1RUH
# GNU Radio version: 3.8.2.0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import os
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
import argparse

parser = argparse.ArgumentParser(prog=None,description="input freq")   
parser.add_argument("--freq", nargs="?",help="option")
args = parser.parse_args()
svc_name = "freq"
freq_tx = int(vars(args).get(svc_name))

class fm_tx(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "transmit using hackrf")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 48e3

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=2000000,
                decimation=96000,
                taps=None,
                fractional_bw=None)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(2000000)
        #self.osmosdr_sink_0.set_center_freq(433e6, 0)
        self.osmosdr_sink_0.set_center_freq(freq_tx, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(12500, 0)
        current = os.getcwd()
        self.blocks_wavfile_source_0 = blocks.wavfile_source(current+'/send.wav', False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(1)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=48000,
        	quad_rate=96000,
        	tau=75e-6,
        	max_dev=5e3,
        	fh=0,
                )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.osmosdr_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

def tx(top_block_cls=fm_tx, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    tb.wait()


if __name__ == '__main__':
    tx()
