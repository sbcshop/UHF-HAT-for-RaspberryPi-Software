# This code write the tag
# Performs a synchronous write. Returns True upon success, or False if no tag was found.
# Upon failure an exception is raised.

import mercury
reader = mercury.Reader("tmr:///dev/ttyS0")

reader.set_region("EU3")
reader.set_read_plan([1], "GEN2")

# write your old epc id 
old_epc = b'E200B5A00B82044123743B00'

# write new epic id 
new_epc = b'E20020470000010020300012'

if reader.write(epc_code=new_epc, epc_target=old_epc):
    print('Tag is Rewrited "{}" with "{}"'.format(old_epc, new_epc))
else:
    print('No tag found')

