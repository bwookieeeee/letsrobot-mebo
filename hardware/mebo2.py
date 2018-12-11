from hardware.mebo.letsrobot_to_mebo_converter import LetsRobotToMeboConverter
from hardware.mebo.letsrobot_commands import LetsRobotCommands
from hardware.mebo.letsrobot_to_param_lookup import letsrobot_to_param_lookup
from hardware.mebo.handle_mebo_command import handle_mebo_command
import hardware.mebo.mebo_constants as mebo_constants
import hardware.mebo.mebo_commands as mebo_commands
import httplib
import socket
import time

def setup(robot_config):
    return

def move(args):
    handle_mebo_command(args)