import unittest
import helper

class TestExercise1(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
# Calculate the sum of all single digit numbers and assign the result to 's'
s = sum(range(10))

# Print the result to the shell
print(s)
            ''',
            "DC_SOLUTION": '''
# Calculate the sum of all single digit numbers and assign the result to 's'
s = sum(range(10))

# Print the result to the shell
print(s)
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
test_function("sum")
test_object("s")
test_function("print")
success_msg("Great job!")
        '''
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

class TestExercise2(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
# Calculate the sum of all single digit numbers and assign the result to 's'
s = sum(range(10))

# Print the result to the shell
print(s)
            ''',
            "DC_SOLUTION": '''
# Calculate the sum of all single digit numbers and assign the result to 's'
s = sum(range(10))

# Print the result to the shell
print(s)
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
test_function("sum", 
                            not_called_msg = "Don't forget to call `sum()` to calculate what's instructed!",
                            incorrect_msg = "Pass the correct argument to `sum()` in order to calculate what's asked for. Use `range()` here.")

msg = "Don't forget to assign the correct value you calculated with `sum()` to `s`."
test_object("s", 
                        undefined_msg = msg,
                        incorrect_msg = msg)

msg = "Print out the resulting object, `s`!"
test_function("print",
                            not_called_msg = msg,
                            incorrect_msg = msg)
success_msg("Great job!")
        '''
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])


class TestExercise3(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
# Calculate the future value of 100 dollar: result
result = 100 * 1.06 ** 6

# Print out the result
print(result)
            ''',
            "DC_SOLUTION": '''
# Calculate the future value of 100 dollar: result
result = 100 * 1.06 ** 6

# Print out the result
print(result)
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
test_operator(index = 1)

msg = "Assign the result of your first operation to `result`."
test_object("result", 
                        undefined_msg = msg,
                        incorrect_msg = msg)

test_function("print")
success_msg("Great!")
        '''
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

class TestExercise4(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
# Calculate the future value of 100 dollar: result
result = 100 * 1.06 ** 6

# Print out the result
print(result)
            ''',
            "DC_SOLUTION": '''
# Calculate the future value of 100 dollar: result
result = 100 * 1.06 ** 6

# Print out the result
print(result)
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
test_operator(index = 1, used = ["**"], do_eval = False,
              incorrect_op_msg = "A little tip: you should use `**` to do this calculation.")

test_object("result", 
            undefined_msg = "Assign the result of your first operation to `result`.",
            incorrect_msg = "You didn't calculate `result` correctly.")

test_function("print")
success_msg("Great!")
        '''
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

class TestExercise5(unittest.TestCase):

    def setUp(self):
        self.data = {
            "DC_PEC": '''''',
            "DC_CODE": '''
# Initialise the row
fib = [0, 1]

# Update the row correctly each loop
for n in range(2, 20):
    fib.append(fib[n-1] - (- fib[n-2]))
            ''',
            "DC_SOLUTION": '''
# Initialise the row
fib = [0, 1]

# Update the row correctly each loop
for n in range(2, 20):
    fib.append(fib[n-2] + fib[n-1])
'''
        }

    def test_Pass(self):
        self.data["DC_SCT"] = '''
msg = "You have to iterate over `range(2, 20)`"
test_for_loop(index = 1, for_iter = lambda msg=msg: test_function("range", not_called_msg = msg, incorrect_msg = msg))

def test_for_body():
    msg = "Make sure your row, `fib`, updates correctly"
    test_object_after_expression("fib",
                                 extra_env = { "fib": [0, 1, 1, 2] },
                                 context_vals = [4],
                                 undefined_msg = msg,
                                 incorrect_msg = msg)
test_for_loop(index = 1, body = test_for_body)
        '''
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

class TestPartChecks(unittest.TestCase):
    def test_pass_simple(self):
        self.data = {
                "DC_SOLUTION": '''
L2 = [i*2 for i in range(0,10) if i>2]
''',
                "DC_SCT": '''
list_comp = Ex().check_list_comp(0, missing_msg="Did you include a list comprehension?")
list_comp.check_body().test_student_typed('i\*2')
list_comp.check_iter().has_equal_value()
list_comp.check_ifs(0).multi([has_equal_value(context_vals=[i]) for i in range(0,10)])
'''
                }
        self.data["DC_CODE"] = "L2 = [i*2 for i in range(10) if i>2]"
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

    def test_pass_complex1(self):
        self.data = {
                "DC_SOLUTION": """L3 = [i*2 if i> 5 else 0 for i in range(0,10)]""",
                "DC_SCT": """
(Ex().check_list_comp(0)                            # first comptehension
        .check_body()                               # comp's body
        .set_context(i=6)
                .check_if_exp(0)                    # body's inline if
                .has_equal_value()                  
        )
"""
                }
        self.data['DC_CODE'] = self.data['DC_SOLUTION']
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

    def test_fail_complex1(self):
        self.data = {
                "DC_SOLUTION": """L3 = [i*2 if i> 5 else 0 for i in range(0,10)]""",
                "DC_SCT": """
(Ex().check_list_comp(0)                            # first comptehension
        .check_body()                               # comp's body
        .set_context(i=6)
                .check_if_exp(0)                    # body's inline if
                .has_equal_value()                  
        )
"""
                }
        self.data['DC_CODE'] = """L3 = [i*2 for i in range(0,10)]"""  # no inline if
        sct_payload = helper.run(self.data)
        self.assertFalse(sct_payload['correct'])

    def test_pass_complex2(self):
        self.data = {
                "DC_SOLUTION": """L3 = [i*2 if i> 5 else 0 for i in range(0,10)]""",
                "DC_SCT": """
(Ex().check_list_comp(0)                            # first comptehension
        .check_body().set_context(i=6).has_equal_value()                  
        )
"""
                }
        self.data['DC_CODE'] = self.data['DC_SOLUTION']
        sct_payload = helper.run(self.data)
        self.assertTrue(sct_payload['correct'])

if __name__ == "__main__":
    unittest.main()
