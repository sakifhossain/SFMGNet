import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
import numpy as np
import torch.utils.data as data_utils
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error

# input: e, dw1, nw_x1, nw_y1
# outputs: repulse force from first neighbor
class Net3_ped1(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw1, nw_x1, nw_y1)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw2, nw_x2, nw_y2
# outputs: repulse force from second neighbor
class Net3_ped2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw2, nw_x2, nw_y2)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw3, nw_x3, nw_y3
# outputs: repulse force from third neighbor
class Net3_ped3(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw3, nw_x3, nw_y3)

        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw4, nw_x4, nw_y4
# outputs: repulse force from fourth neighbor
class Net3_ped4(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw4, nw_x4, nw_y4)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw5, nw_x5, nw_y5
# outputs: repulse force from fifth neighbor
class Net3_ped5(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw5, nw_x5, nw_y5)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw6, nw_x6, nw_y6
# outputs: repulse force from sixth neighbor
class Net3_ped6(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw6, nw_x6, nw_y6)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        
        x = self.fc3(x3_temp)
        
        return x

# input: e, dw7, nw_x7, nw_y7
# outputs: repulse force from seventh neighbor
class Net3_ped7(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw7, nw_x7, nw_y7)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        x = self.fc3(x3_temp)
        return x

# input: e, dw8, nw_x8, nw_y8
# outputs: repulse force from 8-th neighbor
class Net3_ped8(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw8, nw_x8, nw_y8)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        x = self.fc3(x3_temp)
        return x

# input: e, dw9, nw_x9, nw_y9
# outputs: repulse force from 9-th neighbor
class Net3_ped9(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 2)
        self.fc2 = nn.Linear(5, 2)
        self.fc3 = nn.Linear(4, 2)        

    def forward(self, e, x3):
        # x3 = (e^dw9, nw_x9, nw_y9)
        
        x3_alt_input = torch.cat((e, x3), 1)
        x3 = torch.relu(self.fc1(x3))
        # x3_alt_temp = torch.cat((e, x3))
        x3_alt = torch.relu(self.fc2(x3_alt_input))
        x3_temp = torch.cat((x3, x3_alt), 1)
        x = self.fc3(x3_temp)
        return x

# here, dw is actually e^dw

