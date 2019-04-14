#!/usr/bin/env python

# sp800_22_tests.py
#
# Copyright (C) 2017 David Johnston
# This program is distributed under the terms of the GNU General Public License.
#
# This file is part of sp800_22_tests.
#
# sp800_22_tests is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sp800_22_tests is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with sp800_22_tests.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import os
import sys
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
dirpath = os.path.dirname(os.path.abspath(filename))
sys.path.append(dirpath)


def read_bits_from_file(filename, bigendian=True):
    bitlist = list()
    if filename == None:
        f = sys.stdin
    else:
        f = open(filename, "rb")
    while True:
        bytes = f.read(16384)
        if bytes:
            for bytech in bytes:
                if sys.version_info > (3, 0):
                    byte = bytech
                else:
                    byte = ord(bytech)
                for i in range(8):
                    if bigendian:
                        bit = (byte & 0x80) >> 7
                        byte = byte << 1
                    else:
                        bit = (byte >> i) & 1
                    bitlist.append(bit)
        else:
            break
    f.close()
    return bitlist


def test_sequence(filename, bigendian=True):

    # X 3.1  Frequency (Monobits) Test
    # X 3.2  Frequency Test within a Block
    # X 3.3  Runs Test
    # X 3.4  Test for the Longest Run of Ones in a Block
    # X 3.5  Binary Matrix Rank Test
    # X 3.6  Discrete Fourier Transform (Specral) Test
    # X 3.7  Non-Overlapping Template Matching Test
    # X 3.8  Overlapping Template Matching Test
    # X 3.9  Maurers Universal Statistical Test
    # X 3.10 Linear Complexity Test
    # X 3.11 Serial Test
    # X 3.12 Approximate Entropy Test
    # X 3.13 Cumulative Sums Test
    # X 3.14 Random Excursions Test
    # X 3.15 Random Excursions Variant Test

    testlist = [
        'monobit_test',
        'frequency_within_block_test',
        'runs_test',
        'longest_run_ones_in_a_block_test',
        'binary_matrix_rank_test',
        'dft_test',
        'non_overlapping_template_matching_test',
        'overlapping_template_matching_test',
        'maurers_universal_test',
        'linear_complexity_test',
        'serial_test',
        'approximate_entropy_test',
        'cumulative_sums_test',
        'random_excursion_test',
        'random_excursion_variant_test']

    bits = read_bits_from_file(filename, bigendian)
    gotresult = False
    results = list()

    for testname in testlist:
        print("TEST: %s" % testname)
        m = __import__(f'sp800_22_{testname}')
        func = getattr(m, testname)

        (success, p, plist) = func(bits)

        summary_name = testname
        if success:
            print("  PASS")
        else:
            print("  FAIL")

        if p != None:
            print("  P="+str(p))
            summary_p = p

        if plist != None:
            for pval in plist:
                print("P="+str(pval))
            summary_p = min(plist)

        results.append((summary_name, summary_p, success))

    return results


def print_summary(results):
    print()
    print("TEST SUMMARY")
    print("-------")

    for result in results:
        (test_name, p_value, success) = result
        summary_p = str(round(p_value, 15))
        summary_result = "PASS"
        if not success:
            summary_result = "FAIL"
        print(test_name.ljust(40), summary_p.ljust(18), summary_result)
