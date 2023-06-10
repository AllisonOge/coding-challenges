#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/05/10 11: 05
# @Author : AllisonOge

import unittest
import subprocess
import os

class TestSampleProblem(unittest.TestCase):
    def test_sample_set(self):
        root_directory = os.path.dirname(os.path.dirname(__file__))
        test_directory = root_directory + "/test/"
        input_sample_path = test_directory + "/kickstart_challenge1/sample_test_set_1/sample_ts1_input.txt"
        output_sample_path = test_directory + "/kickstart_challenge1/sample_test_set_1/sample_ts1_output.txt"

        sample_problem_program = root_directory + "/python/sample_problem.py"

        with open(input_sample_path, "r") as input_file, open(output_sample_path, "r") as output_file:
            # read input and output files
            input_data = input_file.read()
            expected_output = output_file.read()

            # run the program as a separate process
            process = subprocess.Popen(["python", sample_problem_program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            # send the input data to the program
            actual_output, error = process.communicate(input=input_data)

            # assert the output matches the expected output
            self.assertEqual(expected_output, actual_output)
    
    def test_set_1(self):
        root_directory = os.path.dirname(os.path.dirname(__file__))
        test_directory = root_directory + "/test/"
        input_test_set = test_directory + "/kickstart_challenge1/test_set_1/ts1_input.txt"
        output_test_set = test_directory + "/kickstart_challenge1/test_set_1/ts1_output.txt"

        sample_problem_program = root_directory + "/python/sample_problem.py"

        with open(input_test_set, "r") as input_file, open(output_test_set, "r") as output_file:
            # read input and output files
            input_data = input_file.read()
            expected_output = output_file.read()

            # run the program as a separate process
            process = subprocess.Popen(["python", sample_problem_program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

            # send the input data to the program with time limit
            try:
                actual_output, _ = process.communicate(input=input_data, timeout=40)
            except subprocess.TimeoutExpired:
                self.fail("Test case exceeded the time limit of 40 seconds")

            # assert the output matches the expected output
            self.assertEqual(expected_output.strip(), actual_output.strip())
