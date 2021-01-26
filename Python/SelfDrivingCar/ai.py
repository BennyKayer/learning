'''
This is the heart of the project, it makes car move
'''
import random as rn # for gradient descent batches
import os #saving loading brain
import torch #handles dynamic graphs
import torch.nn as nn #neural networks
import torch.nn.functional as fn #loss funcions etc
import torch.optim as opt #gradient descent becomes stochastic
from torch.autograd import Variable

class Network(nn.Module):
    '''
    https://pytorch.org/docs/stable/nn.html#torch.nn.Module
    https://pytorch.org/docs/stable/nn.html#torch.nn.Module.forward
    https://pytorch.org/docs/master/nn.html#linear
    '''
    def __init__(self, input_size, nb_action):
        super(Network, self).__init__()
        self.input_size = input_size #yellow neurons
        self.nb_action = nb_action #red neurons
        self.fc1 = nn.Linear(input_size, 30)#blue lines from yellow to green
        self.fc2 = nn.Linear(30, nb_action)#blue lines from green to red
    def forward(self, state):
        '''
        Activate the neurons
        Return Q value for each action (based on state)
        https://pytorch.org/docs/stable/nn.html#id27 <- relu(rectifier)
        '''
        hdn = fn.relu(self.fc1(state))
        q_values = self.fc2(hdn)
        return q_values
class ReplayMemory():
    '''
    Used as the ai's memory
    will hold last {capacity} events in {memory}
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []
    def push(self, event):
        '''
        Make sure memory is no longer than {capacity}
        event - tuple(lastState, newState, lastAction, lastReward)
        '''
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]
    def sample(self, batch_size):
        '''
        Random sample from {memory}
        https://www.programiz.com/python-programming/methods/built-in/zip
        https://pytorch.org/docs/stable/torch.html#torch.cat
        '''
        samples = zip(*rn.sample(self.memory, batch_size))#format for pytorch
        return map(lambda x: Variable(torch.cat(x, 0)), samples)
class Dqn():
    '''
    Deep Q Network - implements whole proccess
    https://pytorch.org/docs/stable/nn.html#torch.nn.Module.parameters
    https://pytorch.org/docs/stable/optim.html#torch.optim.Adam
    https://pytorch.org/docs/stable/torch.html#torch.unsqueeze
    '''
    def __init__(self, input_size, nb_action, gamma):
        self.gamma = gamma #delay coefficient
        self.reward_window = [] #mean of last 100 rewards
        self.model = Network(input_size, nb_action)
        self.memory = ReplayMemory(100000)
        self.optimizer = opt.Adam(self.model.parameters(), lr=0.001)
        #create {input_size} dimensions then enter extra dimension at the beginning
        self.last_state = torch.Tensor(input_size).unsqueeze(0)
        self.last_action = 0 #0 1 2 then convert to rotation see map.py
        self.last_reward = 0
    def select_action(self, state):
        '''
        Generally just apply softmax
        Input:
            state -> signal1, signal2, signal3, orientation, -orientation
        Output:
            action -> 0(straight),1(right) or 2(left)
        https://pytorch.org/docs/stable/torch.html#torch.multinomial
        '''
        temp = 100 #high probs get higher low get lower
        probs = fn.softmax(self.model(Variable(state, volatile=True)) * temp)
        action = torch.multinomial(probs, 1)
        return action.data[0, 0] #its tensor that's why
    def learn(self, batch_state, batch_next_state, batch_reward, batch_action):
        '''
        https://pytorch.org/docs/stable/torch.html#torch.gather
        https://pytorch.org/docs/stable/torch.html#torch.squeeze
        https://pytorch.org/docs/stable/tensors.html#torch.Tensor.detach
        https://pytorch.org/docs/stable/torch.html#torch.max
        https://pytorch.org/docs/stable/nn.html#smooth-l1-
        https://pytorch.org/docs/stable/optim.html#torch.optim.Optimizer.zero_grad
        https://pytorch.org/docs/stable/autograd.html#torch.autograd.backward
        '''
        #self.model gets all actions - gather right one, unsq to dest fake, kill fake with sq
        outputs = self.model(batch_state).gather(1, batch_action.unsqueeze(1)).squeeze(1)
        #take max q action (located at 1 since tuple ac#=>0) from detachments 
        next_outputs = self.model(batch_next_state).detach().max(1)[0]
        target = self.gamma * next_outputs + batch_reward
        td_loss = fn.smooth_l1_loss(outputs, target)
        self.optimizer.zero_grad()#pytorch makes us reinitialize gradient
        td_loss.backward()#backpropagation
        self.optimizer.step()#updates weights
    def update(self, reward, new_signal):
        '''
        Purple arrow
        '''
        new_state = torch.Tensor(new_signal).float().unsqueeze(0)
        last_action = torch.LongTensor([int(self.last_action)])
        last_reward = torch.Tensor([self.last_reward])
        self.memory.push((self.last_state, new_state, last_action, last_reward))
        action = self.select_action(new_state)
        if len(self.memory.memory) > 100:
            batch_state, batch_next_state, batch_action, batch_reward = self.memory.sample(100)
            self.learn(batch_state, batch_next_state, batch_reward, batch_action)
        self.last_action = action
        self.last_state = new_state
        self.last_reward = reward
        self.reward_window.append(reward)
        if len(self.reward_window) > 1000:
            del self.reward_window[0]
        return action
    def score(self):
        '''
        1 won't significantly change the output but it will prevent ZeroDivError
        '''
        return sum(self.reward_window) / (len(self.reward_window) + 1)
    def save(self):
        '''
        https://pytorch.org/docs/stable/nn.html#torch.nn.Module.state_dict
        https://pytorch.org/docs/stable/torch.html#torch.save
        '''
        nn_and_opt = {'nn_model' : self.model.state_dict(),
                      'optimizer' : self.optimizer.state_dict()}
        torch.save(nn_and_opt, 'last_brain.pth')
    def load(self):
        '''
        https://pytorch.org/docs/stable/nn.html#torch.nn.Module.load_state_dict
        '''
        if os.path.isfile('last_brain.pth'):
            print("loading checkpoint")
            checkpoint = torch.load('last_brain.pth')
            self.model.load_state_dict(checkpoint['nn_model'])
            self.optimizer.load_state_dict(checkpoint['optimizer'])
            print("done")
        else:
            print("no checkpoint found...")
    