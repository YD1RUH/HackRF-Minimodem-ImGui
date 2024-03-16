#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: receive using hackrf
# Author: yd1ruh
# GNU Radio version: 3.8.2.0

from gnuradio import analog
from gnuradio import audio
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
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
freq_rx = int(vars(args).get(svc_name))

class rx_fm(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "receive using hackrf")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 192000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=10,
                taps=None,
                fractional_bw=None)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=100,
                taps=None,
                fractional_bw=None)
        self.osmosdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + 'hackrf'
        )
        self.osmosdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_source_0.set_sample_rate(8e6)
        self.osmosdr_source_0.set_center_freq(freq_rx, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(15000, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                1,
                80000,
                12500,
                100,
                firdes.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, 'pulse', True)
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=80000,
        	quad_rate=80000,
        	tau=75e-6,
        	max_dev=5e3,
          )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_rx_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_nbfm_rx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate





def main(top_block_cls=rx_fm, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
