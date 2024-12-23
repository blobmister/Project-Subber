# Blinking LED test to ensure GPIO library is properly working on RaspberryPi

The following test is written using python.

Use board pin 18 for positive terminal. If using different pin, change value of ``led`` variable appropriately.

To run test wire up LED appropriately, then navigate to Subber/GPIO and run:

``python3 gpio-python-test.py``

The test runs an infinite loop. Exit by force quitting python script with ``CTRL+z``