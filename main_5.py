# завдання 2// № 20

import platform

plat_str = platform.platform()
processor = platform.processor()
plat_str_0 = platform.python_implementation()
plat_str_1 = platform.python_version()

print("platform() = %s" % (plat_str))
print('python_implementation() = %s' % (plat_str_0))
print('python_version() = %s' % (plat_str_1))
print('processor = %s' % (processor))