class Net3_ped_repulse_total(nn.Module):
    # Total repulsive force from the neighbouring pedestrians
    # Takes Net3_ped1, Net3_ped2. ..., Net3_ped9 as input and returns total neighbouring pedestrian repulsive force
    def __init__(self, model1, model2, model3, model4, model5, model6, model7, model8, model9):
        super().__init__()
        self.model1 = model1
        self.model2 = model2
        self.model3 = model3
        self.model4 = model4
        self.model5 = model5
        self.model6 = model6
        self.model7 = model7
        self.model8 = model8
        self.model9 = model9
        
        self.combiner1 = nn.Linear(18, 10)
        self.combiner2 = nn.Linear(10, 2)       

    def forward(self, e, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        head1 = self.model1(e, x1)
        head2 = self.model2(e, x2)
        head3 = self.model3(e, x3)
        head4 = self.model4(e, x4)
        head5 = self.model5(e, x5)
        head6 = self.model6(e, x6)
        head7 = self.model7(e, x7)
        head8 = self.model8(e, x8)
        head9 = self.model9(e, x9)
        
        combiner_input = torch.cat((head1, head2, head3, head4, head5, head6, head7, head8, head9), 1)
        
        x = torch.relu(self.combiner1(combiner_input))
        x = self.combiner2(x)
        
        return x

class Net3_ped_group(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1 = nn.Linear(3, 20)
        self.fc2 = nn.Linear(20, 2)
        self.fc3 = nn.Linear(2, 20)
        self.fc4 = nn.Linear(20, 2)
        
        self.fc5 = nn.Linear(4, 2)
       
    
    def forward(self, x3_1, x3_2):
        # x3_1 = (v_desired, angle)
        x3_1 = torch.relu(self.fc1(x3_1))
        x3_1 = self.fc2(x3_1)

        # x3_2 = (eta_centroid)
        x3_2 = torch.relu(self.fc3(x3_2))
        x3_2 = self.fc4(x3_2)
        
        temp_x3 = torch.cat((x3_1, x3_2), 1)
        x = self.fc5(temp_x3)
        return x

# net3_obtacle_repulse

class Net3_repulse(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 20)
        self.fc1_1 = nn.Linear(20, 20)
        # final combination
        self.fc2 = nn.Linear(20, 2)
        
    def forward(self, x3):
        x3 = torch.sigmoid(self.fc1(x3))
        x3 = torch.sigmoid(self.fc1_1(x3))
        x3 = self.fc2(x3)
        return x3

# net3_attract

class Net3_attract(nn.Module):
    def __init__(self):
        super().__init__()
        # net1 speed side
        self.fc1 = nn.Linear(10, 10)
        self.fc2 = nn.Linear(10, 1)
        
        # net1 instantaneous velocity side
        self.fc3 = nn.Linear(20, 20)
        self.fc4 = nn.Linear(20, 2)
        # net1 recombination, outputs f0
        self.fc5 = nn.Linear(4, 2)
        

    def forward(self, x1, x2, e):
        # x1 = speed inputs (10)
        # x2 = trajectory inputs (20)
        x1 = torch.sigmoid(self.fc1(x1))
        x1 = self.fc2(x1)
        x1 = x1 * e
        
        x2 = torch.tanh(self.fc3(x2))
        x2 = self.fc4(x2)
        
        temp_x = torch.cat((x1, x2), 1)
        x = self.fc5(temp_x)
        
        return x

# net3 complete/Final

class Net3_complete(nn.Module):
    def __init__(self, model_attract, model_repulse, model_ped, model_group):
        super().__init__()
        self.model_attract = model_attract
        self.model_repulse = model_repulse
        self.model_ped = model_ped
        self.model_group = model_group
        
        self.combiner1 = nn.Linear(8, 20)
        self.combiner2 = nn.Linear(20, 2)       

    def forward(self, e, x_attract1, x_attract2, x_bound, x1, x2, x3, x4, x5, x6, x7, x8, x9, x_angle, x_centroid):
        head1 = self.model_attract(x_attract1, x_attract2, e)
        head2 = self.model_repulse(x_bound)
        head3 = self.model_ped(e, x1, x2, x3, x4, x5, x6, x7, x8, x9)
        temp_v_desired = e * 0.5
        temp_group = torch.cat((temp_v_desired, x_angle), 1)
        head4 = self.model_group(temp_group, x_centroid)
        
        combiner_input = torch.cat((head1, head2, head3, head4), 1)
        
        x = torch.relu(self.combiner1(combiner_input))
        x = self.combiner2(x)
        
        return x

# net3 with attract and obstacle/boundary repulse

class Net3_a_rb(nn.Module):
    def __init__(self, model_attract, model_repulse):
        super().__init__()
        self.model_attract = model_attract
        self.model_repulse = model_repulse
        # self.model_ped = model_ped
        # self.model_group = model_group
        
        self.combiner1 = nn.Linear(4, 20)
        self.combiner2 = nn.Linear(20, 2)       

    def forward(self, e, x_attract1, x_attract2, x_bound):
        head1 = self.model_attract(x_attract1, x_attract2, e)
        head2 = self.model_repulse(x_bound)
        # x3 = (e^dw1, nw_x1, nw_y1)
        
        combiner_input = torch.cat((head1, head2), 1)
        
        x = torch.relu(self.combiner1(combiner_input))
        x = self.combiner2(x)
        
        return x

# net3 with attract, obstacle/boundary repulse and ped repulse

class Net3_a_rb_rp(nn.Module):
    def __init__(self, model_attract, model_repulse, model_ped):
        super().__init__()
        self.model_attract = model_attract
        self.model_repulse = model_repulse
        self.model_ped = model_ped
        
        self.combiner1 = nn.Linear(6, 20)
        self.combiner2 = nn.Linear(20, 2)       

    def forward(self, e, x_attract1, x_attract2, x_bound, x1, x2, x3, x4, x5, x6, x7, x8, x9):
        head1 = self.model_attract(x_attract1, x_attract2, e)
        head2 = self.model_repulse(x_bound)
        head3 = self.model_ped(e, x1, x2, x3, x4, x5, x6, x7, x8, x9)
        
        combiner_input = torch.cat((head1, head2, head3), 1)
        
        x = torch.relu(self.combiner1(combiner_input))
        x = self.combiner2(x)
        
        return x
