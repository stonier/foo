#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# License: BSD
#   https://raw.githubusercontent.com/splintered-reality/py_trees/devel/LICENSE
#

##############################################################################
# Imports
##############################################################################

import unittest

import rclpy

##############################################################################
# Helpers
##############################################################################

##############################################################################
# Tests
##############################################################################


class TestActionServers(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("ROS INIT")
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        print("ROS Shutdown")
        rclpy.shutdown()

    def setUp(self):
        pass

    ########################################
    # Success
    ########################################

    def test_success(self):
        print("Success")
        self.assertEqual(5, 5)

