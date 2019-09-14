import random
import pygame
import sys
import time
from pygame.locals import *

# Quick Sort


class QuickSort:
    def __init__(self):
        pygame.init()
        self.thickness = 5
        size = width, height = (self.thickness * 20 + 20), 150
        self.red = [255, 0, 0]
        self.blue = [0, 0, 255]
        self.black = [0, 0, 0]
        self.screen = pygame.display.set_mode(size)

    def screen_update(self, a):
        time.sleep(0.5)
        self.screen.fill(self.black)
        for x in range(0, len(a)):
            pygame.draw.line(self.screen, self.blue, ((x * 10) + self.thickness * 2, 0), ((x * 10) + self.thickness * 2, a[x]), self.thickness)
        pygame.display.update()

    def quick_sort(self, a, lo, hi):
        if lo < hi:
            p = self.partition(a, lo, hi)
            self.quick_sort(a, lo, p - 1)
            self.quick_sort(a, p + 1, hi)
            self.screen_update(a)

    def get_pivot(self, a, hi, lo):
        mid = (hi + lo) // 2
        pivot = hi
        if a[lo] < a[mid]:
            pivot = mid
        elif a[lo] < a[hi]:
            pivot = lo
        return pivot

    def partition(self, a, lo, hi):
        pivotIndex = self.get_pivot(a, lo, hi)
        pivotValue = a[pivotIndex]
        self.screen.fill(self.black)

        for x in range(0, len(a)):
            if x == pivotIndex or x == lo:
                pygame.draw.line(self.screen, self.red, ((x * 10) + self.thickness*2, 0), ((x * 10) + self.thickness * 2, a[x]), self.thickness)
            else:
                pygame.draw.line(self.screen, self.blue, ((x * 10) + self.thickness*2, 0), ((x * 10) + self.thickness * 2, a[x]), self.thickness)

        pygame.display.update()
        a[pivotIndex], a[lo] = a[lo], a[pivotIndex]
        border = lo
        for i in range(lo, hi+1):
            if a[i] < pivotValue:
                border += 1
                a[i], a[border] = a[border], a[i]

        self.screen.fill(self.black)
        for x in range(0, len(a)):
            if x == lo or x == border:
                pygame.draw.line(self.screen, self.red, ((x * 10) + self.thickness * 2, 0), ((x * 10) + self.thickness * 2, a[x]), self.thickness)
            else:
                pygame.draw.line(self.screen, self.blue, ((x * 10) + self.thickness * 2, 0), ((x * 10) + self.thickness * 2, a[x]), self.thickness)
        pygame.display.update()
        a[lo], a[border] = a[border], a[lo]
        time.sleep(0.3)

        return border


a_list = []
for x in range(0, 10):
    z = random.randint(0, 100)
    a_list.append(z)

quickSort = QuickSort()
quickSort.screen_update(a_list)
quickSort.quick_sort(a_list, 0, len(a_list)-1)
print(a_list)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
