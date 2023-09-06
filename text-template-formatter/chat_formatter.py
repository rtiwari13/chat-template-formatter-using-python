import pyparsing as pp

def format_chat_template(input_text):
    #  for matching {{gen ... }} commands
    gen_command = pp.Suppress('{{gen') + pp.Word(pp.printables + ' ')('command') + pp.Suppress('}}')

    #  for  user and assistant roles
    user_role = pp.Suppress('{{#user}}') + pp.SkipTo('{{/user}}')('user_text') + pp.Suppress('{{/user}}')
    assistant_role = pp.Suppress('{{#assistant}}') + pp.Group(pp.OneOrMore(gen_command | pp.SkipTo('{{/assistant}}')))('assistant_content') + pp.Suppress('{{/assistant}}')

    # Find all occurrences of {{gen ... }} commands and wrap them with assistant tags
    formatted_text = assistant_role.transformString(input_text)

    # Wrap any remaining text segments with user tags
    formatted_text = f'{{{{#user}}}}{formatted_text}{{{{/user}}}}'

    # Ensure the template ends with {{gen 'write' }} command if not already present
    if not formatted_text.endswith('{{gen \'write\' }}'):
        formatted_text += ' {{#assistant}}{{gen \'write\'}}{{/assistant}}'

    return formatted_text

# Get user input 
user_input = input("Enter your chat text: ")


formatted_template = format_chat_template(user_input)

print("Formatted Chat Template:")
print(formatted_template)

