import numpy as np
import math
class _data_config():
    def __init__(self):
        self.center = {'x':145,'y':145}     #  mm

        self.red_box_L = 90     #   mm
        self.red_box_W = 90     #   mm
        self.red_box_H = 41     #   mm

        self.cylinder_d = 106   #  mm
        self.cylinder_h = 40    #  mm

        self.car_L = 154    #   mm
        self.car_W = 66     #   mm
        self.car_H = 40     #   mm

        self.pig_L = 102    #   mm
        self.pig_W = 76     #   mm
        self.pig_H = 71     #   mm

        self.beer_d = 66
        self.beer_h = 168

        self.hitiger_d = 71
        self.hitiger_h = 198

        self.crest_L = 31
        self.crest_W = 200
        self.crest_H = 39
class box_6d(_data_config):
    def __init__(self):
        super().__init__()
        self.__red_box_center = [self.center['x'],self.center['y'],self.red_box_H/2]
        self.redbox = np.array([[self.__red_box_center[0],                        self.__red_box_center[1],                        self.__red_box_center[2]],         # center_point
                                      [self.__red_box_center[0]-self.red_box_L/2,  self.__red_box_center[1]-self.red_box_W/2,  self.__red_box_center[2]-self.red_box_H/2],        # point_1
                                      [self.__red_box_center[0]-self.red_box_L/2,  self.__red_box_center[1]-self.red_box_W/2,  self.__red_box_center[2]+self.red_box_H/2],       # point_2
                                      [self.__red_box_center[0]-self.red_box_L/2,  self.__red_box_center[1]+self.red_box_W/2,  self.__red_box_center[2]-self.red_box_H/2],       # point_3
                                      [self.__red_box_center[0]-self.red_box_L/2,  self.__red_box_center[1]+self.red_box_W/2,  self.__red_box_center[2]+self.red_box_H/2],      # point_4
                                      [self.__red_box_center[0]+self.red_box_L/2,  self.__red_box_center[1]-self.red_box_W/2,  self.__red_box_center[2]-self.red_box_H/2],       # point_5
                                      [self.__red_box_center[0]+self.red_box_L/2,  self.__red_box_center[1]-self.red_box_W/2,  self.__red_box_center[2]+self.red_box_H/2],      # point_6
                                      [self.__red_box_center[0]+self.red_box_L/2,  self.__red_box_center[1]+self.red_box_W/2,  self.__red_box_center[2]-self.red_box_H/2],      # point_7
                                      [self.__red_box_center[0]+self.red_box_L/2,  self.__red_box_center[1]+self.red_box_W/2,  self.__red_box_center[2]+self.red_box_H/2]])       # point_8
        self.redbox_diameter = math.sqrt(pow(self.red_box_H,2)+pow(self.red_box_L,2)+pow(self.red_box_W,2))

        self.__cylinder_center = [self.center['x'],self.center['y'],self.cylinder_h/2]
        self.cylinder_center = [self.center['x'],self.center['y'],self.cylinder_h/2]
        self.cylinder = np.array([[self.__cylinder_center[0],                        self.__cylinder_center[1],                        self.__cylinder_center[2]],         # center_point
                                      [self.__cylinder_center[0]-self.cylinder_d/2,  self.__cylinder_center[1]-self.cylinder_d/2,  self.__cylinder_center[2]-self.cylinder_h/2],        # point_1
                                      [self.__cylinder_center[0]-self.cylinder_d/2,  self.__cylinder_center[1]-self.cylinder_d/2,  self.__cylinder_center[2]+self.cylinder_h/2],       # point_2
                                      [self.__cylinder_center[0]-self.cylinder_d/2,  self.__cylinder_center[1]+self.cylinder_d/2,  self.__cylinder_center[2]-self.cylinder_h/2],       # point_3
                                      [self.__cylinder_center[0]-self.cylinder_d/2,  self.__cylinder_center[1]+self.cylinder_d/2,  self.__cylinder_center[2]+self.cylinder_h/2],      # point_4
                                      [self.__cylinder_center[0]+self.cylinder_d/2,  self.__cylinder_center[1]-self.cylinder_d/2,  self.__cylinder_center[2]-self.cylinder_h/2],       # point_5
                                      [self.__cylinder_center[0]+self.cylinder_d/2,  self.__cylinder_center[1]-self.cylinder_d/2,  self.__cylinder_center[2]+self.cylinder_h/2],      # point_6
                                      [self.__cylinder_center[0]+self.cylinder_d/2,  self.__cylinder_center[1]+self.cylinder_d/2,  self.__cylinder_center[2]-self.cylinder_h/2],      # point_7
                                      [self.__cylinder_center[0]+self.cylinder_d/2,  self.__cylinder_center[1]+self.cylinder_d/2,  self.__cylinder_center[2]+self.cylinder_h/2]])       # point_8
        self.cylinder_diameter = math.sqrt(pow(self.cylinder_d,2)+pow(self.cylinder_h,2))

        self.__car_center = [self.center['x'],self.center['y'],self.car_H/2]
        self.car = np.array([[self.__car_center[0],                        self.__car_center[1],                        self.__car_center[2]],         # center_point
                                      [self.__car_center[0]-self.car_W/2,  self.__car_center[1]-self.car_L/2,  self.__car_center[2]-self.car_H/2],        # point_1
                                      [self.__car_center[0]-self.car_W/2,  self.__car_center[1]-self.car_L/2,  self.__car_center[2]+self.car_H/2],       # point_2
                                      [self.__car_center[0]-self.car_W/2,  self.__car_center[1]+self.car_L/2,  self.__car_center[2]-self.car_H/2],       # point_3
                                      [self.__car_center[0]-self.car_W/2,  self.__car_center[1]+self.car_L/2,  self.__car_center[2]+self.car_H/2],      # point_4
                                      [self.__car_center[0]+self.car_W/2,  self.__car_center[1]-self.car_L/2,  self.__car_center[2]-self.car_H/2],       # point_5
                                      [self.__car_center[0]+self.car_W/2,  self.__car_center[1]-self.car_L/2,  self.__car_center[2]+self.car_H/2],      # point_6
                                      [self.__car_center[0]+self.car_W/2,  self.__car_center[1]+self.car_L/2,  self.__car_center[2]-self.car_H/2],      # point_7
                                      [self.__car_center[0]+self.car_W/2,  self.__car_center[1]+self.car_L/2,  self.__car_center[2]+self.car_H/2]])       # point_8
        self.car_diameter = math.sqrt(pow(self.car_H,2)+pow(self.car_L,2)+pow(self.car_W,2))

        self.__pig_center = [self.center['x'],self.center['y'],self.pig_H/2]
        self.pig = np.array([[self.__pig_center[0],                        self.__pig_center[1],                        self.__pig_center[2]],         # center_point
                                      [self.__pig_center[0]-self.pig_L/2,  self.__pig_center[1]-self.pig_W/2,  self.__pig_center[2]-self.pig_H/2],        # point_1
                                      [self.__pig_center[0]-self.pig_L/2,  self.__pig_center[1]-self.pig_W/2,  self.__pig_center[2]+self.pig_H/2],       # point_2
                                      [self.__pig_center[0]-self.pig_L/2,  self.__pig_center[1]+self.pig_W/2,  self.__pig_center[2]-self.pig_H/2],       # point_3
                                      [self.__pig_center[0]-self.pig_L/2,  self.__pig_center[1]+self.pig_W/2,  self.__pig_center[2]+self.pig_H/2],      # point_4
                                      [self.__pig_center[0]+self.pig_L/2,  self.__pig_center[1]-self.pig_W/2,  self.__pig_center[2]-self.pig_H/2],       # point_5
                                      [self.__pig_center[0]+self.pig_L/2,  self.__pig_center[1]-self.pig_W/2,  self.__pig_center[2]+self.pig_H/2],      # point_6
                                      [self.__pig_center[0]+self.pig_L/2,  self.__pig_center[1]+self.pig_W/2,  self.__pig_center[2]-self.pig_H/2],      # point_7
                                      [self.__pig_center[0]+self.pig_L/2,  self.__pig_center[1]+self.pig_W/2,  self.__pig_center[2]+self.pig_H/2]])       # point_8

        self.__beer_center = [self.center['x'],self.center['y'],self.beer_h/2]
        self.beer_center = [self.center['x'],self.center['y'],self.beer_h/2]
        self.beer = np.array([  [self.__beer_center[0],                        self.__beer_center[1],                        self.__beer_center[2]],         # center_point
                                [self.__beer_center[0]-self.beer_d/2,  self.__beer_center[1]-self.beer_d/2,  self.__beer_center[2]-self.beer_h/2],        # point_1
                                [self.__beer_center[0]-self.beer_d/2,  self.__beer_center[1]-self.beer_d/2,  self.__beer_center[2]+self.beer_h/2],       # point_2
                                [self.__beer_center[0]-self.beer_d/2,  self.__beer_center[1]+self.beer_d/2,  self.__beer_center[2]-self.beer_h/2],       # point_3
                                [self.__beer_center[0]-self.beer_d/2,  self.__beer_center[1]+self.beer_d/2,  self.__beer_center[2]+self.beer_h/2],      # point_4
                                [self.__beer_center[0]+self.beer_d/2,  self.__beer_center[1]-self.beer_d/2,  self.__beer_center[2]-self.beer_h/2],       # point_5
                                [self.__beer_center[0]+self.beer_d/2,  self.__beer_center[1]-self.beer_d/2,  self.__beer_center[2]+self.beer_h/2],      # point_6
                                [self.__beer_center[0]+self.beer_d/2,  self.__beer_center[1]+self.beer_d/2,  self.__beer_center[2]-self.beer_h/2],      # point_7
                                [self.__beer_center[0]+self.beer_d/2,  self.__beer_center[1]+self.beer_d/2,  self.__beer_center[2]+self.beer_h/2]])       # point_8
        self.beer_diameter = math.sqrt(pow(self.beer_d,2)+pow(self.beer_h,2))

        self.__hitiger_center = [self.center['x'],self.center['y'],self.hitiger_h/2]
        self.hitiger_center = [self.center['x'],self.center['y'],self.hitiger_h/2]
        self.hitiger = np.array([  [self.__hitiger_center[0],                        self.__hitiger_center[1],                        self.__hitiger_center[2]],         # center_point
                                [self.__hitiger_center[0]-self.hitiger_d/2,  self.__hitiger_center[1]-self.hitiger_d/2,  self.__hitiger_center[2]-self.hitiger_h/2],        # point_1
                                [self.__hitiger_center[0]-self.hitiger_d/2,  self.__hitiger_center[1]-self.hitiger_d/2,  self.__hitiger_center[2]+self.hitiger_h/2],       # point_2
                                [self.__hitiger_center[0]-self.hitiger_d/2,  self.__hitiger_center[1]+self.hitiger_d/2,  self.__hitiger_center[2]-self.hitiger_h/2],       # point_3
                                [self.__hitiger_center[0]-self.hitiger_d/2,  self.__hitiger_center[1]+self.hitiger_d/2,  self.__hitiger_center[2]+self.hitiger_h/2],      # point_4
                                [self.__hitiger_center[0]+self.hitiger_d/2,  self.__hitiger_center[1]-self.hitiger_d/2,  self.__hitiger_center[2]-self.hitiger_h/2],       # point_5
                                [self.__hitiger_center[0]+self.hitiger_d/2,  self.__hitiger_center[1]-self.hitiger_d/2,  self.__hitiger_center[2]+self.hitiger_h/2],      # point_6
                                [self.__hitiger_center[0]+self.hitiger_d/2,  self.__hitiger_center[1]+self.hitiger_d/2,  self.__hitiger_center[2]-self.hitiger_h/2],      # point_7
                                [self.__hitiger_center[0]+self.hitiger_d/2,  self.__hitiger_center[1]+self.hitiger_d/2,  self.__hitiger_center[2]+self.hitiger_h/2]])       # point_8
        self.hitiger_diameter = math.sqrt(pow(self.hitiger_d,2)+pow(self.hitiger_h,2))

        self.__crest_center = [self.center['x'],self.center['y'],self.crest_H/2]
        self.crest_center = [self.center['x'],self.center['y'],self.crest_H/2]
        self.crest = np.array([[self.__crest_center[0],                        self.__crest_center[1],                        self.__crest_center[2]],         # center_point
                                      [self.__crest_center[0]-self.crest_W/2,  self.__crest_center[1]-self.crest_L/2,  self.__crest_center[2]-self.crest_H/2],        # point_1
                                      [self.__crest_center[0]-self.crest_W/2,  self.__crest_center[1]-self.crest_L/2,  self.__crest_center[2]+self.crest_H/2],       # point_2
                                      [self.__crest_center[0]-self.crest_W/2,  self.__crest_center[1]+self.crest_L/2,  self.__crest_center[2]-self.crest_H/2],       # point_3
                                      [self.__crest_center[0]-self.crest_W/2,  self.__crest_center[1]+self.crest_L/2,  self.__crest_center[2]+self.crest_H/2],      # point_4
                                      [self.__crest_center[0]+self.crest_W/2,  self.__crest_center[1]-self.crest_L/2,  self.__crest_center[2]-self.crest_H/2],       # point_5
                                      [self.__crest_center[0]+self.crest_W/2,  self.__crest_center[1]-self.crest_L/2,  self.__crest_center[2]+self.crest_H/2],      # point_6
                                      [self.__crest_center[0]+self.crest_W/2,  self.__crest_center[1]+self.crest_L/2,  self.__crest_center[2]-self.crest_H/2],      # point_7
                                      [self.__crest_center[0]+self.crest_W/2,  self.__crest_center[1]+self.crest_L/2,  self.__crest_center[2]+self.crest_H/2]])       # point_8
        self.crest_diameter = math.sqrt(pow(self.crest_H,2)+pow(self.crest_L,2)+pow(self.crest_W,2))