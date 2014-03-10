import unittest
import math
from BicycleWheel import *

class BicycleWheelTest(unittest.TestCase):
    def setUp(self):
        self.bicycleWheel = BicycleWheel()
        
    def test_canary(self):
        self.assertTrue(True)
    
    def test_set_wheel_size_when_hub_size_is_less_than_one_forth_new_wheel_size(self):
        self.bicycleWheel.setWheelSize(100.0)
        self.assertEqual(100.0, self.bicycleWheel.wheelSize)
        
    def test_set_wheel_size_when_hub_size_is_equal_to_one_forth_new_wheel_size(self):
        self.bicycleWheel.setWheelSize(40.0)
        self.assertEqual(40.0, self.bicycleWheel.wheelSize)
        
    def test_set_wheel_size_when_hub_size_is_greater_than_one_forth_new_wheel_size(self):
        self.bicycleWheel.setWheelSize(30.0)
        self.assertEqual(80.0, self.bicycleWheel.wheelSize)
        
    def test_set_hub_size_when_new_hub_size_is_less_than_one_forth_wheel_size(self):
        self.bicycleWheel.setHubSize(10.5)
        self.assertEqual(10.5, self.bicycleWheel.hubSize)
        
    def test_set_hub_size_when_new_hub_size_is_equal_to_one_forth_wheel_size(self):
        self.bicycleWheel.setHubSize(20.0)
        self.assertEqual(20.0, self.bicycleWheel.hubSize)
        
    def test_set_hub_size_when_new_hub_size_is_greater_than_one_forth_wheel_size(self):
        self.bicycleWheel.setHubSize(30.0)
        self.assertEqual(10.0, self.bicycleWheel.hubSize)
        
    def test_set_number_of_spokes_when_new_number_of_spoke_is_greater_or_equal_to_8(self):
        self.bicycleWheel.setNumberOfSpokes(10)
        self.assertEqual(10, self.bicycleWheel.numberOfSpokes)
        
    def test_set_number_of_spokes_when_new_number_of_spoke_is_less_than_to_8(self):
        self.bicycleWheel.setNumberOfSpokes(6)
        self.assertEqual(8, self.bicycleWheel.numberOfSpokes)
    
    def test_get_angle_of_spokes_that_number_of_spokes_is_8(self):
        self.assertEqual(math.pi/4, self.bicycleWheel.getAngleOfSpokes())
        
    def test_get_angle_of_spokes_that_number_of_spokes_is_10(self):
        self.bicycleWheel.setNumberOfSpokes(10)
        self.assertEqual(math.pi/5, self.bicycleWheel.getAngleOfSpokes())

    def test_get_position_of_spokes_at_1st_spoke_when_number_of_spokes_is_8(self):
        positionList = self.bicycleWheel.getPositionOfSpokes()
        self.assertEqual([160.0, 80.0, 90.0, 80.0], positionList[0])
              
    def test_get_position_of_spokes_at_3rd_spoke_when_number_of_spokes_is_8(self):
        positionList = self.bicycleWheel.getPositionOfSpokes()
        self.assertEqual([80.0, 0.0, 80.0, 70.0], positionList[2])
    
    def test_load_invalid_file(self):
        self.assertRaises(IOError, self.bicycleWheel.loadFile('invalid.txt'))
        
    def test_load_file_from_previous_save_with_valid_input(self):
        self.bicycleWheel.setWheelSize(100.0)
        self.bicycleWheel.setHubSize(10.0)
        self.bicycleWheel.setNumberOfSpokes(12)
        self.bicycleWheel.saveFile(self.bicycleWheel.FILE_PATH)
        self.assertEqual([100.0, 10.0, 12], self.bicycleWheel.loadFile(self.bicycleWheel.FILE_PATH))
    
    def test_get_default_minimum_wheel_size_allowance_with_default_hub_size_of_10(self):
        self.assertEqual(40, self.bicycleWheel.getMinWheelSizeAllowance())
        
    def test_get_minimum_wheel_size_allowance_when_setting_hub_to_15(self):
        self.bicycleWheel.setHubSize(15)
        self.assertEqual(60, self.bicycleWheel.getMinWheelSizeAllowance())
        
    def test_get_default_maximum_hub_size_allowance_with_default_wheel_size_of_80(self):
        self.assertEqual(20, self.bicycleWheel.getMaxHubSizeAllowance())
        
    def test_get_maximum_hub_size_when_setting_wheel_size_to_100(self):
        self.bicycleWheel.setWheelSize(100)
        self.assertEqual(25, self.bicycleWheel.getMaxHubSizeAllowance())