import logging
import sys
try:
    import obd
except ImportError:
    import subprocess
    subprocess.run([
        'pip',
        'install',
        'git+https://github.com/SLR8/py-obd'
    ])

    import obd

# connection = obd.OBD()

# command = obd.commands.SPEED

# response = connection.query(command)
# print(response.value)


# Executes commands passed from the client
# All commands should start with '$' 
def executor(command_name):
    command = name_to_command(command_name)
    logging.info(command)
    response = connection.query(command)

def has_command(command):
    return obd.commands.has_command(command)

def has_name(name):
    return obd.commands.has_name(name)


def name_to_command(command_name):
    # Ensure upper
    # command_name = upper(command_name)
    # ensure exists
    if has_name(command_name):
        print("Command exists")
        # return obd.commands
        return obd.commands[command_name]
    else:
        logging.error('The command does not exist')



if __name__ == "__main__":
    executor(sys.argv[1])