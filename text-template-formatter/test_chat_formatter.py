import unittest
from chat_formatter import format_chat_template
import pyparsing as pp

class TestFormatChatTemplate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic_input(self):
        input_text = "Hello, how are you?"
        expected_output = "{{#user}}Hello, how are you?{{/user}} {{#assistant}}{{gen 'write'}}{{/assistant}}"
        self.assertEqual(format_chat_template(input_text), expected_output)

    def test_single_gen_command(self):
        input_text = "Generate a random number: {{gen random}} please."
        expected_output = "{{#user}}Generate a random number: {{gen random}} please.{{/user}} {{#assistant}}{{gen 'write'}}{{/assistant}}"
        self.assertEqual(format_chat_template(input_text), expected_output)

    def test_multiple_gen_commands(self):
        input_text = "Generate random numbers: {{gen random}}, {{gen random}}, and {{gen random}}."
        expected_output = "{{#user}}Generate random numbers: {{gen random}}, {{gen random}}, and {{gen random}}.{{/user}} {{#assistant}}{{gen 'write'}}{{/assistant}}"

        self.assertEqual(format_chat_template(input_text), expected_output)

  

def format_chat_template(input_text):
    
    pass

if __name__ == '__main__':
    unittest.main()

