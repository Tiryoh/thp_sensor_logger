#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

VERSION="0.0.1"

def get_thp_value():
    try:
        with open('/dev/ttyACM0', 'r') as f:
            raw_data = f.readline()
        return raw_data.strip()[:-1].split(',')
    except FileNotFoundError:
        print('/dev/ttyACM0 not found')
        exit(-1)

if __name__ == '__main__':
    print('THP Logger version{}'.format(VERSION))
    j = 0
    while(1):
        history = []
        for i in range(100):
            history.append(get_thp_value()) #timestamp, temp, humidity, pressure
            if (i % 10) == 0:
                print('{}, '.format(i), end='')
        for i in range(100):
            with open('log/log{:04}.csv'.format(j), 'a') as f:
                # f.write(str(history[i]))
                writer = csv.writer(f, lineterminator='\n')
                writer.writerow(history[i])
            # print(str(history[i]))
        j = j+1
        print('log{}'.format(j))

