# Domain .ES backorder

Live monitoring .ES domains expiration and execute domain backorder as soon as expired. Notify spanish domains (.ES) expiration.

Examples usage:

You can install linux command "watch" to monitor domain .es status every 0.5 seconds for example:

watch -n 0.5 -d -g ./check_availability.py domain_I_want.es

and inside check_availability.py script, fill line number 37 to indicate shell command to execute as soon as domain becomes AVAILABLE. For example, you can use registrants API to register domain instantly (domain backorder) & catch it!

REQUIREMENTS:

Python v3
Module bs4
Module lxml
USAGE COMMAND:

python check_availability.py domain_I_want.es

COLLABORATIONS:

Collaborations to improve script are always welcome.
