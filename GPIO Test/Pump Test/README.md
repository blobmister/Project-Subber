# Initial code testing for pump

Both files run infinite loops. To exit loop use ``ctrl+C``. **Do not use ``ctrl+Z``**.
Use following links to appropriately wire up pumps:
- [L298N Motor driver module](https://lastminuteengineers.com/l298n-dc-stepper-driver-arduino-tutorial/)
- [Raspberry Pi PinOut diagram](https://www.hackatronic.com/raspberry-pi-5-pinout-specifications-pricing-a-complete-guide/)

## pump-test.py

Code runs an infinite loop with the flow:

1. Both pumps forward for 1 second
2. Both pumps stopped for 1 second
3. Both pumps backward for 1 second
4. Both pumps stopped for 1 second


## pump-forward.py

1. Both pumps forward for 5 seconds
2. Both pumps stopped for 1 second

## analogue-output.py

1. Incremently increase pump speed
2. Incremently decrease pump speed



