from neuron import Neuron
from neuron_layer import NeuronLayer


def connect_to(self, other):
    if self == other:
        return

    for s in self:
        for o in other:
            s.outputs.append(o)
            o.inputs.append(s)

neuron1 = Neuron('n1')
neuron2 = Neuron('n2')
layer1 = NeuronLayer('L1', 3)
layer2 = NeuronLayer('L2', 4)

neuron1.connect_to(neuron2)
neuron1.connect_to(layer1)
layer1.connect_to(neuron2)
layer1.connect_to(layer2)

print(neuron1)
print(neuron2)
print(layer1)
print(layer2)
