#Jared Cousine, mudule for CAN RGX plasma drone for SAIT Supernovas. Takes sensor variables and stores them into a .csv file with their time stamps.  
'''
Copyright (c) 2024 Jared cousine, jared.cousine@gmail.com, SAIT Supernovas
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import time

class CSV_writer:
    def __init__(self):
        self.f_path = 'trial_'
        self.t_num = ''
        self.t_type = ".csv"
        self.path = ''
        self.parameterd = {}
        self.current_box = 1

    def ticks_ms(self):
        return int(time.time() * 1000) % 65534

    def set_trial_number(self, number):
        self.t_num = number
        self.fileprep()

    def fileprep(self):
        parameters = ["time", "humidity", "temp", "pressure", "accel_x", "accel_y", "accel_z", "gyro_x", "gyro_y", "gyro_z", "ozone"]
        for i, parameter in enumerate(parameters):
            self.parameterd[parameter] = i
        self.path = self.f_path + self.t_num + self.t_type
        with open(self.path, 'w') as file:
            file.write(''.join(parameter + ',\n' for parameter in parameters))

    def prewrite(self, row, value):
        col = self.write_time()
        self.write_to_coordinate(row, col, value)

    def write_time(self):
        with open(self.path, 'r') as file:
            lines = file.readlines()

        #timestamp = str(self.ticks_ms())
        timestamp = str(time.ticks_ms())
        lines[0] = lines[0].strip() + ',' + timestamp + '\n'
        
        with open(self.path, 'w') as file:
            file.write(''.join(lines))
        
        return lines[0].count(',')

    def write_to_coordinate(self, row, column, value):
        with open(self.path, 'r') as file:
            lines = file.readlines()

        line = lines[row].strip().split(',')
        while len(line) <= column:
            line.append('')
        line[column] = str(value)
        lines[row] = ','.join(line) + '\n'

        with open(self.path, 'w') as file:
            file.write(''.join(lines))

    def humid(self, value):
        self.prewrite(1, value)

    def set_temp(self, value):
        self.prewrite(2, value)

    def press(self, value):
        self.prewrite(3, value)
    
    def accelx(self, value):
        self.prewrite(4, value)
        
    def accely(self, value):
        self.prewrite(5, value)
        
    def accelz(self, value):
        self.prewrite(6, value)
        
    def gyrox(self, value):
        self.prewrite(7, value)

    def gyroy(self, value):
        self.prewrite(8, value)

    def gyroz(self, value):
        self.prewrite(9, value)

    def ozone(self, value):
        self.prewrite(10, value)

# Example usage
if __name__ == "__main__":
    #current options: humid, set_temp, press, accelx, accely, accelz, gyrox, gyroy, gyroz, and ozone. each will add the current time via self.ticks_ms
    #use lines 112-112\4 to initialize and create the file and writer.<options> to save the value, time and position should be calculated automatically,
    #should time not work uncomment line 55 and comment line 56
    writer = CSV_writer()
    tnum = input("Input trial number: ")
    writer.set_trial_number(tnum)
    writer.humid(4)
    writer.set_temp(5)
    writer.ozone(32)
    writer.press(555)
    writer.set_temp(21)
