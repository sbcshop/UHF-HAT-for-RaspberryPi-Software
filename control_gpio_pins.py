# There are 4 GPIO pins in M6E-NANO (UHF HAT)
import mercury
reader = mercury.Reader("tmr:///dev/ttyS0")

reader.set_region("EU3") # select your region 
reader.set_read_plan([1], "GEN2")

# Get numbers of the GPIO pins available as input pins on the device.
print(reader.get_gpio_inputs())

# Set numbers of the GPIO pins available as input pins on the device.
#reader.set_gpio_inputs(list)
#eg-
reader.set_gpio_inputs([1])


# Set numbers of the GPIO pins available as output pins on the device.
# reader.set_gpio_outputs(list)
reader.set_gpio_outputs([1,2,3,4])

# Get numbers of the GPIO pins available as output pins on the device.
print(reader.get_gpio_outputs())


# Sets value of a GPIO pin configured as output (see get_gpio_outputs).
# reader.gpo_set(pin, value)

# set gpio pins HIGH 
reader.gpo_set(1, True)
'''
reader.gpo_set(2, True)
reader.gpo_set(3, True)
reader.gpo_set(4, True)
'''


# set gpio pins LOW 
reader.gpo_set(2, False)
'''
reader.gpo_set(2, False)
reader.gpo_set(3, False)
reader.gpo_set(4, False)
'''
